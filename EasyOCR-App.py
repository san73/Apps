import streamlit as st
import easyocr as ocr
from PIL import Image
import requests
from io import BytesIO
import numpy as np

st.title('Easy OCR')

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
        st.write("Result:")
        st.write(result_text)
        
    except:
        pass
else:
    pass
    
if upl_image is not None:
    try:
        input_image = Image.open(upl_image) #read image
        st.image(input_image) #display image
    
        with st.spinner("AI is at Work! "): 
    
            result = reader.readtext(np.array(input_image))
    
            result_text = [] #empty list for results
    
            for text in result:
                result_text.append(text[1])
            st.write("Result:")
            st.write(result_text)
    except:
        pass
else:
    pass
