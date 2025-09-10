import streamlit as st
<<<<<<< HEAD
from auth import authenticator
st.set_page_config(page_title='Attendance System',layout='wide')



if st.session_state['authentication_status']:
    authenticator.logout('Logout', 'sidebar', key='unique_key')

    st.write(f'Welcome *{st.session_state["name"]}*')



    st.header('Attendance System using Face Recognition')

    st.success('Model loaded sucesfully')
    st.success('Redis db sucessfully connected')

else:
    authenticator.login('Login', 'main')

=======

st.set_page_config(page_title='GSFC Attendance System', layout='wide')

st.header('Attendance System using Face Recognition')

# Add your image path here
image_path = 'gsfc.jpg'

# Display the image
st.image(image_path, caption='GSFCU Face Attendance System', width='stretch')

with st.spinner("Loading Face Attendance System ..."):
    import face_rec

st.success('Please Punch in Your Attendance via Face Recognition')
>>>>>>> master
