import openai
import json
from pypdf import PdfReader

openai.api_key = ""


'''

This function is used for fill data from form of PDF:

Input:

- pdf_path (str): path to file pdf

- data_fill (arr or str): data use to fill (suggest basic information)

- page fill: page number to fill

Return:

- response (Response obj): Include full information for answering of GPT api

'''

def fill(pdf_path, data_fill, page_fill = 0):

    reader = PdfReader(pdf_path)
    number_of_pages = len(reader.pages)
    page = reader.pages[page_fill]
    text = page.extract_text()

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Fill this form by your personal data {}, Yes/No question will be yes all, return in json format: \n {}".format(str(data_fill),text),
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
    )

    return response


# Quick using
if __name__ == "__main__":

    data_filled = ["Huy", "20/02/2023", "11:02", "Vietnam", "work for something","Trial project"]

    print(fill("gptform.pdf", data_filled))
