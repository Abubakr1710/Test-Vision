from pickle import FRAME
from turtle import color
import cv2
import streamlit as st

st.title('Webcam Test')
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
cam =  cv2.VideoCapture(0)

while run:
    ret, frame = cam.read()
    #frame = cv2.cv
    FRAME_WINDOW.image(frame)
else:
    st.write('Stopped')