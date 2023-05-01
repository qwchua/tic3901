import pytest
from gitpraise.graph import Graph

# Fixture to create a Graph object for testing
@pytest.fixture
def create_graph():
    graph = Graph()
    return graph

# Test if the add_edge method properly adds edges and updates adjacency and parent lists
def test_add_edge(create_graph):
    graph = create_graph
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)

    # Assert if the adjacency list and parent list are as expected after adding edges
    # m_adj_list, keys = the nodes in the graph, values = lists of neighboring nodes.
    assert graph.m_adj_list == {0: [1, 2], 1: [3], 2: [3], 3: []}
    assert graph.m_parents == {0: [], 1: [0], 2: [0], 3: [1, 2]}

# Test if the print_adj_list method properly prints the adjacency list
def test_print_adj_list(capsys, create_graph):
    graph = create_graph
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    graph.print_adj_list()
    captured = capsys.readouterr()

    # Assert if the captured output is as expected for the adjacency list
    assert captured.out == "node 0 :  [1, 2]\nnode 1 :  [3]\nnode 2 :  [3]\nnode 3 :  []\n"

# Test if the print_parent_list method properly prints the parent list
def test_print_parent_list(capsys, create_graph):
    graph = create_graph
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    graph.print_parent_list()
    captured = capsys.readouterr()

    # Assert if the captured output is as expected for the parent list
    assert captured.out == "node 0 :  []\nnode 1 :  [0]\nnode 2 :  [0]\nnode 3 :  [1, 2]\n"

# Test if the topologicalSort method returns a valid topological order
def test_topological_sort(create_graph):
    graph = create_graph
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    result = graph.topologicalSort()

    # Assert if the result is one of the two valid topological orders
    assert result == [0, 2, 1, 3] or result == [0, 1, 2, 3]

def test_add_edge2():
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    assert g.m_adj_list == {1: [2], 2: [3], 3: []}
    assert g.m_parents == {1: [], 2: [1], 3: [2]}

def test_print_adj_list2(capsys):
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.print_adj_list()
    captured = capsys.readouterr()
    assert captured.out == "node 1 :  [2]\nnode 2 :  [3]\nnode 3 :  []\n"

def test_print_parent_list2(capsys):
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.print_parent_list()
    captured = capsys.readouterr()
    assert captured.out == "node 1 :  []\nnode 2 :  [1]\nnode 3 :  [2]\n"

def test_topologicalSort2():
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    assert g.topologicalSort() == [1, 3, 2, 4, 5]

