#/usr/local/bin/python
'Maya-Assist Storage system'
class Room(object):
    def __init__(self, idc, location, name):
        self.ROOM_IDC = idc
        self.location = location
        self.name = name

        self.exist = True
        self.room_systems = {}

        def get_room_systems(self):
            return self.room_systems
        def get_ROOM_IDC(self):
            return self.ROOM_IDC
        def get_location(self):
            return self.location
        def get_name(self):
            return self.name
        def get_exist(self):
            return self.exist

        def set_location(self, var):
            self.location = var
        def set_name(self, var):
            self.name = var
        def set_exist(self, var):
            self.exist = var

class System(object):
    def __init__(self, idc, location, name):
        self.SYSTEM_IDC = idc
        self.location = location
        self.name = name

        self.system_chests = {}
        self.exist = True

        def get_SYSTEM_IDC(self):
            return self.SYSTEM_IDC
        def get_location(self):
            return self.location
        def get_name(self):
            return self.name
        def get_system_chests(self):
            return self.system_chests

        def set_location(self, var):
            self.location = var
        def set_name(self, var):
            self.name = var
        def set_exist(self, var):
            self.exist = var

class Chest(object):
    def __init__(self, system_idc, chest_idc, location, color = 'unkown', name):
        self.system_idc = system_idc
        self.CHEST_IDC = chest_idc
        self.location = location

        self.color = color

        self.name = name

        self.exist = True

        def get_system_idc(self):
            return self.system_idc
        def get_CHEST_IDC(self):
            return self.CHEST_IDC
        def get_location(self):
            return self.location
        def get_name(self):
            return self.name
        def get_exist(self):
            return self.exist

        def set_system_idc(self, var):
            self.system_idc = var
        def set_location(self, var):
            self.location = var
        def set_name(self, var):
            self.exist = var
class Product(object):
    def __init__(self, produkt_idc, chest_idc, name, value = 'Unkown', weight = 'Unkown', mass = 'Unkown'):
        self.PRODUCT_IDC = produkt_idc
        self.chest_idc = chest_idc
        self.name = name
        self.value = value
        self.weight = weight
        self.mass = mass

        self.exist = True

        def get_PRODUCT_IDC(Self):
            return self.PRODUCT_IDC
        def get_chest_idc(self):
            return self.chest_idc