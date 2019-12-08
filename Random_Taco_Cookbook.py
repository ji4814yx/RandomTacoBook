'''
This is Adade's big final project where I have to write a code to create a Random Taco Recipe Book in a new word
processing document with different pages.
I struggled while writing my code because I wanted to get things write and this is part of my work as a "coder". But
I think, there is always someone who will code better than you.  This is not a reason to give up on your code
especially as Brian's student.  sorry for my "bla bla bla"!
Thanks for taking your time to read my introduction
Let's go in the details of my code.
.

many lines of text
to describe
every little tiny detal that happens in this code
i struggled with
this part was easy
'''

'''
Make sure i have all the librarires I need to use
'''
import docx # import this library to create and update a word document
from docx.shared import Inches
from docx.enum.text import WD_BREAK
from docx.enum.text import WD_BREAK # source: stack overflow
import requests



'''
I need to create a new word processing document that will have all the 
'''
document = docx.Document() # create a document

document.add_heading("Random Taco Cookbook", 0) # add the heading Random Taco Cookbook

document.add_picture('Modified_Tai_Taco.jpg', width=Inches(6), height=Inches(4)) # add the resized taco image

document.add_paragraph() # add and empty paragraph after the picture

document.add_paragraph('Credits', 'Heading 3') # add Credits heading to provide the author of the image, the Url source
# and the person who wrote the code to create the document (Adade Gbadoe)

document.add_paragraph('Taco image: Photo by Tai\'s Captures on Unsplash') # write the name of the image author

document.add_paragraph('Source: https://taco-1150.herokuapp.com/random/?full_taco=true') # to write the URL text

# define the paragraph('Code by: Adade Gbadoe') and insert a page break after: thi s will avoid a repetition of
#('Code by: Adade Gbadoe') that will occur if we code: document.add_paragraph('Code by: Adade Gbadoe') before the actual
# paragraph = document.add_paragraph('Code by: Adade Gbadoe')
paragraph = document.add_paragraph('Code by: Adade Gbadoe')
run = paragraph.add_run()
run.add_break(WD_BREAK.PAGE)

# working with Brian

url = 'https://taco-1150.herokuapp.com/random/?full_taco=true' # this will give one random recipe
# this for loop to pull out each random taco recipe
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


document.save('First_Page.docx') # save the world document created