from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
import os as OS

BooksPath=list()

def getallPDFs(Path):
    dirList=OS.listdir(Path)
    for deep1path in dirList:
        deep2path=OS.path.join(Path,deep1path)
        if OS.path.isdir(deep2path):
            getallPDFs(deep2path)
        else:
            BooksPath.append(deep2path)





def convert_pdf_to_txt(path):
    infile=open("E:\NLP\NLTK Project\LDA.txt","w")
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()
    infile.write(text)
    fp.close()
    infile.close()
    device.close()
    retstr.close()
    return text

#convert_pdf_to_txt("E:\NLP\NLTK Project\LDA.pdf")

getallPDFs("E:\NLP\Data Sets\NLP DataBooks")
for files in BooksPath:
    print files,'\n'