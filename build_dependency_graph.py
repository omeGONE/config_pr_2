from get_dependences_wrapper import get_dependencies_wrapper

def build_dependency_graph(current_package, graph, visited, is_test_mode, repo_url, filter_str):
    q = [current_package]
    def BFS(pack):
        if pack in visited:
            return

        visited.add(pack)

        dependencies = get_dependencies_wrapper(pack, is_test_mode, repo_url, filter_str)

        graph[pack] = dependencies

        for dep in dependencies:
            q.append(dep)

    while q:
        BFS(q.pop(0))
