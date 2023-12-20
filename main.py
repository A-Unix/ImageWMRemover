#!/usr/bin/python3

import os
import subprocess
import time
from PIL import Image

print("Checking if Colorama has been installed already or not!")

time.sleep(2)

try:
    from colorama import init, Fore
    print(Fore.LIGHTBLUE_EX + "Colorama has been already installed, We have initialized it for you :)")
except ImportError:
    print(Fore.RED + "Colorama is not installed. Installing it...")
    subprocess.run(["pip", "install", "colorama"], check=True)
    from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

# Clear the terminal screen
os.system("clear")

time.sleep(1)

# Get the terminal size
rows, columns = os.popen('stty size', 'r').read().split()

# Calculate the center position
center_row = int(rows) // 2
center_column = int(columns) // 2

# Set the font size
font_size = 6

# Print an empty line for top margin
print()

# Print empty lines for top margin
for _ in range(center_row - font_size):
    print()

# Print the welcome message at the center with bigger font size
print(" " * center_column + Fore.LIGHTMAGENTA_EX + "Welcome\n".center(font_size * 2))

# Print empty lines for bottom margin
for _ in range(center_row - font_size):
    print()

time.sleep(2)

def get_background_color(img, position):
    # Get the background color based on the specified position
    if position == "top-left":
        return img.getpixel((0, 0))
    elif position == "bottom-left":
        return img.getpixel((0, img.height - 1))
    elif position == "bottom-right":
        return img.getpixel((img.width - 1, img.height - 1))
    elif position == "top-right":
        return img.getpixel((img.width - 1, 0))
    else:
        raise ValueError(Fore.LIGHTRED_EX + "Invalid position. Supported positions: top-left, bottom-left, bottom-right, top-right")

def remove_watermark(input_path, output_path, watermark_position):
    try:
        # Open the image
        img = Image.open(input_path)

        # Get the mode (dominant color) of the image based on the specified position
        mode = get_background_color(img, watermark_position)

        # Replace watermark area with the mode color
        img = img.point(lambda p: mode if p[3] == 0 else p)

        # Save the modified image
        img.save(output_path)
        print(Fore.LIGHTMAGENTA_EX + "Watermark removed and filled successfully.")
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"Error: {e}")

# Input usage
input_path = input(Fore.LIGHTGREEN_EX + "Enter the path of the original image here: ")
output_path = input(Fore.LIGHTYELLOW_EX + "Enter the path of the output image here: ")
watermark_position = input(Fore.LIGHTCYAN_EX + "Enter the position of the watermark (top-left, bottom-left, bottom-right, top-right): ")

remove_watermark(input_path, output_path, watermark_position)
