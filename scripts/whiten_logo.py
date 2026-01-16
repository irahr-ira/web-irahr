from PIL import Image
import os

def whiten_logo(image_path):
    print(f"Whitening logo at {image_path}...")
    try:
        img = Image.open(image_path).convert("RGBA")
        datas = img.getdata()
        
        new_data = []
        for item in datas:
            # item is a tuple (R, G, B, A)
            if item[3] > 0: # If pixel is not fully transparent
                # Set RGB to White (255, 255, 255), keep original Alpha
                new_data.append((255, 255, 255, item[3]))
            else:
                new_data.append(item)
        
        img.putdata(new_data)
        img.save(image_path, "PNG")
        print(f"Successfully updated {image_path} with white pixels.")

    except Exception as e:
        print(f"Error processing image: {e}")

if __name__ == "__main__":
    logo_path = "irarh_logo_white.png"
    if os.path.exists(logo_path):
        whiten_logo(logo_path)
    else:
        print(f"File not found: {logo_path}")
