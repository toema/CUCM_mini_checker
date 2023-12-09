
from st_pages import _hide_pages
import streamlit as st
from pages.methods.getusers import displayData
from pages.methods.getusers import getUsers
from streamlit_extras.switch_page_button import switch_page


# res={}
# def proc(**data):
    
#     st.write(data)
#     st.write(st.session_state)
# apply_button=False

st.markdown("""
<style>
a[href="http://localhost:8501/getUser"]
{
    visibility: hidden;
}

</style>
""",unsafe_allow_html=True)


# _hide_pages(['getUser'])

with st.form("UsersForm"):
# st.write(st.session_state)
    user=st.text_input(label="UserID")

    apply_button=st.form_submit_button(label="Apply")

    if apply_button:
    # runner=st.status("requesting data",state="running")
        
        with st.status("requesting data") as status:
            res=getUsers(user)
            displayData(**res)
            switch_page('getUser')
        
        # print(res)
        # st.session_state["getUser"]=res
        # st.experimental_get_query_params
    # st.write(st.experimental_get_query_params())
        # status.update(label="data has been retrieved",state=None,)

        # runner=st.status("requesting data",state="complete")
        # col1,col2=st.columns(2)
        # with col1:
        #     res_json=st.json(res)
        #     # print(res)
        # with col2:
        #     mapUser(res)

        
    # with st.form("User_basic_info12"):
    #     try:
    #         print("session_state.firstName",st.session_state)
    #     except:
    #         pass
    #     col1,col2=st.columns(2)
        
    #     firstName=st.text_input(label="First Name", placeholder=res["firstName"],key='firstName')
        
    #     # lastName=st.text_input(label="Last Name", value=res["lastName"])
    #     # middleName=st.text_input(label="Middle Name", value=res["middleName"])
    #     # displayName=st.text_input(label="Display Name", value=res["displayName"])
    #     # with col1:
    #     #     userid=st.text_input(label="User iD", value=res["userid"],disabled=True)
    #     # with col2:
    #     #     newUserid=st.text_input(label="New User iD")
    #     # password=st.text_input(label="Password", value=res["password"],type='password')
    #     # pin=st.text_input(label="PIN", value=res["pin"])
    #     # mailid=st.text_input(label="Mail", value=res["mailid"])

    #     # user_info_after={'firstName':firstName,'lastName':lastName,'middleName':middleName,'displayName':displayName,'userid':userid,'password':password,'pin':pin,'mailid':mailid,'newUserid':newUserid}
    #     user_info_after={'firstName':firstName}
    #     # def checker(**res):
    #     print('user_info_after',user_info_after)
    #     try:
    #         if '' in user_info_after['newUserid']:
    #             del user_info_after['newUserid']
    #     except:
    #         pass
    #     # checker(**user_info_after)
    #     apply_changes=st.form_submit_button(label="Apply new changes",on_click=proc
    #                                         ,kwargs=user_info_after)
        
    #     if apply_changes:
    #         print('apply_changes',apply_changes)
    