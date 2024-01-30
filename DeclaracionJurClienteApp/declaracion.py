from fpdf import FPDF

pdf=FPDF(orientation='P', unit='mm', format='Letter')
pdf.add_page()

pdf.output('declaracacion.pdf')
print("exito")
