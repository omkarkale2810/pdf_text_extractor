from flask import Flask, render_template
import PyPDF2

app = Flask(__name__)

def text_extract_from_pdf(pdf_path):
    pdfFileObj = open(pdf_path, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    text = ""
    for page in pdfReader.pages:
        text += page.extract_text()
    pdfFileObj.close()
    pdfcontent = text[:]  
    return pdfcontent


pdf_path = 'bio1.pdf'
pdfcontent = text_extract_from_pdf(pdf_path)

@app.route('/')
def index():
    return render_template('index.html', pdfcontent=pdfcontent)

if __name__ == '__main__':
    app.run(debug=True)
