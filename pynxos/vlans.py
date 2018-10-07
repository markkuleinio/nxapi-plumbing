from pynxos.converters import converted_list_from_table
from pynxos.key_maps import VLAN_KEY_MAP


class BaseFeature(object):
    def __init__(self, device):
        self.device = device

    def get(self, vlan_id):
        raise NotImplementedError

    def get_list(self):
        raise NotImplementedError

    def get_all(self):
        raise NotImplementedError

    def config(self, vlan_id, **params):
        raise NotImplementedError

    def remove(self, vlan_id):
        raise NotImplementedError


class Vlans(BaseFeature):
    def __init__(self, device):
        super(Vlans, self).__init__(device)

    def get_list(self):
        all_vlan_list = self.get_all()
        vlan_id_list = list(str(x["id"]) for x in all_vlan_list)
        return vlan_id_list

    def get_all(self):
        all_vlan_table = self.device.show("show vlan")
        all_vlan_list = converted_list_from_table(
            all_vlan_table, "vlanbrief", VLAN_KEY_MAP
        )
        return all_vlan_list
