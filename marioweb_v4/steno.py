import stegano
import urllib.parse
from stegano.lsb import hide

# Read the flag
flag = "net-sec{st3n0-ch@mP}"

# URL encode the flag
flag_url_encoded = urllib.parse.quote(flag)

# Hide the flag in the image using the least significant bit (LSB) method
secret_image = hide(r"D:\Nw-Docker-website\docker-app\mario\static\images\mario-back.png", flag_url_encoded)

# Save the secret image to a file
secret_image_path = r"D:\Nw-Docker-website\docker-app\mario\static\images\secret.png"
secret_image.save(secret_image_path)
