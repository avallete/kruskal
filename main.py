import random
from source.graph import Graph


def run():
    # data_graph = [
    #     ("A", "D", 5), ("A", "B", 7),
    #     ("B", "A", 7), ("B", "C", 8), ("B", "D", 9), ("B", "E", 7),
    #     ("C", "B", 8), ("C", "E", 5),
    #     ("D", "A", 5), ("D", "B", 9), ("D", "E", 15), ("D", "F", 6),
    #     ("E", "B", 7), ("E", "C", 5), ("E", "D", 15), ("E", "F", 8), ("E", "G", 9),
    #     ("F", "D", 6), ("F", "E", 8), ("F", "G", 11),
    #     ("G", "F", 11), ("G", "E", 9),
    # ]
    data_graph = [
        ("A", "D", 5), ("A", "B", 7),
        ("B", "A", 7), ("B", "C", 8), ("B", "D", 9), ("B", "E", 7),
        ("C", "B", 8), ("C", "E", 5),
        ("D", "A", 5), ("D", "B", 9), ("D", "E", 15), ("D", "F", 6),
        ("E", "B", 7), ("E", "C", 5), ("E", "D", 15), ("E", "F", 8), ("E", "G", 9),
        ("F", "D", 6), ("F", "E", 8), ("F", "G", 11),
        ("G", "F", 11), ("G", "E", 9),
    ]

    random.shuffle(data_graph)

    graph = Graph(data_graph)

    edges = graph.kruskal()

    result = 0
    for edge in edges:
        result += edge[2]

    print(edges)
    print(result)


if __name__ == "__main__":
    run()