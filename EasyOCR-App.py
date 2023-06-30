import streamlit as st
import easyocr as ocr
from PIL import Image
import requests
from io import BytesIO
import numpy as np

st.title('Easy OCR')

image = st.text_input('Enter the image url',placeholder='Type or Paste image url here')
#response = requests.get(image)

# Read the image data into a PIL Image object
#input_image = Image.open(BytesIO(response.content))

st.write('OR')

#Upload image
image = st.file_uploader(label = '',type=['png','jpg','jpeg'])

def load_model(): 
    reader = ocr.Reader(['en'])
    return reader 

reader = load_model()

if image is not None:

    input_image = Image.open(image) #read image
    st.image(input_image) #display image

    with st.spinner("AI is at Work! "): 

        result = reader.readtext(np.array(input_image))

        result_text = [] #empty list for results

        for text in result:
            result_text.append(text[1])

        st.write(result_text)
    #st.success("Here you go!")
    st.balloons()
else:
    pass
