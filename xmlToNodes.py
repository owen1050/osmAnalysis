import xml.etree.ElementTree as ET
from Node import Node

tree = ET.parse('map.osm')
root = tree.getroot()

nodeIDs = {} #node ID to list [] of wayIDS which contain it
nodes = []

for item in root:
	if(item.tag == 'node'):
		tn = Node(item.attrib['lat'], item.attrib['lon'], item.attrib['id'])
		nodes.append(tn)
		nodeIDs[item.attrib['id']] = tn

for node in nodes:
	print(node.id, node.lat, node.lon)
		