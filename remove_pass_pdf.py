import PyPDF2
import sys
import os
file_path = sys.argv[1]

if not file_path.endswith(".pdf"):
    print("Please pass correct pdf file")
    sys.exit(1)
try:
    password = sys.argv[2]
except IndexError as e:
    print("No password passed")
    password = None

def open_and_save_pdf(file_path, password =None):
    print(password)
    f1 = PyPDF2.PdfFileReader(file_path)
    print(f1)
    if f1.isEncrypted:
        try:
            f1.decrypt(password=password)
            print("File Decrypted (PyPDF2)")
        except Exception as err:
            print(err)
    base_dir = os.path.dirname(file_path)
    filename = os.path.basename(file_path)
    new_name = filename.split(".")
    new_name = new_name[0] + "_new." + new_name[1]
    output_file = os.path.join(base_dir, new_name)

    w1 = PyPDF2.PdfFileWriter()
    for page in f1.pages:
        w1.addPage(page)
    with open(output_file, "wb") as output_pdf:
                w1.write(output_pdf)
    print("New file saved ", output_file)


open_and_save_pdf(file_path, password)