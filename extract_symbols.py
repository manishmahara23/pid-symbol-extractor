import fitz
import os

def extract_images(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    count = 0
    
    for file_name in os.listdir(input_dir):
        if file_name.lower().endswith(".pdf"):
            pdf_path = os.path.join(input_dir, file_name)
            pdf = fitz.open(pdf_path)
            
            for page_num in range(len(pdf)):
                for img in pdf[page_num].get_images(full=True):
                    base_image = pdf.extract_image(img[0])
                    file_path = os.path.join(output_dir, f"shape_{count}.{base_image['ext']}")
                    with open(file_path, "wb") as f:
                        f.write(base_image["image"])
                    count += 1
            
    return count

if __name__ == "__main__":
    extract_images("input", "extracted_symbols")