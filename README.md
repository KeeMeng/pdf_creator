# pdf_creator
Crops and adds images onto a template pdf

## Usage

Take screenshots of something (such as textbook questions) with a plain white background, and input the folder. Itw ill then create a pdf with the images added onto your template pdf. 

Example: [Input folder](https://github.com/KeeMeng/pdf_creator/tree/main/example) and [output pdf](https://github.com/KeeMeng/pdf_creator/tree/main/example.pdf). 

Shell Script: `python create.py path_to_folder_with_images`

Make sure to add `template.pdf` to the same directory as this python script. Works with A4 templates only. 


## Suggestions

If you are using this script on macos, you could use the Automator app to create a quick action in finder. After right clicking a folder containing the images and running the quick action, the pdf file will be created in the same directory as your input folder. 

![Automator Workflow](https://github.com/KeeMeng/pdf_creator/blob/main/automator.png "Automator Workflow")
