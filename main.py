import requests
from Searching_for_dependences import find_package_dependencies_from_url

version = input("Введите версию пакета ")

url = f"https://api.nuget.org/v3/registration5-semver1/newtonsoft.json/{version}.json"

response = requests.get(url)
data = response.json()
package_dependencies = find_package_dependencies_from_url(data["packageContent"])
print(package_dependencies)

