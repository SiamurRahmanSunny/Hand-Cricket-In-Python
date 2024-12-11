import tkinter as tk
import random

# MAIN WINDOW
root = tk.Tk()
root.title("Hand Cricket")
root.geometry("800x600")
root.resizable(False, False)
root.configure(bg="black")

# BAT AND BALL LOGO
bat_logo = tk.PhotoImage(file="LOGO\\BATBALL_LOGO\\BAT.png")
ball_logo = tk.PhotoImage(file="LOGO\\BATBALL_LOGO\\BALL.png")

# NECESSARY VARIABLES
user_team = ""
ai_team = ""
user_score = 0
ai_score = 0
user_wicket = 0
ai_wicket = 0
target = 0
balles = 0

# RESTART FUNCTION
def click_on_restart():
    global Logo_instance, user_team, ai_team, Toss_instance, Scorecard_instance, AI_Scorecard_instance

    for widget in root.winfo_children():
        widget.destroy()

    # RESETTING THE TEAMS
    user_team = ""
    ai_team = ""

    # RESETTING THE CLASSES
    Toss_instance = None
    Scorecard_instance = None
    AI_Scorecard_instance = None

    # RECREATING THE LOGO
    Logo_instance = Logo()

# RESULT FUNCTION
def reset_after_result(idx, idxs):
    global user_score, user_wicket, ai_score, ai_wicket, balles, target

    # RESETTING THE VARIABLES
    user_score = 0
    user_wicket = 0
    ai_score = 0
    ai_wicket = 0
    balles = 0
    target = 0

    for widget in root.winfo_children():
        widget.destroy()

    if idx == f"{user_team} WIN":
        result1 = tk.Label(root, text=idx, font=("Arial", 30), bg="black", fg="green")
        result1.place(x=300, y=100)

    else:
        result1 = tk.Label(root, text=idx, font=("Arial", 30), bg="black", fg="red")
        result1.place(x=300, y=100)

    if idxs == f"{ai_team} WIN":
        result2 = tk.Label(root, text=idxs, font=("Arial", 30), bg="black", fg="green")
        result2.place(x=300, y=200)

    else:
        result2 = tk.Label(root, text=idxs, font=("Arial", 30), bg="black", fg="red")
        result2.place(x=300, y=200)

    if idx == f"{user_team} MATCH TIE" or idxs == f"{ai_team} MATCH TIE":
        result1 = tk.Label(root, text=idx, font=("Arial", 30), bg="black", fg="blue")
        result1.place(x=300, y=100)
        result2 = tk.Label(root, text=idxs, font=("Arial", 30), bg="black", fg="blue")
        result2.place(x=300, y=200)

    result3 = tk.Button(root, text="RESTART", font=("Arial", 30), bg="black", fg="yellow", borderwidth=0, command=click_on_restart)
    result3.place(x=300, y=300)

# TOSS RESET FUNCTION
def toss_reset():
    for widget in root.winfo_children():
        widget.destroy()
    return

# SCORECARD SHOW FUNCTION
def scorecard_show():
    global Scorecard_instance, AI_Scorecard_instance

    Scorecard_instance = Scorecard()
    AI_Scorecard_instance = AI_Scorecard()

    if user_team == "AFG":
        Scorecard_instance.user_scorecard.config(bg="skyblue")
        Logo_instance.recreate()
        Logo_instance.AFG.place(x=0, y=0)
    elif user_team == "BD":
        Scorecard_instance.user_scorecard.config(bg="red")
        Logo_instance.recreate()
        Logo_instance.BD.place(x=0, y=0)
    elif user_team == "IND":
        Scorecard_instance.user_scorecard.config(bg="blue")
        Logo_instance.recreate()
        Logo_instance.IND.place(x=0, y=0)
    elif user_team == "PAK":
        Scorecard_instance.user_scorecard.config(bg="green")
        Logo_instance.recreate()
        Logo_instance.PAK.place(x=0, y=0)
    elif user_team == "SL":
        Scorecard_instance.user_scorecard.config(bg="yellow")
        Logo_instance.recreate()
        Logo_instance.SL.place(x=0, y=0)

    if ai_team == "AFG":
        AI_Scorecard_instance.ai_scorecard.config(bg="skyblue")
        Logo_instance.recreate()
        Logo_instance.AFG.place(x=700, y=500)
    elif ai_team == "BD":
        AI_Scorecard_instance.ai_scorecard.config(bg="red")
        Logo_instance.recreate()
        Logo_instance.BD.place(x=700, y=500)
    elif ai_team == "IND":
        AI_Scorecard_instance.ai_scorecard.config(bg="blue")
        Logo_instance.recreate()
        Logo_instance.IND.place(x=700, y=500)
    elif ai_team == "PAK":
        AI_Scorecard_instance.ai_scorecard.config(bg="green")
        Logo_instance.recreate()
        Logo_instance.PAK.place(x=700, y=500)
    elif ai_team == "SL":
        AI_Scorecard_instance.ai_scorecard.config(bg="yellow")
        Logo_instance.recreate()
        Logo_instance.SL.place(x=700, y=500)

# UPDATE SCORECARD FUNCTION
def update_scorecard():
    global Scorecard_instance, AI_Scorecard_instance, user_score, user_wicket, ai_score, ai_wicket, balles, target

    Scorecard_instance.user_scorecard.config(text=f"SCORE: {user_score}/{user_wicket} -----> BALL: {balles} -----> TARGET: {target}")
    AI_Scorecard_instance.ai_scorecard.config(text=f"SCORE: {ai_score}/{ai_wicket} -----> BALL: {balles} -----> TARGET: {target}")

# HIT BALL FUNCTION
def hit_ball(bowles):
    global user_score, user_wicket, ai_score, ai_wicket, balles, target, ai_hit, Scorecard_instance, AI_Scorecard_instance, ball_hit_buttons

    ai_hit = random.choice(["1", "2", "3", "4", "5", "6"])

    if target == 0:
        if bowles == ai_hit:
            Scorecard_instance.user_feedback.config(text=f"{bowles}")
            AI_Scorecard_instance.ai_feedback.config(text="YOU ARE OUT")
            ai_wicket += 1
        else:
            ai_score += int(ai_hit)
            Scorecard_instance.user_feedback.config(text=f"{bowles}")
            AI_Scorecard_instance.ai_feedback.config(text=f"GOOD SHOT. {ai_hit} RUNS")

        balles += 1
        update_scorecard()

        if balles == 40 or ai_wicket == 10:
            target = ai_score + 1
            balles = 0
            user_score = 0
            user_wicket = 0
            ai_score = 0
            ai_wicket = 0
            for button in ball_hit_buttons:
                button.destroy()
            bats()
    else:
        if ai_score > target:
            reset_after_result(f"{user_team} LOSE", f"{ai_team} WIN")
        elif balles == 40 or user_wicket == 10:
            if ai_score > target:
                reset_after_result(f"{user_team} LOSE", f"{ai_team} WIN")
            elif user_score == target:
                reset_after_result(f"{user_team} MATCH TIE", f"{ai_team} MATCH TIE")
            else:
                reset_after_result(f"{user_team} WIN", f"{ai_team} LOSE")
        else:
            if bowles == ai_hit:
                Scorecard_instance.user_feedback.config(text=f"{bowles}")
                AI_Scorecard_instance.ai_feedback.config(text="YOU ARE OUT")
                ai_wicket += 1
            else:
                ai_score += int(ai_hit)
                Scorecard_instance.user_feedback.config(text=f"{bowles}")
                AI_Scorecard_instance.ai_feedback.config(text=f"GOOD SHOT. {ai_hit} RUNS")

            balles += 1
            update_scorecard()

# HIT BAT FUNCTION
def hit_bat(hits):
    global user_score, user_wicket, ai_score, ai_wicket, balles, target, ai_hit, Scorecard_instance, AI_Scorecard_instance, hit_buttons

    ai_hit = random.choice(["1", "2", "3", "4", "5", "6"])

    if target == 0:
        if hits == ai_hit:
            Scorecard_instance.user_feedback.config(text="YOU ARE OUT")
            AI_Scorecard_instance.ai_feedback.config(text=f"{ai_hit}")
            user_wicket += 1
        else:
            user_score += int(hits)
            Scorecard_instance.user_feedback.config(text=f"GOOD SHOT. {hits} RUNS")
            AI_Scorecard_instance.ai_feedback.config(text=f"{ai_hit}")

        balles += 1
        update_scorecard()

        if balles == 40 or user_wicket == 10:
            target = user_score + 1
            balles = 0
            user_score = 0
            user_wicket = 0
            ai_score = 0
            ai_wicket = 0
            for button in hit_buttons:
                button.destroy()
            balls()
    else:
        if user_score > target:
            reset_after_result(f"{user_team} WIN", f"{ai_team} LOSE")
        elif balles == 40 or user_wicket == 10:
            if user_score > target:
                reset_after_result(f"{user_team} WIN", f"{ai_team} LOSE")
            elif ai_score == target:
                reset_after_result(f"{user_team} MATCH TIE", f"{ai_team} MATCH TIE")
            else:
                reset_after_result(f"{user_team} LOSE", f"{ai_team} WIN")
        else:
            if hits == ai_hit:
                Scorecard_instance.user_feedback.config(text="YOU ARE OUT")
                AI_Scorecard_instance.ai_feedback.config(text=f"{ai_hit}")
                user_wicket += 1
            else:
                user_score += int(hits)
                Scorecard_instance.user_feedback.config(text=f"GOOD SHOT. {hits} RUNS")
                AI_Scorecard_instance.ai_feedback.config(text=f"{ai_hit}")

            balles += 1
            update_scorecard()

# BAT FUNCTION
def bats():
    global hit_buttons

    toss_reset()
    scorecard_show()
    hit_buttons = []

    Scorecard_instance.user_feedback.config(text="YOU ARE BATTING")
    AI_Scorecard_instance.ai_feedback.config(text="YOU ARE BOWLING")

    for i, hit in enumerate(["1", "2", "3", "4", "5", "6"]):
        hit_button = tk.Button(root, text=hit, bg="orange", fg="black", font=("Arial", 20), borderwidth=0, command=lambda hits=hit: hit_bat(hits))
        hit_button.place(x=100 + i*100, y=250)
        hit_buttons.append(hit_button)

# BALL FUNCTION
def balls():
    global ball_hit_buttons

    toss_reset()
    scorecard_show()
    ball_hit_buttons = []

    Scorecard_instance.user_feedback.config(text="YOU ARE BOWLING")
    AI_Scorecard_instance.ai_feedback.config(text="YOU ARE BATTING")

    for i, bowls in enumerate(["1", "2", "3", "4", "5", "6"]):
        ball_hit_button = tk.Button(root, text=bowls, bg="orange", fg="black", font=("Arial", 20), borderwidth=0, command=lambda bowles=bowls: hit_ball(bowles))
        ball_hit_button.place(x=100 + i * 100, y=250)
        ball_hit_buttons.append(ball_hit_button)

# TOSS FUNCTION
def toss(choice):
    global ai_toss_choice, ai_batball_choice, bat, ball

    ai_toss_choice = random.choice(["HEAD", "TAIL"])

    if choice == ai_toss_choice:
        bat = tk.Button(root, image=bat_logo, bg="black", borderwidth=0, command=bats)
        ball = tk.Button(root, image=ball_logo, bg="black", borderwidth=0, command=balls)
        bat.place(x= 50, y=250)
        ball.place(x=650, y=250)
    else:
        ai_batball_choice = random.choice(["BATTING", "BOWLING"])

        for widget in root.winfo_children():
            widget.destroy()

        result = tk.Label(root, text=f"{ai_team} WON THE TOSS AND CHOOSE TO {ai_batball_choice}", font=("Arial", 20), bg="black", fg="red")
        result.place(x=100, y=250)

        if ai_batball_choice == "BATTING":
            button = tk.Button(root, text="BOWL", font=("Arial", 30), bg="black", fg="white", borderwidth=0, command=balls)
            button.place(x=300, y=350)
        elif ai_batball_choice == "BOWLING":
            button = tk.Button(root, text="BAT", font=("Arial", 30), bg="black", fg="white", borderwidth=0, command=bats)
            button.place(x=300, y=350)

# SCORECARD CLASS
class Scorecard:
    global user_score, user_wicket, ball, target

    def __init__(self):
        self.user_scorecard = tk.Label(root, text=f"SCORE: {user_score}/{user_wicket} -----> BALL: {balles} -----> TARGET: {target}", bg="Green", width=60, height=3, font=("Arial",12))
        self.user_scorecard.place(x=100, y=0)
        self.user_feedback = tk.Label(root, text="FeedBack", bg="black", fg="white", width=25, height=4)
        self.user_feedback.place(x=648, y=0)

    def reset_scorecard(self):
        self.user_scorecard.destroy()
        self.user_feedback.destroy()

# AI_SCORECARD CLASS
class AI_Scorecard:
    global ai_score, ai_wicket, ball, target

    def __init__(self):
        self.ai_scorecard = tk.Label(root, text=f"SCORE: {ai_score}/{ai_wicket} -----> BALL: {balles} -----> TARGET: {target}", bg="Green", width=60, height=3, font=("Arial",12))
        self.ai_scorecard.place(x=150, y=540)
        self.ai_feedback = tk.Label(root, text="FeedBack", bg="black", fg="white", width=25, height=4)
        self.ai_feedback.place(x=0, y=540)

    def reset_scorecard(self):
        self.ai_scorecard.destroy()
        self.ai_feedback.destroy()

# TOSS CLASS
class Toss:
    def __init__(self):
        self.HEAD_LOGO = tk.PhotoImage(file="LOGO\\TOSS_LOGO\\HEAD.png")
        self.TAIL_LOGO = tk.PhotoImage(file="LOGO\\TOSS_LOGO\\TAIL.png")
        self.HEAD = tk.Button(root, image=self.HEAD_LOGO, bg="black", borderwidth=0, command=lambda: toss("HEAD"))
        self.TAIL = tk.Button(root, image=self.TAIL_LOGO, bg="black", borderwidth=0, command=lambda: toss("TAIL"))
        self.TITLE = tk.Label(root, text="CHOOSE HEAD OR TAIL", font=("Arial", 30), bg="black", fg="white")
        self.HEAD.place(x=50, y=250)
        self.TAIL.place(x=650, y=250)
        self.TITLE.place(x=200, y=0)

    def toss_reset(self):
        self.HEAD.destroy()
        self.TAIL.destroy()
        self.TITLE.destroy()

# LOGO CLASS
class Logo:
    def __init__(self):
        # Load the images
        self.AFG_LOGO = tk.PhotoImage(file="LOGO\\TEAM_LOGO\\AFG.png")
        self.BD_LOGO = tk.PhotoImage(file="LOGO\\TEAM_LOGO\\BD.png")
        self.IND_LOGO = tk.PhotoImage(file="LOGO\\TEAM_LOGO\\IND.png")
        self.PAK_LOGO = tk.PhotoImage(file="LOGO\\TEAM_LOGO\\PAK.png")
        self.SL_LOGO = tk.PhotoImage(file="LOGO\\TEAM_LOGO\\SL.png")
        self.AFG = tk.Button(root, image=self.AFG_LOGO, bg="black", borderwidth=0, command=lambda: toss_initialize("AFG"))
        self.BD = tk.Button(root, image=self.BD_LOGO, bg="black", borderwidth=0, command=lambda: toss_initialize("BD"))
        self.IND = tk.Button(root, image=self.IND_LOGO, bg="black", borderwidth=0, command=lambda: toss_initialize("IND"))
        self.PAK = tk.Button(root, image=self.PAK_LOGO, bg="black", borderwidth=0, command=lambda: toss_initialize("PAK"))
        self.SL = tk.Button(root, image=self.SL_LOGO, bg="black", borderwidth=0, command=lambda: toss_initialize("SL"))
        self.TITLE = tk.Label(root, text="CHOOSE YOUR TEAM", font=("Arial", 30), bg="black", fg="white")
        self.EXIT = tk.Button(root, text="EXIT", font=("Arial", 16), bg="orange", fg="white", borderwidth=0, width=66, command=root.destroy)
        self.AFG.place(x=50, y=100)
        self.BD.place(x=650, y=100)
        self.IND.place(x=50, y=300)
        self.PAK.place(x=650, y=300)
        self.SL.place(x=350, y=450)
        self.TITLE.place(x=200, y=0)
        self.EXIT.place(x=0, y=550)

    def reset(self):
        self.AFG.destroy()
        self.BD.destroy()
        self.IND.destroy()
        self.PAK.destroy()
        self.SL.destroy()
        self.TITLE.destroy()

    def recreate(self):
        self.AFG = tk.Button(root, image=self.AFG_LOGO, bg="black", borderwidth=0)
        self.BD = tk.Button(root, image=self.BD_LOGO, bg="black", borderwidth=0)
        self.IND = tk.Button(root, image=self.IND_LOGO, bg="black", borderwidth=0)
        self.PAK = tk.Button(root, image=self.PAK_LOGO, bg="black", borderwidth=0)
        self.SL = tk.Button(root, image=self.SL_LOGO, bg="black", borderwidth=0)

# Initializing Class Logo
Logo_instance = Logo()

# Initially Classes Set To None
Toss_instance = None
Scorecard_instance = None
AI_Scorecard_instance = None

# Initializing Class Toss
def toss_initialize(team):
    global Toss_instance, user_team, ai_team

    if team == "AFG":
        user_team = "AFG"
        ai_team_choice = random.choice(["BD", "IND", "PAK", "SL"])

    elif team == "BD":
        user_team = "BD"
        ai_team_choice = random.choice(["AFG", "IND", "PAK", "SL"])

    elif team == "IND":
        user_team = "IND"
        ai_team_choice = random.choice(["AFG", "BD", "PAK", "SL"])

    elif team == "PAK":
        user_team = "PAK"
        ai_team_choice = random.choice(["AFG", "BD", "IND", "SL"])

    elif team == "SL":
        user_team = "SL"
        ai_team_choice = random.choice(["AFG", "BD", "IND", "PAK"])

    else:
        print("Invalid Team")

    if ai_team_choice == "AFG":
        ai_team = "AFG"

    elif ai_team_choice == "BD":
        ai_team = "BD"

    elif ai_team_choice == "IND":
        ai_team = "IND"

    elif ai_team_choice == "PAK":
        ai_team = "PAK"

    elif ai_team_choice == "SL":
        ai_team = "SL"

    if Toss_instance is None:

        Logo_instance.reset()

        Toss_instance = Toss()

# Initializing Class Scorecard
def scorecard_initialize():

    global Scorecard_instance

    if Scorecard_instance is None:

        Scorecard_instance = Scorecard()

# Initializing Class AI_Scorecard
def ai_scorecard_initialize():

    global AI_Scorecard_instance

    if AI_Scorecard_instance is None:

        AI_Scorecard_instance = AI_Scorecard()

root.mainloop()