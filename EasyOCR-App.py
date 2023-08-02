import streamlit as st
import easyocr as ocr
from PIL import Image
import requests
from io import BytesIO
import numpy as np
from pytesseract import pytesseract


st.title('OCR')

url_image = st.text_input('Enter the image url',placeholder='Type or Paste image url here')

st.write('OR')

#Upload image
upl_image = st.file_uploader('Upload the image',type=['png','jpg','jpeg'])

def load_model(): 
    reader = ocr.Reader(['en'])
    return reader 

reader = load_model()

if url_image is not None:
    try:
        response = requests.get(url_image)
    
        # Read the image data into a PIL Image object
        input_image = Image.open(BytesIO(response.content))
        
        st.image(input_image) #display image
    
        result = reader.readtext(np.array(input_image))

        result_text = [] #empty list for results

        for text in result:
            result_text.append(text[1])
        st.write("Easy OCR Result:")
        st.write(result_text)

        #Tesseract
        text = pytesseract.image_to_string(input_image)

        # Displaying the extracted text
        st.write("Tesseract OCR Result:")
        st.write(text[:-1])

        
    except:
        pass
else:
    pass
    
if upl_image is not None:
    try:
        input_image = Image.open(upl_image) #read image
        st.image(input_image) #display image
    
        result = reader.readtext(np.array(input_image))

        result_text = [] #empty list for results

        for text in result:
            result_text.append(text[1])
        st.write("Easy OCR Result:")
        st.write(result_text)

        #Tesseract
        text = pytesseract.image_to_string(input_image)
        
        # Displaying the extracted text
        st.write("Tesseract OCR Result:")
        st.write(text[:-1])
        
    except:
        pass
else:
    pass
