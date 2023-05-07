import xml.etree.ElementTree as ET

tree = ET.parse('map.osm')
root = tree.getroot()

nodes = {} #node ID to list [] of wayIDS which contain it
streets = []
validStreetTypes = ['residential', 'tertiary']


types = []
print(len(nodes))
for item in root:
	if(item.tag == 'way'):
		for nd in item:
			if(nd.tag == 'tag' and nd.attrib['k'] == 'highway'):
				if(nd.attrib['v'] in types):
					pass
				else:
					types.append(nd.attrib['v'])


print(types)