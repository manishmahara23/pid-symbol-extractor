import fitz
import os

def analyze_pdfs(input_dir):
    if not os.path.exists(input_dir):
        return
    
    for file_name in os.listdir(input_dir):
        if file_name.lower().endswith(".pdf"):
            pdf = fitz.open(os.path.join(input_dir, file_name))
            print(f"Analyzing: {file_name}")
            
            for page_num in range(len(pdf)):
                page = pdf[page_num]
                print(f"Page {page_num + 1} -> Images: {len(page.get_images(full=True))}, Vector Paths: {len(page.get_drawings())}")

if __name__ == "__main__":
    analyze_pdfs("input")