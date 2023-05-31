from fpdf import FPDF

def gera_pdf(cliente, projeto, hora_estimada, valor_hora, prazo, total_orcamento):
    pdf = FPDF()

    pdf.add_page()
    pdf.set_font('Arial')

    pdf.image('template.png', x=0, y=0)

    nome_cliente = f'Cliente: {cliente}'

    pdf.text(115, 145, projeto)
    pdf.text(115, 160, hora_estimada)
    pdf.text(115, 175, valor_hora)
    pdf.text(115, 190, prazo)
    pdf.text(115, 205, str(total_orcamento))
    pdf.text(115, 220, nome_cliente)

    pdf.output(f'orçamento_{cliente}.pdf')