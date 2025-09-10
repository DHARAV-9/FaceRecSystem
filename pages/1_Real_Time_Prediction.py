iimport streamlit as st
from Home import face_rec
from streamlit_webrtc import webrtc_streamer
import av
import time
from auth import authenticator

# Check authentication status
if st.session_state.get('authentication_status'):
    authenticator.logout('Logout', 'sidebar', key='unique_key')

    with st.spinner("Loading Models and Connecting to Redis db ..."):
        import face_rec

    # Page header
    st.subheader('Real-Time Attendance System')

    # Retrieve the data from Redis Database
    with st.spinner('Retrieving Data from Redis DB ...'):
        redis_face_db = face_rec.retrive_data(name='academy:register')
        st.dataframe(redis_face_db)

    st.success("Data successfully retrieved from Redis")

    # Time setup for saving logs
    waitTime = 30  # seconds
    setTime = time.time()
    realtimepred = face_rec.RealTimePred()  # Real-time prediction class

    # Real-time video callback function
    def video_frame_callback(frame):
        nonlocal setTime  # use nonlocal since setTime is in enclosing scope

        img = frame.to_ndarray(format="bgr24")  # Convert to 3D numpy array

        # Perform face prediction
        pred_img = realtimepred.face_prediction(
            img,
            redis_face_db,
            'facial_features',
            ['Name', 'Role'],
            thresh=0.5
        )

        # Save logs every `waitTime` seconds
        timenow = time.time()
        difftime = timenow - setTime
        if difftime >= waitTime:
            realtimepred.saveLogs_redis()
            setTime = time.time()  # reset timer
            print('Saved data to Redis database')

        return av.VideoFrame.from_ndarray(pred_img, format="bgr24")

    # Streamlit WebRTC streamer
    webrtc_streamer(
        key="realtimePrediction",
        video_frame_callback=video_frame_callback,
        rtc_configuration={
            "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
        }
    )

else:
    authenticator.login('Login', 'main')
