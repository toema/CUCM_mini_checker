from .connect import   cucm
from zeep import helpers
import streamlit as st

def get_extensions(*lines):
    # print(lines)
    deviceLine={}
    lines_res=[]
    for line in lines:
        line_exists=False
        if line["dirn"]["routePartitionName"]["_value_1"]:
            deviceLine=helpers.serialize_object(cucm.get_directory_number(pattern=f'{line["dirn"]["pattern"]}',routePartitionName=f'{line["dirn"]["routePartitionName"]["_value_1"]}'),dict)
            
        else:
            deviceLine=helpers.serialize_object(cucm.get_directory_number(pattern=f'{line["dirn"]["pattern"]}'),dict)
            print(deviceLine["uuid"])
        try:
            for line in lines_res:
                if line["uuid"]==deviceLine["uuid"]:
                    print(deviceLine)
                    line_exists=True
                
        except:
            print("cannot find lines")
        if not line_exists:
                    lines_res.append(deviceLine)
                
        # print("deviceLine",deviceLine)
    st.session_state["lines"]=lines_res


    pass

def get_devices(user):
    if user["primaryExtension"]["pattern"]:


        UserDevicesFind=cucm.list_route_plan_specific(pattern=user["primaryExtension"]["pattern"])
        # print(UserDevicesFind)
        if UserDevicesFind["return"]!=None:
            gen1=[device for device in UserDevicesFind["return"]["routePlan"] if device["type"]=="Device"]
            devices=[]

            for device in gen1:
                # print("devicev",device["routeDetail"])
                # try:
                devicePhone=helpers.serialize_object(cucm.get_phone(name=f'{device["routeDetail"]}'),dict)
                devices.append(devicePhone)
                # except:
                #     deviceProfile=helpers.serialize_object(cucm.get_device_profile(name=f'{device["routeDetail"]}'),dict)
                #     # print("deviceProfile",deviceProfile)
                #     devices.append({"type":"Profile","device":deviceProfile})

            with open("temp.json","a",encoding ='utf8') as file:
                import json,time
                json.dump({"action":"get devices","component":devices,"time":time.asctime()},file, indent=4)
                json.dump(file,separators=',')

            return(devices)
        
# def get_CCS(device):
#     if device['callingSearchSpaceName']
                
def get_assocaited_devices(user):
    

    devices=[]
    lines=[]
    if user["associatedRemoteDestinationProfiles"]:
        print(user["associatedRemoteDestinationProfiles"]["remoteDestinationProfile"])
    if user["associatedDevices"]:

        for device in user["associatedDevices"]["device"]:
            
            devicePhone=helpers.serialize_object(cucm.get_phone(name=device),dict)
            devices.append(devicePhone)
            if devicePhone['lines']:
                for line in devicePhone['lines']['line']:
                    lines.append(line)
    if  user['phoneProfiles']:
        
        for device in user['phoneProfiles']['profileName']:
            
            devicePhone=helpers.serialize_object(cucm.get_device_profile(name=device["_value_1"]),dict)
            devices.append(devicePhone)
            # print("devicePhone",devicePhone)
            if devicePhone['lines']:
                for line in devicePhone['lines']['line']:
                    lines.append(line)
    get_extensions(*lines)
    with open("temp.json","a",encoding ='utf8') as file:
                import time,json
                json.dump({"action":"get devices","component":devices,"time":time.asctime()},file, indent=4)
                file.write(",")
    return(devices)
    # if user["associatedDevices"]["device"]:

    
# def get_assocaited_RDP(user)


                
        # print(UserDevicesFind["return"]["routePlan"])
    
