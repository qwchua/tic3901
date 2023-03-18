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

    def print_parent_list(self):
        for key in self.m_parents.keys():
            print("node", key, ": ", self.m_parents[key])

    def topologicalSortUtil(self,v,visited,stack):
 
        visited[v] = True
 
        for i in self.m_adj_list[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,stack)

        stack.insert(0,v)
 
    def topologicalSort(self):
        visited = {}

        for key, value in self.m_adj_list.items():
            visited[key] = False

        stack =[]

        for key, value in self.m_adj_list.items():
            if visited[key] == False:
                self.topologicalSortUtil(key,visited,stack)

        # for i in range(numOfNodes):
        #     if visited[i] == False:
        #         self.topologicalSortUtil(i,visited,stack)

        return stack