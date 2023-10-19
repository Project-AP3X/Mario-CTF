import stegano
from stegano.lsb import lsb
from PIL import Image

# Load the secret image
secret_image_path = r"D:\Nw-Docker-website\docker-app\mario\static\images\secret (1).png"
secret_image = Image.open(secret_image_path)

# Extract the hidden message using the least significant bit (LSB) method
flag = lsb.reveal(secret_image)

# Print the flag
print(flag)
