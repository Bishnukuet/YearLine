# this file contains all the  variables pointing to some directory or file path
import os as OS
from shutil import copy2
DATA_DIR="E:\NLP\Data Sets\NLP DataBooks\A\AA - Unice"

source_path=""#"E:\NLP\Data Sets\NLP DataBooks\PDFs\NLPtxt\NLPtxt"
destination_path=""#"E:\NLP\Data Sets\NLP DataBooks\\novels\\"
BooksPath=list()
def getallfiles(Path,dst):
    dirList=OS.listdir(Path)
    for deep1path in dirList:
        deep2path=OS.path.join(Path,deep1path)
        if OS.path.isdir(deep2path):
            getallfiles(deep2path,dst)
        else:
            BooksPath.append(deep2path)
            copy2(deep2path,dst)

if __name__ == '__main__':
    getallfiles(source_path,destination_path)


