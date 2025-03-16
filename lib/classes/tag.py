class Tag:
    def __init__(self, class_name, atribute, value):
        self.tag = f"{class_name.upper()}_{atribute.upper()}"
        self.value = value
    
class Dictionary:
    def __init__(self, *instances):
        self.tags = (self.generate_dictionary(instances))
        
    def generate_dictionary(self, instances):
        tags = []
        
        for instance in instances:
            class_name = instance.__class__.__name__
            
            for atribute, value in vars(instance).items():
                if isinstance(value, list) and all(hasattr(v, "html_list") for v in value):
                    tag_value = "".join([v.html_list() for v in value])
                else:
                    tag_value = value
                tags.append(Tag(class_name, atribute, tag_value))
        return tags