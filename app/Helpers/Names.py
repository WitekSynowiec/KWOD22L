from dataclasses import dataclass


class Names():
    class AppViewPane():
        proceedButton = "Create PDFs"
        clearButton = "Clear"
        patientData = "Patient Data:"
        testLanguages = "Test languages:"
        testData = "Test data:"
        infoPane = "Additional information:"
        title = "COVID-19 Test Multi-language Exporter"
        windowTitle = "COVID-19 Test Multi-language Exporter"

    class PatientDataPane():
        name = "Name:"
        surname = "Surname:"
        sex = "Sex:"
        docId = "Document id:"
        dob = "Date of birth: "

        namePlaceholder = "eg. John"
        surnamePlaceholder = "eg. Deere"
        docIdPlaceholder = "eg. RG88890"

        sexComboBox = ["Male", "Female"]

    class TestDataPane():
        collectedMaterial = "Collected material:"
        dateOfCollection = "Date of collection:"
        dateOfAcceptance = "Date of acceptance:"
        testName = "Test name:"
        result = "Result:"

        collectedMaterialComboBox = ["nasal swab", "nasopharyngeal swab"]
        resultComboBox = ["Negative", "Positive", "Unclear"]
        testNameComboBox = ["SARS-CoV-2 Antigen", "SARS-CoV-2 PCR"]

    class TestLanguages():
        # languages = ["English", "Polish", "German", "Spanish","Portugese", "French", "Swedish", "Norwegian", "Czech", "Slovakian", "Ukrainian","Hungarian", "Russian", "Japanease", "Korean", "Chinease", "Arabic", "Hebrew", "Hindhi"]
        languages = {
            'afrikaans':            'af',
            'albanian' :            'sq',
            'arabic':               'ar',
            'belarusian':           'be',
            'bulgarian':            'bg',
            'catalan':              'ca',
            'chinese_simplified':   'zh-CN',
            'chinese_traditional':  'zh-TW',
            'croatian':             'hr',
            'czech':                'cs',
            'danish':               'da',
            'dutch':                'nl',
            'english':              'en',
            'esperanto':            'eo',
            'estonian':             'et',
            'filipino':             'tl',
            'finnish':              'fi',
            'french':               'fr',
            'galician':             'gl',
            'german':               'de',
            'greek' :               'el',
            'hebrew' :              'iw',
            'hindi' :               'hi',
            'hungarian':            'hu',
            'icelandic':            'is',
            'indonesian' :          'id',
            'irish' :               'ga',
            'italian':              'it',
            'japanese':             'ja',
            'korean':               'ko',
            'latin':                'la',
            'latvian':              'lv',
            'lithuanian':           'lt',
            'macedonian':           'mk',
            'malay':                'ms',
            'maltese':              'mt',
            'norwegian':            'no',
            'persian':              'fa',
            'polish':               'pl',
            'portuguese':           'pt',
            'romanian':             'ro',
            'russian':              'ru',
            'serbian':              'sr',
            'slovak':               'sk',
            'slovenian':            'sl',
            'spanish':              'es',
            'swahili':              'sw',
            'swedish':              'sv',
            'thai':                 'th',
            'turkish':              'tr',
            'ukrainian':            'uk',
            'vietnamese':           'vi',
            'welsh':                'cy',
            'yiddish':              'yi',
        }
    class PdfTemplate():
        dummy = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        labCredentials = "Laboratorium Medyczne \nGynCentrum \nOddzial Sosnowiec \nPracownia Wirusologii \nGyncentrum Sp. z o. o. \nul. Zelazna 1, 40-851 Katowice \ntel.: 32 506 50 86"
        title = "SARS-CoV-2 Rapid Antigen Test"