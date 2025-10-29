import requests
import zipfile
import xml.etree.ElementTree as ET
import io

def find_package_dependencies_from_url(nupkg_url):
    dependencies_by_framework = {}
    response = requests.get(nupkg_url)

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
                    framework = group.get('targetFramework', 'all')  # 'all' если платформа не указана

                    framework_deps = []
                    for dependency in group.findall(f'{namespace}dependency'):
                        package_id = dependency.get('id')
                        version = dependency.get('version')
                        if package_id and version:
                            framework_deps.append({'id': package_id, 'version': version})

                    if framework_deps:
                        dependencies_by_framework[framework] = framework_deps

                    # Обрабатываем случай, когда зависимости не сгруппированы (старый формат)
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