class BaseDictable:

    def __init__(self, attr_filter_func=None, attr_map_func=None):
        self.attr_filter_func = attr_filter_func or (lambda x: x)
        self.attr_map_func = attr_map_func or (lambda x: x)

    def to_dict(self):
        result = {}

        def has_to_dict(attr):
            return hasattr(attr, "to_dict") and callable(getattr(attr, "to_dict"))
        
        def process_attr(attr):
            return attr.to_dict() if has_to_dict(attr) else attr
        
        def process_list(lst):
            return [process_attr(item) for item in lst]
        
        def process_dict(dict):
            return {key: process_list(value) if isinstance(value, list) else process_attr(value) for (key, value) in attr_value.items()}
        


        for attr_name in list(filter(self.attr_filter_func, dir(self))):
            if not attr_name.startswith("__"):
                attr_value = getattr(self, attr_name)
                attr_name = self.attr_map_func(attr_name)
                if callable(attr_value):
                    continue
                elif isinstance(attr_value, list):
                    result[attr_name] = process_list(attr_value)
                elif isinstance(attr_value, dict):
                    result[attr_name] = process_dict(attr_value)
                elif has_to_dict(attr_value):
                    result[attr_name] = attr_value.to_dict()
                else:
                    result[attr_name] = attr_value
                    
        return result