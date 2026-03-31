import streamlit as st
import os
import tempfile
from extractor import extract_text, extract_images
from report_generator import generate_ddr

st.set_page_config(page_title="AI DDR Generator", layout="wide")

st.title("🏗️ AI DDR Report Generator")

inspection_file = st.file_uploader("Upload Inspection Report (PDF)", type="pdf")
thermal_file = st.file_uploader("Upload Thermal Report (PDF)", type="pdf")

if st.button("Generate DDR Report"):

    if not inspection_file or not thermal_file:
        st.error("Please upload both files")
    else:
        with st.spinner("Processing..."):

            # ✅ Extract text
            inspection_text = extract_text(inspection_file)
            thermal_text = extract_text(thermal_file)

            # ✅ Reset file pointer
            inspection_file.seek(0)
            thermal_file.seek(0)

            # ✅ FIX: Use TEMP directory (no OneDrive issues)
            base_temp = tempfile.gettempdir()

            img_folder = os.path.join(base_temp, "ai_ddr_images")
            os.makedirs(img_folder, exist_ok=True)

            # Extract images
            inspection_images = extract_images(inspection_file, img_folder, "inspection")
            thermal_images = extract_images(thermal_file, img_folder, "thermal")

            # ✅ Generate DDR
            report = generate_ddr(inspection_text, thermal_text)

            # ✅ Attach images
            report += "\n\n---\n## 📸 Extracted Images\n"

            all_images = inspection_images + thermal_images

            if all_images:
                for img in all_images:
                    report += f"\n![Image]({img})\n"
            else:
                report += "\nImage Not Available\n"

            # ✅ Save report in temp folder
            output_path = os.path.join(base_temp, "ddr_report.md")

            with open(output_path, "w", encoding="utf-8") as f:
                f.write(report)

        st.success("✅ Report Generated!")

        # ✅ Download button
        st.download_button(
            label="📥 Download Report",
            data=report,
            file_name="DDR_Report.md",
            mime="text/markdown"
        )

        st.markdown(report)




# import streamlit as st
# import os
# from extractor import extract_text, extract_images
# from report_generator import generate_ddr

# st.set_page_config(page_title="AI DDR Generator", layout="wide")

# st.title("🏗️ AI DDR Report Generator")

# # ✅ FIX 1: Use absolute base directory
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# inspection_file = st.file_uploader("Upload Inspection Report (PDF)", type="pdf")
# thermal_file = st.file_uploader("Upload Thermal Report (PDF)", type="pdf")

# if st.button("Generate DDR Report"):

#     if not inspection_file or not thermal_file:
#         st.error("Please upload both files")
#     else:
#         with st.spinner("Processing..."):

#             # ✅ Extract text
#             inspection_text = extract_text(inspection_file)
#             thermal_text = extract_text(thermal_file)

#             # ✅ Reset file pointer
#             inspection_file.seek(0)
#             thermal_file.seek(0)

#             # ✅ FIX 2: Proper absolute image folder path
#             img_folder = os.path.join(BASE_DIR, "outputs", "images")

#             # ✅ FIX 3: Ensure folder exists BEFORE using it
#             os.makedirs(img_folder, exist_ok=True)

#             # Extract images
#             inspection_images = extract_images(inspection_file, img_folder, "inspection")
#             thermal_images = extract_images(thermal_file, img_folder, "thermal")

#             # ✅ Generate DDR
#             report = generate_ddr(inspection_text, thermal_text)

#             # ✅ Attach images
#             report += "\n\n---\n## 📸 Extracted Images\n"

#             all_images = inspection_images + thermal_images

#             if all_images:
#                 for img in all_images:
#                     # Convert to relative path for markdown display
#                     relative_path = os.path.relpath(img, BASE_DIR)
#                     report += f"\n![Image]({relative_path})\n"
#             else:
#                 report += "\nImage Not Available\n"

#             # ✅ FIX 4: Proper output folder path
#             output_folder = os.path.join(BASE_DIR, "outputs")
#             os.makedirs(output_folder, exist_ok=True)

#             output_path = os.path.join(output_folder, "ddr_report.md")

#             with open(output_path, "w", encoding="utf-8") as f:
#                 f.write(report)

#         st.success("✅ Report Generated!")

#         st.download_button(
#             label="📥 Download Report",
#             data=report,
#             file_name="DDR_Report.md",
#             mime="text/markdown"
#         )

#         st.markdown(report)




# import streamlit as st
# import os
# from extractor import extract_text, extract_images
# from report_generator import generate_ddr

# st.set_page_config(page_title="AI DDR Generator", layout="wide")

# st.title("🏗️ AI DDR Report Generator")

# inspection_file = st.file_uploader("Upload Inspection Report (PDF)", type="pdf")
# thermal_file = st.file_uploader("Upload Thermal Report (PDF)", type="pdf")

# if st.button("Generate DDR Report"):

#     if not inspection_file or not thermal_file:
#         st.error("Please upload both files")
#     else:
#         with st.spinner("Processing..."):

#             # Extract text
#             inspection_text = extract_text(inspection_file)
#             thermal_text = extract_text(thermal_file)

#             # Reset file pointer for image extraction
#             inspection_file.seek(0)
#             thermal_file.seek(0)

#             # Extract images
#             img_folder = "outputs/images"
#             inspection_images = extract_images(inspection_file, img_folder, "inspection")
#             thermal_images = extract_images(thermal_file, img_folder, "thermal")

#             # Generate DDR
#             report = generate_ddr(inspection_text, thermal_text)

#             # Attach images (simple version)
#             report += "\n\n---\n## 📸 Extracted Images\n"

#             if inspection_images or thermal_images:
#                 for img in inspection_images + thermal_images:
#                     report += f"\n![Image]({img})\n"
#             else:
#                 report += "\nImage Not Available\n"

#             # Save report
#             os.makedirs("outputs", exist_ok=True)
#             output_path = "outputs/ddr_report.md"

#             with open(output_path, "w", encoding="utf-8") as f:
#                 f.write(report)

#         st.success("✅ Report Generated!")

#         st.download_button(
#             label="📥 Download Report",
#             data=report,
#             file_name="DDR_Report.md",
#             mime="text/markdown"
#         )

#         st.markdown(report)