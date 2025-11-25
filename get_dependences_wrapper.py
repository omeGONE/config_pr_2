from Searching_for_dependences import find_package_dependencies_from_url

def get_dependencies_wrapper(package_id, is_test_mode, repo_url, filter_str):
    dependencies_ids = set()

    if int(is_test_mode) == 1:

        dependencies_ids = eval(open(repo_url).read())[package_id]

    else:
        formatted_url = f"{repo_url}/{package_id.lower()}/index.json"

        raw_data = find_package_dependencies_from_url(formatted_url)

        for framework, deps in raw_data.items():
            for dep in deps:
                dependencies_ids.add(dep['id'])

    filtered_deps = []
    for dep_id in dependencies_ids:
        if filter_str and filter_str.lower() in dep_id.lower():
            continue
        filtered_deps.append(dep_id)

    return filtered_deps