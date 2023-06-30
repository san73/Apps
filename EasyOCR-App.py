import streamlit
import easyocr as ocr
from PIL import Image
import requests
from io import BytesIO
import numpy as np

st.write('Easy OCR - Text from Images')

#Upload image
image = st.file_uploader(label = "Upload your image here",type=['png','jpg','jpeg'])

# Send a GET request to retrieve the image

st.write('OR')

#image = st.text_input('Enter the image url')
#response = requests.get(image)

# Read the image data into a PIL Image object
#input_image = Image.open(BytesIO(response.content))


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
    st.write("Upload an Image")
