import streamlit as st
from Home import face_rec
import cv2
import numpy as np
from streamlit_webrtc import webrtc_streamer
import av
from auth import authenticator

# Authentication check
if st.session_state['authentication_status']:
    authenticator.logout('Logout', 'sidebar', key='unique_key')

    st.subheader('Registration Form')

    ## init registration form
    registration_form = face_rec.RegistrationForm()

    # Step-1: Collect person name and role and other details
    name = st.text_input(label='Name', placeholder='Enter First name and Last name')
    role = st.selectbox(label='Role', options=('--select--', 'Student', 'Teacher'))
    course = st.selectbox(label='Select Course', options=('--select--', 'Computer Science', 'Electrical', 'Electronics'))
    year_level = st.selectbox(label='Year Level', options=('--select--', 'I - First Year', 'II - Second Year', 'III - Third Year', 'IV - Fourth Year'))
    address = st.text_area(label='Address', placeholder='Enter your address')
    contact = st.text_input(label='Contact Number', placeholder='Enter your contact number')
    email = st.text_input(label='Email', placeholder='Enter Email Address')

    st.write('Click on Start button to collect your face samples')
    with st.expander('Instructions'):
        st.caption('1. Give different expressions to capture your face details.')
        st.caption('2. Click on stop after getting 200 samples.')

    # Step-2: Collect facial embedding of that person
    def video_callback_func(frame):
        img = frame.to_ndarray(format='bgr24')  # 3D array BGR
        reg_img, embedding = registration_form.get_embedding(img)
        
        # Save embedding locally
        if embedding is not None:
            with open('face_embedding.txt', mode='ab') as f:
                np.savetxt(f, embedding)

        return av.VideoFrame.from_ndarray(reg_img, format='bgr24')

    # Streamlit webrtc for live face capture
    webrtc_streamer(
        key='registration',
        video_frame_callback=video_callback_func,
        rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
    )

    # Step-3: Save the data in Redis database
    if st.button('Submit'):
        return_val = registration_form.save_data_in_redis_db(name, role)
        if return_val == True:
            st.success(f"{name} registered successfully")
        elif return_val == 'name_false':
            st.error('Please enter the name: Name cannot be empty or spaces')
        elif return_val == 'file_false':
            st.error('face_embedding.txt is not found. Please refresh the page and execute again.')

else:
    authenticator.login('Login', 'main')
