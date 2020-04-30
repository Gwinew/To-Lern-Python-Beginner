class Foo:

    a_class_attribute = 0

    def __init__(self):
        self.an_instance_attribute = 42
        Foo.a_class_attribute = 64
        self.a_class_attribute = 'actually makes an instance attribute'

    @staticmethod
    def a_static_method():
        return 'No args, just lives in the class'

    @classmethod
    def a_class_method(cls):
        cls.a_class_attribute += 1

    @classmethod
    def a_named_constructor(cls):
        return cls()

    @property
    def a_property(self):
        return self.an_instance_attribute

    @a_property.setter
    def a_property(self, value):
        self.an_instance_attribute = value
