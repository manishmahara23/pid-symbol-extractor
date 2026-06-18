import fitz
import os

os.makedirs("outputs/pages", exist_ok=True)

for file_name in os.listdir("input"):
    if file_name.lower().endswith(".pdf"):
        pdf = fitz.open(os.path.join("input", file_name))
        pdf_name = os.path.splitext(file_name)[0]
        
        for page_num in range(len(pdf)):
            pix = pdf[page_num].get_pixmap(matrix=fitz.Matrix(4, 4))
            pix.save(os.path.join("outputs/pages", f"{pdf_name}_page_{page_num+1}.png"))