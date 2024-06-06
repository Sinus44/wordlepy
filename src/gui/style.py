"""
Гайд по карте копирования
первый ключ - какая именно карта

карта копирования при создании стиля:
    второй ключ - из стиля какого элемента копировать при создании ЭТОГО стиля
    третий ключ - имя свойства ИЗ копируемого стиля
    значение для 3-го ключа - НОВОЕ название свойства

"""


class Style:
    COPY_MAP = {}

    def __init__(self):
        self._properties = {
            "normal": {},
            "hovered": {},
            "active": {},
            "disabled": {}
        }
        self.state = "normal"
        self.change_handlers = []
        self.__self = {}

    def _call_events(self):
        for handler in self.change_handlers:
            handler(None, self)

    def create_property(self, state, property_name, value=None):
        if state in self._properties:
            self._properties[state][property_name] = value
            self._call_events()
        else:
            raise Exception(f"Unknown state {state}")

    def set_property(self, state, property_name, value):
        if state in self._properties:
            if property_name in self._properties["normal"]:
                if self._properties[state].get(property_name) != value:
                    self._properties[state][property_name] = value
                    self._call_events()
            else:
                raise Exception(f"Cant set property {type(self).__name__}: Unknown property name {property_name}")
        else:
            raise Exception(f"Can't set property {type(self).__name__}: Unknown state {state}")

    def get_property(self, property_name):
        if self.state not in self._properties:
            raise Exception(f"Unknown state {self.state}")

        if property_name in self._properties[self.state]:
            return self._properties[self.state][property_name]

        elif property_name in self._properties["normal"]:
            return self._properties["normal"][property_name]

        else:
            raise Exception(f"Cant get property: Unknown property name {property_name}")

    """
    def copy_all_property(self, source_style, copying_name, name=None):
        name = name or copying_name

        for state in self._properties:
            if copying_name in source_style._properties[state]:
                self._properties[state][name] = source_style._properties[state][copying_name]

    def copy_property(self, source_style, copying_name, name=None):
        '''
        Only for normal state (source any state => self normal state) / условно, откуда (copying name) -> куда (name)
        '''
        name = name or copying_name
        self._properties["normal"][name] = source_style.get_property(copying_name)
    
    def copy_style(self, style):
        '''Copy all properties from style from args to this style'''

        for state_name in style._properties:
            # For every state from arg-style create dict in self properties if not exist
            self._properties[state_name] = self._properties[state_name] or {}

            # For every property from arg-style for every state, set self properties to arg-style properties
            for property_name in style._properties[state_name]:
                self._properties[state_name][property_name] = style._properties[state_name][property_name]
    
    """

    def copy_property_by_map(self, from_style, copy_map):
        for copy_name in copy_map:
            self._properties["normal"][copy_name] = from_style.get_property(copy_map[copy_name])

        self._call_events()

    def create_state(self, state_name):
        if state_name in self._properties:
            raise Exception(f"[ERROR] State \"{state_name}\" already exists")

        self._properties[state_name] = self._properties.get(state_name) or {}
        self._call_events()

    def copy_style_by_map(self, from_style, copy_map):
        for property_name in copy_map:
            if property_name not in from_style._properties["normal"]:
                raise Exception(f"При создании стиля \"{type(self).__name__}\" в карте копирования из стиля "
                                f"\"{type(from_style).__name__}\" произошла ошибка: параметр \"{property_name}\" не был"
                                f" обнаружен")

            self._properties["normal"][copy_map[property_name]] = from_style._properties["normal"][property_name]

        for property_name in from_style._properties["normal"]:
            if property_name not in copy_map:
                print(f"[WARNING] Из стиля \"{type(self).__name__}\" не передается параметр \"{property_name}\" в "
                      f"\"{type(from_style).__name__}\"")

        self._call_events()
