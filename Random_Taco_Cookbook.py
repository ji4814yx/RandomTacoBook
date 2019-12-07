import docx # import this library to create and update a word document
from docx.shared import Inches
from docx.enum.text import WD_BREAK
from docx.enum.text import WD_BREAK # source: stack overflow
import requests
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

# Bold the last paragraph: Adade Gbadoe
last_paragraph = document.paragraphs[-1]
last_run = last_paragraph.runs[-1]
last_run.bold = True

# get the last paragraph, add the run to the last paragraph and use the run to add the break
for paragraph in document.paragraphs:
    if 'Adade Gbadoe' in paragraph.text:
        run = paragraph.add_run()
        run.add_break(WD_BREAK.PAGE)
#document.paragraphs[0].runs[0].add_break(docx.text.WD_BREAK.PAGE)

# document.add_heading("First Taco Recipe", 0) # add the heading for the First Taco Recipe

# working with Brian


url = 'https://taco-1150.herokuapp.com/random/?full_taco=true' # this will give one random recipe

for i in range(3):
    if i == 0:
        document.add_heading("First Taco Recipe", 0)
    if i == 1:
        document.add_heading("Second Taco Recipe", 0)
    if i == 2:
        document.add_heading("Third Taco Recipe", 0)

    response = requests.get(url).json() # provide a dictionary containing a taco recipe. For the next program
    # print(response)

    # get the recipe from each of the five components of the recipe: seasoning, condiment, mixin, base_layer and shell
    seasoning = response['seasoning']['recipe']
    seasoning_name = response['seasoning']['name']

    condiment = response['condiment']['recipe']
    condiment_name = response['condiment']['name']

    mixin = response['mixin']['recipe']
    mixin_name = response['mixin']['name']

    base_layer = response['base_layer']['recipe']
    base_layer_name = response['base_layer']['name']

    shell = response['shell']['recipe']
    shell_name = response['shell']['name']

    document.add_paragraph(seasoning_name, 'Heading 3')
    document.add_paragraph(seasoning)

    document.add_paragraph(condiment_name, 'Heading 3')
    document.add_paragraph(condiment)

    document.add_paragraph(mixin_name, 'Heading 3')
    document.add_paragraph(mixin)

    document.add_paragraph(base_layer_name, 'Heading 3')
    document.add_paragraph(base_layer)

    document.add_paragraph(shell_name, 'Heading 3')
    paragraph = document.add_paragraph(shell)
    run = paragraph.add_run()
    run.add_break(WD_BREAK.PAGE)


document.save('First_Page.docx')