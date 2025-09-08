import os
from fpdf import FPDF
from datetime import datetime

# Define a arte ASCII para o cabeçalho do relatório
WATCHDOG_LOGO_ASCII = """
 _    _       _       _    ______            
| |  | |     | |     | |   |  _  \           
| |  | | __ _| |_ ___| |__ | | | |___   __ _ 
| |/\| |/ _` | __/ __| '_ \| | | / _ \ / _` |
\  /\  / (_| | || (__| | | | |/ / (_) | (_| |
 \/  \/ \__,_|\__\___|_| |_|___/ \___/ \__, |
                                        __/ |
                                       |___/ 
"""

class PDFReport(FPDF):
    def __init__(self, runbook_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.runbook_name = runbook_name

    def header(self):
        logo_path = os.path.join('assets', 'logo.jpg')

        if os.path.exists(logo_path):
            self.image(logo_path, x=90, y=15, w=30)
            self.ln(30)

        self.set_font('Courier', 'B', 8)
        for line in WATCHDOG_LOGO_ASCII.splitlines():
            self.cell(0, 4, line, 0, 1, 'C')

        self.ln(5)
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, f'Relatório de Incidentes - {self.runbook_name}', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 10)
        self.cell(0, 6, title, 0, 1, 'L')
        self.ln(4)

    def chapter_body(self, item):
        # Separa a mensagem em duas partes: o prefixo "Passo X:" e o restante
        message_parts = item.get("message").split(":", 1)
        step_prefix = message_parts[0] + ": "
        step_message = message_parts[1]
        
        # Define a cor com base no status
        if item.get("status") == "success":
            self.set_text_color(10, 140, 40)  # RGB para verde
            symbol = "+"
        else:
            self.set_text_color(220, 50, 50)  # RGB para vermelho
            symbol = "-"

        # Imprime o símbolo
        self.cell(5, 5, symbol)

        # Imprime o prefixo em negrito e na cor do status
        self.set_text_color(0, 0, 0)
        self.set_font('Arial', 'B', 10)
        self.cell(self.get_string_width(step_prefix), 5, " " + step_prefix)
        
        # Volta para a cor preta e fonte normal
        self.set_text_color(0, 0, 0)
        self.set_font('Arial', '', 10)
        
        # Imprime o restante da mensagem
        self.multi_cell(0, 5, step_message)
        
        self.ln()

def generate_report(content, threat_name, runbook_name_full):
    reports_dir = "reports"
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)

    pdf = PDFReport(runbook_name_full)
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    pdf.chapter_title("Detalhes da Execução do Runbook")
    
    for item in content:
        pdf.chapter_body(item)
    
    timestamp = datetime.now().strftime('%Y%m%d%H%M')
    filename = os.path.join(reports_dir, f"{threat_name}_{timestamp}.pdf")
    
    pdf.output(filename)
    print(f"\nRelatório gerado com sucesso: {filename}")