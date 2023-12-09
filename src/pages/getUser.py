import streamlit as st
from pages.methods.devices import device_page
from pages.methods.extensions import ex_page
from pages.methods.gets import get_devices

from pages.methods.mapUserInfo import EU_page
from pages.methods.rdps import rdp_page


st.markdown("""
<style>
.st-emotion-cache-1y4p8pa
{
max-width: unset; 
}
a[href="http://localhost:8501/getUser"]
{
    visibility: hidden;
}

</style>
""",unsafe_allow_html=True)

col1,col2=st.columns([4,9])
with st.container():
    with col1:
        if "user" in st.session_state:
            # st.json(st.session_state)
            EU_page(st.session_state["user"])
    # st.markdown("||")
    with col2:
        if st.session_state["user"]["associatedDevices"] or st.session_state["user"]['phoneProfiles']:
            # tab1,tab2,tab3=st.tabs(["Devices","Extensions","RDPs"])
            tab1,tab2=st.tabs(["Devices","Extensions"])
            with tab1:
                device_page(st.session_state["user"])
            with tab2:
                if st.session_state["lines"]:
                    ex_page()
                else:
                    st.write("No extensions associated were found")
            # with tab3:
            #     if st.session_state["lines"]:
            #         rdp_page()
            #     else:
            #         st.write("No RDP associated were found")
            
            
        else:
            st.write("No devices were found")
        
            
    # with col3:
    #     st.write(st.session_state)

    


def mapUser(UserInfo):
    # print(UserInfo)
    # with st.form("userInfo"):
    if UserInfo:
        EU_page(st.session_state["user"])


