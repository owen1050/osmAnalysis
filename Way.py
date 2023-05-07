import math

class Way:

    length = 0
    c = ""
    nodes = []
    name = ""
    id = ""


    def __init__(self, length_, nodes_, roadType_, name_, id_):
        self.length = 0
        self.nodes = nodes_
        self.roadType = roadType_
        self.name = name_
        self.id = id_

    def calculateLength(self):
        for i in range(len(self.nodes) - 1):
            x1d = math.pow(self.nodes[i].lon - self.nodes[i+1].lon, 2)
            y1d = math.pow(self.nodes[i].lat - self.nodes[i+1].lat, 2)
            t = math.sqrt(x1d + y1d)
            self.length = self.length + t
        self.length = self.length * 60