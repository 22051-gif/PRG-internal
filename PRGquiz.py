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
    "Which axes determine the horizontal location of an object",
    "To draw in oblique you typically first draw the 2d shape",
    "What is a donut shape called in Blender",
    "What does DVC stand for?",
    "Eevee, Workbench and Cycles are the 3 different render engines used in Blender",
    "What is the most recent version of Blender as of June 2026",
    "2 point perspective drawing mainly uses 45 degree angle lines",
    "To render(shade) a drawing first you...",
    "What is an example of a good opportunity to use Blender",
    "In DVC you can design architecture or products",
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
    ["Taking a photo", "Moving around objects", "Viewing the project", "Modifing a selected object"],
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
quiz_len=10
used_questions=[""]*(quiz_len*2)
retry="no"
quest_count=0
previouspressed="no"

#creates GUI
root = tk.Tk()

#GUI name
root.title("DVC Quiz")

#GUI size and shape
root.geometry("600x530+600+200")

#intro_screen function to create the intro screen
def intro_screen():

    #globalises frame_intro
    global frame_intro

    #creates the frame_intro frame for the intro screen
    frame_intro=tk.Frame(root, width="600", height="600", bg="light steel blue")
    frame_intro.place(x=0, y=0)

    #creates the labels for introducing the user to the program
    label_intro=tk.Label(frame_intro, width=36, height=2, text="Welcome to the 9DVC quiz!", font="arial 20")
    label_intro.place(x=10, y=10)

    label_explain=tk.Label(frame_intro, text="You will be given 10 9DVC related", font="arial 15", bg="light steel blue")
    label_explain.place(x=140, y=120)

    label_explain2=tk.Label(frame_intro, text="multi-choice and true/false questions", font="arial 15", bg="light steel blue")
    label_explain2.place(x=135, y=150)

    label_explain3=tk.Label(frame_intro, text="You may choose not to attempt a question by skipping it", font="arial 15", bg="light steel blue")
    label_explain3.place(x=60, y=180)

    label_explain4=tk.Label(frame_intro, text="(this will not be included into your score)", font="arial 15", bg="light steel blue")
    label_explain4.place(x=120, y=210)

    label_explain3=tk.Label(frame_intro, text="Have fun!", font="arial 17", bg="light steel blue")
    label_explain3.place(x=250, y=280)

    #creates the button for starting the program that sends you to the action_start function
    button_start=tk.Button(frame_intro, text="Start", font="arial 15", width=12, command=action_start)
    button_start.place(x=430, y=400)

#action_start function that is called with the start button
def action_start():

    #globalises the variables
    global quest_count
    global answers

    #initialises variables
    answers=[""] * quiz_len
    quest_count=0

    #calls the main_loop function
    main_loop()

#main_loop function that contains most of the main code
def main_loop():
    global quest_count

    #while loop to loop 10 times for 10 different questions
    if quest_count<quiz_len:

        #calls the what_question function
        what_question()

        if retry=="no" and quest_count==0 and previouspressed=="no":
            frame_intro.pack_forget()
        elif retry=="yes" and quest_count==0 and previouspressed=="no":
            frame_end.pack_forget()
        else:
            frame_question.pack_forget()

        #calls the question_screen function
        question_screen()
    else:

        #calls the calc_score function
        calc_score()

        #calls the end_screen function
        end_screen()

#the what_question function that decides what question to show the user and makes sure that it hasn't been used before
def what_question():

    #globalises the question_num variable
    global question_num, quest_count

    #If the user has chosen to return to a past question they are sent to the last question they answered
    #or if they are returning back to the next question after clicking previous then they are taken back to the same question
    if used_questions[quest_count]!="":
        
        #defines question_num (the question we are on) as the last question that was used
        question_num=used_questions[quest_count]
    
    #if the user has chosen to move on to the next question
    else:

        #Generates a random number between 0-18 for the question number
        question_num=random.randint(0,19)

        #if the question has already been used then it generates another
        while question_num in used_questions:
            question_num=random.randint(0,19)

        #Adds the question number onto the used_questions list so it cannot be used again
        used_questions[quest_count]=question_num

#the question_screen function that prints the question screen
def question_screen():
    #globalises the rad_grp_var variable
    global rad_grp_var, quest_count, question_num
    global frame_question

    #creates the frame frame_question for the question screen
    frame_question=tk.Frame(root, height=600, width=600, bg="light steel blue")
    frame_question.pack(fill="both", expand=True)
    frame_question.pack_propagate(False)

    #converts the question number into a string so it can be printed onto a label
    quest_count2=str(quest_count+1)

    #label_questnum to display the question number
    label_questnum=tk.Label(frame_question, font="arial 13", text=("Question", quest_count2), bg="light steel blue")
    label_questnum.place(x=10, y=10)

    #label_question to display the question
    label_question=tk.Label(frame_question, text=questions[0][question_num], font="arial 12")
    label_question.place(x=10, y=50)

    #if the question is not question 1
    if quest_count!=0:

        #prints the previous button
        button_previous=tk.Button(frame_question, text="Previous", width=12, font="arial 15", command=action_previous)
        button_previous.place(x=30, y=400)

    #prints the next button
    button_next=tk.Button(frame_question, text="Next", width=12, font="arial 15", command=action_next)
    button_next.place(x=430, y=400)

    #if the question is true or false
    if questions[1][question_num]=="true/false":
        
        #prints the true and false radiobuttons
        rad_grp_var = tk.StringVar()
        radiobutton_true = tk.Radiobutton(frame_question, text="True", font="arial 13", bg="light steel blue", variable=rad_grp_var, value="True")
        radiobutton_false = tk.Radiobutton(frame_question, text="False", font="arial 13", bg="light steel blue", variable=rad_grp_var, value="False")
        radiobutton_true.place(x=30, y=100)
        radiobutton_false.place(x=30, y=150)
    
    #if the question is multi-choice
    elif questions[1][question_num]!="true/false":

        #prints a, b, c, d radiobuttons
        rad_grp_var = tk.StringVar()
        radiobutton_a = tk.Radiobutton(frame_question, text=options[question_num][0], font="arial 13", bg="light steel blue", variable=rad_grp_var, value="a")
        radiobutton_b = tk.Radiobutton(frame_question, text=options[question_num][1], font="arial 13", bg="light steel blue", variable=rad_grp_var, value="b")
        radiobutton_c = tk.Radiobutton(frame_question, text=options[question_num][2], font="arial 13", bg="light steel blue", variable=rad_grp_var, value="c")
        radiobutton_d = tk.Radiobutton(frame_question, text=options[question_num][3], font="arial 13", bg="light steel blue", variable=rad_grp_var, value="d")
        radiobutton_a.place(x=30, y=100)
        radiobutton_b.place(x=30, y=170)
        radiobutton_c.place(x=30, y=240)
        radiobutton_d.place(x=30, y=310)

#the action_next function to move onto the next question
def action_next():
    global quest_count

    #finds the answer from the last question
    answer=rad_grp_var.get()

    #if the answer is correct
    if answer==questions[2][question_num]:

        #It logs in the answers list variable corresponding to that question that the answer was correct
        answers[quest_count]="correct"

    #if the answer is incorrect
    elif (answer!=questions[2][question_num]) and (answer!=""):

        #It logs in the answers list variable corresponding to that question that the answer was incorrect
        answers[quest_count]="incorrect"
    
    #if no answer has been entered the question is counted as not attempted
    elif answers[quest_count]=="":
        answers[quest_count]="Not attempted"

    #adds one to the quest_count variable to move onto the next question
    quest_count=quest_count+1

    previouspressed="no"

    #calls the main_loop function
    main_loop()

#the action_previous function to return to the last question
def action_previous():

    #globalises the variables
    global quest_count, previouspressed

    #takes away one from the quest_count variable to return to the last question
    quest_count=quest_count-1

    previouspressed="yes"

    #calls the main_loop function
    main_loop()

#the calc_score function to calculate the user's score and grade
def calc_score():
    #globalises the variables
    global score
    global correct
    global incorrect
    global grade

    #correct=how manny times "correct" appears in answers
    correct=answers.count("correct")

    #incorrect=how many times "incorrect" appears in answers
    incorrect=answers.count("incorrect")

    if correct+incorrect==0:
        score=0
    else:
            
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
    global frame_end

    #hides the question screen
    frame_question.pack_forget()

    #creates the frame frame_end
    frame_end=tk.Frame(root, bg="light steel blue", height="600", width="600")
    frame_end.pack(fill="both")

    #the message telling them how many questions they got right
    message=f"You answered {correct} out of {correct+incorrect} questions correctly"

    label_score=tk.Label(frame_end, bg="light steel blue", text=message, font="arial 15")
    label_score.place(x=80, y=120)

    #if the user achieved excellence
    if grade=="excellence":

        #prints a congratulations message
        label_congrats=tk.Label(frame_end, text="Congratulations!", width=36, height=2, font="arial 20")
        label_congrats.place(x=10, y=10)

        #tells them their score
        label_grade=tk.Label(frame_end, bg="light steel blue", text="You have achieved excellence!", font="arial 17")
        label_grade.place(x=150, y=230)
    else:

        #prints a motivational message
        label_congrats=tk.Label(frame_end, text="Good try!", width=36, height=2, font="arial 20")
        label_congrats.place(x=10, y=10)

        #if the user got a not achieved
        if grade=="not achieved":
            #tells them their score
            label_grade=tk.Label(frame_end, bg="light steel blue", text="This is a not achieved", font="arial 17")
            label_grade.place(x=190, y=230)

        #if the user got an achieved
        elif grade=="achieved":
            #tells them their score
            label_grade=tk.Label(frame_end, bg="light steel blue", text="This is an achieved", font="arial 17")
            label_grade.place(x=200, y=230)

        #if the user got a merit
        elif grade=="merit":
            #tells them their score
            label_grade=tk.Label(frame_end, bg="light steel blue", text="This is a merit", font="arial 17")
            label_grade.place(x=210, y=230)
        
        #prints a motivational message
        label_retry=tk.Label(frame_end, bg="light steel blue", text="Retry?", font="arial 15")
        label_retry.place(x=260, y=260)

    #if this is not their second attempt
    if retry!="yes":

        #prints the retry button
        button_retry=tk.Button(frame_end, text="Retry", width=12, font="arial 15", command=action_retry)
        button_retry.place(x=30, y=400)

    #prints the end button
    button_end=tk.Button(frame_end, text="End", width=12, font="arial 15", command=action_end)
    button_end.place(x=430, y=400)

#the action_retry function that lets the user retry the quiz with different questions
def action_retry():
    #globalises the retry variable
    global retry

    #tells the program that the user is retrying the quiz so they cannot do it another time
    retry="yes"

    #calls the action_start function
    action_start()

#the action_end function that closes the program
def action_end():

    #close program
    exit()

#calls the intro_screen function
intro_screen()

#starts the GUI
root.mainloop()