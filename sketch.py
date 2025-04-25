import cv2
import numpy as np
import matplotlib.pyplot as plt

def sketch_image(image_path, output_path):
    # Read the image
    img = cv2.imread(image_path)

    # Convert to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Invert the grayscale image
    inverted_img = cv2.bitwise_not(gray_img)

    # Blur the inverted image
    blurred_img = cv2.GaussianBlur(inverted_img, (111, 111), 0)

    # Invert the blurred image
    inverted_blurred_img = cv2.bitwise_not(blurred_img)

    # Sketch: Divide the grayscale image by the inverted blurred image
    sketch_img = cv2.divide(gray_img, inverted_blurred_img, scale=256.0)

    # Save the sketch image
    cv2.imwrite(output_path, sketch_img)

    # Optionally, display the image using matplotlib
    plt.imshow(cv2.cvtColor(sketch_img, cv2.COLOR_BGR2RGB))
    plt.axis('off')  # Turn off axis
    plt.show()

# Example usage
image_path = 'C:\\Users\\Pc\\Desktop\\Sketch\\sew5.jpg'  # Provide the path to your input image
output_path = 'C:\\Users\\Pc\\Desktop\\Sketch\\try.jpg'       # Provide the path where the output image will be saved
sketch_image(image_path, output_path)
