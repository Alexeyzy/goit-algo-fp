import uuid
import networkx as nx
import matplotlib.pyplot as plt
import colorsys

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4()) 
        
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, colors=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    if colors:
        color_map = [colors[node[0]] for node in tree.nodes(data=True)]
    else:
        color_map = [node[1]['color'] for node in tree.nodes(data=True)]

    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=color_map)
    plt.show()

def generate_color(index, total):
    hue = index / total
    r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    return f'#{int(r * 255):02X}{int(g * 255):02X}{int(b * 255):02X}'

def dfs(root):
    if not root:
        return []

    stack = [root]
    visited = []
    order = 0
    colors = {}

    while stack:
        node = stack.pop()
        if node.id not in visited:
            visited.append(node.id)
            colors[node.id] = generate_color(order, len(stack) + 1)
            order += 1
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    return colors

def bfs(root):
    if not root:
        return []

    queue = [root]
    visited = []
    order = 0
    colors = {}

    while queue:
        node = queue.pop(0)
        if node.id not in visited:
            visited.append(node.id)
            colors[node.id] = generate_color(order, len(queue) + 1)
            order += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return colors

root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# DFS
dfs_colors = dfs(root)
draw_tree(root, dfs_colors)

# BFS
bfs_colors = bfs(root)
draw_tree(root, bfs_colors)
