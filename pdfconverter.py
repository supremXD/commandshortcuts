import sys
import subprocess
from fpdf import FPDF
from pathlib import Path


def txt_to_pdf():
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    with open(f"{filename}", "r", encoding="utf-8") as f:
        for linea in f:
            pdf.multi_cell(0, 8, linea)

    pdf.output(output)


def odt_to_pdf():
    subprocess.run([
        "libreoffice",
        "--headless",
        "--convert-to", "pdf",
        filename
    ])


if len(sys.argv) < 2:
    print()
    filename = input("Introduce el nombre completo del archivo--> ")
    extension = filename.lower().split(".")
    if extension[-1] == "txt":
        output = input("Introduce el nombre del pdf a crear--> ")
        if output == "":
            output = filename.lower().split(".")
            output[-1] = "pdf"
            output = ".".join(output)    
        txt_to_pdf()   
    elif extension[-1] == "odt":
        odt_to_pdf()
else:
    filename = sys.argv[1]
    if len(sys.argv) > 2:
        output = sys.argv[2]
    else:
        output = filename.lower().split(".")
        output[-1] = "pdf"
        output = ".".join(output)
    extension = filename.lower().split(".")
    if extension[-1] == "txt":
        txt_to_pdf()
    elif extension[-1] == "odt":
        odt_to_pdf()