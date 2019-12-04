import docx # import this library to create and update a word document
from docx.shared import Inches
from docx.enum.text import WD_BREAK
from docx.enum.text import WD_BREAK # source: stack overflow
document = docx.Document() # create a document

document.add_heading("Random Taco Cookbook", 0) # add the heading Random Taco Cookbook

document.add_picture('Modified_Tai_Taco.jpg', width=Inches(6), height=Inches(4)) # add the resized taco image

document.add_paragraph("Photo by Tai's Captures on Unsplash") # write the name of the image author

document.add_paragraph()

document.add_paragraph("Source: https://taco-1150.herokuapp.com/random/?full_taco=true") # to write the URL text
document.add_paragraph()
document.add_paragraph()
document.add_paragraph()
document.add_paragraph()
document.add_paragraph()
document.add_paragraph()

document.add_paragraph("Adade Gbadoe", "Heading 3") # to write my name with Heading 3 style
# get the last paragraph, add the run to the last paragraph and use the run to add the break
for paragraph in document.paragraphs:
    if 'Adade Gbadoe' in paragraph.text:
        run = paragraph.add_run()
        run.add_break(WD_BREAK.PAGE)
#document.paragraphs[0].runs[0].add_break(docx.text.WD_BREAK.PAGE)

# document.paragraphs[0].runs[0].add_break()
document.save('First_Page.docx')





