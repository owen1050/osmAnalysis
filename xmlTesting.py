import xml.etree.ElementTree as ET

tree = ET.parse('map.osm')
root = tree.getroot()

nodes = {} #node ID to list [] of wayIDS which contain it
streets = []
streetNames = []
validStreetTypes = ['motorway_link', 'residential', 'tertiary', 'trunk', 'tertiary_link', 'primary', 'secondary', 'trunk_link', 'secondary_link', 'unclassified', 'primary_link', 'motorway', 'bridleway']
streetTypes = []

print(len(nodes))
for item in root:
	if(item.tag == 'way'):
		nam = ''
		ad = False
		for nd in item:
			
			if(nd.tag == 'tag' and nd.attrib['k'] == 'name'):
				nam = nd.attrib['v']

			if(nd.tag == 'tag' and nd.attrib['k'] == 'highway' and nd.attrib['v'] in validStreetTypes ):
				streets.append(item.attrib['id'])
				streetTypes.append(nd.attrib['v'])
				ad = True
		if(ad):
			streetNames.append(nam)



for i in range(len(streets)):
	print(streets[i], streetNames[i], streetTypes[i])