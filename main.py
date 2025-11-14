import requests
from Searching_for_dependences import find_package_dependencies_from_url
from BFS_rec import BFS_rec
import xml.etree.ElementTree as ET

package =
version = input("Введите версию пакета ")

# print(BFS_rec(package, version))

url = f"https://api.nuget.org/v3/registration5-semver1/{package.lower()}/{version}.json"

package_dependencies = find_package_dependencies_from_url(url)[".NETStandard2.0"]
print(package_dependencies)

