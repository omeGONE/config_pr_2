import xml.etree.ElementTree as ET


def application():
    tree = ET.parse("config.xml")
    root = tree.getroot()
    for children in root:
        print(children.attrib)

    if not(root[0].attrib["name"]):
        print("Param name mustn't be empty")

    if root[1].attrib["URL"][:6] != "https:":
        print("Invalid URL")

    try:
        int(root[2].attrib["mode"])
    except:
        print("Param mode must be int")

    if not(root[3].attrib["version"]):
        print("Param version mustn't be empty")

    try:
        int(root[4].attrib["ASCIImode"])
    except:
        print("Param ASCIImode must be int")

    if not(root[5].attrib["filtration"]):
        print("Param filtrarion mustn't be empty")