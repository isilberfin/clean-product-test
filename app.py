import streamlit as st
import subprocess
import os
import cv2


def main():
    st.title("Text Recognition Application")

    # Button to capture from video
    if st.button("Capture from Video"):
        subprocess.run(["python", "capture_from_video.py"])

    # Button to load from device
    if st.button("Load from Device"):
        uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

        if uploaded_file is not None:
            # Specify the directory to save the uploaded file
            save_dir = "./images"
            os.makedirs(save_dir, exist_ok=True)  # Create the directory if it doesn't exist

            # Save the uploaded file to the specified directory
            save_path = os.path.join(save_dir, uploaded_file.name)
            with open(save_path, "wb") as f:
                f.write(uploaded_file.read())

            # Display the uploaded image
            st.image(uploaded_file, caption='Uploaded Image')


if __name__ == "__main__":
    main()