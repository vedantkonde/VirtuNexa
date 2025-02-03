import os
import PyPDF2

def merge_pdfs(pdf_list, output_filename):

    merger = PyPDF2.PdfMerger()

    for pdf in pdf_list:
        if os.path.exists(pdf) and pdf.lower().endswith(".pdf"):
            merger.append(pdf)
        else:
            print(f"Warning: Skipping invalid or missing file '{pdf}'.")

    if not merger.pages:
        print("Error: No valid PDFs to merge.")
        return

    merger.write(output_filename)
    merger.close()
    print(f"Merged PDF saved as: {output_filename}")

def split_pdf(input_pdf):
    
    if not os.path.exists(input_pdf) or not input_pdf.lower().endswith(".pdf"):
        print(f"Error: Invalid or missing file '{input_pdf}'.")
        return

    with open(input_pdf, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        total_pages = len(reader.pages)

        if total_pages == 0:
            print("Error: The PDF has no pages.")
            return

        for i in range(total_pages):
            writer = PyPDF2.PdfWriter()
            writer.add_page(reader.pages[i])

            output_filename = f"{os.path.splitext(input_pdf)[0]}_page_{i + 1}.pdf"
            with open(output_filename, "wb") as output_pdf:
                writer.write(output_pdf)
            print(f"Saved: {output_filename}")

def main():
    
    while True:
        print("\nPDF Merger & Splitter")
        print("1. Merge PDFs")
        print("2. Split a PDF")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ").strip()

        if choice == "1":
            pdf_files = input("Enter PDF filenames (comma-separated): ").split(",")
            pdf_files = [pdf.strip() for pdf in pdf_files if pdf.strip()]
            if not pdf_files:
                print("Error: No valid PDFs provided.")
                continue
            output_file = input("Enter output filename (e.g., merged.pdf): ").strip()
            if not output_file.endswith(".pdf"):
                print("Error: Output file must be a .pdf.")
                continue
            merge_pdfs(pdf_files, output_file)

        elif choice == "2":
            pdf_file = input("Enter the PDF file to split: ").strip()
            split_pdf(pdf_file)

        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
