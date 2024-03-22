from fpdf import FPDF
from fpdf.enums import XPos, YPos

class PDF(FPDF):
    def header(self):
        self.image('oxemed.png', 10, 8, 60)

        self.set_y(14)
        self.set_font('helvetica', 'B', 12)
        self.cell(0, 0, f'Dr. Fulano de Tal', align='R')

        self.set_y(19)
        self.set_font('helvetica', '', 10)
        self.cell(0, 0, 'CRM 00000', align='R')

        self.ln(20)

        self.set_font('helvetica', 'B', 14)
        self.cell(0,0, f'Fabril Doenço da Silva', align='C')
        self.ln(15)

    def footer(self):
        self.image('oxemed_bg.png', -8, 78, 165)
        
        self.set_y(-15)
        self.set_x(-30)
        self.set_font('helvetica', '', 10)
        self.cell(0, 0, '26 de dezembro de 2024', align='R')

# Formulário em modo retrato, medido em milímetros, no tamanho de folha A5
form = PDF('P', 'mm', 'A5')

form.set_auto_page_break(auto=True, margin = 35)

form.add_page()

form.set_font('courier', '', 14)

for i in range(1, 20):
    form.multi_cell(0, 0, '- Dipirona 50g depois de toda refeição\n', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    form.ln(2)

form.output('receituario_1.pdf')