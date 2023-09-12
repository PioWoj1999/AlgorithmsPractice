from collections import deque


def bfs(graph: dict, node) -> None:
    visited = []
    queue = deque()

    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop()
        print(s)
        for i in graph[s]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
    print(f"Visited in graph: {visited}")


def main():
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E", "F"],
        "C": ["G"],
        "D": [],
        "E": [],
        "F": [],
        "G": [],
        "H": [],
        "I": [],
    }
    bfs(graph, "A")


if __name__ == "__main__":
    main()
