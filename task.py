
'''
data.txt
Pages	31
Words	14676
Characters	92763
Characters excluding spaces	78593

'''
--------------------------------------------------------------
'''

500 words as i/p
500 words as o/p


> for each 500 i/p generate 3 mcqs

3 mcqs for each 500 words
total = 500 + 500 + 500 = 1500 words
'''
'''
prompt to pass to chatGPT with the text content

text content + (generate 3 mcqs for this text content and also specify the answer
use format:
Q) question
a) answer1
a) answer2
a) answer3
a) answer4
solution: answerx
)

generate 

'''
--------------------------------------------------


complete_response = ""
while ind < len(data_lst):
    prompt = get_prompt()
    if len(prompt) < 500:
        break
    response = process_prompt(prompt)
    complete_response += response
    # time.sleep(10)

with open('mcq.txt', 'a') as mcq_file:
    mcq_file.write(complete_response + '\n')