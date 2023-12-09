
import streamlit as st

from pages.methods.jsonReply import ex_mapper





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


        

def ex_page():
    # # missing Hunt group FIELD
    with st.form("Extension_info"):
        st.form_submit_button(label="Submit extension",on_click=ex_mapper)

        for line in st.session_state["lines"]:
            with st.container():
                st.subheader(line["pattern"]+" - "+f'{line["routePartitionName"]["_value_1"] if line["routePartitionName"]["_value_1"] else None}' )
                col1,col2=st.columns(2)
                with col1:
                    pattern=st.text_input(label="pattern", value=line["pattern"],key=f'{line["pattern"]},{line["routePartitionName"]["_value_1"] if line["routePartitionName"]["_value_1"] else None},pattern',disabled=True)
                    

                    description=st.text_input(label="Description", value=line["description"],key=f'{line["pattern"]},{line["routePartitionName"]["_value_1"] if line["routePartitionName"]["_value_1"] else None},description')
                    asciiAlertingName=st.text_input(label="asciiAlertingName", value=line["asciiAlertingName"],key=f'{line["pattern"]},{line["routePartitionName"]["_value_1"] if line["routePartitionName"]["_value_1"] else None},asciiAlertingName')
                    voiceMailProfileName=st.text_input(label="voiceMailProfileName", value=line["voiceMailProfileName"]["_value_1"] if line["voiceMailProfileName"]["_value_1"] else None,key=f'{line["pattern"]},{line["routePartitionName"]["_value_1"] if line["routePartitionName"]["_value_1"] else None},voiceMailProfileName')
                    # directoryURIs=st.text_input(label="directoryURIs", value=line["directoryURIs"] if line["directoryURIs"] else None,key=f'{line["pattern"]},{line["routePartitionName"]["_value_1"] if line["routePartitionName"]["_value_1"] else None},directoryURIs')
                    forwardTime=st.text_input(label="No Answer Ring Duration (seconds)", value=line["callForwardNoAnswer"]["duration"] ,key=f'{line["pattern"]},{line["routePartitionName"]["_value_1"] if line["routePartitionName"]["_value_1"] else None},forwardTime')
                    
                    
                    forwardToNoAnswer=st.text_input(label="callForwardNoAnswer", value=line["callForwardNoAnswer"]["destination"] if line["callForwardNoAnswer"]["destination"] else None,key=f'{line["pattern"]},{line["routePartitionName"]["_value_1"] if line["routePartitionName"]["_value_1"] else None},callForwardNoAnswer,destination')
                    forwardToVoiceMailNoAnswer=st.checkbox(label="forwardToVoiceMail NoAnswer", value=line["callForwardNoAnswer"]["forwardToVoiceMail"] if line["callForwardNoAnswer"]["forwardToVoiceMail"]=="true" else False,key=f'{line["pattern"]},{line["routePartitionName"]["_value_1"] if line["routePartitionName"]["_value_1"] else None},callForwardNoAnswer,forwardToVoiceMail')
                    uuid=st.text_input(label="uuid", value=line["uuid"],key=f'{line["pattern"]},{line["routePartitionName"]["_value_1"] if line["routePartitionName"]["_value_1"] else None},uuid')
                with col2:
                    newPattern=st.text_input(label="New Pattern",key=f'{line["pattern"]},{line["routePartitionName"]["_value_1"] if line["routePartitionName"]["_value_1"] else None},newPattern')
                    routePartitionName=st.text_input(label="Route Partition", value=line["routePartitionName"]["_value_1"] if line["routePartitionName"]["_value_1"] else None,key=f'{line["pattern"]},{line["routePartitionName"]["_value_1"] if line["routePartitionName"]["_value_1"] else None},routePartitionName,_value_1')
                    associatedDevices=st.text_input(label="associatedDevices", value=line["associatedDevices"]["device"],key=f'{line["pattern"]},{line["routePartitionName"]["_value_1"] if line["routePartitionName"]["_value_1"] else None},associatedDevices,device',disabled=True)
                    alertingName=st.text_input(label="alertingName", value=line["alertingName"],key=f'{line["pattern"]},{line["routePartitionName"]["_value_1"] if line["routePartitionName"]["_value_1"] else None},ale8rtingName')
                    shareLineAppearanceCssName=st.text_input(label="callingSearchSpaceName", value=line["shareLineAppearanceCssName"]["_value_1"] if line["shareLineAppearanceCssName"]["_value_1"] else None,key=f'{line["pattern"]},{line["routePartitionName"]["_value_1"] if line["routePartitionName"]["_value_1"] else None},shareLineAppearanceCssName')
                    # advertiseGloballyIls=st.checkbox(label="advertiseGloballyIls", value=line["advertiseGloballyIls"] if line["advertiseGloballyIls"]=="t" else False,key=f'{line["pattern"]},{line["routePartitionName"]["_value_1"] if line["routePartitionName"]["_value_1"] else None},advertiseGloballyIls')
                    forwardCSS=st.text_input(label="Forward CSS", value=line["callForwardAll"]["callingSearchSpaceName"]["_value_1"] if line["callForwardAll"]["callingSearchSpaceName"]["_value_1"] else None ,key=f'{line["pattern"]},{line["routePartitionName"]["_value_1"] if line["routePartitionName"]["_value_1"] else None},forwardCSS')
                    
                    forwardToAll=st.text_input(label="forwardToAll", value=line["callForwardAll"]["destination"] if line["callForwardAll"]["destination"] else None,key=f'{line["pattern"]},{line["routePartitionName"]["_value_1"] if line["routePartitionName"]["_value_1"] else None},callForwardAll,destination')

                    forwardToVoiceMailAll=st.checkbox(label="forwardToVoiceMail All", value=line["callForwardAll"]["forwardToVoiceMail"] if line["callForwardAll"]["forwardToVoiceMail"]=="true" else False,key=f'{line["pattern"]},{line["routePartitionName"]["_value_1"] if line["routePartitionName"]["_value_1"] else None},callForwardAll,forwardToVoiceMail')
                    
                    forwardToBusy=st.text_input(label="callForwardBusy", value=line["callForwardBusy"]["destination"] if line["callForwardBusy"]["destination"] else None,key=f'{line["pattern"]},{line["routePartitionName"]["_value_1"] if line["routePartitionName"]["_value_1"] else None},callForwardBusy,destination')
                    forwardToVoiceMailBusy=st.checkbox(label="forwardToVoiceMail Busy", value=line["callForwardBusy"]["forwardToVoiceMail"] if line["callForwardBusy"]["forwardToVoiceMail"]=="true" else False,key=f'{line["pattern"]},{line["routePartitionName"]["_value_1"] if line["routePartitionName"]["_value_1"] else None},callForwardBusy,forwardToVoiceMail')
                    
           
    
        ##layer 1 of objects












        # gen_all_L1={k:v for k,v in userInfo.items()}
        # for kInfo1,vInfo1 in gen_all_L1.items():
        #     # print(type(vInfo1),kInfo1)
        #     ##data with specific types
        #     ##no lists inside layer 1 but just to make sure
        #     if type(vInfo1)==str or type(vInfo1)==int or type(vInfo1)==list:

        #         st.text_input(label=kInfo1, value=vInfo1 ,key=kInfo1)
        #     elif vInfo1=="None":
        #         st.text_input(label=kInfo1, key=kInfo1)
            
            
        #     elif type(vInfo1)==dict:
                

        #         gen1={kInfo2:vInfo2 for kInfo2,vInfo2 in vInfo1.items() if type(vInfo2)==str or kInfo2!="_value_1" or kInfo2!="uuid"}
        #         for kInfo2,vInfo2 in gen1.items():
        #             # print(kInfo2,vInfo2)
        #             st.text_input(label=kInfo2, value=vInfo2 ,key=kInfo2)
        #         gen2={kInfo2:vInfo2 for kInfo2,vInfo2 in vInfo1.items() if type(vInfo2)==str or kInfo2=="_value_1"}
        #         for kInfo2,vInfo2 in gen2.items():
        #             # print(kInfo2,vInfo2)
        #             st.text_input(label=kInfo1, value=vInfo2 ,key=kInfo1)
            
        #         ## layer 2 of objects inside objects
        #         # try:
        #         gen_all_L2={k:v for k,v in vInfo1.items()}
        #         for kInfo2,vInfo2 in gen_all_L2.items():
        #             if vInfo2=="None":
        #                 st.text_input(label=kInfo2, key=kInfo2)
        #             elif kInfo2=="pattern":
        #                 st.text_input(label=kInfo1,value=vInfo2, key=kInfo1)
        #             elif kInfo2=="device" :
        #                 st.text_input(label=kInfo1,value=vInfo2, key=kInfo1)
        #             elif type(vInfo2)==str or type(vInfo2)==int and kInfo2!="device" and kInfo2!="pattern":
        #                 st.text_input(label=kInfo2, value=vInfo2 ,key=kInfo2)
                    
        #             elif type(vInfo2)==list and kInfo2!="device" and kInfo2!="pattern":
        #                 st.text_input(label=kInfo2, value=vInfo2,key=kInfo2)
        #             # elif type(vInfo2)==dict:
        #             #     st.text_input(label=kInfo2, value=vInfo2,key=kInfo2)
        #             #     print(type(vInfo2),vInfo2)
                    
        #         # except:
        #         #     pass
        #             # if type(vInfo2)==str and kInfo2!="_value_1" and kInfo2!="uuid" :
                        
        #                 # if kInfo1=="presenceGroupName":
        #                 #     st.text_input(label="presenceGroupName", value=vInfo2 ,key="presenceGroupName")
        #             # if type(vInfo2)==str and kInfo2=="_value_1":
        #             #     st.text_input(label=kInfo1, value=vInfo2 ,key=kInfo1)
    
        #     else:
        #         st.text_input(label=kInfo1, value=vInfo1,key=kInfo1)
    # except:
    #     st.error(userInfo)
                    
        
    
    