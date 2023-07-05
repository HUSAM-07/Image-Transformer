import os
import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter

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

    upload_path = ""
    download_path = ""

    st.image(main_image, use_column_width='auto')
    st.title("✨ PropReturns Internal Image Enhancer  ")
    st.info('✨ Supports all popular image formats - PNG, JPG, BMP ')

    uploaded_file = st.file_uploader("Upload Image 🖼", type=["png", "jpg", "bmp", "jpeg"])

    if uploaded_file is not None:
        with open(os.path.join(upload_path, uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())

        with st.spinner(f"Enhancing... "):
            uploaded_image = os.path.abspath(os.path.join(upload_path, uploaded_file.name))
            downloaded_image = os.path.abspath(os.path.join(download_path, str("enhanced_" + uploaded_file.name)))
            enhance_image(uploaded_image, downloaded_image)

            final_image = Image.open(downloaded_image)
            st.markdown("---")
            st.image(final_image, caption='This is how your enhanced image looks like 😉')
            with open(downloaded_image, "rb") as file:
                if uploaded_file.name.endswith(('.jpg', '.JPG')):
                    if st.download_button(
                            label="Download Enhanced Image 📷",
                            data=file,
                            file_name=str("enhanced_" + uploaded_file.name),
                            mime='image/jpg'
                    ):
                        download_success()

                elif uploaded_file.name.endswith(('.jpeg', '.JPEG')):
                    if st.download_button(
                            label="Download Enhanced Image 📷",
                            data=file,
                            file_name=str("enhanced_" + uploaded_file.name),
                            mime='image/jpeg'
                    ):
                        download_success()

                elif uploaded_file.name.endswith(('.png', '.PNG')):
                    if st.download_button(
                            label="Download Enhanced Image 📷",
                            data=file,
                            file_name=str("enhanced_" + uploaded_file.name),
                            mime='image/png'
                    ):
                        download_success()

                else:
                    st.warning('⚠ Please upload an image file with a supported format!')

    else:
        st.warning('⚠ Please upload your image file!')

    st.markdown("<br><hr><center>Made by <a href='mailto:workforhusam@gmail.com?subject=Propreturns Image Enhancement WebApp!&body=Please specify the issue you are facing with the app.'><strong>Mohammed Husamuddin</strong></a></center><hr>", unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()
