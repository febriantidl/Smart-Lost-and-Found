import streamlit as st
import cv2
import numpy as np
import os

from sklearn.metrics.pairwise import cosine_similarity

st.title("Smart Lost & Found")
st.write("Sistem pencarian barang hilang di Polindra menggunakan AI dan Image Processing.")
