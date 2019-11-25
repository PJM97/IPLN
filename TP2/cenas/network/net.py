from pyvis.network import Network


net = Network()

net.add_node(1, label="Node 1") # node id = 1 and label = Node 1

net.add_node(2) # node id and label = 2

nodes = ["a", "b", "c", "d"]

net.add_nodes(nodes) # node ids and labels = ["a", "b", "c", "d"]

net.add_nodes("hello") # node ids and labels = ["h", "e", "l", "o"]

g = Network()

g.add_nodes([1,2,3], value=[10, 100, 400], title=["I am node 1", "node 2 here", "and im node 3"], x=[21.4, 54.2, 11.2], y=[100.2, 23.54, 32.1], label=["NODE 1", "NODE 2", "NODE 3"], color=["#00ff1e", "#162347", "#dd4b39"])