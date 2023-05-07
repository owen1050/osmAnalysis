import xml.etree.ElementTree as ET

tree = ET.parse('foothillHoffman.osm')
root = tree.getroot()

nodes = {} #node ID to list [] of wayIDS which contain it
streets = []
validStreetTypes = ['motorway_link', 'residential', 'tertiary', 'trunk', 'tertiary_link', 'primary', 'secondary', 'trunk_link', 'secondary_link', 'unclassified', 'primary_link', 'motorway', 'bridleway']
for item in root:
	if(item.tag == 'node'):
		nodes[item.attrib['id']] = []


print(len(nodes))
for item in root:
	if(item.tag == 'way'):
		for nd in item:
			if(nd.tag =='nd'):
				#print(nd.attrib['ref'])
				if(nodes[nd.attrib['ref']] == None):
					nodes[nd.attrib['ref']] = [1]
				nodes[nd.attrib['ref']].append(item.attrib['id'])
		
			if(nd.tag == 'tag' and nd.attrib['k'] == 'highway' and nd.attrib['v'] in validStreetTypes ):
				streets.append(item.attrib['id'])



for node in nodes:
	if(len(nodes[node]) > 0):
		#print(nodes[node])
		pass

print(streets)