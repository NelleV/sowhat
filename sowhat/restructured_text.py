
def add_toc():
    restructured_text = ".. contents::\n\n"
    return restructured_text


def add_title(title, level="="):
    restructured_text = title + "\n"
    restructured_text = restructured_text + len(restructured_text) * level
    restructured_text = restructured_text + "\n\n"
    return restructured_text


def add_image(image_url):
    restructured_text = ".. image:: %s\n\n" % image_url
    return restructured_text


def add_link(name, link):
    restructured_text = "`%s <%s>`_" % (name, link)
    return restructured_text
