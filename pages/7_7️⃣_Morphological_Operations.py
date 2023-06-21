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
    img = st.file_uploader("Choose original image...", type=["jpg","png"])
    if img is not None:
        img = np.frombuffer(img.read(), np.uint8)
        img = cv2.imdecode(img, cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Original Image
        with st.expander("Original Image"):
            func.show_image_st(img, 'Original Image', None)

        binary_setting(img)

# FUNCTIONS
# Set Page
def set_page():
    st.set_page_config(
        page_title="Morphological Operations",
        page_icon="7️⃣",
        layout="centered",
        initial_sidebar_state="auto",
    )

    if 'converted' not in st.session_state:
        st.session_state.converted = False

    if 'threshold' not in st.session_state:
        st.session_state.threshold = 0

# tab
def tab(img):
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Erosion", "Dilation", "Opening", "Closing", "Gradient", "Boundary Extraction", "Skeletonization"])

    with tab1:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>Erosion</h1>", unsafe_allow_html=True)

        # Erosion Image
        erosion(img)

    with tab2:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>Dilation</h1>", unsafe_allow_html=True)

        # Dilation Image
        dilation(img)

    with tab3:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>Opening</h1>", unsafe_allow_html=True)

        # Opening Image
        opening(img)

    with tab4:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>Closing</h1>", unsafe_allow_html=True)

        # Closing Image
        closing(img)

    with tab5:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>Gradient</h1>", unsafe_allow_html=True)

        # Gradient Image
        gradient(img)

    with tab6:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>Boundary Extraction</h1>", unsafe_allow_html=True)

        # Boundary Extraction Image
        boundary_extraction(img)

    with tab7:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>Skeletonization</h1>", unsafe_allow_html=True)

        # Skeletonization Image
        skeletonization(img)

# Erosion
def erosion(img):
    # Kernel
    kernel = st.slider("Kernel", 1, 10, 3, 1, key="erosion")

    # Erosion
    erosion = cv2.erode(img, np.ones((kernel, kernel), np.uint8), iterations=1)

    # Show Image
    func.show_image_st(erosion, 'Erosion Image', None)

# Dilation
def dilation(img):
    # Kernel
    kernel = st.slider("Kernel", 1, 10, 3, 1, key="dilation")

    # Dilation
    dilation = cv2.dilate(img, np.ones((kernel, kernel), np.uint8), iterations=1)

    # Show Image
    func.show_image_st(dilation, 'Dilation Image', None)

# Opening
def opening(img):
    # Kernel
    kernel = st.slider("Kernel", 1, 10, 3, 1, key="opening")

    # Opening
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, np.ones((kernel, kernel), np.uint8))

    # Show Image
    func.show_image_st(opening, 'Opening Image', None)

# Closing
def closing(img):
    # Kernel
    kernel = st.slider("Kernel", 1, 10, 3, 1, key="closing")

    # Closing
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, np.ones((kernel, kernel), np.uint8))

    # Show Image
    func.show_image_st(closing, 'Closing Image', None)

# Gradient
def gradient(img):
    # Kernel
    kernel = st.slider("Kernel", 1, 10, 3, 1, key="gradient")

    # Gradient
    gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, np.ones((kernel, kernel), np.uint8))

    # Show Image
    func.show_image_st(gradient, 'Gradient Image', None)

# Boundary Extraction
def boundary_extraction(img):
    # Kernel
    kernel = st.slider("Kernel", 1, 10, 3, 1, key="boundary_extraction")

    # Erosion
    erosion = cv2.erode(img, np.ones((kernel, kernel), np.uint8), iterations=1)

    # Boundary Extraction
    boundary_extraction = img - erosion

    # Show Image
    func.show_image_st(boundary_extraction, 'Boundary Extraction Image', None)

# Skeletonization
def skeletonization(img):
    # Kernel
    element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    skel = np.zeros(img.shape, np.uint8)

    # Apply morphological transformation
    while True:
        open = cv2.morphologyEx(img, cv2.MORPH_OPEN, element)
        temp = cv2.subtract(img, open)
        eroded = cv2.erode(img, element)
        skel = cv2.bitwise_or(skel, temp)
        img = eroded.copy()

        if (cv2.countNonZero(img) == 0):
            break

    # Show Image
    func.show_image_st(skel, 'Skeletonization Image', None)

# Setting
def binary_setting(img):
    # Button
    if not st.session_state.converted:
        # Threshold
        threshold = st.slider("Threshold", 0, 255, 127, 1, key="binary_setting")

        # Convert Image to Grayscale
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        # Convert Image to Binary
        ret, binary_img = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)

        st.session_state.threshold = threshold
        print(threshold)

        st.button("Apply Threshold", key="binary_button_apply", on_click=applyBinary)

        # Show Image
        func.show_image_st(binary_img, 'Binary Image', None)
    else:
        st.button("Reset Threshold", key="binary_button_reset", on_click=resetBinary)

    if (st.session_state.converted):
        # Get Threshold Value
        threshold = st.session_state.threshold

        # Convert Image to Grayscale
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        # Convert Image to Binary
        ret, binary_img = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)

        tab(binary_img)
    else:
        st.write("Please apply threshold first")

# Apply Binary
def applyBinary():
    st.session_state.converted = True

# Reset Binary
def resetBinary():
    st.session_state.converted = False

# MAIN CONFIG
if __name__ == "__main__":
    main()