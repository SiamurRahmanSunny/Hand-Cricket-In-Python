import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Hand Cricket")
root.geometry("600x600")
root.resizable(False, False)
root.configure(bg="orange")

# VARIABLES
user_name = tk.StringVar()
over = tk.StringVar()
buttons = ["1", "2", "3", "4", "5", "6"]
ai_button_choose = ["1", "2", "3", "4", "5", "6"]
toss = ["HEAD", "TAIL"]
ai_toss_choose_list = ["HEAD", "TAIL"]
choose = ["BAT", "BALL"]
ai_choose_batball = ["BAT", "BALL"]
user_score = 0
ai_score = 0
user_wicket = 0
ai_wicket = 0
target = 0
ovr = 0
# VARIABLES

def reset():
    l4 = tk.Label(main_design_instance.f5, bg="orange", text="Enter Your Name: ", font=("arial", 16))
    l5 = tk.Entry(main_design_instance.f5, bg="grey", textvariable=user_name, font=("arial", 16))
    l6 = tk.Label(main_design_instance.f6, bg="orange", text="Balls (10-20): ", font=("arial", 16))
    l7 = tk.Entry(main_design_instance.f6, bg="grey", textvariable=over, font=("arial", 16))
    l4.pack(side="left")
    l5.pack(side="left")
    l6.pack(side="left")
    l7.pack(side="left")
    main_design_instance.b1.config(text="Submit", state=tk.NORMAL, command=submit_name)

def show_result():
    global user_score, ai_score, user_wicket, ai_wicket, target, ovr
    print("Result")
    for widget in main_design_instance.f5.winfo_children():
        widget.destroy()
    user_score = 0
    ai_score = 0
    user_wicket = 0
    ai_wicket = 0
    target = 0
    ovr = 0
    main_design_instance.b1.config(text="Play Again", state=tk.NORMAL, command=reset)

def start_bowling(indi):
    global user_wicket, user_score, over, ovr, target, ai_score, ai_wicket
    ai_choose = random.choice(ai_button_choose)
    if ovr == int(over.get()) or ai_wicket == 10:
        if target == 0:
            ovr = 0
            target = ai_score
            batting()
            main_design_instance.b1.config(text="Went To Batting")
        else:
            if ai_score > target:
                main_design_instance.l1.config(text=f"{user_name.get()} Lost The Match")
                show_result()
            elif ai_score == target:
                main_design_instance.l1.config(text="Match Draw")
                show_result()
            else:
                main_design_instance.l1.config(text=f"{user_name.get()} Win")
                show_result()
    else:
        if indi == ai_choose:
            ai_wicket += 1
            messagebox.showinfo("You Wicked", "Wicket Down")
            ovr += 1
        else:
            ai_score += int(ai_choose)
            ovr += 1
    main_design_instance.l1.config(text=f"AI Score: {ai_score}/Wicket: {ai_wicket} - Target: {target}")
    if target != 0:
        if ai_score > target:
            main_design_instance.l1.config(text=f"{user_name.get()} Lost The Match")
            show_result()
        elif ovr == int(over.get()) or ai_wicket == 10:
            if ai_score == target:
                main_design_instance.l1.config(text="Match Draw")
                show_result()
            else:
                main_design_instance.l1.config(text=f"{user_name.get()} Win")
                show_result()

def start_batting(indi):
    global user_wicket, user_score, over, ovr, target
    ai_choose = random.choice(ai_button_choose)
    if ovr == int(over.get()) or user_wicket == 10:
        if target == 0:
            ovr = 0
            target = user_score
            bowling()
            main_design_instance.b1.config(text="Went To Bowling")
        else:
            if user_score > target:
                main_design_instance.l1.config(text=f"{user_name.get()} Win")
                show_result()
            elif user_score == target:
                main_design_instance.l1.config(text="Match Draw")
                show_result()
            else:
                main_design_instance.l1.config(text=f"{user_name.get()} Lost The Match")
                show_result()
    else:
        if indi == ai_choose:
            user_wicket += 1
            messagebox.showinfo("You Wicked", "Wicket Down")
            ovr += 1
        else:
            user_score += int(indi)
            ovr += 1
    main_design_instance.l1.config(text=f"{user_name.get()} Score: {user_score}/Wicket: {user_wicket} - Target: {target}")
    if target != 0:
        if user_score > target:
            main_design_instance.l1.config(text=f"{user_name.get()} Win")
            show_result()
        elif ovr == int(over.get()) or ai_wicket == 10:
            if user_score == target:
                main_design_instance.l1.config(text="Match Draw")
                show_result()
            else:
                main_design_instance.l1.config(text=f"{user_name.get()} Lost The Match")
                show_result()

def bowling():
    global over
    for widget in main_design_instance.f5.winfo_children():
        widget.destroy()
    for i, button in enumerate(buttons):
        ball_button = tk.Button(
            main_design_instance.f5,
            text=button,
            bg="blue",
            fg="white",
            font=("Arial", 16),
            borderwidth=0,
            command=lambda idx=button: start_bowling(idx)
        )
        ball_button.pack(pady=5)
    main_design_instance.b1.config(text="", state=tk.DISABLED)
def batting():
    global over
    for widget in main_design_instance.f5.winfo_children():
        widget.destroy()
    for i, button in enumerate(buttons):
        bat_button = tk.Button(
            main_design_instance.f5,
            text=button,
            bg="blue",
            fg="white",
            font=("Arial", 16),
            borderwidth=0,
            command=lambda idx=button: start_batting(idx)
        )
        bat_button.pack(pady=5)
    main_design_instance.b1.config(text="", state=tk.DISABLED)
def check_choose(indix):
    global over
    print(indix)
    if indix == "BAT":
        for widget in main_design_instance.f5.winfo_children():
            widget.destroy()
        main_design_instance.b1.config(text="Start Batting", command=batting)
        main_design_instance.l1.config(text=f"{user_name.get()} Choosed Batting")
    else:
        for widget in main_design_instance.f5.winfo_children():
            widget.destroy()
        main_design_instance.b1.config(text="Start Bowling", command=bowling)
        main_design_instance.l1.config(text=f"{user_name.get()} Choosed Bowling")

def check_toss(index):
    global over
    ai_toss_choose = random.choice(ai_toss_choose_list)
    for widget in main_design_instance.f5.winfo_children():
        widget.destroy()
    if index == ai_toss_choose:
        main_design_instance.b1.config(text="You Won The Toss")
        for i,chc in enumerate(choose):
            choose_button = tk.Button(
                main_design_instance.f5,
                text=chc,
                bg="hot pink",
                font=("arial", 16),
                command=lambda idx=chc: check_choose(idx)
            )
            choose_button.pack(pady=10)
    else:
        main_design_instance.b1.config(text="You Lost The Toss")
        ai_select = random.choice(ai_choose_batball)
        if ai_select == "BAT":
            main_design_instance.b1.config(text="Start Bowling", command=bowling)
            main_design_instance.l1.config(text="AI Choose Batting So You Have To Do Bowling")
        else:
            main_design_instance.b1.config(text="Start Batting", command=batting)
            main_design_instance.l1.config(text="AI Choose Bowling So You Have To Do Batting")

def submit_name():
    global over
    if user_name.get() == "":
        messagebox.showerror("Error", "Please enter a name")
    elif over.get() == "":
        messagebox.showerror("Error", "Please enter Over")
    elif int(over.get()) < 10 or int(over.get()) > 20:
        messagebox.showerror("Error", "Please enter Over between 10 to 20")
    else:
        messagebox.showinfo("Success", "Name and Over submitted")
        main_design_instance.l1.config(text=f"Welcome to Hand Cricket, {user_name.get()}. You Choosed {over.get()} Overs")
        for widget in main_design_instance.f5.winfo_children():
            widget.destroy()
        for widget in main_design_instance.f6.winfo_children():
            widget.destroy()
        for i,tosses in enumerate(toss):
            toss_button = tk.Button(
                main_design_instance.f5,
                text=tosses,
                bg="green",
                font=("Arial", 16),
                borderwidth=0,
                command=lambda idx=tosses: check_toss(idx)
            )
            toss_button.pack(pady=5)

class main_design:
    def __init__(self, master):
        self.f1 = tk.Frame(master, bg="black")
        self.f2 = tk.Frame(master, bg="black")
        self.f3 = tk.Frame(master, bg="black")
        self.f4 = tk.Frame(master, bg="black")
        self.f5 = tk.Frame(master, bg="orange")
        self.f6 = tk.Frame(master, bg="orange")
        self.l1 = tk.Label(self.f1, bg="black", fg="white", text="Welcome to Hand Cricket Programmed By Python", font=("arial", 16))
        self.l2 = tk.Label(self.f2, bg="black", fg="white", text="   ", font=("arial", 16))
        self.l3 = tk.Label(self.f3, bg="black", fg="white", text="   ", font=("arial", 16))
        self.l4 = tk.Label(self.f5, bg="orange", text="Enter Your Name: ", font=("arial", 16))
        self.l5 = tk.Entry(self.f5, bg="grey", textvariable=user_name, font=("arial", 16))
        self.l6 = tk.Label(self.f6, bg="orange", text="Balls (10-20): ", font=("arial", 16))
        self.l7 = tk.Entry(self.f6, bg="grey", textvariable=over, font=("arial", 16))
        self.b1 = tk.Button(self.f4, bg="black", fg="white", text="Submit", font=("arial", 16), borderwidth=0, command=submit_name)
        self.f1.pack(side="top", fill="x")
        self.f2.pack(side="left", fill="y")
        self.f3.pack(side="right", fill="y")
        self.f4.pack(side="bottom", fill="x")
        self.f5.pack(side="top", fill="x")
        self.f6.pack(side="top", fill="x")
        self.l1.pack(side="top", fill="x")
        self.l2.pack(side="left", fill="y")
        self.l3.pack(side="right", fill="y")
        self.l4.pack(side="left")
        self.l5.pack(side="left")
        self.l6.pack(side="left")
        self.l7.pack(side="left", padx=52)
        self.b1.pack(side="bottom", fill="x")

main_design_instance = main_design(root)

root.mainloop()