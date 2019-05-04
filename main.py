#!/usr/bin/env python
# coding: utf-8

import os
import PyPDF2 as p2
import re
from datetime import datetime
import pandas as pd


class Datecheck:
    # get working directory
    dirpath = os.getcwd()

    # initiation to open pdf file
    def __init__(self):
        print("Processing pdf to find the latest updated page:")
        self.pdffile = open("electric-tariff.pdf", "rb")
        self.pdfread = p2.PdfFileReader(self.pdffile)

    def docinfo(self):
        # pull up document info
        docinfo = self.pdfread.getDocumentInfo()
        # extract the date for latest edits
        lastdate = docinfo['/ModDate']
        print("The latest edit was made on Day %s, Month %s, Year %s." % (lastdate[9:10], lastdate[7:8], lastdate[2:6]))

        # number of pages in total
        print("There are %s pages in total." % (self.pdfread.getNumPages()))

    def extractnsort(self):
        print("Now begin the date extraction process:")
        # create loop to extract single page
        i = 1  # skip the cover page
        datelist = []

        while i < self.pdfread.getNumPages():
            print("processing Page %s..." % (i+1))
            x = self.pdfread.getPage(i)
            page_content = x.extractText()
            page_content = ''.join(page_content.split())
            # print(page_content)

            # attempt to locate date string (!!need to make sure there are no other dates)
            # example: 03/01/2014
            try:
                page_date = re.search('\d{2}\/\d{2}\/\d{4}', page_content).group(0)
                page_date = datetime.strptime(str(page_date), "%m/%d/%Y").date()
            except AttributeError:
                page_date = "NaN"
            # print(page_date)
            datelist.append([i + 1, page_date])
            i += 1

        print("Extraction complete. Now preview the table sorted by pages.")
        df = pd.DataFrame(datelist, columns=["Page", "Date"])
        print(df[:5])

        # drop pages that we fail to load
        df.clean = df[df["Date"] != 'NaN']

        page_failure = len(df)-len(df.clean)
        print("%s pages are unreadable in total." % page_failure)

        # sort loaded pages based on dates
        self.df_sorted = df.clean.sort_values(by="Date", ascending=False)
        print("After sorting the date, now preview the top updated pages.")
        print(self.df_sorted[:5])

    def singletest(self):
        print("For testing:")
        # create loop to extract single page
        i = 6
        datelist = []

        x = self.pdfread.getPage(i)
        page_content = x.extractText()
        page_content = ''.join(page_content.split())
        print(page_content)

        # attempt to locate date string (!!need to make sure there are no other dates)
        # example: 03/01/2014
        try:
            page_date = re.search('\d{2}\/\d{2}\/\d{4}', page_content).group(0)
            page_date = datetime.strptime(str(page_date), "%m/%d/%Y").date()
        except AttributeError:
            page_date = "error in extracting date"
        print(page_date)
        datelist.append([i + 1, page_date])

    def savefile(self):
        self.df_sorted.to_csv("output_table.csv", index=False)



def main():
    test = Datecheck()
    test.docinfo()
    test.extractnsort()
    #test.singletest() # for testing only
    test.savefile()


if __name__ == "__main__":
    main()
