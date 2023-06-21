# Package / Library
import streamlit as st
import cv2
import numpy as np 
import FUNCTIONS as func
import matplotlib.pyplot as plt

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

        tab(img)

# FUNCTIONS
# Set Page
def set_page():
    st.set_page_config(
        page_title="Spatial Filters",
        page_icon="6️⃣",
        layout="centered",
        initial_sidebar_state="auto",
    )

def tab(img):
    tab1, tab2, tab3, tab4 = st.tabs(["Low Pass Filter", "High Pass Filter", "Band Pass Filter", "Median Filter"])

    with tab1:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>Low Pass Filter</h1>", unsafe_allow_html=True)

        # Low Pass Filter
        low_pass_filter(img)

    with tab2:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>High Pass Filter</h1>", unsafe_allow_html=True)

        # High Pass Filter
        high_pass_filter(img)

    with tab3:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>Band Pass Filter</h1>", unsafe_allow_html=True)

        # Band Pass Filter
        band_pass_filter(img)

    with tab4:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>Median Filter</h1>", unsafe_allow_html=True)

        # Median Filter
        median_filter(img)

def low_pass_filter(img):
    # Kernel Size
    kernel_size = st.slider("Kernel Size:", 1, 99, 1, 2, key="low_pass_filter")

    # Low Pass Filter
    img_low_pass = cv2.blur(img, (kernel_size, kernel_size))

    # Show Image
    func.show_image_st(img_low_pass, None, None)

def high_pass_filter(img):
    # Kernel Size
    kernel_size = st.slider("Kernel Size:", 1, 99, 1, 2, key="high_pass_filter")

    # High Pass Filter
    img_high_pass = cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

    # Show Image
    func.show_image_st(img_high_pass, None, None)

def band_pass_filter(img):
    # Kernel Size
    kernel_size = st.slider("Kernel Size:", 3, 99, 3, 2, key="band_pass_filter")

    # Convert to Gray
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # High Pass Filter
    img_high_pass = cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

    # Low Pass Filter
    img_low_pass = cv2.blur(img, (kernel_size, kernel_size))

    # Band Pass Filter
    img_band_pass = img_high_pass - img_low_pass

    # Show Image
    func.show_image_st(img_band_pass, None, None)

def median_filter(img):
    # Kernel Size
    kernel_size = st.slider("Kernel Size:", 1, 99, 1, 2, key="median_filter")

    # Median Filter 
    img_median = cv2.medianBlur(img, kernel_size)

    # Show Image
    func.show_image_st(img_median, None, None)

# MAIN CONFIG
if __name__ == "__main__":
    main()