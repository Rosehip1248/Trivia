# Trivia
This is a Python program that allows a player to take a multiple choice quiz where the questions are read from a plain text file.

Questions are stored in "trivia_questions.txt" and the list of players' scores is stored in "trivia_hscores.txt".

If you wish to use this quiz architecture then there are a few things to note based on the way the main program (Trivia.py) reads from the plain text files:
- In neither of the .txt files must there be any blank lines otherwise this could cause the main program to read and stop reading at undesirable times.
- The structure of the file "trivia_questions.txt" is as follows:
          - The first line is reserved for the title of the entire quiz episode (my title is 'Python Trivia'). Every line after              this belongs to a 'question block'.
          - The question blocks' structure is as follows: 1 line for the Category that classfies the question, 1 line for the                actual question itself, 4 lines for each of the 4 possible responses (1 line each), 1 line for the correct answer (a             number from 1 to 4 relative to the correct response's position in the block of 4 responses), 1 line for the number of             points that question is worth and 1 line for the explanation of the question's correct answer.
          - For each of the lines, you can make them as long as you desire but as they can sometimes get quite long, a newline               character may be requried to make the quiz easier to read in the terminal so please use the "/" character in 
            "trivia_questions.txt" and this tells the main program where you would like a newline character to be placed (a good             rule of thumb is a newline character every 10-12 words).
- The structure of the file "trivia_hscores.txt" is as follows:
          - Each player has a score block which consists of 2 lines, the first line is the player's name and the second is that              player's score.

This is built on the example about reading from plain text files in the text book "Python Programming Third Edition For The Absolute Beginner" by Michael Dawson.
