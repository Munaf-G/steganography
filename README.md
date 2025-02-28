# Image Steganography using OpenCV

## Problem Statement
This project aims to hide a secret message inside an image by modifying its pixel values. The goal is to provide a simple and secure way to encode and decode messages using image steganography, ensuring that the message remains hidden within the image pixels without significantly altering the visual appearance.

## Technologies Used
- **Python**: Core programming language for implementation.
- **OpenCV (cv2)**: Used for image processing and manipulation.
- **OS Module**: Handles file operations and system commands.

## Wow Factor
- **Simple Yet Secure**: Uses pixel-level manipulation to embed messages without affecting the visual integrity of the image.
- **Lightweight Encryption**: ASCII encoding ensures efficient and fast data storage.
- **Steganography-Based Approach**: Unlike traditional encryption, the message is hidden inside an image, making it less noticeable and easily shareable.

## End Users
- Individuals seeking a discreet way to communicate securely.
- Cybersecurity enthusiasts exploring steganography techniques.
- Researchers and students working on data-hiding mechanisms.

## Features
- Encode a secret message within an image.
- Secure decryption using a passcode.
- Prevents unauthorized access to the hidden message.
- Supports basic ASCII character encoding.

## Installation
1. Clone this repository:
   ```sh
   git clone <https://github.com/Munaf-G/steganography.git>
   ```
2. Install dependencies:
   ```sh
   pip install opencv-python
   ```
3. Run the script:
   ```sh
   python steganography.py
   ```

## Usage
1. **Encoding the Message:**
   - The script prompts the user to enter a secret message and a passcode.
   - The message is embedded within the pixel values of the selected image.
   - The modified image is saved as `encryptedImage.jpg`.

2. **Decoding the Message:**
   - The script asks for a passcode to retrieve the hidden message.
   - If the correct passcode is entered, the message is decrypted.
   - Unauthorized access attempts are denied.

## Example
```
Enter secret message: HelloWorld
Enter a passcode: 1234
Encrypted image saved as encryptedImage.jpg

Enter passcode for Decryption: 1234
Decryption message: HelloWorld
```

## Future Scope
- Implement stronger encryption algorithms to enhance security.
- Support for different image formats and color models.
- Develop a GUI-based application for better user experience.
- Use deep learning to detect and counteract steganographic attacks.

## Result
The program successfully encodes a message inside an image and retrieves it upon entering the correct password. Unauthorized attempts fail, ensuring message confidentiality.

## Conclusion
This project showcases a simple yet effective approach to image steganography. By encoding ASCII values within an image’s pixel data, users can securely hide and retrieve messages. The implementation demonstrates how images can act as carriers of confidential data.

## GitHub Link
https://github.com/Munaf-G/steganography.git

