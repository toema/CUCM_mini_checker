import streamlit as st
from pages.methods.jsonReply import json_mapper



# from pages.methods.getusers import getUsers
# def json_reply(**reply):
#     json_mapper(reply=reply)
    # user_info_after={'firstName':st.session_state.firstName,'lastName':st.session_state.lastName,'middleName':st.session_state.middleName,'displayName':st.session_state.displayName,'userid':st.session_state.userid,'password':st.session_state.password,'pin':st.session_state.pin,'mailid':st.session_state.mailid,'newUserid':st.session_state.newUserid}
    # st.write(st.session_state)
    # print('user_info_after',user_info_after)
    
    # try:
    #     if '' in user_info_after['newUserid']:
    #         del user_info_after['newUserid']
    # except:
        # pass
    # print(reply)
st.markdown("""<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" />""",unsafe_allow_html=True)

def ldap_status(userInfo):
    if userInfo['status']==1 and userInfo["ldapDirectoryName"]['_value_1']!=None:
        return "Active Enabled LDAP"
    elif userInfo['status']==1 and userInfo["ldapDirectoryName"]['_value_1']==None:
        return "Enabled Local User"
    else:
        return "undefined"
    


def list_map(data):
    if data==None:
        return ""
    groups=[]
    if "userGroup" in data:
        for g in data["userGroup"] or data["profileName"]:
            gen1=[v for k,v in g.items() if k=="name" ]
        for k in gen1:
            groups.append(k)
        return groups
    elif "profileName" in data:
        for g in data["profileName"]:
            gen1=[v for k,v in g.items() if  k=="_value_1"]
        for k in gen1:
            groups.append(k)
        return groups
    # elif "remoteDestinationProfile" in data:
    #     for g in data["remoteDestinationProfile"]:
    #     #     gen1=[v for k,v in g.items() if  k=="_value_1"]
    #     # for k in gen1:
    #         groups.append(g)
    #     return groups

def EU_page(userInfo):
    # print("userInfo",userInfo)
    with st.form("User_basic_info"):
        
        st.form_submit_button(label="Submit",on_click=json_mapper)


        col1,col2=st.columns(2)
        
        UserStatus=st.text_input(label="User status", value=ldap_status(userInfo),disabled=True,key='UserStatus')
        with col1:
            userid=st.text_input(label="User iD", value=userInfo["userid"],disabled=True,key='userid')
        with col2:
            newUserid=st.text_input(label="New User iD",key='newUserid')
        password=st.text_input(label="Password", value=userInfo["password"],type='password',key='password')
        digestCredentials=st.text_input(label="Digest Credentials", value=userInfo["digestCredentials"],type='password',key='digestCredentials')
        selfService=st.text_input(label="Self Service", value=userInfo["selfService"],key='selfService')
        pin=st.text_input(label="PIN", value=userInfo["pin"],type='password',key='pin')
        lastName=st.text_input(label="Last Name", value=userInfo["lastName"],key='lastName')
        middleName=st.text_input(label="Middle Name", value=userInfo["middleName"],key='middleName')
        firstName=st.text_input(label="First Name", value=userInfo['firstName'],key='firstName')
        displayName=st.text_input(label="Display Name", value=userInfo["displayName"],key='displayName')
        title=st.text_input(label="Title", value=userInfo["title"],key='title')
        directoryUri=st.text_input(label="Directory Uri", value=userInfo["directoryUri"],key='directoryUri')
        
        telephoneNumber=st.text_input(label="Telephone Number", value=userInfo["telephoneNumber"],key='telephoneNumber')
        mailid=st.text_input(label="Mail", value=userInfo["mailid"],key='mailid')
        department=st.text_input(label="Department", value=userInfo["department"],key='department')
        userLocale=st.text_input(label="User Locale", value=userInfo["userLocale"],key='userLocale')
        nameDialing=st.text_input(label="Name Dialing", value=userInfo["nameDialing"],key='nameDialing')
        userIdentity=st.text_input(label="User Identity", value=userInfo["userIdentity"],key='userIdentity')
        
        associatedGroups=st.text_input(label="Associated Groups", value=list_map(userInfo["associatedGroups"] ),key='associatedGroups',help="Please add User Groups with "+"[,]"+"as seperator between device e.g.[\'group1\',\'group2\',...]\n for empty write [] -empty brackets-")
        phoneProfiles=st.text_input(label="Phone Profiles", value=list_map(userInfo["phoneProfiles"] ),key='phoneProfiles',help="Please add profiles with "+"[,]"+"as seperator between device e.g.[\'profile1\',\'profile2\',...]\n for empty write [] -empty brackets-")
        
        defaultProfile=st.text_input(label="Default Profiles", value=userInfo["defaultProfile"]["_value_1"],key='defaultProfile')
        # c11,c22=st.columns([95,5])
        # with c11:
        associatedDevices=st.text_input(label="Associated Devices", value=userInfo["associatedDevices"]["device"] if userInfo["associatedDevices"] else None,key='associatedDevices',help="Please add devices with "+"[,]"+"as seperator between device e.g.[\'device1\',\'device2\',...]\n for empty write [] -empty brackets-")
        # with c22:
#             st.markdown("""<a href="/getUser" target="_blank" rel="noopener noreferrer" style="
#     position: absolute;
#     top: 2rem;
# "><span class="material-symbols-outlined">
# open_in_new
# </span></a>""",unsafe_allow_html=True)
#             st.markdown("""<style>
#             .material-symbols-outlined{
#             font-variation-settings:
#             position: absolute;
#                 top: 2.3rem;
#             }
#             </style>""",unsafe_allow_html=True)
        primaryExtension=st.text_input(label="Primary Extension", value=f'{userInfo["primaryExtension"]["pattern"] if userInfo["primaryExtension"] else None}'+f'/{userInfo["primaryExtension"]["routePartitionName"] if userInfo["primaryExtension"] else "None" }',key='primaryExtension')
        associatedPc=st.text_input(label="Associated PC", value=userInfo["associatedPc"],key='associatedPc')
        homeCluster=st.checkbox(label="Home Cluster", value=userInfo["homeCluster"],key='homeCluster')
        c1,c2=st.columns([0.01,0.99])
        with c2:
            imAndPresenceEnable=st.checkbox(label="Enable User for Unified CM IM and Presence (Configure IM and Presence in the associated UC Service Profile)", value=userInfo["imAndPresenceEnable"],key='imAndPresenceEnable')
            calendarPresence=st.checkbox(label="Include meeting information in presence(Requires Exchange Presence Gateway to be configured on CUCM IM and Presence server)", value=userInfo["calendarPresence"],key='calendarPresence')
        enableCti=st.checkbox(label="Allow Control of Device from CTI", value=userInfo["enableCti"],key='enableCti')
        enableEmcc=st.checkbox(label="Enable Extension Mobility Cross Cluster", value=userInfo["enableEmcc"],key='enableEmcc')
        with st.container():
            st.subheader("Mobility Information")
            enableMobility=st.checkbox(label="Enable Mobility", value=userInfo["enableMobility"],key='enableMobility')
            enableMobileVoiceAccess=st.checkbox(label="Enable Mobile Voice Access", value=userInfo["enableMobileVoiceAccess"],key='enableMobileVoiceAccess')
        
            maxDeskPickupWaitTime=st.text_input(label="Maximum Wait Time for Desk Pickup", value=userInfo["maxDeskPickupWaitTime"],key='maxDeskPickupWaitTime')
            remoteDestinationLimit=st.text_input(label="Remote Destination Limit", value=userInfo["remoteDestinationLimit"],key='remoteDestinationLimit')
            associatedRemoteDestinationProfiles=st.text_input(label="Remote Destination Profiles", value=list_map(userInfo["associatedRemoteDestinationProfiles"] ),key='associatedRemoteDestinationProfiles', disabled=True)
        # def checker(**userInfo["user"]):
        
        # checker(**user_info_after)
        # if apply_changes:
        #     print('apply_changes',apply_changes)
            # res=helpers.serialize_object(getUsers(user), dict)
            
            

        #     print("apply button has been clicked")
        #     submit_user_info(userid=userid)
        

def EU_page2(userInfo):
    # try:
        ##layer 1 of objects
        gen_all_L1={k:v for k,v in userInfo.items()}

        for kInfo1,vInfo1 in gen_all_L1.items():
            # print(type(vInfo1),kInfo1)
            ##data with specific types
            ##no lists inside layer 1 but just to make sure
            if type(vInfo1)==str or type(vInfo1)==int or type(vInfo1)==list:

                st.text_input(label=kInfo1, value=vInfo1 ,key=kInfo1)
            elif vInfo1=="None":
                st.text_input(label=kInfo1, key=kInfo1)
            
            
            elif type(vInfo1)==dict:
                

                gen1={kInfo2:vInfo2 for kInfo2,vInfo2 in vInfo1.items() if type(vInfo2)==str or kInfo2!="_value_1" or kInfo2!="uuid"}
                for kInfo2,vInfo2 in gen1.items():
                    # print(kInfo2,vInfo2)
                    st.text_input(label=kInfo2, value=vInfo2 ,key=kInfo2)
                gen2={kInfo2:vInfo2 for kInfo2,vInfo2 in vInfo1.items() if type(vInfo2)==str or kInfo2=="_value_1"}
                for kInfo2,vInfo2 in gen2.items():
                    # print(kInfo2,vInfo2)
                    st.text_input(label=kInfo1, value=vInfo2 ,key=kInfo1)
            
                ## layer 2 of objects inside objects
                # try:
                gen_all_L2={k:v for k,v in vInfo1.items()}
                for kInfo2,vInfo2 in gen_all_L2.items():
                    if vInfo2=="None":
                        st.text_input(label=kInfo2, key=kInfo2)
                    elif kInfo2=="pattern":
                        st.text_input(label=kInfo1,value=vInfo2, key=kInfo1)
                    elif kInfo2=="device" :
                        st.text_input(label=kInfo1,value=vInfo2, key=kInfo1)
                    elif type(vInfo2)==str or type(vInfo2)==int and kInfo2!="device" and kInfo2!="pattern":
                        st.text_input(label=kInfo2, value=vInfo2 ,key=kInfo2)
                    
                    elif type(vInfo2)==list and kInfo2!="device" and kInfo2!="pattern":
                        st.text_input(label=kInfo2, value=vInfo2,key=kInfo2)
                    # elif type(vInfo2)==dict:
                    #     st.text_input(label=kInfo2, value=vInfo2,key=kInfo2)
                    #     print(type(vInfo2),vInfo2)
                    
                # except:
                #     pass
                    # if type(vInfo2)==str and kInfo2!="_value_1" and kInfo2!="uuid" :
                        
                        # if kInfo1=="presenceGroupName":
                        #     st.text_input(label="presenceGroupName", value=vInfo2 ,key="presenceGroupName")
                    # if type(vInfo2)==str and kInfo2=="_value_1":
                    #     st.text_input(label=kInfo1, value=vInfo2 ,key=kInfo1)
    
            else:
                st.text_input(label=kInfo1, value=vInfo1,key=kInfo1)
    # except:
    #     st.error(userInfo)
                    
        
    
    
