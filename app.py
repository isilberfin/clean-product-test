import streamlit as st
import subprocess
import os
import cv2

def main():
    st.title("Text Recognition Application")

    # Button to capture from video
    if st.button("Capture from Video"):
        subprocess.run(["python", "capture_from_video.py"])

    uploadbtn = st.button("Upload Image")

    if "uploadbtn_state" not in st.session_state:
        st.session_state.uploadbtn_state = False
    if uploadbtn or st.session_state.uploadbtn_state:
        st.session_state.uploadbtn_state = True
        uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
        print(uploaded_file)
        if uploaded_file is not None:
            # Save the uploaded file to the "test-img" folder
            file_path = os.path.join("test-img", "test_img.png")
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success("File uploaded successfully.")

if __name__ == "__main__":
    main()
