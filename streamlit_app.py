import os
import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
import tempfile
import shutil
import sys
import subprocess

# Check if running in development
if __name__ == "__main__":
    try:
        import streamlit
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "streamlit"])
        import streamlit

# Create temp directories for upload and download
def create_temp_directories():
    temp_upload = tempfile.mkdtemp()
    temp_download = tempfile.mkdtemp()
    return temp_upload, temp_download

# Clean up temp directories
def cleanup_temp_directories(upload_dir, download_dir):
    shutil.rmtree(upload_dir, ignore_errors=True)
    shutil.rmtree(download_dir, ignore_errors=True)

def enhance_image(input_image_path, output_image_path):
    # Open the image
    image = Image.open(input_image_path)

    # Enhance brightness
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(1.2)  # Increase brightness by 20%

    # Enhance contrast
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(1.2)  # Increase contrast by 20%

    # Enhance sharpness
    enhancer = ImageEnhance.Sharpness(image)
    image = enhancer.enhance(1.6)  # Increase sharpness by 20%

    # Save the enhanced image
    image.save(output_image_path)

# Function to handle successful download
def download_success():
    st.success('Download completed successfully!')

# Main function
def main():
    st.set_page_config(
        page_title="PropReturns Image Enhancer",
        page_icon="✨",
        layout="centered",
        initial_sidebar_state="auto",
    )
    main_image = Image.open('static/main_banner.png')

    upload_path, download_path = create_temp_directories()

    st.image(main_image, use_container_width=True)
    st.title("✨ PropReturns Internal Image Enhancer  ")
    st.info('✨ Supports all popular image formats - PNG, JPG, BMP ')

    uploaded_file = st.file_uploader("Upload Image 🖼", type=["png", "jpg", "bmp", "jpeg"])

    if uploaded_file is not None:
        # Save uploaded file to temp directory
        temp_upload_path = os.path.join(upload_path, uploaded_file.name)
        with open(temp_upload_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        with st.spinner("Enhancing... "):
            temp_download_path = os.path.join(download_path, f"enhanced_{uploaded_file.name}")
            enhance_image(temp_upload_path, temp_download_path)

            final_image = Image.open(temp_download_path)
            st.markdown("---")
            st.image(final_image, caption='This is how your enhanced image looks like 😉')
            
            # Simplified download handling
            with open(temp_download_path, "rb") as file:
                file_extension = os.path.splitext(uploaded_file.name)[1].lower()
                mime_types = {
                    '.jpg': 'image/jpg',
                    '.jpeg': 'image/jpeg',
                    '.png': 'image/png',
                    '.bmp': 'image/bmp'
                }
                
                if file_extension in mime_types:
                    if st.download_button(
                        label="Download Enhanced Image 📷",
                        data=file,
                        file_name=f"enhanced_{uploaded_file.name}",
                        mime=mime_types[file_extension]
                    ):
                        download_success()
                else:
                    st.warning('⚠ Please upload an image file with a supported format!')

    else:
        st.warning('⚠ Please upload your image file!')

    st.markdown("<br><hr><center>Made by <a href='mailto:workforhusam@gmail.com?subject=Propreturns Image Enhancement WebApp!&body=Please specify the issue you are facing with the app.'><strong>Mohammed Husamuddin</strong></a></center><hr>", unsafe_allow_html=True)

    # Clean up temp directories when the session ends
    cleanup_temp_directories(upload_path, download_path)

# Run the app
if __name__ == "__main__":
    main()
