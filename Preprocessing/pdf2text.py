from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
import os as OS

#following Variables are mean to form input and output path
OutputDir="E:\NLP\Data Sets\NLP DataBooks\PDFs\DF" #  your final .txt files are here.
InputDir="E:\NLP\Data Sets\NLP DataBooks\InputBooks"  # this path contains your  book folders
YourName="BishnuDF" # write your first Name Please Make sure first letter is Capital. This is obligatory
BooksCount=1
Threshold=1
#251,565,677,681,697,716,792,803,1001,1025,1051,52,53
BooksPath=list()

def getallPDFs(Path):
    dirList=OS.listdir(Path)
    for deep1path in dirList:
        deep2path=OS.path.join(Path,deep1path)
        if OS.path.isdir(deep2path):
            getallPDFs(deep2path)
        else:
            BooksPath.append(deep2path)





def convert_pdf_to_txt(path,outpath):
    infile=open(outpath,"w")
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

if  not OS.path.exists(OutputDir):
     OS.makedirs(OutputDir)
getallPDFs(InputDir)
print 'Total Books:',len(BooksPath)
print BooksPath[Threshold]

count=1
for PDFs in BooksPath:
    if BooksCount >=Threshold:
        print BooksPath[BooksCount]
        outfile=YourName+'_'+ str(BooksCount)+'.txt'
        BooksCount=BooksCount+1
        outpath=OS.path.join(OutputDir,outfile)
        try:
            convert_pdf_to_txt(PDFs,outpath)
            print 'text is ready:', outfile
        except:
            BooksCount=BooksCount+1

    else:
        BooksCount=BooksCount+1
