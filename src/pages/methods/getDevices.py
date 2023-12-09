
from .connect import   cucm


def getDeviceProfileUUID(devices):
    if "," in devices:
        splited_devices=devices.split(",")
        # print(splited_devices)
        uuids=[]
        for device in splited_devices:
            dev=cucm.get_device_profile(name=device)
            # print("uuid",dev["uuid"])
            uuids.append({'uuid':dev["uuid"][1:-1]})
        return {'profileName':uuids}
    else:
        try:
            device=cucm.get_device_profile(name=devices)
            # print("device uuid",device["uuid"])
            return {'profileName':{'uuid':device["uuid"][1:-1]}}
        except:
            pass

