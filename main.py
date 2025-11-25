from build_dependency_graph import build_dependency_graph
from build_reverse_dependency_graph import build_reverse_dependency_graph
import xml.etree.ElementTree as ET


tree = ET.parse("config.xml")
root = tree.getroot()

package = root[0].attrib["name"]
version = root[3].attrib["version"]
mode = root[2].attrib["mode"]
filter_str = root[5].attrib["filtration"]
url = root[1].attrib["URL"]



# https://api.nuget.org/v3/registration5-semver1

graph = {}
re_graph = {}
visited = set()

# build_dependency_graph(
#         package,
#         graph,
#         visited,
#         mode,
#         url,
#         filter_str
#     )
#
# print(graph)

if int(mode) == 1:
    build_reverse_dependency_graph(package, eval(open(url).read()), re_graph)

print(re_graph)
