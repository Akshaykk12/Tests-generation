import streamlit as st
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import easyocr
import numpy as np
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("API_KEY"))

reader = easyocr.Reader(['en'])

@st.cache_resource
def load_blip_model():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

def generate_image_caption(image):
    inputs = blip_processor(images=image, return_tensors="pt")
    caption_ids = blip_model.generate(**inputs)
    caption = blip_processor.decode(caption_ids[0], skip_special_tokens=True)
    return caption

def combine_input(image_caption, optional_text=None):
    if optional_text:
        return f"Image Description: {image_caption}. Context: {optional_text}."
    return f"Image Description: {image_caption}."

def create_prompt_with_example(image_caption, optional_text):
    example = """
    Example:
    Input: Image Description: a shopping cart page showing items, quantities, and a "Checkout" button.
Context (optional): "The user should be able to review the items in the cart and proceed to checkout."
Output:
Test Case 2: Shopping Cart Review and Checkout

Description: Ensures that users can review the items in their cart and proceed to the checkout page.
Pre-conditions:
User must be logged in.
At least one item should be added to the cart.
Testing Steps:
Open the shopping cart page.
Verify that the correct items and quantities are listed.
Click the "Checkout" button.
Expected Result:
User is taken to the checkout page.
The correct total price is displayed.
    """

    prompt = f"""
    Based on the following description and context, generate a detailed test case including:
    - Description: A brief explanation of what the test case is about.
    - Pre-conditions: Any conditions that must be met before starting the test.
    - Testing Steps: A step-by-step guide on how to perform the test.
    - Expected Result: What the expected outcome should be if the feature works correctly.

    {example}

    Now, generate a test case for the following:

    Image Description: {image_caption}
    Context: {optional_text}

    Test Case:
    """
    return prompt

def generate_test_instructions_flant5(input_text):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(input_text)
    return response.text

def perform_ocr(image):
    image_np = np.array(image)
    results = reader.readtext(image_np)
    text = ' '.join([result[1] for result in results])
    return text

st.title("AI-Powered Test Case Generator")

uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
blip_processor, blip_model = load_blip_model()

if uploaded_image:
    image = Image.open(uploaded_image)

    st.image(image, caption="Uploaded Image", use_column_width=True)
    optional_text = st.text_input("Enter optional context")
    
    if st.button("Generate Testcase"):
        ocr_text = perform_ocr(image)
        caption = generate_image_caption(image)
        prompt = create_prompt_with_example(caption, optional_text) + f"\n Use buttons that are in images: {ocr_text}, dont come up with your buttons and steps."
        
        test_instructions = generate_test_instructions_flant5(prompt)
        st.write("Generated Test Instructions:")
        st.code(test_instructions)
