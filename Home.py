import streamlit as st
from auth import authenticator

st.set_page_config(page_title='Attendance System', layout='wide')

if 'authentication_status' not in st.session_state:
    st.session_state['authentication_status'] = False

if st.session_state['authentication_status']:
    authenticator.logout('Logout', 'sidebar', key='unique_key')
    st.write(f'Welcome *{st.session_state.get("name", "User")}*')
    st.header('Attendance System using Face Recognition')

    # Add your image path here
    image_path = 'gsfc.jpg'
    st.image(image_path, caption='GSFCU Face Attendance System', use_column_width=True)

    with st.spinner("Loading Face Attendance System ..."):
        import face_rec  # Make sure this import works as expected

    st.success('Model loaded successfully')
    st.success('Redis db successfully connected')
    st.success('Please Punch in Your Attendance via Face Recognition')

else:
    authenticator.login('Login', 'main')

