"""
Trivia
Trivia is a multiple choice quiz that reads from a plain text file
This quiz comes with a top 5 score listing
"""

import sys
from _dbus_bindings import String

def open_file(file_name, mode):
    """Opening the quiz file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file %s. Ending program.\n%s" % file_name, e)
        print("Try making sure the file exists.")
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return next line from the trivia file with some formatting."""
    line = the_file.readline()
    line = line.replace("/", "\n") #allows newline characters to be placed in the console relative to the text file 
    return line

def next_block(the_file):
    """Return the next question block from the trivia file."""
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    points = next_line(the_file)
    explanation = next_line(the_file)
    return category, question, answers, correct, points, explanation

def welcome(title):
    """Welcomes the user."""
    print("\t\tWelcome to Trivia!\n")
    print("\t\t  %s" % title)

def append_score(score_file, score):
    name = raw_input("\nWhat is your name?: ")
    score_file.writelines(name + "\n")
    score_file.writelines(String(score) + "\n")

def next_score(hscores_file):
    name = hscores_file.readline() #name captures the score element from the corresponding high score in the document
    name = name.replace("\n", "")
    score = hscores_file.readline() #score captures the name element from the corresponding high score in the document
    score = score.replace("\n", "")
    return score, name

def main():
    trivia_file = open_file("trivia_questions.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    #get first question block
    category, question, answers, correct, points, explanation = next_block(trivia_file)
    while category:
        #ask a question
        print(category)
        print(question)
        for i in range(4):
            print("\t%s - %s" % (i+1, answers[i]))

        #get an answer
        answer = None
        while answer not in range (1,5):
            try:
                answer = input("What's your answer (enter corresponding number): ")
            except:
                answer = input("What's your answer (enter corresponding number): ")
                
        #check the answer
        if answer == int(correct):
            print("\nCorrect! ")
            score += int(points)
        else:
            print("\nSorry, that's not right. ")
        
        print(explanation)    
        print("Score: %s\n" % score)
        
        # get next block
        category, question, answers, correct, points, explanation = next_block(trivia_file)

    trivia_file.close() # close the file
    
    print("That was the last question!")
    print("Your final score is %s." % score)
    
    hscores_file = open_file("trivia_hscores.txt", "a")
    append_score(hscores_file, score) #add player's score to the high-scores file
    hscores_file.close()
    
    hscores_file = open_file("trivia_hscores.txt", "r") #need to re-open to get back to top of file
    #construct a list of the top 5 scores
    score, name = next_score(hscores_file)
    hscore_list = []
    while name: #exits when entry reads nothing
        entry = (score, name)
        hscore_list.append(entry)
        score, name = next_score(hscores_file) #get next score
    hscore_list.sort(reverse=True) #descending order
    hscore_list = hscore_list[:5] #only show top 5
    
    #prints top 5 scores
    print("\nTop 5 Scores:")
    print("\nName\tScore\n")
    for pair in hscore_list:
        score, name = pair
        print("%s\t%s" % (name, score))    
    hscores_file.close()
    
#start the game
main()
raw_input("\n\nPress the enter key to exit.")