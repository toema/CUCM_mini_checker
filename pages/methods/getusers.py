from .connect import   cucm
import streamlit as st

def displayData(**EU_info):
    st.session_state["user"]=EU_info
    
    return EU_info

def getUsers(userid):
    from zeep import helpers
    import json
    user=helpers.serialize_object(cucm.get_user(userid=userid), dict)

    # with open("temp.json", "a",encoding ='utf8') as file:
    #     json.dump(user, file, indent=4)
    #     file.write(",")

    return user



    # for kInfo,vInfo in UserInfo.items():
    # st.text_input(label='First Name', value=UserInfo['firstName'] ,key=UserInfo['firstName'])

        # if UserInfo:
        #     apply_changes=st.form_submit_button(label="Apply new changes")

