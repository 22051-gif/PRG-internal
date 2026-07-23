import tkinter as tk
import random

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

used_questions=[]
quiz_len=10
returnn=0

root = tk.Tk()

root.title("DVC Quiz")

root.geometry("600x600+10+10")

def intro_screen():
    #print intro screen
    frame_intro=tk.Frame(root, width="600", height="600")
    frame_intro.pack()

    label_intro=tk.Label(frame_intro, width="600", text="Welcome to the 9DVC quiz!")
    label_intro.place(x=100, y=100)

    button_start=tk.Button(frame_intro, command=action_start)
    button_start.place(x=100, y=150)

def action_start():
    main_loop()

def main_loop():
    global quest_count
    global answers
    answers=[],[],[],[],[],[],[],[],[],[]
    quest_count=0

    if quest_count<quiz_len:
        what_question()

        question_screen()

def what_question():
    global question_num

    if returnn==1:
        question_num=used_questions(quest_count)
    else:
        question_num=random.randint(0,18)

        while question_num in used_questions:
             question_num=random.randint(0,18)

        used_questions.append(question_num)

def question_screen():
    global rad_grp_var

    #print question screen
    frame_question=tk.Frame(root)

    quest_count2=str(quest_count)

    label_questnum=tk.Label(frame_question, text=("Question"+ quest_count2))
    label_questnum.pack()

    label_question=tk.Label(frame_question, text=questions[0][question_num])
    label_question.pack()

    if quest_count!=0:
        button_previous=tk.Button(frame_question, text="Previous", command=action_previous)
        button_previous.pack()

    button_next=tk.Button(frame_question, text="Next", command=action_next)
    button_next.pack()

    if questions[1][(question_num-1)]=="true/false":
        rad_grp_var = tk.IntVar()
        radiobutton_true = tk.Radiobutton(frame_question, text="True", variable=rad_grp_var, value="True")
        radiobutton_false = tk.Radiobutton(frame_question, text="False", variable=rad_grp_var, value="False")
        radiobutton_true.pack()
        radiobutton_false.pack()
    else:
        rad_grp_var = tk.IntVar()
        radiobutton_a = tk.Radiobutton(frame_question, text=options[(question_num-1)][0], variable=rad_grp_var, value="a")
        radiobutton_b = tk.Radiobutton(frame_question, text=options[(question_num-1)][1], variable=rad_grp_var, value="b")
        radiobutton_c = tk.Radiobutton(frame_question, text=options[(question_num-1)][2], variable=rad_grp_var, value="c")
        radiobutton_d = tk.Radiobutton(frame_question, text=options[(question_num-1)][3], variable=rad_grp_var, value="d")
        radiobutton_a.pack()
        radiobutton_b.pack()
        radiobutton_c.pack()
        radiobutton_d.pack()

def action_next():
    answer=rad_grp_var.get()

    if answer==questions[2][(question_num-1)]:
        answers[quest_count]="correct"
    else:
        answers[quest_count]="incorrect"

    quest_count=quest_count+1

    returnn=0

def action_previous():
    quest_count=quest_count-1
    returnn=1

intro_screen()

root.mainloop()