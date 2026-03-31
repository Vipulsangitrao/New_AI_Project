import pdfplumber
import fitz  # PyMuPDF
import os

def extract_text(pdf_file):
    text = ""

    pdf_file.seek(0)  # ✅ Ensure file pointer at start

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            content = page.extract_text()
            if content:
                text += content + "\n"

    return text


def extract_images(pdf_file, output_folder, prefix):
    # ✅ Ensure folder exists
    os.makedirs(output_folder, exist_ok=True)

    # ✅ IMPORTANT: Reset file pointer before reading
    pdf_file.seek(0)

    # Open PDF from stream
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")

    image_paths = []

    for page_index in range(len(doc)):
        page = doc[page_index]
        images = page.get_images(full=True)

        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)

            # ✅ Safety check
            if "image" not in base_image:
                continue

            image_bytes = base_image["image"]

            img_name = f"{prefix}_p{page_index}_{img_index}.png"
            img_path = os.path.join(output_folder, img_name)

            with open(img_path, "wb") as f:
                f.write(image_bytes)

            image_paths.append(img_path)

    return image_paths



# import pdfplumber
# import fitz  # PyMuPDF
# import os

# def extract_text(pdf_file):
#     text = ""
#     with pdfplumber.open(pdf_file) as pdf:
#         for page in pdf.pages:
#             content = page.extract_text()
#             if content:
#                 text += content + "\n"
#     return text


# def extract_images(pdf_file, output_folder, prefix):
#     os.makedirs(output_folder, exist_ok=True)
#     doc = fitz.open(stream=pdf_file.read(), filetype="pdf")

#     image_paths = []

#     for page_index in range(len(doc)):
#         page = doc[page_index]
#         images = page.get_images(full=True)

#         for img_index, img in enumerate(images):
#             xref = img[0]
#             base_image = doc.extract_image(xref)
#             image_bytes = base_image["image"]

#             img_name = f"{prefix}_p{page_index}_{img_index}.png"
#             img_path = os.path.join(output_folder, img_name)

#             with open(img_path, "wb") as f:
#                 f.write(image_bytes)

#             image_paths.append(img_path)

#     return image_paths