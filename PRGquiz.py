#imports
import tkinter as tk
import random

#Questions list including the question, question type and correct answer
questions=[[
    "What is Blender typically used for by 9DVC students at GDC?",
    "What is the keyboard shortcut for generating new objects in Blender?",
    "What is editing mode used for in Blender?",
    "In Blender, to render means to edit a project",
    "What angle are the horizontal lines in Isometric drawing?",
    "In Blender, the scale tool can adjust the size of an object",
    "Which axes determind the horizontal location of an object",
    "To draw in oblique you typically first draw the 2d shape",
    "What is a donut shape called in Blender",
    "What does DVC stand for?",
    "Eevee, Workbench and Cycles are the 3 different render engines used in Blender",
    "What is the most recent version of Blender as of June 2026",
    "2 point perspective drawing mainly uses 45 degree angle lines",
    "To render(shade) a drawing first you...",
    "What is an example of a good opportunity to use Blender",
    "In DVC you can design architecture of products",
    "What is the purpose of a design breif?",
    "A design cannot be changed once the first iteration has been created",
    "What is the purpose of a mood board",
    "It is helpful to consider multiple different designs before deciding on one"], 
    ["multi-choice", "multi-choice", "multi-choice", "true/false", "multi-choice", 
    "true/false", "multi-choice", "true/false", "multi-choice", "multi-choice", 
    "true/false", "multi-choice", "true/false", "multi-choice", "multi-choice", 
    "true/false", "multi-choice", "true/false", "multi-choice", "true/false"], 
    ["b", "a", "d", "False", "a", "True", "a", "True", "c", "b", "True", "d", "False", "a", "d", "True", "b", "False", "d", "True"]]

#Question options to be written onto radiobuttons
options=[
    ["Game making", "3D modeling", "Drawing", "Designing"],
    ["Shift+a", "Ctrl+1", "Right click, create sphere", "Shift+o"],
    ["Taking a photo", "Moving around objects", "Viewing the project", "Modifing a delected object"],
    ["True", "False"],
    ["30 degrees", "45 degrees", "50 degrees", "90 degrees"],
    ["True", "False"],
    ["x & y", "z & x", "y & z", "All of the above"],
    ["True", "False"],
    ["Circle", "Sphere", "Torus", "Bagel"],
    ["Designing of Versatile creations", "Design and Visual Communications", "Describing Vital Communication", "Design Visual Creations"],
    ["True", "False"],
    ["3.1.2", "5.4.5", "4.4.3", "5.1.2"],
    ["True", "False"],
    ["Determine where the light source is", "Colour the whole drawing", "Draw it again", "Erase the drawing"],
    ["You would like to practice using it", "You have a design that is difficult to draw", "You would like to 3D print a design", "All of the above"],
    ["True", "False"],
    ["To explore different possible designs", "To communicate what you are designing", "To show people your finished design", "To communicate functional aspects of your design"],
    ["True", "False"],
    ["To show similar designs to what you would like to design", "To visually show your inspiration", "To communicate the aesthetic you are aiming for in your design", "All of the above"],
    ["True", "False"]]

#initialises variables and constants
used_questions=[]
quiz_len=10
returnn=0

#creates GUI
root = tk.Tk()

#GUI name
root.title("DVC Quiz")

#GUI size and shape
root.geometry("600x600+10+10")

#intro_screen function to create the intro screen
def intro_screen():

    #creates the frame_intro frame for the intro screen
    frame_intro=tk.Frame(root, width="600", height="600")
    frame_intro.pack()

    #creates the label for introducing the user to the program
    label_intro=tk.Label(frame_intro, width="600", text="Welcome to the 9DVC quiz!")
    label_intro.place(x=100, y=100)

    #creates the button for starting the program that sends you to the action_start function
    button_start=tk.Button(frame_intro, command=action_start)
    button_start.place(x=100, y=150)

#action_start function that is called with the start button
def action_start():

    #calls the main_loop function
    main_loop()

#main_loop function that contains most of the main code
def main_loop():
    #globalises the variables
    global quest_count
    global answers

    #initialises variables
    answers=[],[],[],[],[],[],[],[],[],[]
    quest_count=0

    #while loop to loop 10 times for 10 different questions
    while quest_count<quiz_len:

        #calls the what_question function
        what_question()

        #calls the question_screen function
        question_screen()

    #calls the calc_score function
    calc_score()

    #calls the end_screen function
    end_screen()

#the what_question function that decides what question to show the user and makes sure that it hasn't been used before
def what_question():

    #globalises the question_num variable
    global question_num

    #If the user has chosen to return to a past question they are sent to the last question they answered
    if returnn==1:
        
        #defines question_num (the question we are on) as the last question that was used
        question_num=used_questions(quest_count)
    
    #if the user has chosen to move on to the next question
    else:

        #Generates a random number between 0-18 for the question number
        question_num=random.randint(0,18)

        #if the question has already been used then it generates another
        while question_num in used_questions:
            question_num=random.randint(0,18)

        #Adds the question number onto the used_questions list so it cannot be used again
        used_questions.append(question_num)

#the question_screen function that prints the question screen
def question_screen():
    #globalises the rad_grp_var variable
    global rad_grp_var

    #creates the frame frame_question for the question screen
    frame_question=tk.Frame(root, height=600, width=600, bg="blue")
    frame_question.pack()

    #converts the question number into a string so it can be printed onto a label
    quest_count2=str(quest_count)

    #label_questnum to display the question number
    label_questnum=tk.Label(frame_question, text=("Question"+ quest_count2))
    label_questnum.pack()

    #label_question to display the question
    label_question=tk.Label(frame_question, text=questions[0][question_num])
    label_question.pack()

    #if the question is not question 1
    if quest_count!=0:

        #prints the previous button
        button_previous=tk.Button(frame_question, text="Previous", command=action_previous)
        button_previous.pack()

    #prints the next button
    button_next=tk.Button(frame_question, text="Next", command=action_next)
    button_next.pack()

    #if the question is true or false
    if questions[1][(question_num-1)]=="true/false":
        
        #prints the true and false radiobuttons
        rad_grp_var = tk.IntVar()
        radiobutton_true = tk.Radiobutton(frame_question, text="True", variable=rad_grp_var, value="True")
        radiobutton_false = tk.Radiobutton(frame_question, text="False", variable=rad_grp_var, value="False")
        radiobutton_true.pack()
        radiobutton_false.pack()
    
    #if the question is multi-choice
    elif questions[1][(question_num-1)]=="true/false":

        #prints a, b, c, d radiobuttons
        rad_grp_var = tk.IntVar()
        radiobutton_a = tk.Radiobutton(frame_question, text=options[(question_num-1)][0], variable=rad_grp_var, value="a")
        radiobutton_b = tk.Radiobutton(frame_question, text=options[(question_num-1)][1], variable=rad_grp_var, value="b")
        radiobutton_c = tk.Radiobutton(frame_question, text=options[(question_num-1)][2], variable=rad_grp_var, value="c")
        radiobutton_d = tk.Radiobutton(frame_question, text=options[(question_num-1)][3], variable=rad_grp_var, value="d")
        radiobutton_a.pack()
        radiobutton_b.pack()
        radiobutton_c.pack()
        radiobutton_d.pack()

#the action_next function to move onto the next question
def action_next():
    global returnn

    #finds the answer from the last question
    answer=rad_grp_var.get()

    #if the answer is correct
    if answer==questions[2][(question_num-1)]:

        #It logs in the answers list variable corresponding to that question that the answer was correct
        answers[quest_count]="correct"
    
    #if the answer is incorrect
    else:

        #It logs in the answers list variable corresponding to that question that the answer was incorrect
        answers[quest_count]="incorrect"

    #adds one to the quest_count variable to move onto the next question
    quest_count=quest_count+1

    #the returnn variable tells the program that it is not returning to a past question
    returnn=0

def action_previous():

    #globalises the returnn variable
    global returnn

    #takes away one from the quest_count variable to return to the last question
    quest_count=quest_count-1
    
    #the returnn variable tells the program that it is returning to a past question
    returnn=1

def calc_score():
    #globalises the variables
    global score
    global correct
    global incorrect
    global grade

    #correct=how manny times "correct" appears in answers
    correct=1

    #incorrect=how many times "incorrect" appears in answers
    incorrect=1

    #calculates the score percentage
    score=(correct/(correct+incorrect))*100

    #if the user got over 80% correct
    if score>=80:

        #the user's grade is an excellence
        grade="excellence"

    #if the user got between 55%-80% correct
    elif (score>=55) and (score<80):

        #the user's grade is a merit
        grade="merit"

    #if the user got between 30%-55% correct
    elif (score>=30) and (score<55):

        #the user's grade is an achieved
        grade="achieved"

    #if the user got less than 30% correct
    elif score<30:

        #the user's grade is a not achieved
        grade="not achieved"

#the end_screen function that shows the final screen
def end_screen():

    #creates the frame frame_end
    frame_end=tk.Frame(root, height=600, width=600)
    frame_end.pack()

    #if the user achieved excellence
    if score=="excellence":

        #prints a congratulations message
        label_congrats=tk.Label(frame_end, text="Congratulations!")
        label_congrats.pack()

        #the message telling them how many questions they got right
        message="You answered", correct, "out of ", (correct+incorrect), "questions correctly"

        label_score=tk.Label(frame_end, text=message)
        label_score.pack()

        #tells them their score
        label_grade=tk.Label(frame_end, text="You have achieved excellence!")
        label_grade.pack()

        #if this is not their second attempt
        if retry!="yes":

            #prints the retry button
            button_retry=tk.Button(frame_end, text="Retry", command=action_retry)
            button_retry.pack()

        #prints the end button
        button_end=tk.Button(frame_end, text="end", command=action_end)
        button_end.pack()

#the action_retry function that lets the user retry the quiz with different questions
def action_retry():
    #globalises the retry variable
    global retry

    #tells the program that the user is retrying the quiz so they cannot do it another time
    retry="yes"

    #calls the main_loop function
    main_loop()

#the action_end function that closes the program
def action_end():

    #close program
    print("close program")

#calls the intro_screen function
intro_screen()

#starts the GUI
root.mainloop()