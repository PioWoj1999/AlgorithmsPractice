from collections import deque


def dfs(graph: dict, node) -> None:
    visited = []
    stack = []

    visited.append(node)
    stack.append(node)

    while stack:
        s = stack.pop()
        print(s)
        for i in reversed(graph[s]):
            if i not in visited:
                visited.append(i)
                stack.append(i)


def dfs_recursive(graph, start, visited=None):
    """https://www.programiz.com/dsa/graph-dfs"""
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)
    for next in graph[start] - visited:
        dfs_recursive(graph, next, visited)
    return visited


def main():
    graph = {
        "A": ["B", "G"],
        "B": ["C", "D", "E"],
        "C": [],
        "D": [],
        "E": ["F"],
        "F": [],
        "G": ["H"],
        "H": ["I"],
        "I": [],
    }
    dfs(graph, "A")

    graph_recursive = {
        "0": set(["1", "2"]),
        "1": set(["0", "3", "4"]),
        "2": set(["0"]),
        "3": set(["1"]),
        "4": set(["2", "3"]),
    }
    dfs_recursive(graph_recursive, "0")


if __name__ == "__main__":
    main()
