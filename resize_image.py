from PIL import Image
import sys

def resize_image(input_path, output_path, size):
    # Open an image file
    with Image.open(input_path) as img:
        # Resize image
        img_resized = img.resize(size)
        # Save resized image
        img_resized.save(output_path)
        print(f"Image saved to {output_path}")

if __name__ == "__main__":
    # Check if the user provided the required arguments
    if len(sys.argv) != 5:
        print("Usage: python resize_image.py input_path output_path width height")
    else:
        input_path = sys.argv[1]
        output_path = sys.argv[2]
        width = int(sys.argv[3])
        height = int(sys.argv[4])
        size = (width, height)
        
        resize_image(input_path, output_path, size)
