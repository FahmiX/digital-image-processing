# Package / Library
import streamlit as st
import cv2
import numpy as np
import matplotlib.pyplot as plt
import FUNCTIONS as func
from scipy import ndimage

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
        page_title="Countour",
        page_icon="9️⃣",
        layout="centered",
        initial_sidebar_state="auto",
    )

# tab
def tab(img):
    tab1, tab2 = st.tabs(["Contour", "Convex Hull"])

    with tab1:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>Contour</h1>", unsafe_allow_html=True)

        # Contour
        contour(img)

    with tab2:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>Convex Hull</h1>", unsafe_allow_html=True)

        # Convex Hull
        convex_hull(img)

# Chain Code
def contour(img):
    countour_img = img.copy()

    # Choose color
    color = choose_color('contour')

    # Convert image to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Blur image
    img_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)

    # Thresholding
    ret, img_thresh = cv2.threshold(img_blur, 1, 255, cv2.THRESH_OTSU)

    # Find contours
    contours, hierarchy = cv2.findContours(img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours
    img_contour = cv2.drawContours(countour_img, contours, -1, color, 2)

    # Show image
    func.show_image_st(img_contour, 'Chain Code', None)

# Convex Hull  
def convex_hull(img):
    hull_img = img.copy()

    # Choose color
    color = choose_color('convex_hull')

    # Convert image to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Blur image
    img_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)

    # Thresholding
    ret, img_thresh = cv2.threshold(img_blur, 1, 255, cv2.THRESH_OTSU)

    # Find contours
    contours, hierarchy = cv2.findContours(img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Convex Hull
    hull = []
    for i in range(len(contours)):
        hull.append(cv2.convexHull(contours[i], False))

    # Draw contours
    img_contour = cv2.drawContours(hull_img, hull, -1, color, 2)

    # Show image
    func.show_image_st(img_contour, 'Convex Hull', None)

def choose_color(key=None):
    color = st.selectbox("Choose color", ("red", "green", "blue", "yellow", "magenta", "cyan", "white", "black", "gray"), key=key)
    return func.colors(color)

# MAIN CONFIG
if __name__ == "__main__":
    main()