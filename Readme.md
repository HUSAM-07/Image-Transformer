# PropReturns Image Enhancer Documentation

The PropReturns Image Enhancer is a web application built using Streamlit and hosted on Streamlit Cloud. It allows users to upload images in popular formats such as PNG, JPG, BMP, and JPEG, and enhances them by adjusting brightness, contrast, and sharpness. The enhanced image can then be downloaded.

## Application Features

- Supports popular image formats: PNG, JPG, BMP, and JPEG.
- Enhances uploaded images by adjusting brightness, contrast, and sharpness.
- Displays the enhanced image and provides an option to download it.
- Provides feedback messages for successful image uploads and downloads.
- Created by Mohammed Husamuddin.

## Installation

To use the PropReturns Image Enhancer application locally, follow these steps:

1. Install the required dependencies by running the following command in your terminal:

```pip install streamlit Pillow```

2. Save the code provided in a Python file, for example, `image_enhancer.py`.

3. Run the application using the following command:

```streamlit run image_enhancer.py```

## Usage

1. Open the PropReturns Image Enhancer web application using the following URL: [PropReturns Image Enhancer](https://propreturns-image-enhancer.streamlit.app/).

2. You will see the main banner and title of the application.

3. Click the "Upload Image 🖼" button to select an image file from your local device. Only files with the extensions `.png`, `.jpg`, `.bmp`, and `.jpeg` are supported.

4. Once the image is uploaded, the application will display a spinner and start enhancing the image. The enhancement process involves increasing the brightness, contrast, and sharpness of the image.

5. After the enhancement is complete, the application will display the enhanced image along with a caption indicating the result.

6. Below the enhanced image, you will find a "Download Enhanced Image 📷" button. Clicking this button will initiate the download of the enhanced image file.

7. Depending on the format of the uploaded image, the downloaded file will have the prefix "enhanced_" added to its original filename.

8. If the uploaded file has an unsupported format or no file is uploaded, the application will display a warning message.

## Code Explanation

The provided code consists of several functions and the main application logic. Let's understand the code structure and the purpose of each part:

### Required Libraries

- `os`: Provides functions for interacting with the operating system.
- `streamlit`: The Streamlit library for building web applications.
- `PIL`: The Python Imaging Library for image processing.

### Image Enhancement Function

The `enhance_image` function takes the input image path and output image path as parameters. It performs image enhancement by increasing the brightness, contrast, and sharpness of the image using the `ImageEnhance` module from PIL. The enhanced image is then saved to the specified output path.

### Download Success Function

The `download_success` function displays a success message indicating that the download has completed successfully. This function is called when the user successfully downloads the enhanced image.

### Main Function

The `main` function is the entry point of the application. It sets the Streamlit page configuration, loads the main banner image, and defines the layout and behavior of the application.

Within the `main` function:

- The file uploader component allows users to upload an image file.
- If an image is uploaded, it is saved to a temporary path and then passed to the `enhance_image` function for enhancement.
- The enhanced image is displayed using the Streamlit `image` component.
- Depending on the format of the uploaded image, a download button is displayed for downloading the enhanced image.
- The `download_success` function is called when the user clicks the download button and the download completes successfully.

### Running the Application

The `if __name__ == "__main__"` block ensures that the `main` function is executed only when the script is run directly and not when imported as a module.

## Hosting

The PropReturns Image Enhancer application is hosted on Streamlit Cloud. You can access it using the following link: [PropReturns Image Enhancer](https://propreturns-image-enhancer.streamlit.app/)

## Author

The PropReturns Image Enhancer application was created by Mohammed Husamuddin. If you encounter any issues or have any feedback, you can reach out to him via email at [workforhusam@gmail.com](mailto:workforhusam@gmail.com?subject=Propreturns%20Image%20Enhancement%20WebApp!).




