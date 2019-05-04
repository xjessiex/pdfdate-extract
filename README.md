# Date Extraction Tool for PDF
#### Project Status: [Completed]

## Project Intro/Objective
To help my friend easily identify the latest update in a long PDF file, this python tool is built to find the most updated pages in a 618-page [tariff document](https://www.coned.com/_external/cerates/documents/elecPSC10/electric-tariff.pdf) for electricity service. Each page has its effective date on the top left corner. Thus, my tasks are:
* read the text content for each PDF page
* extract the date format
* convert it into datetime objects and sort all the dates for pages

### Methods Used
* PDF processing: `PyPDF2`;
* Date Extraction: `re`, `datetime`;

## Results
* It's worth noticing that there are 10 pages that are just not able to be processed by `PyPDF2`. I exclude those unreadable pages in order to sort the pages based on dates.
* The `re` package is powerful but I need to read more about how to fully utilize the [package](https://docs.python.org/2/library/re.html). Right now, I locate the first matching date pattern to extract the date. I should identify the before and after string to avoid errors.

## Sample Output
![sample_image](https://github.com/xjessiex/pdfdate-extract/blob/master/sample_output.PNG =150x)
