from tracking_decorator.trash_collections import trash_collection

def track_changes(*attributes):
    def class_decorator(cls):
        original_init = cls.__init__

        def remove_specification(attribute_name):
            if attribute_name.endswith('_r') or attribute_name.endswith('_d'):
                return attribute_name[:-2]
            return attribute_name

        def make_getter(attribute_name):
            storage_name = '_' + attribute_name
            def getter(self):
                return getattr(self, storage_name)
            return getter

        def make_setter(attribute_name, attribute_to_track):
            storage_name = '_' + attribute_name

            def setter(self, value):
                self.tracked_attributes.add(attribute_to_track)
                setattr(self, storage_name, value)
                    
            return setter
        
        def make_only_change_setter(attribute_name, attribute_to_track):
            storage_name = '_' + attribute_name

            def setter(self, value):
                if getattr(self, storage_name) != value:
                    self.tracked_attributes.add(attribute_to_track)
                    setattr(self, storage_name, value)
                    
            return setter
        
        def make_collection_removal_setter(attribute_name, attribute_to_track):
            storage_name = '_' + attribute_name

            def setter(self, value):
                self.tracked_attributes.add(attribute_to_track)
                TrashCollection = trash_collection(value)
                setattr(self, storage_name, TrashCollection)

            return setter

        for attribute in attributes:
            if isinstance(attribute, tuple):
                attribute, attribute_to_track = attribute
            else:
                attribute, attribute_to_track = attribute, remove_specification(attribute)

            if attribute.endswith('_r'):
                attribute = attribute[:-2]
                setter_func = make_collection_removal_setter(attribute, attribute_to_track)
            elif attribute.endswith('_d'):
                attribute = attribute[:-2]
                setter_func = make_only_change_setter(attribute, attribute_to_track)
            else:
                setter_func = make_setter(attribute, attribute_to_track)

            getter_func = make_getter(attribute)

            setattr(cls, attribute, property(getter_func, setter_func))

        # Modify the __init__ to initialize properties
        def new_init(self, *args, **kwargs):
            self.tracked_attributes = set()

            for attribute_name in attributes:
                if isinstance(attribute_name, tuple):
                    attribute_name = attribute_name[0]
                attribute_name = remove_specification(attribute_name)
                storage_name = '_' + attribute_name
                setattr(self, storage_name, None)

            original_init(self, *args, **kwargs)
            self.clear()

        def clear(self):
            self.tracked_attributes.clear()
        
        cls.__init__ = new_init
        cls.clear = clear
        return cls
    
    return class_decorator