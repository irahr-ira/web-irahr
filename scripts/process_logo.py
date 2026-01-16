from PIL import Image, ImageOps
import numpy as np
import os

def process_logo(input_path, output_path):
    print(f"Processing {input_path}...")
    
    try:
        img = Image.open(input_path).convert("RGBA")
        datas = img.getdata()
        
        new_data = []
        for item in datas:
            # Change all white (also shades of whites) to transparent
            if item[0] > 200 and item[1] > 200 and item[2] > 200:
                new_data.append((255, 255, 255, 0))
            else:
                new_data.append(item)
        
        img.putdata(new_data)
        
        # Crop (getbbox)
        bbox = img.getbbox()
        if bbox:
            img = img.crop(bbox)
            print(f"Cropped to {bbox}")
            
        img.save(output_path, "PNG")
        print(f"Saved to {output_path}")

    except Exception as e:
        print(f"Error processing image: {e}")

if __name__ == "__main__":
    # Path to the uploaded image in artifacts
    input_file = r"C:\Users\inigo\.gemini\antigravity\brain\a45fc62b-3f67-452a-8537-4189187b8512\uploaded_image_1768498152861.png"
    output_file = "irarh_logo_white.png"
    
    if os.path.exists(input_file):
        process_logo(input_file, output_file)
    else:
        print(f"Input file not found: {input_file}")
