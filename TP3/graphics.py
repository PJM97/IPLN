from pyvis.network import Network
import pandas as pd

def generateHTML(lista,fo):
    got_net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")

    # set the physics layout of the network
    got_net.barnes_hut()
 
   
    for e in lista:
        src = e[0]
        dst = e[1]
        w = e[2]

        got_net.add_node(src, src, title=src)
        got_net.add_node(dst, dst, title=dst)
        got_net.add_edge(src, dst, value=w)

    neighbor_map = got_net.get_adj_list()

    # add neighbor data to node hover data
    for node in got_net.nodes:
        node["title"] += " Neighbors:<br>" + "<br>".join(neighbor_map[node["id"]])
        node["value"] = len(neighbor_map[node["id"]])
    #Escrever o ficheiro html.
    got_net.show(fo)

