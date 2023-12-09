


import time,json
from pages.methods.connect import cucm
import streamlit as st

def ex_reply(**reply):
    # print(reply)
    try:
        
            print("extension inreply",reply)
            
            print(time.asctime())
            extension_update=cucm.update_directory_number(**reply)
            print("extension_update",extension_update)
            try:
                if  extension_update['return']:
                    st.toast(':green[Your edited extension was saved!]', icon='😍')
            except:
                if extension_update:
                    st.toast(f':red[{extension_update}]', icon='😕')
                else:
                    st.toast(':red[Somthing wrong with updating the extension!]', icon='😔')
        # reply["manager"]=st.session_state.manager if st.session_state.manager else None
            # with open("temp.json","a",encoding ='utf8') as file:
            #         json.dump({"action":"submit extension","component":reply,"time":time.asctime(),"results":extension_update},file, indent=4)
            #         file.write(",")
    except:
        print("error in ex_reply reply values")
        # print("extension_update",extension_update)
        pass