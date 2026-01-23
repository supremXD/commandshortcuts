import sys
from fpdf import FPDF

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)

if len(sys.argv) < 2:
    print()
    filename = input("Introduce el nombre completo del archivo--> ")
    output = input("Introduce el nombre del pdf a crear--> ")
else:
    filename = sys.argv[1]
    output = sys.argv[2]

with open(f"{filename}", "r", encoding="utf-8") as f:
    for linea in f:
        pdf.multi_cell(0, 8, linea)

pdf.output(output)
