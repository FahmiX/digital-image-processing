# Package / Library
import streamlit as st
import numpy as np
import cv2
import matplotlib.pyplot as plt
import pandas as pd
import datetime
from PIL import Image

# Fungsi Show Image
def show_image_plt(image, title="", type=""):
    # Set the size of the figure
    fig, ax = plt.subplots(figsize=(5, 5))
    
    # Show the image
    ax.imshow(image, cmap=type)
    
    # Set the title and turn off the axis
    ax.set_title(title)
    ax.axis("off")
    
    # Display the plot using Streamlit
    st.pyplot(fig)

def show_image_st(image, title=None, size=None):
    if (size is not None):
        image = cv2.resize(image, (size, size))

    # Show the image
    st.image(image, caption=title, use_column_width=True)

def download_image(img, title):
    # Convert Image to BGR again
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # Decode Numpy
    _, encoded_img = cv2.imencode(".png", img)
    result = encoded_img.tobytes()

    # Download Image
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

    st.download_button(
        label="Download {} Image".format(title),
        data=result,
        file_name="{}.{}.png".format(title, timestamp),
        mime="image/png",
    )