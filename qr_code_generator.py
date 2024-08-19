import qrcode

# Function to generate QR code
def generate_qr_code(data, filename):
    # Create a QR code object
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code (1-40)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
        box_size=10,  # size of each box in pixels
        border=4,  # thickness of the border (in boxes)
    )
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image to a file
    img.save(filename)

# Example usage
if __name__ == "__main__":
    data = "https://www.example.com"
    filename = "example_qr.png"
    generate_qr_code(data, filename)
    print(f"QR code generated and saved as {filename}")
