from .base_dictable import BaseDictable

class Edge(BaseDictable):
    def __init__(self, start: int, end: int):
        mapping = {
            "start": "from",
            "end": "to"
        }
        change_start_to_from_and_end_to_to = lambda attr: mapping.get(attr, attr)
        super().__init__(attr_map_func = change_start_to_from_and_end_to_to)
        self.start = start
        self.end = end

    def __repr__(self):
        return f"Edge({self.start}, {self.end})"