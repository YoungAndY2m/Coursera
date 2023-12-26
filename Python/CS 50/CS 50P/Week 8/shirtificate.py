from fpdf import FPDF

class PDF:
    def __init__(self, name):
        # A4 portrait and the measure unit is millimeter
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        # The first line - CS50 Shirtificate
        pdf.set_font('helvetica', 'B', size=60)
        pdf.cell(0, 30, text="CS50 Shirtificate", align="C")

        # Add shirt image
        shirt_path = "shirtificate.png"
        width = 180
        height = 220
        center_x = (pdf.w - width) / 2
        pdf.image(shirt_path, x=center_x, y=60, w=width, h=height)

        # The second line - user's name in white text
        pdf.set_font("helvetica", 'B', size=36)
        pdf.set_text_color(255, 255, 255)
        pdf.text(x=55, y=150, text=f"{name} took CS50")

        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.output("shirtificate.pdf")

def main():
    name = input("Name: ")
    pdf = PDF(name)

if __name__ == "__main__":
    main()
