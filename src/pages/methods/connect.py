import os
import streamlit as st
from ciscoaxl import axl

# os.environ['username']="dummy"
# os.environ['password']="dummy"
# os.environ['host']="dummy"
# os.environ['version']="dummy"

@st.cache_resource
def init_connection(username,password,host,version):
    connection=axl(username=username,password=password,cucm=host,cucm_version=version)
    test_connection=connection.get_CCM_Version()
    if test_connection:
        st.write("Connected")
        return connection
        
    else:
        st.write("trying to connect...")


cucm=init_connection(os.environ['username'],
    os.environ['password'],
    os.environ['host'],
    os.environ['version'])

