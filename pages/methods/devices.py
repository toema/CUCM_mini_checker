
import copy
import streamlit as st
from pages.methods.gets import get_assocaited_devices
from pages.methods.jsonReply import device_mapper
from collections import defaultdict


def device_page(userInfo):
    # print("userInfo",userInfo)
    devices=get_assocaited_devices(userInfo)
    # print("devicepage",devices)
    with st.form("Devices_info"):
        
        st.form_submit_button(label="Submit",on_click=device_mapper,args=copy.deepcopy(devices))
        
        for device in devices:
            # deviceInfo=device["device"]
            # print(device["type"])
            dev_name=defaultdict(dict)
            with st.container():
                col1,col2=st.columns(2)
                with col1:
                    st.subheader(device["class"]+"-"+device["name"])
                    name=st.text_input(label="Device Name", value=device["name"],key=f'{device["name"]},name')
                    model=st.text_input(label="Model", value=device["model"],key=f'{device["name"]},model',disabled=True)
                    protocol=st.text_input(label="Protocol", value=device["protocol"],key=f'{device["name"]},protocol',disabled=True)
                    phoneTemplateName=st.text_input(label="Phone Button Template", value=device["phoneTemplateName"]["_value_1"] if device["phoneTemplateName"] else None,key=f'{device["name"]},phoneTemplateName,_value_1')
                    softkeyTemplateName=st.text_input(label="Softkey Template", value=device["softkeyTemplateName"]["_value_1"] if device["softkeyTemplateName"] else None,key=f'{device["name"]},softkeyTemplateName,_value_1')
                    userLocale=st.text_input(label="User Locale", value=device["userLocale"] if device["userLocale"] else None,key=f'{device["name"]},userLocale')
                    if "callingSearchSpaceName" in device:
                        callingSearchSpaceName=st.text_input(label="Calling Search Space", value=device["callingSearchSpaceName"]["_value_1"] if device["callingSearchSpaceName"] else None,key=f'{device["name"]},callingSearchSpaceName')
                    if "devicePoolName" in device:
                        devicePoolName=st.text_input(label="Device Pool", value=device["devicePoolName"]['_value_1'] if device["devicePoolName"]else None,key=f'{device["name"]},devicePoolName,_value_1')
                    # uuid=st.text_input(label="User Locale", value=device["uuid"] ,key=f'{device["name"]},uuid',disabled=True)
                    st.markdown("---")
                with col2:
                    if device["lines"]!=None:
                        for line in device["lines"]["line"]:
                            st.subheader(line["dirn"]["pattern"]+"("+f'{line["dirn"]["routePartitionName"]["_value_1"] if line["dirn"]["routePartitionName"]["_value_1"] else None}' +")"+"=>"+device["name"])
                            index=st.text_input(label="Index", value=line["index"],key=f'{device["name"]},line,{line["dirn"]["pattern"]},{line["dirn"]["routePartitionName"]["_value_1"]},index')
                            pattern=st.text_input(label="Pattern", value=line["dirn"]["pattern"],key=f'{device["name"]},line,{line["dirn"]["pattern"]},{line["dirn"]["routePartitionName"]["_value_1"]},dirn,pattern')
                            routePartitionName=st.text_input(label="Partition", value=line["dirn"]["routePartitionName"]["_value_1"],key=f'{device["name"]},line,{line["dirn"]["pattern"]},{line["dirn"]["routePartitionName"]["_value_1"]},dirn,routePartitionName,_value_1')
                            display=st.text_input(label="Display (Caller ID)", value=line["display"],key=f'{device["name"]},line,{line["dirn"]["pattern"]},{line["dirn"]["routePartitionName"]["_value_1"]},display')
                            displayAscii=st.text_input(label="ASCII Display (Caller ID)", value=line["displayAscii"],key=f'{device["name"]},line,{line["dirn"]["pattern"]},{line["dirn"]["routePartitionName"]["_value_1"]},displayAscii')
                            label=st.text_input(label="Line Text Label", value=line["label"],key=f'{device["name"]},line,{line["dirn"]["pattern"]},{line["dirn"]["routePartitionName"]["_value_1"]},label')
                            e164Mask=st.text_input(label="External Phone Number Mask", value=line["e164Mask"],key=f'{device["name"]},line,{line["dirn"]["pattern"]},{line["dirn"]["routePartitionName"]["_value_1"]},e164Mask')
                            missedCallLogging=st.checkbox(label="Log Missed Calls", value=line["missedCallLogging"] if line["missedCallLogging"]=='true' else False ,key=f'{device["name"]},line,{line["dirn"]["pattern"]},{line["dirn"]["routePartitionName"]["_value_1"]},missedCallLogging')
                            maxNumCalls=st.text_input(label="Maximum Number of Calls", value=line["maxNumCalls"],key=f'{device["name"]},line,{line["dirn"]["pattern"]},{line["dirn"]["routePartitionName"]["_value_1"]},maxNumCalls')
                            busyTrigger=st.text_input(label="Busy Trigger", value=line["busyTrigger"],key=f'{device["name"]},line,{line["dirn"]["pattern"]},{line["dirn"]["routePartitionName"]["_value_1"]},busyTrigger')
                            with st.container():
                                st.subheader("Forwarded Call Information Display")
                                callerName=st.checkbox(label="Caller Name", value=line["callInfoDisplay"]["callerName"] if line["callInfoDisplay"]["callerName"]=="true" else False,key=f'{device["name"]},line,{line["dirn"]["pattern"]},{line["dirn"]["routePartitionName"]["_value_1"]},callInfoDisplay,callerName')
                                callerNumber=st.checkbox(label="Caller Number", value=line["callInfoDisplay"]["callerNumber"] if line["callInfoDisplay"]["callerNumber"]=="true" else False,key=f'{device["name"]},line,{line["dirn"]["pattern"]},{line["dirn"]["routePartitionName"]["_value_1"]},callInfoDisplay,callerNumber')
                                redirectedNumber=st.checkbox(label="Redirected Number", value=line["callInfoDisplay"]["redirectedNumber"] if line["callInfoDisplay"]["redirectedNumber"]=="true" else False,key=f'{device["name"]},line,{line["dirn"]["pattern"]},{line["dirn"]["routePartitionName"]["_value_1"]},callInfoDisplay,redirectedNumber')
                                dialedNumber=st.checkbox(label="Dialed Number", value=line["callInfoDisplay"]["dialedNumber"] if line["callInfoDisplay"]["dialedNumber"]=='true' else False,key=f'{device["name"]},line,{line["dirn"]["pattern"]},{line["dirn"]["routePartitionName"]["_value_1"]},callInfoDisplay,dialedNumber')
                            associatedEndusers=st.text_input(label="Associated End Users", value= [v['userId'] for v in line["associatedEndusers"]["enduser"]] if line["associatedEndusers"] else None,key=f'{device["name"]},line,{line["dirn"]["pattern"]},{line["dirn"]["routePartitionName"]["_value_1"]},associatedEndusers,enduser'
                                                             ,help="For now it only support 1 user"
                                                            #  ,help="e.g. [\"userid1\",\"userid2\",...]\n For Empty [][Empty Brackets]"
                                                             
                                                             )
                        st.markdown("---")
