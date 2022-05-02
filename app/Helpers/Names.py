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
        languages = ["English", "Polish", "German", "Spanish","Portugese", "French", "Swedish", "Norwegian", "Czech", "Slovakian", "Ukrainian","Hungarian", "Russian", "Japanease", "Korean", "Chinease", "Arabic", "Hebrew", "Hindhi"]

