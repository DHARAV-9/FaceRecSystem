import streamlit as st

st.set_page_config(page_title='GSFC Attendance System', layout='wide')

st.header('Attendance System using Face Recognition')

# Add your image path here
image_path = 'gsfc.jpg'

# Display the image
st.image(image_path, caption='GSFCU Face Attendance System',
         use_container_width=True

with st.spinner("Loading Face Attendance System ..."):
    import face_rec

st.success('Please Punch in Your Attendance via Face Recognition')
