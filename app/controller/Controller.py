from app.Helpers.Names import Names
from app.controller.PdfTemplate import PdfTemplate
from app.view.ExportLanguagePane import ExportLanguagePane
from app.view.InfoPane import InfoPane
from app.view.PatientDataPane import PatientDataPane
from app.view.TestDataPane import TestDataPane


class Controller:
    def __init__(self, pdPane: PatientDataPane, tdPane: TestDataPane, elPane: ExportLanguagePane, iPane: InfoPane):
        super().__init__()
        self.pdPane = pdPane
        self.tdPane = tdPane
        self.elPane = elPane
        self.iPane = iPane

    def exportPDF(self):
        for lang in self.elPane.languageCheckBoxes:
            if lang.isChecked():
                langEtyq = lang.text().replace(' ', '_').lower()
                pdf = PdfTemplate( lang=Names.TestLanguages.languages[langEtyq] )
                pdf.output( 'Test in {}.pdf'.format(langEtyq), 'F' )
