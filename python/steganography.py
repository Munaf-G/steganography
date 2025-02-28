import cv2
import os

# Load image
img = cv2.imread("mypic.jpg")  # Ensure this path is correct
if img is None:
    print("Error: Image not found!")
    exit()

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Character mappings
d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}

# Variables for pixel manipulation
n, m, z = 0, 0, 0
rows, cols, _ = img.shape  # Get image dimensions

# Encoding the message
for i in range(len(msg)):
    if n >= rows or m >= cols:  # Prevent out-of-bounds errors
        print("Error: Message too long for image!")
        exit()
    
    img[n, m, z] = d[msg[i]]  # Store ASCII value in pixel
    z = (z + 1) % 3  # Cycle through BGR channels
    if z == 0:  # Move to next pixel after 3 channels
        m += 1
        if m >= cols:
            m = 0
            n += 1

# Save encrypted image
cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Open the image (Windows)

# Decryption process
message = ""
n, m, z = 0, 0, 0

pas = input("Enter passcode for Decryption: ")
if password == pas:
    for i in range(len(msg)):
        if n >= rows or m >= cols:  # Prevent out-of-bounds errors
            print("Error: Corrupted or incorrect image!")
            exit()
        
        message += c[img[n, m, z]]  # Retrieve ASCII character
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m >= cols:
                m = 0
                n += 1
    print("Decryption message:", message)
else:
    print("YOU ARE NOT AUTHORIZED!")
