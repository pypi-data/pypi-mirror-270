from .base_dictable import BaseDictable
from typing import Dict, Self

class Options(BaseDictable):
    class Nodes(BaseDictable):
        def __init__(self):
            super().__init__()
            self.scaling = {
                "min": 10,
                "max": 60,
            }

        def set_scaling(self, min, max):
            self.scaling.update({
                "min": min,
                "max": max,
            })
        
    class Edges(BaseDictable):
        def __init__(self):
            super().__init__()
            self.color = "GRAY"
            self.smooth = False

    class Physics(BaseDictable):
        def __init__(self):
            super().__init__()
            self.barnesHut = {
                "gravitationalConstant": None,
            }
            self.stabilization = {
                "iterations": None
            }

        def set_barnesHut(self, gravitationalConstant):
            self.barnesHut.update({
                "gravitationalConstant": gravitationalConstant
            })

        def set_stabilization(self, iterations):
            self.stabilization.update({
                "iterations": iterations
            })

    def __init__(self, height="100%", width="100%"):
        super().__init__()
        self.height = height
        self.width = width
        self.nodes = Options.Nodes()
        self.edges = Options.Edges()
        self.physics = Options.Physics()
    
    def set_edges(self, color, smooth: bool):
        self.edges.color = color
        self.edges.smooth = smooth


    