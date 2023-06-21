# Package / Library
import streamlit as st
import numpy as np
import cv2
import FUNCTIONS as func
import matplotlib.pyplot as plt
from skimage import exposure
from skimage.exposure import match_histograms

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
        page_title="Histogram",
        page_icon="5️⃣",
        layout="centered",
        initial_sidebar_state="auto",
    )

def tab(img):
    tab1, tab2, tab3 = st.tabs(["Histogram Original", "Histogram Equalization", "Histogram Matching"])

    with tab1:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>Histogram</h1>", unsafe_allow_html=True)

        # Histogram Image
        histogram(img)

    with tab2:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>Histogram Equalization</h1>", unsafe_allow_html=True)

        # Histogram Equalization Image
        histogram_equalization(img)

    with tab3:
        # Title
        st.markdown("<h1 style='text-align: center; color: white;'>Histogram Matching</h1>", unsafe_allow_html=True)

        # Histogram Matching Image
        histogram_matching(img)

def histogram(img):
    # Colors
    colors = ('r','g','b')

    # Histogram Image
    with st.expander("Histogram Original"):
        # Plot
        fig, ax = plt.subplots(1, 3, figsize=(15, 5))
        for i, col in enumerate(colors):
            histr = cv2.calcHist([img], [i], None, [256], [0, 256])
            ax[i].plot(histr, color=col)
            ax[i].set_xlim([0, 256])
            ax[i].set_title(col.upper())
            ax[i].set_xlabel('Bins')
            ax[i].set_ylabel('Number of Pixels')
        st.pyplot(fig)

        fig, ax = plt.subplots()
        ax.set_title("RGB")
        ax.set_xlabel("Bins")
        ax.set_ylabel("Number of Pixels")
        for i, col in enumerate(colors):
            hist = cv2.calcHist([img], [i], None, [256], [0,256])
            ax.plot(hist, color=col)
            ax.set_xlim([0,256])
        st.pyplot(fig)        

def histogram_equalization(img):
    # Colors
    colors = ('r','g','b')

    # Convert Image from RGB to YCrCb
    img_yuv = cv2.cvtColor(img, cv2.COLOR_RGB2YCrCb)

    # Equalize the histogram of the Y channel
    img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])

    # Convert the YUV image back to RGB format
    img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YCrCb2RGB)

    # Show Image
    with st.expander("Output Image"):
        func.show_image_st(img_output, 'Output Image', None)

    # Histogram Equalization Image
    with st.expander("Histogram Equalization"):
        # Plot
        fig, ax = plt.subplots(1, 3, figsize=(15, 5))
        for i, col in enumerate(colors):
            histr = cv2.calcHist([img_output], [i], None, [256], [0, 256])
            ax[i].plot(histr, color=col)
            ax[i].set_xlim([0, 256])
            ax[i].set_title(col.upper())
            ax[i].set_xlabel('Bins')
            ax[i].set_ylabel('Number of Pixels')
        st.pyplot(fig)

        fig, ax = plt.subplots()
        ax.set_title("RGB")
        ax.set_xlabel("Bins")
        ax.set_ylabel("Number of Pixels")
        for i, col in enumerate(colors):
            hist = cv2.calcHist([img_output], [i], None, [256], [0,256])
            ax.plot(hist, color=col)
            ax.set_xlim([0,256])
        st.pyplot(fig)

def histogram_matching(img):
    img2 = st.file_uploader("Choose image to match...", type=["jpg", "png"])
    if img2 is not None:
        img2 = np.frombuffer(img2.read(), np.uint8)
        img2 = cv2.imdecode(img2, cv2.IMREAD_COLOR)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

        # Match Size
        img2 = cv2.resize(img2, (img.shape[1], img.shape[0]))

        # Match Histogram
        matched = match_histograms(img, img2, channel_axis=-1)

        # Show Image
        with st.expander("Reference Image"):
            func.show_image_st(img2, 'Reference Image', None)

        with st.expander("Output Image"):
            func.show_image_st(matched, 'Output Image', None)

        # Histogram Matching Image
        with st.expander("Histogram Matching"):
            # Colors
            colors = ('r','g','b')

            # Plot
            fig, ax = plt.subplots(1, 3, figsize=(15, 5))
            for i, col in enumerate(colors):
                histr = cv2.calcHist([matched], [i], None, [256], [0, 256])
                ax[i].plot(histr, color=col)
                ax[i].set_xlim([0, 256])
                ax[i].set_title(col.upper())
                ax[i].set_xlabel('Bins')
                ax[i].set_ylabel('Number of Pixels')
            st.pyplot(fig)

            fig, ax = plt.subplots()
            ax.set_title("RGB")
            ax.set_xlabel("Bins")
            ax.set_ylabel("Number of Pixels")
            for i, col in enumerate(colors):
                hist = cv2.calcHist([matched], [i], None, [256], [0,256])
                ax.plot(hist, color=col)
                ax.set_xlim([0,256])
            st.pyplot(fig)

# MAIN CONFIG
if __name__ == "__main__":
    main()