from PIL import Image
import numpy as np

def read_and_resize_image(file_path, output_path, target_size=(256, 256)):
    try:
        # Open the image file
        with Image.open(file_path) as img:
            # Resize the image
            resized_img = img.resize(target_size)
            
            # Save the resized image
            resized_img.save(output_path)
            print(f"Resized image saved to: {output_path}")

            # Convert the image to a NumPy array
            img_array = np.array(resized_img)
            return img_array
    except Exception as e:
        print(f"Error reading and resizing image: {e}")
        return None

# Get the file path and output path from the user
file_path = input("Enter the path of the original image file: ")
output_path = input("Enter the path to save the resized image: ")

# Read, resize, and save the image
image_data = read_and_resize_image(file_path, output_path)

if image_data is not None:
    # Now you can use 'image_data' as input to your model
    print("Image loaded, resized, and saved successfully.")
    print("Shape of the preprocessed image array:", image_data.shape)
    # Further processing or model prediction can be performed here
else:
    print("Failed to load and resize the image.")
