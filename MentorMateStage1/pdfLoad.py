from custom_pdf_loader import CustomPDFLoader

loader = CustomPDFLoader('testData/IntroToBio.pdf')

pages = loader.load()

for page in pages:
    print(page.page_content)
    print()
    print(str(page.metadata['page']))
    print()
    print()


