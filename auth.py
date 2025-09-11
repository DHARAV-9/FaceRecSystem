import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

authenticator.login('Login', 'main')

auth_status = st.session_state.get("authentication_status")

if auth_status:
    authenticator.logout('Logout', 'sidebar', key='unique_key')
    st.write(f'Welcome *{st.session_state.get("name", "User")}*')
    st.title('Some content')
elif auth_status is False:
    st.error('Username/password is incorrect')
elif auth_status is None:
    st.warning('Please enter your username and password')
