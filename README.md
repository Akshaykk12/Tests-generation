# AI-Powered Test Case Generator

## Introduction

This Streamlit application generates detailed test cases based on image captions and optional context. It uses the BLIP (Bootstrapped Language-Image Pre-training) model to generate captions from uploaded images and EasyOCR for extracting text from images. The application then combines these elements to create comprehensive test cases with the help of Google Generative AI.

### Features

- **Image Upload:** Upload an image to be processed.
- **Image Captioning:** Generate captions for the uploaded image using the BLIP model.
- **OCR Text Extraction:** Extract text from the image using EasyOCR.
- **Test Case Generation:** Create detailed test cases based on the image caption and optional context.

## Get Started

### Prerequisites

- Python 3.7 or higher
- Pip (Python package installer)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv myenv
   ```

3. **Activate the virtual environment:**
   *On Windows:*
   ```bash
   myenv\Scripts\activate
   ```
   *On macOS/Linux:*
   ```bash
   source myenv/bin/activate
   ```
   
4. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables:**
   Create a .env file in the root directory of the project with the following content:

   ```bash
   API_KEY=your_google_api_key
   ```

6. **Run the Streamlit application:**
   ```bash
   streamlit run main.py
   ```
   
## Usage
**Upload an Image:**
Click on the "Upload an image" button to select an image file (PNG, JPG, or JPEG).

**Enter Optional Context:**
Provide any additional context related to the image in the text input field.

**Generate Test Case:**
Click the "Generate Testcase" button to process the image and generate test instructions.

**View Results:**
The generated test instructions will be displayed below the button.

## Troubleshooting
**API Key Issues:** Ensure that you have set the API_KEY in the .env file correctly. For more details on obtaining a Google API key, refer to the Google Generative AI documentation.

Contact
For any questions or inquiries, please reach out to akshaykudalkar.12@gmail.com.

