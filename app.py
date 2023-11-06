from utility import *
import time
from icecream import ic

PROMPT_LENGTH = 500
ind = 0

start_GPT4FREE()
file_content = read_file_content('data.txt')
data_lst = file_content.split(' ')

def generate_prompt(start_index, end_index):
    return ' '.join(data_lst[start_index:end_index])

def get_prompt():
    global ind
    global summary

    if len(summary) >= 250:
        summary = shorten_summary(summary)

    rest_size = PROMPT_LENGTH - len(summary)
    new_ind = ind + rest_size

    if new_ind >= len(data_lst):
        new_ind = len(data_lst) - 1

    result = generate_prompt(ind, new_ind)
    ind = new_ind

    result += """
    Generate 3 MCQs for this text content
    Use format:
    Q) Question
    a) Answer 1
    b) Answer 2
    c) Answer 3
    d) Answer 4
    Solution: Answer X

    For each MCQ, use at most 50 words.
    """
    return result

complete_response = ""

while ind < len(data_lst):
    prompt = get_prompt()
    if(len(prompt) < 500):
        break
    response = process_prompt(prompt)
    complete_response += response
    time.sleep(10)
with open('mcq.txt', 'a') as mcq_file:
    mcq_file.write(complete_response + '\n')