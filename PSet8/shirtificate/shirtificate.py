"""
implement a program that prompts the user for their name and outputs, using 
fpdf2, a CS50 shirtificate in a file called shirtificate.pdf similar to this
one for John Harvard, with these specifications:

    The orientation of the PDF should be Portrait.
    The format of the PDF should be A4, which is 210mm wide by 297mm tall.
    The top of the PDF should say “CS50 Shirtificate” as text, centered 
        horizontally.
    The shirt’s image should be centered horizontally.
    The user’s name should be on top of the shirt, in white text.

All other details we leave to you. You’re even welcome to add borders, colors, 
and lines. Your shirtificate needn’t match John Harvard’s precisely. And no 
need to wrap long names across multiple lines.

Before writing any code, do read through fpdf2’s tutorial to learn how to use 
it. Then skim fpdf2’s API (application programming interface) to see all of 
its functions and parameters therefor.

No need to submit any PDFs with your code. But, if you would like, you’re 
welcome (but not expected) to share a shirtificate with your name on it in 
any of CS50’s communities!
"""

from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 40)
        title = "CS50 Shirtificate"
        title_width = self.get_string_width(title)
        pdf_width = self.w
        self.set_x((pdf_width - title_width) / 2)
        self.cell(title_width, 10, title, align="C")

    def shirt_text(self, name):
        self.name = name
        name_width = self.get_string_width(self.name)
        pdf_width = self.w
        pdf_height = self.h
        self.set_y(pdf_height / 3)
        self.set_x((pdf_width - name_width) / 2)
        self.set_text_color(255, 255, 255)
        self.set_font("Times", size=30)
        self.cell(name_width, 10, self.name, align="C")


def main():
    name = input("Name: ") + " took CS50"
    pdf = PDF()
    pdf.add_page()
    pdf.image("shirtificate.png", 15, 40, w=pdf.w - 30)
    pdf.shirt_text(name)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
