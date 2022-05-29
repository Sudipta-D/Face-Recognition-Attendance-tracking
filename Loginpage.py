import streamlit as st
import streamlit_authenticator as stauth

names = ['Sudipta','Elon Musk','Steve Jobs','Susan W','Bill Gates']
usernames = ['sudi','emusk','sjobs','sw','bgates']
passwords = ['abc','def','ghi','jkl','mno']

hashed_passwords = stauth.Hasher(passwords).generate()

authenticator = stauth.Authenticate(names,usernames,hashed_passwords,
    'some_cookie_name','some_signature_key',cookie_expiry_days=30)

st.title("Welcome to Attendance Tracker")

name, authentication_status, username = authenticator.login('Login','main')

if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write('Welcome *%s*' % (name))
    st.title('Some content')
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')

    if st.session_state['authentication_status']:
        authenticator.logout('Logout', 'main')
        st.write('Welcome *%s*' % (st.session_state['name']))
        st.title('Some content')
    elif st.session_state['authentication_status'] == False:
        st.error('Username/password is incorrect')
    elif st.session_state['authentication_status'] == None:
        st.warning('Please enter your username and password')
