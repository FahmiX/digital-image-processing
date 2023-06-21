# Package / Library
import streamlit as st
import cv2
import numpy as np
import FUNCTIONS as func

# MAIN PAGE
def main():
    # Set Page Config
    set_page()

    # Content
    img = st.file_uploader("Choose original image...", type=["jpg", "png"])
    if img is not None:
        img = np.frombuffer(img.read(), np.uint8)
        img = cv2.imdecode(img, cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Original Image
        with st.expander("Original Image"):
            func.show_image_st(img, 'Original Image', None)

        tab(img)
    

# FUNCTIONS
# Set Page
def set_page():
    st.set_page_config(
        page_title="Logical Operations",
        page_icon="4️⃣",
        layout="centered",
        initial_sidebar_state="auto",
    )

# Tab
def tab(img):
    tab1, tab2, tab3, tab4 = st.tabs(["AND", "OR", "XOR", "NOT"])

    with tab1:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>AND</h1>", unsafe_allow_html=True)

        # AND Image
        and_img(img)

    with tab2:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>OR</h1>", unsafe_allow_html=True)

        # OR Image
        or_img(img)

    with tab3:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>XOR</h1>", unsafe_allow_html=True)

        # XOR Image
        xor_img(img)

    with tab4:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>NOT</h1>", unsafe_allow_html=True)

        # NOT Image
        not_img(img)

def and_img(img):
    # AND Image
    img2 = st.file_uploader("Choose and image...", type=["jpg", "png"])
    if img2 is not None:
        img2 = np.frombuffer(img2.read(), np.uint8)
        img2 = cv2.imdecode(img2, cv2.IMREAD_COLOR)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

        # Match Image Size
        img2 = cv2.resize(img2, (img.shape[1], img.shape[0]))

        # AND
        img_and = cv2.bitwise_and(img, img2)

        # Show Image
        func.show_image_st(img_and, None, None)

def or_img(img):
    # OR Image
    img2 = st.file_uploader("Choose or image...", type=["jpg", "png"])
    if img2 is not None:
        img2 = np.frombuffer(img2.read(), np.uint8)
        img2 = cv2.imdecode(img2, cv2.IMREAD_COLOR)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

        # Match Image Size
        img2 = cv2.resize(img2, (img.shape[1], img.shape[0]))

        # OR
        img_or = cv2.bitwise_or(img, img2)

        # Show Image
        func.show_image_st(img_or, None, None)

def xor_img(img):
    # XOR Image
    img2 = st.file_uploader("Choose xor image...", type=["jpg", "png"])
    if img2 is not None:
        img2 = np.frombuffer(img2.read(), np.uint8)
        img2 = cv2.imdecode(img2, cv2.IMREAD_COLOR)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

        # Match Image Size
        img2 = cv2.resize(img2, (img.shape[1], img.shape[0]))

        # XOR
        img_xor = cv2.bitwise_xor(img, img2)

        # Show Image
        func.show_image_st(img_xor, None, None)

def not_img(img):
    # NOT
    img_not = cv2.bitwise_not(img)

    # Show Image
    func.show_image_st(img_not, None, None)

# MAIN CONFIG
if __name__ == "__main__":
    main()