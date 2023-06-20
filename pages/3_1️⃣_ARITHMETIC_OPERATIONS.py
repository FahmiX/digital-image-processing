# Package / Library
import streamlit as st
import numpy as np
import cv2
import FUNCTIONS as func

# MAIN PAGE
def main():
    # Set Page Config
    set_page()

    # Content
    img = st.file_uploader("Choose an image...", type="jpg")
    if img is not None:
        img = np.frombuffer(img.read(), np.uint8)
        img = cv2.imdecode(img, cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
        # Original Image
        with st.expander("Original Image"):
            func.show_image_st(img, 'Original Image', None)

        tab(img)

# FUNCTIONS
# setup page
def set_page():
    st.set_page_config(
        page_title="ARITHMETIC OPERATIONS",
        page_icon="🔢",
        layout="centered",
        initial_sidebar_state="auto",
    )

# tab
def tab(img):
    tab1, tab2, tab3, tab4 = st.tabs(["Addition", "Subtraction", "Multiplication", "Division"])

    with tab1:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>Addition</h1>", unsafe_allow_html=True)

        # Addition Image
        addition(img)

def addition(img):
    tab1, tab2 = st.tabs(["Addition Between Image and Number", "Addition Between Image and Image"])

    # Addition Between Image and Number
    with tab1:
        # Number
        option = st.selectbox(
            'Choose a number:',
            ('slider', 'input'),
            label_visibility='collapsed'
        )

        if option == 'slider':
            number = st.slider('Choose a number:', 0, 255, 0)
        elif option == 'input':
            number = st.number_input('Choose a number:', 0, 255, 0)

        addition_value = np.ones_like(img) * number

        # Addition
        result = cv2.add(img, addition_value)

        # Show Image
        with st.container():
            # Result Image
            with st.expander("Result Image"):
                func.show_image_st(result, 'Result Image', None)

    # If Addition Between Image and Image
    with tab2:
        # Image
        img2 = st.file_uploader("Choose adder image...", type="jpg")
        if img2 is not None:
            img2 = np.frombuffer(img2.read(), np.uint8)
            img2 = cv2.imdecode(img2, cv2.IMREAD_COLOR)
            img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

            # Match Image Size
            img2 = cv2.resize(img2, (img.shape[1], img.shape[0]))

            # Addition
            result = cv2.add(img, img2)

            # Show Image
            func.show_image_st(result, None, None)

# MAIN CONFIG
if __name__ == "__main__":
    main()