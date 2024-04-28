from .base_dictable import BaseDictable
from .utils import open_file, save_file
from .node import Node
from .edge import Edge
from jinja2 import Environment, PackageLoader, select_autoescape
from typing import Dict

class Network(BaseDictable):

    def __init__(self, name="Network", data:Dict = {"nodes": [], "edges": []}, width="600px", height="400px"):
        only_show_data_attr = lambda attr: attr == "data"
        super().__init__(attr_filter_func=only_show_data_attr)
        self.name = name
        self.width = width
        self.height = height
        self.data = data
        self.env = Environment(
            loader=PackageLoader("pyvisjs"),
            autoescape=select_autoescape()
        )

    def __repr__(self):
        return f"Network(\'{self.name}\', \'{self.width}\', \'{self.height}\')"
    
    def add_node(self, node_id, label=None):
        if not [node.id for node in self.data["nodes"] if node.id == node_id]:
            self.data["nodes"].append(Node(node_id, label))

    def add_edge(self, from_id, to_id):
        self.add_node(from_id)
        self.add_node(to_id)

        if not [edge.start for edge in self.data["edges"] if edge.start == from_id and edge.end == to_id]:
            self.data["edges"].append(Edge(from_id, to_id))

    def to_dict(self):
        return super().to_dict()["data"]

    def show(self, file_name):
        self.render_template(open_in_browser=True, output_filename=file_name)

    def render_template(self, open_in_browser=False, save_to_output=False, output_filename="default.html", template_filename="basic.html") -> str:
        html_output = self.env \
            .get_template(template_filename) \
            .render(
                width=self.width,
                height=self.height,
                data=self.to_dict()
            )

        if save_to_output or open_in_browser:
            file_path = save_file(output_filename, html_output)

        if open_in_browser:
            open_file(file_path)

        return html_output
        
