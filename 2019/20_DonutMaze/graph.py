# Copied from https://dev.to/mxl/dijkstras-algorithm-in-python-algorithms-for-beginners-dkc

from collections import deque, namedtuple


# we'll use infinity as a default distance to nodes.
inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')


def make_edge(start, end, cost=1):
    return Edge(start, end, cost)


class Graph:
    def __init__(self, edges):
        # let's check that the data is right
        wrong_edges = [i for i in edges if len(i) not in [2, 3]]
        if wrong_edges:
            raise ValueError('Wrong edges data: {}'.format(wrong_edges))

        self.edges = [make_edge(*edge) for edge in edges]

    @property
    def vertices(self):
        return set(
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            )
        )

    def get_node_pairs(self, n1, n2, both_ends=True):
        if both_ends:
            node_pairs = [[n1, n2], [n2, n1]]
        else:
            node_pairs = [[n1, n2]]
        return node_pairs

    def remove_edge(self, n1, n2, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

    def add_edge(self, n1, n2, cost=1, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError('Edge {} {} already exists'.format(n1, n2))

        self.edges.append(Edge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=n2, end=n1, cost=cost))

    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))

        return neighbours

    def dijkstra(self, source, dest):
        #print("dijkstra: s=%s, d=%s" % (source, dest))
        assert source in self.vertices, 'Such source node doesn\'t exist'
        distances = {vertex: inf for vertex in self.vertices}
        previous_vertices = {
            vertex: None for vertex in self.vertices
        }
        distances[source] = 0
        vertices = self.vertices.copy()

        while vertices:
            current_vertex = min(
                vertices, key=lambda vertex: distances[vertex])
            vertices.remove(current_vertex)
            if distances[current_vertex] == inf:
                break
            for neighbour, cost in self.neighbours[current_vertex]:
                #print("cv=%s, n=%s, c=%d" % (current_vertex, neighbour, cost))
                alternative_route = distances[current_vertex] + cost
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex
        # print(previous_vertices)
        path, current_vertex = deque(), dest
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)
        return path

# DW: put graph and test into main and and added find_edge and cost functions

    def find_edge(self, source, dest):
        for edge in self.edges:
            if edge.start == source and edge.end == dest:
                return edge
        return None

    def cost(self, path):
        "Return the cost of this path"

        # 1. It's free
        total = 0

        # 2. Loop for all the paths
        path_list = list(path)
        for pnum in range(1, len(path_list)):

            # 3. find this edge of the path
            source = path_list[pnum - 1]
            dest = path_list[pnum]
            edge = self.find_edge(source, dest)

            # 4. Add code of this edge to the total
            total += edge.cost

        # 5. Return the total cost
        return total


def main():
    graph = Graph([
        ("a", "b", 7), ("a", "c", 9), ("a", "f", 14), ("b", "c", 10),
        ("b", "d", 15), ("c", "d", 11), ("c", "f", 2), ("d", "e", 6),
        ("e", "f", 9)])

    result = graph.dijkstra("a", "e")
    print(result)
    print(graph.cost(result))

    graph2 = Graph([
        ("a", "b", 7), ("a", "c", 9), ("a", "f", 14), ("b", "c", 10),
        ("b", "d", 15), ("c", "d", 11), ("c", "f", 2), ("d", "e", 6),
        ("e", "f", 9), ('a', 'e', 99)])

    result = graph2.dijkstra("a", "e")
    print(result)
    print(graph2.cost(result))

    graph3 = Graph([
        ((1, 1), (2, 2), 7), ((1, 1), (3, 3), 9), ((1, 1), (6, 6), 14), ((2, 2), (3, 3), 10),
        ((2, 2), (4, 4), 15), ((3, 3), (4, 4), 11), ((3, 3), (6, 6), 2), ((4, 4), (5, 5), 6),
        ((5, 5), (6, 6), 9), ((1, 1), (5, 5), 30), ((4, 4), (3, 3), 11)])

    result = graph3.dijkstra((1, 1), (5, 5))
    print(result)
    print(graph3.cost(result))

    graph4 = Graph([
        ((9, 2), (9, 6), 4), ((9, 6), (2, 8), 1), ((2, 8), (6, 10), 6),
        ((6, 10), (2, 13), 1), ((2, 13), (2, 15), 4), ((2, 15), (11, 12), 1),
        ((11, 12), (13, 16), 6)])

    result = graph4.dijkstra((9, 2), (13, 16))
    print(result)
    if result is not None:
        print(graph4.cost(result))

    graph5 = Graph([
        ((9, 2), (9, 6), 4), ((9, 6), (2, 8), 1), ((2, 8), (6, 10), 6),
        ((6, 10), (2, 13), 1), ((2, 13), (2, 15), 4), ((2, 15), (11, 12), 1),
        ((11, 12), (13, 16), 6)])

    result = graph5.dijkstra((9, 2), (13, 16))
    print(result)
    if result is not None:
        print(graph5.cost(result))


if __name__ == '__main__':
    main()
