import PyPDF2, sys, os

def addMargins(inPath, margin = 0.4):
    #READ
    file = open(inPath, 'rb')
    inpdf = PyPDF2.PdfFileReader(file)

    # WRITE
    outPath = inPath[:-4] + '-R.pdf'
    outpdf = PyPDF2.PdfFileWriter()
    for pnum in range(inpdf.numPages):
        page = inpdf.getPage(pnum)

        # create empty A4 size page
        #print(page.mediaBox.getWidth())
        tarw = round(int(page.mediaBox.getWidth())/(1 - margin))
        tarh = page.mediaBox.getHeight()
        emptyPage = PyPDF2.pdf.PageObject.createBlankPage(width=tarw, height=tarh)

        emptyPage.mergeTranslatedPage(page, 0, 0)

        outpdf.addPage(emptyPage)

    resultPdf = open(outPath, 'wb')
    outpdf.write(resultPdf)
    print('Added margins successfully: ' + outPath)
    resultPdf.close()

def deleteSparePDFs():
    for e in os.listdir():
        if len(e) >= 6:
            if e[-4:] == '.pdf' and e[-6:] != '-R.pdf':
                os.system('rm -rf ' + '"' + e + '"')



os.chdir(os.path.expanduser("~"))
os.chdir("MakingStuffFaster/PDFs")

def startJob():
    os.chdir(os.path.expanduser("~"))
    os.chdir("MakingStuffFaster/PDFs")
    folderFiles = os.listdir()
    for e in folderFiles:
        if len(e) >= 6:
            if e[-4:] == '.pdf' and e[-6:] != '-R.pdf':
                addMargins(e)
    deleteSparePDFs()

startJob()
