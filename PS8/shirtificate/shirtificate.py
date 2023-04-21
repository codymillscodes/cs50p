from fpdf import FPDF

def main():
    name = input("Name: ")
    create_shirt(name)

def create_shirt(name: str) -> None:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('courier', 'B', 40)

    pdf.image('shirtificate.png', x="C", y=80, w=180, h=180)
    pdf.cell(40)
    pdf.ln()
    pdf.ln()
    pdf.cell(20)
    pdf.cell(w=None, h=None, txt="CS50 Shirtificate", align="C")
    pdf.set_xy(55, 297/2)

    pdf.set_font('courier', 'B', 24)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(txt=f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")

if __name__ == '__main__':
    main()