class Graph:
    def __init__(self):
        self.m_adj_list = {}
        self.m_parents = {}       

    def add_edge(self, node1, node2):
        if node1 not in self.m_adj_list:
            self.m_adj_list[node1] = []
        if node2 not in self.m_adj_list:
            self.m_adj_list[node2] = []

        if node1 not in self.m_parents:
            self.m_parents[node1] = []
        if node2 not in self.m_parents:
            self.m_parents[node2] = []
        
        # append the neighbor node to its corresponding key node 
        self.m_adj_list[node1].append(node2)
        self.m_parents[node2].append(node1)

    def print_adj_list(self):
        for key in self.m_adj_list.keys():
            print("node", key, ": ", self.m_adj_list[key])