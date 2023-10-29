#import the PyPDF2 module
import PyPDF2
import fitz
import re

file='eng1'
#open the PDF file
def pdf(file):
    PDFfile = open(file+".pdf", 'rb')

    PDFfilereader = PyPDF2.PdfFileReader(PDFfile)

    #print the number of pages
    pages=PDFfilereader.numPages
    print(pages)
    textfile=open(file+".txt","a+")
    #provide the page number
    for page in range(pages):
        pages = PDFfilereader.getPage(page)
        text=pages.extractText()
        text = re.sub(r'[^\w\s]|_', '', text)
        #extracting the text in PDF file
        textfile.write(text)

    #close the PDF file
    PDFfile.close()

    import fitz
    import io
    from PIL import Image
    #open the file
    pdf_file = fitz.open(file+".pdf")   
    #iterate over PDF pages
    for page_index in range(pdf_file.page_count):
        #get the page itself
        page = pdf_file[page_index]
        image_li = page.get_images()
        #printing number of images found in this page
        #page index starts from 0 hence adding 1 to its content
        if image_li:
            print(f"[+] Found a total of {len(image_li)} images in page {page_index+1}")
        else:
            print(f"[!] No images found on page {page_index+1}")
        for image_index, img in enumerate(page.get_images(), start=1):
            #get the XREF of the image
            xref = img[0]
            #extract the image bytes
            base_image = pdf_file.extract_image(xref)
            image_bytes = base_image["image"]
            #get the image extension
            image_ext = base_image["ext"]
            #load it to PIL
            image = Image.open(io.BytesIO(image_bytes))
            #save it to local disk
            image.save(open(f"image{page_index+1}_{image_index}.{image_ext}", "wb"))