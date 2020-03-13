import os
import sys
import shutil
from distutils.command.clean import clean as Clean


DISTNAME = 'sowhat'
DESCRIPTION = 'Creating rst reports easily.'
MAINTAINER = 'Nelle Varoquaux'
MAINTAINER_EMAIL = 'nelle.varoquaux@gmail.com'
VERSION = '0.0.0-git'

# Optional setuptools features
# We need to import setuptools early, if we want setuptools features,
# as it monkey-patches the 'setup' function
# For some commands, use setuptools
SETUPTOOLS_COMMANDS = set([
    'develop', 'release', 'bdist_egg', 'bdist_rpm',
    'bdist_wininst', 'install_egg_info', 'build_sphinx',
    'egg_info', 'easy_install', 'upload', 'bdist_wheel',
    '--single-version-externally-managed',
])

if SETUPTOOLS_COMMANDS.intersection(sys.argv):
    import setuptools
    extra_setuptools_args = dict(
        zip_safe=False,  # the package can run out of an .egg file
        include_package_data=True,
        extras_require={
            'alldeps': (
            ),
        },
    )
else:
    extra_setuptools_args = dict()


class CleanCommand(Clean):
    description = ("Remove build directories, and compiled file in the "
                   "source tree")

    def run(self):
        Clean.run(self)
        if os.path.exists('build'):
            shutil.rmtree('build')
        for dirpath, dirnames, filenames in os.walk('pastis'):
            for filename in filenames:
                if (filename.endswith('.so') or filename.endswith('.pyd')
                   or filename.endswith('.dll')
                   or filename.endswith('.pyc')):
                    os.unlink(os.path.join(dirpath, filename))


def configuration(parent_package='', top_path=None):
    if os.path.exists('MANIFEST'):
        os.remove('MANIFEST')

    from numpy.distutils.misc_util import Configuration
    config = Configuration(None, parent_package, top_path)

    config.add_subpackage('sowhat')

    return config


def setup_package():
    metadata = dict(
        configuration=configuration,
        name=DISTNAME,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        description=DESCRIPTION,
        version=VERSION,
        scripts=[],
        classifiers=[
            'Intended Audience :: Science/Research',
            'Intended Audience :: Developers',
            'License :: OSI Approved',
            'Programming Language :: C',
            'Programming Language :: Python',
            'Topic :: Software Development',
            'Topic :: Scientific/Engineering',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: POSIX',
            'Operating System :: Unix',
            'Operating System :: MacOS'],
        **extra_setuptools_args)

    if len(sys.argv) == 1 or (
            len(sys.argv) >= 2 and ('--help' in sys.argv[1:] or
                                    sys.argv[1] in ('--help-commands',
                                                    'egg_info',
                                                    '--version',
                                                    'clean'))):
        # For these actions, NumPy is not required
        #
        # They are required to succeed without Numpy for example when
        # pip is used to install Scikit-learn when Numpy is not yet present in
        # the system.
        try:
            from setuptools import setup
        except ImportError:
            from distutils.core import setup

        metadata['version'] = VERSION
    else:
        from numpy.distutils.core import setup

        metadata['configuration'] = configuration

    setup(**metadata)


if __name__ == "__main__":
    setup_package()
