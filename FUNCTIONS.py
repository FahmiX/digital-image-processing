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

def colors(color):
    match color:
        case "red":
            return (255, 0, 0)
        case "green":
            return (0, 255, 0)
        case "blue":
            return (0, 0, 255)
        case "yellow":
            return (255, 255, 0)
        case "magenta":
            return (255, 0, 255)
        case "cyan":
            return (0, 255, 255)
        case "white":
            return (255, 255, 255)
        case "black":
            return (0, 0, 0)
        case "gray":
            return (128, 128, 128)
        case _:
            return (0, 0, 0)
        
def hex_to_rgb(hex):
    hex = hex.lstrip("#")
    hlen = len(hex)
    return tuple(int(hex[i:i+hlen//3], 16) for i in range(0, hlen, hlen//3))