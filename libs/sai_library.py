from sai_methods.deflt_dev_methods import *


# ********************************************************************************
class Device:

    def __init__(self, dev_name='', dev_id='', dev_type='', dev_status=INACTIVE,
                 dev_state=IDLE, dev_value=None, dev_area=None):
        self.dev_properties = dict(dev_name=dev_name,
                                   dev_id=dev_id,
                                   dev_type=dev_type,
                                   dev_status=dev_status,
                                   dev_state=dev_state,
                                   dev_value=dev_value,
                                   dev_area=dev_area,
                                   dev_method=assign_method(dev_type),
                                   icon='',)

    def __delete__(self, instance):
        del instance
        return None


    # ***** setters methods *****
    def set_name(self, dev_name):
        self.dev_properties['dev_name'] = dev_name
        return 0

    def set_id(self, dev_id):
        self.dev_properties['dev_id'] = dev_id
        return 0

    def set_type(self, dev_type):
        self.dev_properties['dev_type'] = dev_type
        return 0

    def set_method(self, dev_method):
        self.dev_properties['dev_method'] = dev_method
        return 0

    def set_status(self, dev_status):
        self.dev_properties['dev_status'] = dev_status
        return 0

    def set_properties(self, dev_name='', dev_id='', dev_type='', dev_method=None, dev_status=None):
        self.set_name(dev_name)
        self.set_id(dev_id)
        self.set_type(dev_type)
        self.set_method(dev_method)
        self.set_status(dev_status)
        return 0


    # ***** getters methods *****
    def get_name(self):
        return self.dev_properties['dev_name']

    def get_id(self):
        return self.dev_properties['dev_id']

    def get_type(self):
        return self.dev_properties['dev_type']

    def get_status(self):
        return self.dev_properties['dev_status']

    def get_properties(self):
        return self.dev_properties

    def method_call(self, action=None, params=()):
        return self.dev_properties['dev_method'](self, action, *params)
# ********************************************************************************


# ********************************************************************************
class HomeArea:

    def __init__(self, ha_name=''):
        self.ha_properties = dict(ha_name=ha_name,
                                  ha_devices=dict(),
                                  icon='',)

    def set_name(self, ha_name=''):
        self.ha_properties['ha_name'] = ha_name
        return 0

    def add_device(self, c_device=None):
        self.ha_properties['ha_devices'][c_device.get_name()] = c_device
        return 0

    def get_devices_list(self):
        return self.ha_properties['ha_devices'].keys()

    def get_name(self):
        return self.ha_properties['ha_name']

    def remove_device(self, dev_name=''):
        del self.ha_properties['ha_devices'][dev_name]
# ********************************************************************************


# ********************************************************************************
class Home:

    def __init__(self, home_name=''):
        self.home = dict(home_name=home_name,
                         homeareas=dict(),
                         icon='',)

    def add_area(self, home_area=None):
        self.home['homeareas'][home_area.get_name()] = home_area
        return 0


    def get_areas_list(self):
        return self.home['homeareas'].keys()


    def get_areas_obj(self):
        return [area_obj for area_obj in self.home['homeareas'].itervalues()]


    def get_name(self):
        return self.home['home_name']
# ********************************************************************************
