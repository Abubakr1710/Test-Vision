# from black import Encoding
# import cv2
# import streamlit as st
# from PIL import Image
# import numpy as np
# header = st.container()

# with header:
#     st.title("'Test Vision' hizmatingizda")
#     st.markdown('#### Bizning aqlli test javoblarini hisoblagich orqali natijalarini odatdagidan kamida 3 barobar tezroq')

# def image_view():
#      image_file = st.file_uploader("Upload Your Image", type=['jpg', 'png', 'jpeg'])
#      if not image_file:
#         return None
     
#      original_image = Image.open(image_file)
#      original_image = np.array(original_image)
#      st.text('Original Image')
#      st.image(original_image)

# if __name__ == '__main__':
#      image_view()




import cv2
import streamlit as st
import numpy as np
from PIL import Image


def brighten_image(image, amount):
    img_bright = cv2.convertScaleAbs(image, beta=amount)
    return img_bright


def blur_image(image, amount):
    blur_img = cv2.GaussianBlur(image, (11, 11), amount)
    return blur_img


def enhance_details(img):
    hdr = cv2.detailEnhance(img, sigma_s=12, sigma_r=0.15)
    return hdr


def main_loop():
    st.title("OpenCV Demo App")
    st.subheader("This app allows you to play with Image filters!")
    st.text("We use OpenCV and Streamlit for this demo")

    blur_rate = st.sidebar.slider("Blurring", min_value=0.5, max_value=3.5)
    brightness_amount = st.sidebar.slider("Brightness", min_value=-50, max_value=50, value=0)
    apply_enhancement_filter = st.sidebar.checkbox('Enhance Details')

    image_file = st.file_uploader("Upload Your Image", type=['jpg', 'png', 'jpeg'])
    if not image_file:
        return None

    original_image = Image.open(image_file)
    original_image = np.array(original_image)

    processed_image = blur_image(original_image, blur_rate)
    processed_image = brighten_image(processed_image, brightness_amount)
    resized_img = cv2.resize(processed_image, (500,500))

    if apply_enhancement_filter:
        processed_image = enhance_details(processed_image)

    st.text("Original Image vs Processed Image")
    st.image([original_image, resized_img])


if __name__ == '__main__':
    main_loop()