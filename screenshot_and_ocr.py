import os
from datetime import datetime
import pytesseract
from playwright.sync_api import sync_playwright

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  

def read_urls_from_file(file_path):
    
    with open(file_path, 'r') as file:
        urls = file.readlines()
    return [url.strip() for url in urls]

def take_screenshot_and_ocr(url, screenshot_path, ocr_output_path, device_scale_factor=1):
   
    with sync_playwright() as p:
        browser = p.chromium.launch()
       
        context = browser.new_context(device_scale_factor=device_scale_factor)
        
        page = context.new_page()

        page.goto(url)
        
        page.set_viewport_size({"width": 1920, "height": 1080})
         
       # page.wait_for_timeout(5000)
       ## Wait for a specific selector to appear
        #page.wait_for_selector(".product-card", timeout=60000)  # Waits up to 60 seconds for the element to appear

        page.screenshot(path=screenshot_path, full_page=True)  
        browser.close()

    
    ocr_text = pytesseract.image_to_string(screenshot_path)
    with open(ocr_output_path, 'w') as file:
        file.write(ocr_text)

def main():
    
    url_file_path = 'urls.txt'

    
    urls = read_urls_from_file(url_file_path)
    

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    
    screenshots_dir = os.path.join('screenshots', timestamp)
    ocr_output_dir = os.path.join('ocr_output', timestamp)
    os.makedirs(screenshots_dir, exist_ok=True)
    os.makedirs(ocr_output_dir, exist_ok=True)

    
    screenshot_paths_file = os.path.join(screenshots_dir, 'screenshot_paths.txt')
    with open(screenshot_paths_file, 'w') as file:
        
        for i, url in enumerate(urls):
            
            screenshot_filename = f'screenshot_{i + 1}.png'
            ocr_output_filename = f'ocr_output_{i + 1}.txt'

            screenshot_path = os.path.join(screenshots_dir, screenshot_filename)
            ocr_output_path = os.path.join(ocr_output_dir, ocr_output_filename)

            print(f"Processing {url}...")
            
            device_scale_factor = 2
            take_screenshot_and_ocr(url, screenshot_path, ocr_output_path, device_scale_factor)
            
            print(f"Screenshot saved to {screenshot_path}")
            print(f"OCR output saved to {ocr_output_path}")
            
            
            file.write(f'{screenshot_path}\n')

if __name__ == "__main__":
    main()
