from fpdf import FPDF, XPos, YPos
from googletrans import Translator

from app.Helpers.Names import Names


class PdfTemplate(FPDF):
    def __init__(self, lang = 'en'):
        super().__init__()
        self.lang = lang
        self.translator = Translator()
        self.body()

    # METHOD TRANSLATES STRING TO CURRENT PDF TEMPLATE LANGUAGE. JUST PUT ANY STRING.
    def t(self, text):
        return self.translator.translate( text=text, dest=self.lang ).text

    # DUMMY HEADER
    def header(self):
        self.set_font( 'Times', '', 6 )
        self.multi_cell( 40, 3, Names.PdfTemplate.labCredentials,  new_x=XPos.RIGHT, new_y=YPos.TOP, max_line_height=20 )
        self.set_font('Times', 'B', 17)
        self.multi_cell(110, 21, self.t(Names.PdfTemplate.title) , ln = 3, align = 'C',  max_line_height=20)
        self.image( "logo_pb.jpg", w=0, h=21 )
        self.cell(0,0,ln=1)
        self.cell(0,0,ln=1)
        self.cell(0,0,ln=1)

    # DUMMY FOOTER
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)

    # DUMMY BODY
    def body(self):
        data = (
            ("First name", "Last name", "Age", "City"),
            ("Jules", "Smith", "34", "San Juan"),
            ("Mary", "Ramos", "45", "Orlando"),
            ("Carlson", "Banks", "19", "Los Angeles"),
        )

        self.add_page()
        self.set_font( "Times", size=10 )
        line_height = self.font_size
        col_width = 40
        self.set_left_margin(27)
        self.set_right_margin(27)


        lh_list = []  # list with proper line_height for each row
        use_default_height = 0  # flag
        for row in data:
            for datum in row:
                word_list = datum.split()
                number_of_words = len( word_list )  # how many words
                if number_of_words > 2:  # names and cities formed by 2 words like Los Angeles are ok)
                    use_default_height = 1
                new_line_height = self.font_size * (number_of_words / 2)  # new height change according to data
            if not use_default_height:
                lh_list.append( line_height )
            else:
                lh_list.append( new_line_height )
        use_default_height = 0

        for j, row in enumerate( data ):
            for datum in row:
                line_height = lh_list[j]  # choose right height for current row
                self.multi_cell( col_width, line_height, datum, border=1, align='C', ln=3,
                                max_line_height=self.font_size )
            self.ln( line_height )


