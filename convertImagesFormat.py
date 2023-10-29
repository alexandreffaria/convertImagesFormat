import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image
import argparse
from tqdm import tqdm  # Import tqdm for progress bar

def convert_images(input_dir, output_dir, input_format, output_format):
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith(f".{input_format}"):
                input_file_path = os.path.join(root, file)
                output_subdir = f"{output_format}_output"
                output_dir = os.path.join(input_dir, output_subdir)
                os.makedirs(output_dir, exist_ok=True)
                output_file_path = os.path.join(output_dir, file.replace(f".{input_format}", f".{output_format}"))
                with Image.open(input_file_path) as image:
                    if output_format.lower() == "jpg":
                        image = image.convert("RGB")
                    image.save(output_file_path)
                    
# Helper function to count files
def count_files(input_dir, input_format):
    count = 0
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith(f".{input_format}"):
                count += 1
    return count

def select_directory(initial_path):
    input_dir = filedialog.askdirectory(title="Select the directory containing image files", initialdir=initial_path)
    if input_dir:
        return input_dir
    else:
        return None

def main():
    parser = argparse.ArgumentParser(description="Image Format Converter")
    parser.add_argument("-i", "--input-format", type=str, choices=["png", "webp"], required=True, help="Input image format (png or webp)")
    parser.add_argument("-o", "--output-format", type=str, choices=["jpg", "png"], required=True, help="Output image format (jpg or png)")
    parser.add_argument("-od", "--output-directory", type=str, help="Output directory to save converted images")

    args = parser.parse_args()

    input_format = args.input_format
    output_format = args.output_format

    initial_path = "/mnt/c/Users/alexa/Desktop"  # Change this path to your desired location

    root = tk.Tk()
    root.withdraw()  # Hide the main window

    input_directory = select_directory(initial_path)

    if input_directory:
        if args.output_directory:
            output_directory = args.output_directory
        else:
            output_subdir = f"{output_format}_output"
            output_directory = os.path.join(input_directory, output_subdir)
        os.makedirs(output_directory, exist_ok=True)
        
        # Count the total number of files to create the progress bar
        total_files = count_files(input_directory, input_format)
        
        # Create a progress bar using tqdm
        with tqdm(total=total_files) as pbar:
            for root, _, files in os.walk(input_directory):
                for file in files:
                    if file.lower().endswith(f".{input_format}"):
                        input_file_path = os.path.join(root, file)
                        output_subdir = f"{output_format}_output"
                        output_dir = os.path.join(input_directory, output_subdir)
                        os.makedirs(output_dir, exist_ok=True)
                        output_file_path = os.path.join(output_dir, file.replace(f".{input_format}", f".{output_format}"))
                        with Image.open(input_file_path) as image:
                            if output_format.lower() == "jpg":
                                image = image.convert("RGB")
                            image.save(output_file_path)
                            pbar.update(1)  # Update progress bar
                        

if __name__ == "__main__":
    main()
