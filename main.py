#!/usr/bin/env python
# coding: utf-8

import os
import PyPDF2 as p2
import re
# import calendar

class Datecheck:
    # get working directory
    dirpath = os.getcwd()

    # initiation to open pdf file
    def __init__(self):
        print("Processing pdf to find the latest updated page:")
        self.pdffile = open("electric-tariff.pdf","rb")
        self.pdfread = p2.PdfFileReader(self.pdffile)

    def docinfo(self):
        # pull up document info
        docinfo = self.pdfread.getDocumentInfo()
        # extract the date for latest edits
        lastdate = docinfo['/ModDate']
        print("The latest edit was made on Day %s, Month %s, Year %s." % (lastdate[9:10], lastdate[7:8],lastdate[2:6]))

        # number of pages in total
        print("There are %s pages in total." % (self.pdfread.getNumPages()))

    def extractdate(self):

        # create loop to extract single page
        # i = 0
        #while i < self.pdfread.getNumPages():
            #x = self.pdfread.getPage(i)
            #page_content = x.extractText()


        x = self.pdfread.getPage(495)
        page_content = x.extractText()
        page_date = re.search('Date:(.+?)', page_content).group(1)
        # print(page_content)
        print(page_date)

def main():
    test = Datecheck()
    test.docinfo()
    test.extractdate()


if __name__ == "__main__":
    main()