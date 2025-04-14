import networkx as nx
import json

def build_graph(cmdb_path):
    G = nx.DiGraph()
    with open(cmdb_path) as f:
        relationships = json.load(f)
        for rel in relationships:
            G.add_edge(rel["source"], rel["target"])
    return G
