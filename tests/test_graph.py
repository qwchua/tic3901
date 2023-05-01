from gitpraise.graph import Graph

def test_add_edge():
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    assert g.m_adj_list == {1: [2], 2: [3], 3: []}
    assert g.m_parents == {1: [], 2: [1], 3: [2]}

def test_print_adj_list(capsys):
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.print_adj_list()
    captured = capsys.readouterr()
    assert captured.out == "node 1 :  [2]\nnode 2 :  [3]\nnode 3 :  []\n"

def test_print_parent_list(capsys):
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.print_parent_list()
    captured = capsys.readouterr()
    assert captured.out == "node 1 :  []\nnode 2 :  [1]\nnode 3 :  [2]\n"

def test_topologicalSort():
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    assert g.topologicalSort() == [1, 3, 2, 4, 5]