import pdfkit
import os

def save_pdf(url,path):
    os.chdir(r'G:\python\zhihu\ribao\content')
    file_name = str(path) + '.pdf'
    if os.path.exists(file_name):
        pass
    else:
        print(file_name)
        pdfkit.from_url(url,file_name)