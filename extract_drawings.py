import fitz
import os

def rects_close(a, b, pad):
    return not (
        a.x1 + pad < b.x0 or b.x1 + pad < a.x0 or
        a.y1 + pad < b.y0 or b.y1 + pad < a.y0
    )

def merge_rects(a, b):
    return fitz.Rect(
        min(a.x0, b.x0), min(a.y0, b.y0),
        max(a.x1, b.x1), max(a.y1, b.y1)
    )

def group_into_shapes(rects, pad=10):
    groups = [fitz.Rect(r) for r in rects]

    changed = True
    while changed:
        changed = False
        for i in range(len(groups)):
            if groups[i] is None:
                continue
            for j in range(i + 1, len(groups)):
                if groups[j] is None:
                    continue
                if rects_close(groups[i], groups[j], pad):
                    groups[i] = merge_rects(groups[i], groups[j])
                    groups[j] = None
                    changed = True
        groups = [g for g in groups if g is not None]

    return groups

def extract_drawings(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    count = 5  # shape_0 to shape_4 are already taken by extract_symbols.py

    for file_name in os.listdir(input_dir):
        if not file_name.lower().endswith(".pdf"):
            continue

        pdf = fitz.open(os.path.join(input_dir, file_name))

        for page_num in range(len(pdf)):
            page = pdf[page_num]
            page_w, page_h = page.rect.width, page.rect.height

            shapes = []

            # vector paths, skip the big page border / background lines
            for d in page.get_drawings():
                r = d["rect"]
                if r.width > 0.8 * page_w and r.height > 0.8 * page_h:
                    continue
                shapes.append(r)

            # tag text next to the symbols, e.g PV-1000, HEX-300, XV-200
            # "Shape-N" captions are skipped, they are not part of the symbol
            for block in page.get_text("dict")["blocks"]:
                for line in block.get("lines", []):
                    for span in line["spans"]:
                        text = span["text"].strip()
                        if text and not text.startswith("Shape"):
                            shapes.append(fitz.Rect(span["bbox"]))

            # nearby paths/text get grouped into one symbol, then cropped
            for r in group_into_shapes(shapes):
                margin = 5
                clip = fitz.Rect(
                    r.x0 - margin, r.y0 - margin,
                    r.x1 + margin, r.y1 + margin
                )
                pix = page.get_pixmap(matrix=fitz.Matrix(4, 4), clip=clip)
                pix.save(os.path.join(output_dir, f"shape_{count}.png"))
                count += 1

    return count

if __name__ == "__main__":
    total = extract_drawings("input", "extracted_symbols")
    print(f"Extracted vector shapes, total symbols now: {total}")