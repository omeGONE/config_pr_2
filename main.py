import requests
from Searching_for_dependences import find_package_dependencies_from_url
from build_dependency_graph import build_dependency_graph
import xml.etree.ElementTree as ET

tree = ET.parse("config.xml")
root = tree.getroot()

package = root[0].attrib["name"]
version = root[3].attrib["version"]
mode = root[2].attrib["mode"]
filter_str = root[5].attrib["filtration"]
url = root[1].attrib["url"]

graph = {}
visited = set()
test_data = {}

build_dependency_graph(
        package,
        graph,
        visited,
        mode,
        url,
        test_data,
        filter_str
    )

print(graph)


#
# package_dependencies = find_package_dependencies_from_url(url)[".NETStandard2.0"]
# print(package_dependencies)

