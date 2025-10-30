#!/usr/bin/env python3
import os
from PIL import Image
import math

def next_power_of_two(n):
    return 2 ** math.ceil(math.log2(n))

def process_image(input_path, output_path):
    # æå¼å¾ç
    img = Image.open(input_path)
    
    # è·ååå§å°ºå¯¸
    width, height = img.size
    
    # è®¡ç®æ°çå°ºå¯¸ï¼2çå¹æ¬¡æ¹ï¼
    new_width = next_power_of_two(width)
    new_height = next_power_of_two(height)
    
    # å¦æå°ºå¯¸å·²ç»æ¯2çå¹æ¬¡æ¹ï¼åè·³è¿
    if new_width == width and new_height == height:
        print(f"Skipping {input_path} - already power of two")
        return
    
    # åå»ºæ°çéæç»å¸
    new_img = Image.new('RGBA', (new_width, new_height), (0, 0, 0, 0))
    
    # å°åå¾ç²è´´å°å·¦ä¸è§
    new_img.paste(img, (0, 0))
    
    # ä¿å­æ°å¾ç
    new_img.save(output_path)
    print(f"Processed {input_path} -> {output_path} ({width}x{height} -> {new_width}x{new_height})")

def process_directory(input_dir, output_dir):
    # ç¡®ä¿è¾åºç®å½å­å¨
    os.makedirs(output_dir, exist_ok=True)
    
    # éåæææä»¶
    for root, dirs, files in os.walk(input_dir):
        # è®¡ç®ç¸å¯¹è·¯å¾
        rel_path = os.path.relpath(root, input_dir)
        if rel_path == '.':
            rel_path = ''
            
        # åå»ºå¯¹åºçè¾åºå­ç®å½
        output_subdir = os.path.join(output_dir, rel_path)
        os.makedirs(output_subdir, exist_ok=True)
        
        # å¤çææPNGæä»¶
        for file in files:
            if file.lower().endswith('.png'):
                input_path = os.path.join(root, file)
                output_path = os.path.join(output_subdir, file)
                process_image(input_path, output_path)

def main():
    # å¤ç1xå2xç®å½
    base_dir = 'resources/textures'
    for scale in ['1x', '2x']:
        input_dir = os.path.join(base_dir, scale)
        output_dir = os.path.join(base_dir, f"{scale}_power_of_two")
        print(f"\nProcessing {scale} directory...")
        process_directory(input_dir, output_dir)

if __name__ == '__main__':
    main() 