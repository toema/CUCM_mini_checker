import os,time
import streamlit as st


from pages.methods.connect import   init_connection,cucm



# def submit_user_info(func):
#     def wrapper(*args,**info):
#     # print(info)
#         print(time.time())
#         data=func()
#         print('info from decorator',info)
#         print('data from decorator', data)
        
#         submit=cucm.update_user(data)

#     return wrapper



# @submit_user_info
# def checker(**info):
#     # print(info)
#     if info['newUserid'] and '' in info['newUserid']:
#         del info['newUserid']
#     return info


def user_update(**info):
    print(time.asctime())
    # print('info',info)
    if "userid" in info.keys():
        submit=cucm.update_user(**info)
        try:
            if submit['return']:
                    st.toast(':green[Your edited user was saved!]', icon='😍')
        except:
            if submit:
                st.toast(f':red[{submit}]', icon='😕')
            else:
                st.toast(':red[Somthing wrong with updating the user!]', icon='😔')
        print('submit',submit)
    else:
        print("User ID is not found")



# cucm=init_connection()

