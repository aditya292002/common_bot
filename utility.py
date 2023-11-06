import g4f

def start_GPT4FREE():
    g4f.debug.logging = True
    g4f.check_version = False
    print(g4f.version)
    print(g4f.Provider.Ails.params)

def read_file_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()

summary = ""  # Initialize summary

def shorten_summary(summary):
    input_text = f"{summary}\nshorten this in 80-100 words, keep all the necessary points and remove unnecessary details"
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": input_text}],
        stream=True,
    )

    output = ""
    for message in response:
        output += str(message)
    
    return output

def process_prompt(prompt):
    input_text = f"{prompt}\nGenerate 3 MCQs for this text content Use format: Q) Question a) Answer 1 b) Answer 2 c) Answer 3 d) Answer 4 Solution: Answer X For each MCQ, use at most 50 words."
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": input_text}],
        stream=True,
    )

    output = ""
    for message in response:
        output += str(message)
    
    return output
