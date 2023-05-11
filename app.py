import streamlit as st
import subprocess
import os
import cv2
import subprocess
#Loading utils for required funcs
from evaluate import find_similar_chemicals, search_risky_chemicals

def page1():
    st.title("Your Product is safe! :pray:")
    st.write("No chemicals from our risky list are detected in your product.")

def page2(risky_chemicals):
    st.title("Product Warning! :warning:")
    st.write("Chemicals from our risky list are detected in your product.")
    st.write( str(risky_chemicals).strip('[]'))
    st.write("You can read more about the chemicals from following website : https://www.byrdie.com/toxic-beauty-ingredients-4782646")
    

def main():
    st.title("Product Safety App \U0001F9EA")
    st.write("Please provide the photo of ingredients for testing")
    # Button to capture from video
    if st.button("Capture from Camera"):
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

    
    chemical_list_file = 'chemicals.txt'
    risky_chemicals = search_risky_chemicals(chemical_list_file)

    # Check if the result list is empty
    if not risky_chemicals:
        page1()  # Display page 1
    else:
        page2(risky_chemicals)  # Display page 2




if __name__ == "__main__":
    main()
