# Package / Library
import streamlit as st
from PIL import Image
import numpy as np
import cv2
import FUNCTIONS as func

# MAIN PAGE
def main():
    # Set Page Config
    set_page()

    # Content
    img = st.file_uploader("Choose an image...", type=["jpg","png"])
    if img is not None:
        img = np.frombuffer(img.read(), np.uint8)
        img = cv2.imdecode(img, cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        tab(img)

# FUNCTIONS
# Page Config
def set_page():
    st.set_page_config(
        page_title="Color Space",
        page_icon="2️⃣",
        layout="centered",
        initial_sidebar_state="auto",
    )

# Tab
def tab(img):
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11 = st.tabs(["RGB", "RGBA", "BGR", "XYZ", "YCrCb", "HSV", "Lab", "Luv", "HLS", "YUV", "GRAY"])
    
    with tab1:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>RGB</h1>", unsafe_allow_html=True)

        # Show Image
        func.show_image_st(img, None, None)

    with tab2:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>RGBA</h1>", unsafe_allow_html=True)

        # Convert Image to RGBA and give alpha value
        result = cv2.cvtColor(img, cv2.COLOR_RGB2RGBA)
        result[:, :, 3] = 5000

        # Show Image
        func.show_image_st(result, None, None)

    with tab3:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>BGR</h1>", unsafe_allow_html=True)

        # Convert Image to BGR
        result = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        # Show Image
        func.show_image_st(result, None, None)

    with tab4:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>XYZ</h1>", unsafe_allow_html=True)

        # Convert Image to XYZ
        result = cv2.cvtColor(img, cv2.COLOR_RGB2XYZ)

        # Show Image
        func.show_image_st(result, None, None)

    with tab5:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>YCrCb</h1>", unsafe_allow_html=True)

        # Convert Image to YCrCb
        result = cv2.cvtColor(img, cv2.COLOR_RGB2YCrCb)

        # Show Image
        func.show_image_st(result, None, None)

    with tab6:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>HSV</h1>", unsafe_allow_html=True)

        # Convert Image to HSV
        result = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

        # Show Image
        func.show_image_st(result, None, None)

    with tab7:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>Lab</h1>", unsafe_allow_html=True)

        # Convert Image to Lab
        result = cv2.cvtColor(img, cv2.COLOR_RGB2Lab)

        # Show Image
        func.show_image_st(result, None, None)

    with tab8:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>Luv</h1>", unsafe_allow_html=True)

        # Convert Image to Luv
        result = cv2.cvtColor(img, cv2.COLOR_RGB2Luv)

        # Show Image
        func.show_image_st(result, None, None)

    with tab9:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>HLS</h1>", unsafe_allow_html=True)

        # Convert Image to HLS
        result = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)

        # Show Image
        func.show_image_st(result, None, None)

    with tab10:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>YUV</h1>", unsafe_allow_html=True)

        # Convert Image to YUV
        result = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)

        # Show Image
        func.show_image_st(result, None, None)

    with tab11:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>GRAY</h1>", unsafe_allow_html=True)

        # Convert Image to GRAY
        result = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        # Show Image
        func.show_image_st(result, None, None)

# MAIN CONFIG
if __name__ == "__main__":
    main()