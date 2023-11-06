import g4f

g4f.debug.logging = True # enable logging
g4f.check_version = False # Disable automatic version checking
print(g4f.version) # check version
print(g4f.Provider.Ails.params)  # supported args

# Automatic selection of provider

# input_text = input("Ask Question : ")
input_text = """
"Marvel's The Avengers[5] (classified under the name Marvel Avengers Assemble "
             'in the United Kingdom and Ireland),[1][6] or simply The Avengers, is a 2012 '
             'American superhero film based on the Marvel Comics superhero team of the '
             'same name. Produced by Marvel Studios and distributed by Walt Disney Studios '
             'Motion Pictures,[a] it is the sixth film in the Marvel Cinematic Universe '
             '(MCU). Written and directed by Joss Whedon, the film features an ensemble '
             'cast including Robert Downey Jr., Chris Evans, Mark Ruffalo, Chris '
             'Hemsworth, Scarlett Johansson, and Jeremy Renner as the Avengers, alongside '
             'Tom Hiddleston, Stellan Skarsgård, and Samuel L. Jackson. In the film, Nick '
             'Fury and the spy agency S.H.I.E.L.D. recruit Tony Stark, Steve Rogers, Bruce '
             'Banner, Thor, Natasha Romanoff, and Clint Barton to form a team capable of '
             "stopping Thor's brother Loki from subjugating Earth.
            "
             '
            '
             "The film's development began when Marvel Studios received a loan from "
             'Merrill Lynch in April 2005. After the success of the film Iron Man in May '
             '2008, Marvel announced that The Avengers would be released in July 2011 and '
             'would bring together Stark (Downey), Rogers (Evans), Banner (at the time '
             "Edward Norton),[b] and Thor (Hemsworth) from Marvel's previous films. With "
             'the signing of Johansson as Romanoff in March 2009, Renner as Barton in June '
             '2010, and Ruffalo replacing Norton as Banner in July 2010, the film was '
             'pushed back for a 2012 release. Whedon was brought on board in April 2010 '
             'and rewrote the original screenplay by Zak Penn. Production began in April '
             '2011 in Albuquerque, New Mexico, before moving to Cleveland, Ohio in August '
             'and New York City in September. The film has more than 2,200 visual effects '
             'shots.
            '
             '
            '
             'The Avengers premiered at the El Capitan Theatre in Los Angeles on April 11, '
             '2012, and was released in the United States on May 4, as the final film in '
             "Phase One of the MCU. The film received praise for Whedon's direction and "
             'screenplay, visual effects, action sequences, acting, and musical score. The '
             'film grossed over $1.5 billion worldwide, setting numerous box office '
             'records and becoming the third-highest-grossing film of all time at the time '
             'of its release and the highest-grossing film of 2012, as well as the first '
             'Marvel production to generate $1 billion in ticket sales. In 2017, The '
             'Avengers was featured as one of the 100 greatest films of all time in an '
             'Empire magazine poll. It received a nomination for Best Visual Effects at '
             'the 85th Academy Awards, among numerous other accolades. Three sequels have '
             'been released: Avengers: Age of Ultron (2015), Avengers: Infinity War '
             '(2018), and Avengers: Endgame (2019) 
            '
             'generate 3 mcqs for this text content 
            '
             'use format:
            '
             'Q) question
            '
             'a) answer1
            '
             'a) answer2
            '
             'a) answer3
            '
             'a) answer4
            '
             'solution: answerx
            '
             '
            '
             'for each mcq use atmost 50 words
            ')
Using GptGo provider
The production of genetically modified organisms (GMOs) involves altering the genetic composition of an organism through the insertion of genes from different organisms. This process is achieved through various techniques such as gene splicing and recombinant DNA technology. GMOs have been created for a variety of purposes ranging from crop improvement to the production of pharmaceuticals. Despite the potential benefits of GMOs, their production and consumption have been met with controversy and concerns over their impact on human health and the environment. Critics argue that GMOs may have long-term health risks and could disrupt natural ecosystems.
ic| ind: 426, new_ind: 426
Using RetryProvider provider
ic| prompt: ('(2019) 
            '
             'generate 3 mcqs for this text content 
            '
             'use format:
            '
             'Q) question
            '
             'a) answer1
            '
             'b) answer2
            '
             'c) answer3
            '
             'd) answer4
            '
             'solution: answerx
            '
             '
            '
             'for each mcq use atmost 50 words
            ')

"""
# streamed completion
response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": input_text}],
    stream=True,
)

output = ""
for message in response:
    output += str(message)
print(output)