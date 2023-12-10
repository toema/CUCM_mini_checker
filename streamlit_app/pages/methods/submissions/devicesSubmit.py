import time
from pages.methods.connect import   init_connection,cucm
import streamlit as st



def devices_reply(*reply):
    # print(reply)
    try:
        for device in reply:
            print("device inreply",device)
            print(time.asctime())
            device_update=cucm.update_phone(**device)
            print(device_update)
            try:
                if device_update['return']:
                    
                    st.toast(':green[Your edited device was saved!]', icon='😍')
            except:
                if device_update:
                    st.toast(f':red[{device_update}]', icon='😕')
                else:
                    st.toast(':red[Somthing wrong with updating the device!]', icon='😔')
            
        # reply["manager"]=st.session_state.manager if st.session_state.manager else None
    except:
        print("error in devices_reply reply values")
        pass
    
#     try:
#         device={'name': 'TABUSER009', 'lines': {'line': [{'index': '1', 'label': None, 'display': None, 'dirn': {'pattern': '1009', 'routePartitionName': None, 'uuid': 
# '{6B8989F2-4405-9736-9635-95B035C28549}'}, 'displayAscii': None, 'e164Mask': None, 'maxNumCalls': '3', 'busyTrigger': '2',  'associatedEndusers': {'enduser': [{'userId': 'user09'}]}, 'missedCallLogging': True, 'callerName': True}]}}
#         print("device inreply",device)
#         print(time.asctime())
#         device_update=cucm.update_phone(**device)
#         print(device_update)
#         # reply["manager"]=st.session_state.manager if st.session_state.manager else None
#     except:
#         print("error in devices_reply reply values")
#         pass