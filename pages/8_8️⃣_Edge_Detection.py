# Package / Library
import streamlit as st
import cv2
import numpy as np
import FUNCTIONS as func
import matplotlib.pyplot as plt
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
        page_title="Edge Detection",
        page_icon="8️⃣",
        layout="centered",
        initial_sidebar_state="auto",
    )

# tab
def tab(img):
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Roberts", "Sobel", "Prewitt", "Laplace", "LoG", "Kirsch", "Canny"])

    with tab1:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>Roberts</h1>", unsafe_allow_html=True)

        # Roberts Operator
        roberts(img)

    with tab2:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>Sobel</h1>", unsafe_allow_html=True)

        # Sobel Operator
        sobel(img)

    with tab3:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>Prewitt</h1>", unsafe_allow_html=True)

        # Prewitt Operator
        prewitt(img)

    with tab4:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>Laplace</h1>", unsafe_allow_html=True)

        # Laplace Operator
        laplace(img)

    with tab5:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>LoG</h1>", unsafe_allow_html=True)

        # LoG Operator
        log(img)

    with tab6:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>Kirsch</h1>", unsafe_allow_html=True)

        # Kirsch Operator
        kirsch(img)

    with tab7:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>Canny</h1>", unsafe_allow_html=True)

        # Canny Operator
        canny(img)

# Roberts Operator
def roberts(img):
    # Convert Image to Grayscale
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY).astype('float64')

    # Kernel X
    kernel_x = np.array([
        [1, 0],
        [0, -1]
    ])
    
    # Kernel Y
    kernel_y = np.array([
        [0, 1],
        [-1, 0]
    ])

    # Roberts X
    roberts_x = cv2.filter2D(img, -1, kernel_x)

    # Roberts Y
    roberts_y = cv2.filter2D(img, -1, kernel_y)

    # Combine Roberts X and Roberts Y
    roberts = np.sqrt(np.square(roberts_x) + np.square(roberts_y))
    roberts = np.round(roberts)
    roberts = np.clip(roberts, 0, 255)

    # Show Image
    cv2.imwrite('output.jpg', roberts)
    func.show_image_st('output.jpg', 'Roberts', None)

# Sobel Operator
def sobel(img):
    # Convert Image to Grayscale
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY).astype('float64')
    
    # Kernel X
    kernel_x = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ])

    # Kernel Y
    kernel_y = np.array([
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]
    ])

    # Sobel X
    sobel_x = cv2.filter2D(img, -1, kernel_x)

    # Sobel Y
    sobel_y = cv2.filter2D(img, -1, kernel_y)

    # Combine Sobel X and Sobel Y
    sobel = np.sqrt(np.square(sobel_x) + np.square(sobel_y))

    # Show Image
    cv2.imwrite('output.jpg', sobel)
    func.show_image_st('output.jpg', 'Sobel', None)

# Prewitt Operator
def prewitt(img):
    # Convert Image to Grayscale
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY).astype('float64')
    
    # Kernel X
    kernel_x = np.array([
        [-1, 0, 1],
        [-1, 0, 1],
        [-1, 0, 1]
    ])

    # Kernel Y
    kernel_y = np.array([
        [-1, -1, -1],
        [0, 0, 0],
        [1, 1, 1]
    ])

    # Prewitt X
    prewitt_x = cv2.filter2D(img, -1, kernel_x)

    # Prewitt Y
    prewitt_y = cv2.filter2D(img, -1, kernel_y)

    # Combine Prewitt X and Prewitt Y
    prewitt = np.sqrt(np.square(prewitt_x) + np.square(prewitt_y))

    # Show Image
    cv2.imwrite('output.jpg', prewitt)
    func.show_image_st('output.jpg', 'Prewitt', None)

# Laplace Operator
def laplace(img):
    # Convert Image to Grayscale
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Laplace
    laplace = cv2.Laplacian(img, cv2.CV_64F)

    # Show Image
    cv2.imwrite('output.jpg', laplace)
    func.show_image_st('output.jpg', 'Laplace', None)

# LoG Operator
def log(img):
    # Convert Image to Grayscale
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # LoG
    log = ndimage.gaussian_laplace(img, sigma=1)

    # Show Image
    cv2.imwrite('output.jpg', log)
    func.show_image_st('output.jpg', 'LoG', None)

# Kirsch Operator
def kirsch(img):
    # West
    kernel_west = np.array([
        [-3, -3, 5],
        [-3, 0, 5],
        [-3, -3, 5]
    ])

    # North West
    kernel_north_west = np.array([
        [-3, 5, 5],
        [-3, 0, 5],
        [-3, -3, -3]
    ])

    # North
    kernel_north = np.array([
        [5, 5, 5],
        [-3, 0, -3],
        [-3, -3, -3]
    ])

    # North East
    kernel_north_east = np.array([
        [5, 5, -3],
        [5, 0, -3],
        [-3, -3, -3]
    ])

    # East
    kernel_east = np.array([
        [5, -3, -3],
        [5, 0, -3],
        [5, -3, -3]
    ])

    # South East
    kernel_south_east = np.array([
        [-3, -3, -3],
        [5, 0, -3],
        [5, 5, -3]
    ])

    # South
    kernel_south = np.array([
        [-3, -3, -3],
        [-3, 0, -3],
        [5, 5, 5]
    ])

    # South West
    kernel_south_west = np.array([
        [-3, -3, -3],
        [-3, 0, 5],
        [-3, 5, 5]
    ])

    # Convert Image to Grayscale
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Kirsch
    kirsch_west = cv2.filter2D(img, -1, kernel_west)

    kirsch_north_west = cv2.filter2D(img, -1, kernel_north_west)

    kirsch_north = cv2.filter2D(img, -1, kernel_north)

    kirsch_north_east = cv2.filter2D(img, -1, kernel_north_east)

    kirsch_east = cv2.filter2D(img, -1, kernel_east)

    kirsch_south_east = cv2.filter2D(img, -1, kernel_south_east)

    kirsch_south = cv2.filter2D(img, -1, kernel_south)

    kirsch_south_west = cv2.filter2D(img, -1, kernel_south_west)

    # Combine Kirsch
    kirsch = np.maximum(kirsch_west, kirsch_north_west)
    kirsch = np.maximum(kirsch, kirsch_north)
    kirsch = np.maximum(kirsch, kirsch_north_east)
    kirsch = np.maximum(kirsch, kirsch_east)
    kirsch = np.maximum(kirsch, kirsch_south_east)
    kirsch = np.maximum(kirsch, kirsch_south)
    kirsch = np.maximum(kirsch, kirsch_south_west)

    # Show Image
    cv2.imwrite('output.jpg', kirsch)
    func.show_image_st('output.jpg', 'Kirsch', None)

# Canny Operator
def canny(img):
    upper_threshold = st.slider('Upper Threshold', 0, 255, 100)
    lower_threshold = st.slider('Lower2 Threshold', 0, 255, 200)

    # Convert Image to Grayscale
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Canny
    canny = cv2.Canny(img, lower_threshold, upper_threshold, apertureSize=3, L2gradient=True)

    # Show Image
    cv2.imwrite('output.jpg', canny)
    func.show_image_st('output.jpg', 'Canny', None)

# MAIN CONFIG
if __name__ == "__main__":
    main()