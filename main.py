
import streamlit as st
import os
# class connect():
from st_pages import Page, show_pages, hide_pages




#     def __init__(self,user,password,host,version) -> None:
#         self.user=user
#         self.password=password
#         self.host=host
#         self.version=version

##add #cluster# as parameter if you need multi cluster configuration



# cucm=init_connection()


# show_pages([
#     Page("main.py","main"),
#     Page("pages/Users.py","Users"),
#     Page("pages/getUser.py","getUser")
# ])

# hide_pages(['getUser'])
st.markdown("""
<style>
a[href="http://localhost:8501/getUser"]
{
    visibility: hidden;
}

</style>
""",unsafe_allow_html=True)

# st.sidebar.write("here lives the sidebar")

# router = StreamlitRouter()

# @router.map("/")

with st.form("CUCM intiation"):
    
    st.header("CUCM Athuntication")
    st.write(
        """
        Please use this page for authentication with the CUCM as follows
        """
    )
    # cluster=st.text_input(label="Cluster Name" , help="provide a name for the following configuration")
    col1, col2 = st.columns(2)
    with col1:
        username=st.text_input(label="Username",help="UserID of the application user your've created")
        password=st.text_input(label="Password", help="Password of the application user your've created", type="password")
        
    with col2:
        host=st.text_input(label="Host",help="IP address of the publisher")
        version=st.text_input(label="Version",help="Version of the CUCM")
    apply_button=st.form_submit_button(label="Apply")
    if apply_button:
        def add_conn_vars(**kargs):
            os.environ['username']=kargs['username']
            os.environ['password']=kargs['password']
            os.environ['host']=kargs['host']
            os.environ['version']=kargs['version']
            from pages.methods.connect import cucm
            if cucm:
                return st.write("connected")
        ##add #cluster# as parameter if you need multi cluster configuration
        add_conn_vars(username=username,password=password,host=host,version=version)
            # init_connection()

            
        
# router.register(index, '/')
# router.register(users,"/Users")
# router.serve()
