from PIL import Image


# Define a function to convert the heatmap image to text
def heatmap_to_text(image_path: str, width=20, height=10) -> list[str]:
    # Load the image
    img = Image.open(image_path)

    # Convert to grayscale
    img = img.convert("L")

    # Resize the image (optional, for a smaller output)
    img = img.resize((width, height))

    # Define characters for different intensity levels
    # ascii_chars = [" ", ".", ":", "*", "%", "#", "@"]
    ascii_chars = ["*"] * 7
    for i in range(5):
        ascii_chars[i] = " "

    # Function to map pixel intensity to an ascii character
    def pixel_to_char(pixel_value):
        # Scale the pixel value to an index in the ascii_chars list
        return ascii_chars[pixel_value // 36]  # 255/7 ~ 36

    # Loop through the pixels and convert to text
    res = []
    text_representation = ""
    for y in range(height):
        line = ""
        for x in range(width):
            # Get the pixel value at (x, y)
            pixel_value = img.getpixel((x, y))

            # Convert the pixel value to a corresponding character
            line += pixel_to_char(pixel_value)

        # Add a newline after each row
        res.append(line)

    return res


if __name__ == '__main__':
    # Path to your heatmap image
    image_path = "image.png"

    # Generate the text representation
    text_heatmap = heatmap_to_text(image_path, height=10, width=10)

    # Print the text representation
    print(text_heatmap)
