import xml.etree.ElementTree as ET
from Way import Way
from Node import Node

tree = ET.parse('map.osm')
root = tree.getroot()

nodeIDs = {} #node ID to list [] of wayIDS which contain it
nodes = []
validStreetTypes = ['motorway_link', 'residential', 'tertiary', 'trunk', 'tertiary_link', 'primary', 'secondary', 'trunk_link', 'secondary_link', 'unclassified', 'primary_link', 'motorway', 'bridleway']


for item in root:
	if(item.tag == 'node'):
		tn = Node(float(item.attrib['lat']), float(item.attrib['lon']), item.attrib['id'])
		nodes.append(tn)
		nodeIDs[item.attrib['id']] = tn


print("nodes done, starting ways")
ways = []

for item in root:
	nodes = []
	name = ""
	type = ""
	if(item.tag == 'way'):
		for t in item:
			if(t.tag == "nd"):
				n = nodeIDs[t.attrib['ref']]
				nodes.append(n)
			if(t.tag == "tag" and t.attrib['k'] == "highway"):
				type = t.attrib['v']
			if(t.tag == "tag" and t.attrib['k'] == "name"):
				name = t.attrib['v']

		w = Way(-1, nodes, type, name, item.attrib['id'])
		w.calculateLength()
		if(type in validStreetTypes):
			ways.append(w)
		
totalLen = 0
for way in ways:
	print(way.id, way.name, way.length, way.roadType)
	totalLen = totalLen + way.length
		

print(totalLen)