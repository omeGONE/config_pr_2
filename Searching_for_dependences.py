import requests
import zipfile
import xml.etree.ElementTree as ET
import io

def find_package_dependencies_from_url(url):
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    items = data.get("items", [])
    last_page = items[-1]
    versions_list = last_page.get("items")
    if not versions_list:
        page_response = requests.get(last_page["@id"])
        versions_list = page_response.json().get("items", [])
    if not versions_list:
        return {}

    latest_package_entry = versions_list[-1]
    leaf_url = latest_package_entry["@id"]
    response = requests.get(leaf_url)
    data = response.json()
    dependencies_by_framework = {}
    response = requests.get(data["packageContent"])

    with zipfile.ZipFile(io.BytesIO(response.content)) as archive:
        nuspec_file = None
        for file_info in archive.infolist():
            if file_info.filename.endswith('.nuspec'):
                nuspec_file = file_info.filename
                break

        if nuspec_file:
            with archive.open(nuspec_file) as xml_file:
                tree = ET.parse(xml_file)
                root = tree.getroot()

                namespace = '{' + root.tag.split('}')[0].strip('{') + '}' if '}' in root.tag else ''

                metadata = root.find(f'{namespace}metadata')

                dependencies_element = metadata.find(f'{namespace}dependencies')

                for group in dependencies_element.findall(f'{namespace}group'):
                    framework = group.get('targetFramework', 'all')

                    framework_deps = []
                    for dependency in group.findall(f'{namespace}dependency'):
                        package_id = dependency.get('id')
                        version = dependency.get('version')
                        if package_id and version:
                            framework_deps.append({'id': package_id, 'version': version})

                    if framework_deps:
                        dependencies_by_framework[framework] = framework_deps

                if not dependencies_by_framework:
                    direct_deps = []
                    for dependency in dependencies_element.findall(f'{namespace}dependency'):
                        package_id = dependency.get('id')
                        version = dependency.get('version')
                        if package_id and version:
                            direct_deps.append({'id': package_id, 'version': version})
                    if direct_deps:
                        dependencies_by_framework['all'] = direct_deps

    return dependencies_by_framework