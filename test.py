from IGraph import IGraph
import matplotlib.pyplot as  plt

#ex1
G = IGraph()
G.set_from_dotFile('idk.dot')

#G.set_node_color("A", "blue")
#G.set_node_color("B", "blue")



#ex2
nodes = {
    "17" : "red",
    "14" : "red",
    "8" : "red",
    "1" : "red",
    "2" : "red",
    "3" : "red",
}

G.set_node_color(color_dic = nodes)

G.set_edge_color(edge=('17', '14'), color='red')
G.set_edge_color(edge=('14', '8'), color='red')
G.set_edge_color(edge=('8', '1'), color='red')
G.set_edge_color(edge=('1', '2'), color='red')
G.set_edge_color(edge=('2', '3'), color='red')

nodes = ['17', '14', '8', '1', '2', '3']
edges = [('17', '14'), ('14', '8'), ('8', '1'), ('1', '2'), ('2', '3')]

for item in nodes:
    G.set_node_attribute(node = item, value='R', name=' ')

for item in edges:
    G.set_edge_weight(edge=item, weight=10)

B = IGraph()
B.set_from_dotFile('2nd.dot')

Leaves =  ['H','I','J','K','L','M','N','O']

for item in Leaves:
    B.set_node_color(node=item, color='red')

Leaves_Values_dic = {'H' : {'leaf_1'}, 'I' : {'leaf_2'},  'J' : {'leaf_3'}, 'K' : {'leaf_4'}, 'L' : {'leaf_5'} , 'M' : {'leaf_6'}, 'N' : {'leaf_7'}, 'O' : {'leaf_8'}}

for leaf in Leaves:
    B.set_node_attribute(node = leaf, values_dict = Leaves_Values_dic)

B.draw()
plt.show()