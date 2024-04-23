import PyPDF2

pdf_file = '202403039498-1.pdf'  # 替換為你下載的 PDF 檔案名稱
text = ''
with open(pdf_file, 'rb') as file:
    pdf_reader = PyPDF2.PdfReader(file)
    for page in pdf_reader.pages:
        text += page.extract_text()

with open('output.txt', 'w', encoding='utf-8').write(text):  # 替換輸出檔案名稱
    print('Success!')
