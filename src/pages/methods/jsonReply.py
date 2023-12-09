import ast
import copy
import imp
import json
import time
import streamlit as st

from pages.methods.getDevices import getDeviceProfileUUID
from pages.methods.submissions.devicesSubmit import devices_reply
from pages.methods.submissions.extensionSubmit import ex_reply
from pages.methods.submissions.userSubmit import user_update


# User_info_after={'firstName': st.session_state.firstName if st.session_state.firstName else None, 'displayName': st.session_state.displayName if st.session_state.displayName else None, 'middleName': st.session_state.middleName if st.session_state.middleName else None, 'lastName': st.session_state.lastName if st.session_state.lastName else None, 'userid': st.session_state.userid if st.session_state.userid else None,'newUserId': st.session_state.newUserId if st.session_state.newUserId  else None, 'password': st.session_state.password if st.session_state.password else None, 'pin': st.session_state.pin if st.session_state.pin else None, 'mailid': st.session_state.mailid if st.session_state.mailid else None, 'department': st.session_state.department if st.session_state.department else None, 'manager': st.session_state.manager if st.session_state.manager else None, 'userLocale': st.session_state.userLocale if st.session_state.userLocale else None, 'associatedDevices': {'device': st.session_state.associatedDevices if st.session_state.associatedDevices else None }, 'primaryExtension': {'pattern': st.session_state.associatedDevices.pasttern if st.session_state.associatedDevices.pasttern else None, 'routePartitionName': st.session_state.associatedDevices.routePartitionName if st.session_state.associatedDevices.routePartitionName else None}, 'associatedGroups': {'userGroup': st.session_state.userGroup if st.session_state.userGroup else None}, 'enableCti': st.session_state.enableCti if st.session_state.enableCti else None, 'digestCredentials': st.session_state.digestCredentials if st.session_state.digestCredentials else None, 'phoneProfiles': st.session_state.phoneProfiles if st.session_state.phoneProfiles else None, 'defaultProfile': { 'uuid': st.session_state.defaultProfile.uuid if st.session_state.defaultProfile.uuid else None }, 'presenceGroupName': {'_value_1': 'Standard Presence group', 'uuid': '{AD243D17-98B4-4118-8FEB-5FF2E1B781AC}'}, 'subscribeCallingSearchSpaceName': {'_value_1': None, 'uuid': None}, 'enableMobility': 'false', 'enableMobileVoiceAccess': 'false', 'maxDeskPickupWaitTime': 10000, 'remoteDestinationLimit': 4, 'associatedRemoteDestinationProfiles': None, 'passwordCredentials': 
# {'pwdCredPolicyName': {'_value_1': 'Default Credential Policy', 'uuid': None}, 'pwdCredUserCantChange': 'false', 'pwdCredUserMustChange': 'false', 'pwdCredDoesNotExpire': 'false', 'pwdCredTimeChanged': 'November 24, 2012 18:00:39 GMT', 'pwdCredTimeAdminLockout': None, 'pwdCredLockedByAdministrator': 'false', 'pwdResetHackCount': None}, 'pinCredentials': {'pinCredPolicyName': {'_value_1': 'Default Credential Policy', 'uuid': None}, 'pinCredUserCantChange': 'false', 'pinCredUserMustChange': 'false', 'pinCredDoesNotExpire': 'false', 'pinCredTimeChanged': 'November 24, 2012 18:00:39 GMT', 'pinCredTimeAdminLockout': None, 'pinCredLockedByAdministrator': 'false', 'pinResetHackCount': None}, 'associatedTodAccess': None, 'status': 1, 'enableEmcc': 'false', 'associatedCapfProfiles': None, 'ctiControlledDeviceProfiles': None, 'patternPrecedence': None, 'numericUserId': None, 'mlppPassword': None, 'customUserFields': None, 'homeCluster': 'true', 'imAndPresenceEnable': 'true', 'serviceProfile': {'_value_1': 'Default User Profile', 'uuid': '{BF83632F-A455-0CBF-A5A8-97FB424BE968}'}, 'lineAppearanceAssociationForPresences': {'lineAppearanceAssociationForPresence': [{'laapAssociate': {'_value_1': 't', 'uuid': None}, 'laapProductType': 'Cisco Jabber for Tablet', 'laapDeviceName': 'TABUSER009', 'laapDirectory': '1009', 'laapPartition': None, 'laapDescription': None, 'uuid': '{C2D4E9B5-BAA5-E01A-8342-25F2418B98E1}'}]}, 'directoryUri': None, 'telephoneNumber': None, 'title': None, 'mobileNumber': None, 
# 'homeNumber': None, 'pagerNumber': None, 'extensionsInfo': {'extension': [{'sortOrder': 0, 'pattern': {'_value_1': '1009', 'uuid': '{6B8989F2-4405-9736-9635-95B035C28549}'}, 'routePartition': None, 'linePrimaryUri': None, 'partition': None, 'uuid': '{791A8068-076A-3D0E-1155-C877548643C9}'}]}, 'selfService': '1009', 'userProfile': {'_value_1': None, 'uuid': None}, 'calendarPresence': 'true', 'ldapDirectoryName': {'_value_1': None, 'uuid': None}, 'userIdentity': None, 'nameDialing': None, 'ipccExtension': {'_value_1': None, 'uuid': None}, 'ipccRoutePartition': {'_value_1': None, 'uuid': None}, 'convertUserAccount': {'_value_1': None, 'uuid': None}, 'enableUserToHostConferenceNow': 'false', 'attendeesAccessCode': None, 'zeroHop': None, 'customerName': {'_value_1': None, 'uuid': None}, 'uuid': '{0F064897-107A-1788-A058-69D27ADD211D}'}

# def list_mapper(grouped,type):
#     if grouped==None:
#         return None
#     else:
#         gen2=[group for group in grouped["userGroup"] if grouped["userGroup"] ]
#         if type=="associatedGroups":
            
#             try:
#                 groups=[]
#                 for kgroup,vgroup in gen2.items():
#                     print("group1",group["name"])
#                 #     groups.append({"name":group})
#                 # return {"userGroup":groups}
#             except:
#                 print("error getting Agroups")
#         elif type=="phoneProfiles":
#             try:
#                 groups=[]
#                 for group in gen2:
#                     print("group2",group)
#                     getDeviceProfile(group)
#                     groups.append({"uuid":"BF83632F-A455-0CBF-A5A8-97FB424BE968"})
#                 return {"profileName":groups}
#             except:
#                 pass

def json_mapper(**reply):
    
    
    try:
        if reply['UserStatus']=='Active Enabled LDAP':
            try:
                if "" in st.session_state["newUserId"]:
                    del st.session_state["newUserId"]
                else:
                    reply["newUserId"]=st.session_state['newUserId'] if st.session_state['newUserId'] else None
            except:
                pass
            reply["firstName"]=st.session_state['firstName'] if st.session_state['firstName'] else None
            reply["middleName"]=st.session_state["middleName"] if st.session_state["middleName"] else None
            reply["lastName"]=st.session_state["lastName"] if st.session_state["lastName"] else None
            reply["userid"]=st.session_state['userid'] if st.session_state['userid'] else None
            reply["password"]=st.session_state['password'] if st.session_state['password'] else None
            reply["department"]=st.session_state['department'] if st.session_state['department'] else None
            reply["mailid"]=st.session_state['mailid'] if st.session_state['mailid'] else None
            reply["displayName"]=st.session_state['displayName'] if st.session_state['displayName'] else None
            reply["userIdentity"]=st.session_state['userIdentity'] if st.session_state['userIdentity'] else None
            reply["nameDialing"]=st.session_state['nameDialing'] if st.session_state['nameDialing'] else None
        reply["pin"]=st.session_state['pin'] if st.session_state['pin'] else None
        
        reply["userLocale"]=st.session_state['userLocale'] if st.session_state['userLocale'] else None
        # print(dict['associatedGroups']["userGroup"])
        reply["associatedDevices"]=[st.session_state['associatedDevices'][2:-2]] if st.session_state['associatedDevices'] else None
        
        reply["associatedGroups"]={"userGroup":[st.session_state['associatedGroups'][2:-2]]} if st.session_state['associatedGroups'] else None
        # print("still running")
        reply["phoneProfiles"]=getDeviceProfileUUID(st.session_state['phoneProfiles'][2:-2]) if st.session_state['phoneProfiles'] else None
        reply["ctiControlledDeviceProfiles"]=getDeviceProfileUUID(st.session_state['phoneProfiles'][2:-2]) if st.session_state['phoneProfiles'] else None
        reply["defaultProfile"]=st.session_state["defaultProfile"] if st.session_state["defaultProfile"] else None
        reply["primaryExtension"]={'pattern':str(st.session_state["primaryExtension"]).rsplit('/')[0]} if st.session_state["primaryExtension"] else None
        reply["homeCluster"]=st.session_state['homeCluster'] if st.session_state['homeCluster'] else False
        reply["imAndPresenceEnable"]=st.session_state['imAndPresenceEnable'] if st.session_state['imAndPresenceEnable'] else False
        reply["calendarPresence"]=st.session_state['calendarPresence'] if st.session_state['calendarPresence'] else False
        reply["enableCti"]=st.session_state['enableCti'] if st.session_state['enableCti'] else False
        reply["enableEmcc"]=st.session_state['enableEmcc'] if st.session_state['enableEmcc'] else False
        reply["enableMobility"]=st.session_state['enableMobility'] if st.session_state['enableMobility'] else False
        reply["enableMobileVoiceAccess"]=st.session_state['enableMobileVoiceAccess'] if st.session_state['enableMobileVoiceAccess'] else False
        reply["maxDeskPickupWaitTime"]=st.session_state['maxDeskPickupWaitTime'] if st.session_state['maxDeskPickupWaitTime'] else 1000
        reply["remoteDestinationLimit"]=st.session_state['remoteDestinationLimit'] if st.session_state['remoteDestinationLimit'] else 4
       
    except:
        print("error in json_mapper reply values")
        pass


    
    
    try:
        if "lineAppearanceAssociationForPresences" in reply:
            del reply["lineAppearanceAssociationForPresences"]
        if "extensionsInfo" in reply:
            del reply["extensionsInfo"]
        
        
    except:
        pass
    user_update(**reply)



def device_mapper(*data):
    # print("device_mapper",list(data))
    list_devices=list(data)
    # devices=[]
    reply_devices=[]
    dev={}
    # # gen1=
    # keys=[]
    gen1=[key.split(",") for key in st.session_state.keys() if "," in key]
    # # gen2={k:v }
    for key in gen1:
        gen2=[device for device in list_devices if key[0]==device['name'] ]
        
        gen3=[device for device in gen2 if key[1]!="line"]
        for device in gen3:
            
            
            try:
                device[f'{key[1]}']=st.session_state[f'{key[0]},{key[1]}']
            except:
                pass
            try:
                device[f'{key[1]}'][f'{key[2]}']=st.session_state[f'{key[0]},{key[1]},{key[2]}']
            except:
                pass
        gen4=[device for device in gen2 if key[1]=="line"]
        for device in gen4:
            # if device['lines'] else None
            try:
                del device['lines']['lineIdentifier']
            except:
                pass
            for line in device['lines']['line'] :
                try:

                    del line['uuid']
                    del line['ctiid']
                    del line['recordingMediaSource']
                    del line['partitionUsage']
                    del line['speedDial']
                    del line['audibleMwi']
                    del line['recordingFlag']
                    del line['monitoringCssName']
                    del line['recordingProfileName']
                    del line['mwlPolicy']
                    del line['dialPlanWizardId']
                    del line['ringSettingActivePickupAlert']
                    del line['ringSettingIdlePickupAlert']
                    del line['consecutiveRingSetting']
                    del line['ringSetting']
                    

                except:
                    pass

                if key[2]==line['dirn']['pattern']:
                    # print(line['dirn']['pattern'],st.session_state[f'{key[0]},{key[1]},{key[2]},{key[3]},dirn,pattern'])
                    if st.session_state[f'{key[0]},{key[1]},{key[2]},{key[3]},associatedEndusers,enduser']:
                        # x=st.session_state[f'{key[0]},{key[1]},{key[2]},{key[3]},associatedEndusers,enduser']
                        # x=ast.literal_eval(x)
                        # eu_list=[]
                        # # print("associatedEndusers")
                        # endUsers=copy.deepcopy(st.session_state[f'{key[0]},{key[1]},{key[2]},{key[3]},associatedEndusers,enduser'])
                        # eu=endUsers.strip("][\"'")
                        # print(eu,type(eu))
                        # if "," in eu:
                        #     eu_list=endUsers.split(",")
                        # else:
                        #     eu_list.append(eu)
                        # print(eu_list,type(eu_list))
                        # line['associatedEndusers']['enduser']=list()
                        # print("line['associatedEndusers']['enduser']",line['associatedEndusers'])
                        # line['associatedEndusers']['enduser']=list(eu_list)
                        # print("newEndusers",line['associatedEndusers'])
                        # line['associatedEndusers']={'enduser':eu_list}
                        line['associatedEndusers']['enduser']=[st.session_state[f'{key[0]},{key[1]},{key[2]},{key[3]},associatedEndusers,enduser'][2:-2]]

                    if len(key)==5:
                        line[f'{key[4]}']=st.session_state[f'{key[0]},{key[1]},{key[2]},{key[3]},{key[4]}']
                        # print('5keys',st.session_state[f'{key[0]},{key[1]},{key[2]},{key[3]},{key[4]}'])
                    
                    elif len(key)==6:
                        line[f'{key[4]}'][f'{key[5]}']=st.session_state[f'{key[0]},{key[1]},{key[2]},{key[3]},{key[4]},{key[5]}']
                    elif len(key)==7:
                        line[f'{key[4]}'][f'{key[5]}'][f'{key[6]}']=st.session_state[f'{key[0]},{key[1]},{key[2]},{key[3]},{key[4]},{key[5]},{key[6]}']
                        # print('6keys',st.session_state[f'{key[0]},{key[1]},{key[2]},{key[3]},{key[4]},{key[5]}'])

                
    
    for device in list_devices:
        dev['name']=device['name']
        dev['phoneTemplateName']=device['phoneTemplateName']
        dev['softkeyTemplateName']=device['softkeyTemplateName']
        if 'callingSearchSpaceName' in device.keys():
            dev['callingSearchSpaceName']=device['callingSearchSpaceName']
        if 'devicePoolName' in device.keys():
            
            dev['devicePoolName']=device['devicePoolName']
            if dev['devicePoolName']["uuid"] or dev['devicePoolName']["uuid"]==None:
                del dev['devicePoolName']["uuid"]
        if dev['phoneTemplateName']["uuid"] or dev['phoneTemplateName']["uuid"]==None:
            del dev['phoneTemplateName']["uuid"]
        if dev['softkeyTemplateName']["uuid"] or dev['softkeyTemplateName']["uuid"]==None:
            del dev['softkeyTemplateName']["uuid"]
       
        
        
        dev['lines']=device['lines']
      
        reply_devices.append(dev)
        print("reply_devices",reply_devices)
        # st.session_state['reply_devices']=reply_devices
    # reply_devices_tuple=tuple(reply_devices)
    # print(reply_devices)
        devices_reply(*reply_devices)



def ex_mapper():
    lines=[]
    gen1=[key.split(",") for key in st.session_state.keys() if "," in key]
    print("ex_mapper is working")
    for key in gen1:
        # gen2=[line for line in st.session_state['lines'] ]

        for line in st.session_state['lines']:
            if key[0]==line['pattern'] and str(key[1])==str(line['routePartitionName']['_value_1']) :
                if key[2]=='forwardCSS':
                    line["callForwardAll"]["callingSearchSpaceName"]=line["callForwardAll"]["secondaryCallingSearchSpaceName"]=line["callForwardBusy"]["callingSearchSpaceName"]=line["callForwardBusyInt"]["callingSearchSpaceName"]=line["callForwardNoAnswer"]["callingSearchSpaceName"]=line["callForwardNoAnswerInt"]["callingSearchSpaceName"]=line["callForwardNoCoverage"]['callingSearchSpaceName']=line["callForwardNoCoverageInt"]['callingSearchSpaceName']=line["callForwardOnFailure"]['callingSearchSpaceName']=line["callForwardAlternateParty"]['callingSearchSpaceName']=line["callForwardNotRegistered"]['callingSearchSpaceName']=line["callForwardNotRegisteredInt"]['callingSearchSpaceName']=st.session_state[f'{key[0]},{key[1]},forwardCSS']
                elif key[2]=='forwardTime':
                    line["callForwardNoAnswer"]=line["callForwardNoAnswerInt"]={'duration':st.session_state[f'{key[0]},{key[1]},forwardTime']}
                    # print('forwardTime S')
                elif len(key)==3 and key[2]!='forwardTime' and key[2]!='forwardCSS':
                    line[f'{key[2]}']=st.session_state[f'{key[0]},{key[1]},{key[2]}']
                    # print("newPattern",key[2])
                    # print('key2 S')
                elif key[2]=='callForwardAll':
                    line[f'{key[2]}'][f'{key[3]}']=st.session_state[f'{key[0]},{key[1]},{key[2]},{key[3]}']
                    # print('callForwardAll S')

                elif len(key)==4 and key[2]!='callForwardAll' :
                    line[f'{key[2]}'][f'{key[3]}']=st.session_state[f'{key[0]},{key[1]},{key[2]},{key[3]}']
                elif len(key)==4 and key[2]=='callForwardNoAnswer' or key[2]=='callForwardBusy':
                    ##should apply for forwarding only
                    line[f'{key[2]}Int'][f'{key[3]}']=st.session_state[f'{key[0]},{key[1]},{key[2]},{key[3]}']
                    # print('key4 S')
                # lines.append(line)

    for line in st.session_state['lines']:
        # print("line",line)




        reply_line={}
        # print('linenewPattern',line['newPattern'])
        if  line['newPattern']!='':
            reply_line['newPattern']=line['newPattern']
        # print("ex_mapper is working1")
        reply_line['uuid']=line['uuid']
        # reply_line['pattern']=line['pattern']
        # print(reply_line,"2")
        # reply_line['routePartitionName']=line['routePartitionName']
        reply_line['description']=line['description']
        reply_line['asciiAlertingName']=line['asciiAlertingName']
        reply_line['alertingName']=line['alertingName']
        reply_line['voiceMailProfileName']=line['voiceMailProfileName']
        # reply_line["callForwardNoAnswer"]=reply_line["callForwardNoAnswerInt"]={'duration':line["callForwardNoAnswer"]['duration']}
        reply_line["callForwardAll"]=line['callForwardAll']
        reply_line["callForwardBusy"]=reply_line["callForwardBusyInt"]=line['callForwardBusy']
        # reply_line["associatedDevices"]=[line['associatedDevices']['device'][2:-2]]
        reply_line["callForwardNoAnswer"]=reply_line["callForwardNoAnswerInt"]=line['callForwardNoAnswer']
        # 
    
        # # =line['callForwardNoAnswer,destination']
        reply_line['shareLineAppearanceCssName']=line['shareLineAppearanceCssName'] 
        reply_line["callForwardAll"]["callingSearchSpaceName"]=reply_line["callForwardAll"]["secondaryCallingSearchSpaceName"]=reply_line["callForwardBusy"]["callingSearchSpaceName"]=reply_line["callForwardBusyInt"]["callingSearchSpaceName"]=reply_line["callForwardNoAnswer"]["callingSearchSpaceName"]=reply_line["callForwardNoAnswerInt"]["callingSearchSpaceName"]=line["callForwardAll"]["callingSearchSpaceName"]
        reply_line["callForwardNoCoverage"]=reply_line["callForwardNoCoverageInt"]=reply_line["callForwardOnFailure"]=reply_line["callForwardAlternateParty"]=reply_line["callForwardNotRegistered"]=reply_line["callForwardNotRegisteredInt"]={'callingSearchSpaceName':line["callForwardAll"]["callingSearchSpaceName"]}
        
        ex_reply(**reply_line)
   