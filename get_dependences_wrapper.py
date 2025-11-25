from Searching_for_dependences import find_package_dependencies_from_url
from GRAPH import graph
from GRAPH1 import graph_1

def get_dependencies_wrapper(package_id, is_test_mode, repo_url, test_data, filter_str):
    dependencies_ids = set()

    if int(is_test_mode) == 1:

        raw_deps = graph_1[package_id]
        dependencies_ids.update(raw_deps)

    else:
        # --- Реальный режим ---
        # Формируем URL для NuGet V3 API
        # Обычно это: https://api.nuget.org/v3/registration5-gz-semver2/{id}/index.json
        # Но для упрощения используем переданный repo_url как базу

        # ВАЖНО: NuGet чувствителен к регистру в URL, лучше переводить в lower()
        formatted_url = f"{repo_url}/{package_id.lower()}/index.json"

        raw_data = find_package_dependencies_from_url(formatted_url)

        # Извлекаем уникальные ID из всех фреймворков
        for framework, deps in raw_data.items():
            for dep in deps:
                dependencies_ids.add(dep['id'])

    # --- Фильтрация (Требование 3.2) ---
    # Исключаем пакеты, содержащие подстроку filter_str
    filtered_deps = []
    for dep_id in dependencies_ids:
        if filter_str and filter_str.lower() in dep_id.lower():
            continue  # Пропускаем этот пакет
        filtered_deps.append(dep_id)

    return filtered_deps