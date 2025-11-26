from get_dependences_wrapper import get_dependencies_wrapper

def build_reverse_dependency_graph(target_package, forward_graph, end_graph):
    inverse_graph = {}

    for parent, children in forward_graph.items():
        for child in children:
            if child not in inverse_graph:
                inverse_graph[child] = []

            if parent not in inverse_graph:
                inverse_graph[parent] = []

            if parent not in inverse_graph[child]:
                inverse_graph[child].append(parent)

    q = [target_package]
    visited = set()

    def BFS(pack):

        if pack in visited:
            return

        visited.add(pack)

        dependencies = inverse_graph[pack]
        end_graph[pack] = dependencies
        for dep in dependencies:
            q.append(dep)

    while q:
        BFS(q.pop(0))