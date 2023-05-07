import xml.etree.ElementTree as ET
from Node import Node
import geopy


def get_zipcode(geolocator, lat_field, lon_field):
    location = geolocator.reverse((lat_field, lon_field))
    return location.raw['address']['postcode']

geolocator = geopy.Nominatim(user_agent= "testApplication")
tree = ET.parse('map.osm')
root = tree.getroot()

print(get_zipcode(geolocator, 1,1))

nodeIDs = {} #node ID to list [] of wayIDS which contain it
nodes = []

for item in root:
	if(item.tag == 'node'):
		tn = Node(item.attrib['lat'], item.attrib['lon'], item.attrib['id'])
		nodes.append(tn)
		nodeIDs[item.attrib['id']] = tn

for node in nodes:
	print(node.id, node.lat, node.lon)
		