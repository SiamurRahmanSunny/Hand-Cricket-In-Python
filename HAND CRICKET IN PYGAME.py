# VERSION 1.0

# LINES OF CODE = 1114

# THIS IS THE GAME DETAILS

"""

        HAND CRICKET GAME IN PYGAME

        AT FIRST USER WILL SELECT THE TEAM

        THEN USER WILL SELECT THE TOSS

        THEN USER WILL SELECT BAT OR BALL IF HE WIN THE TOSS OTHERWISE AI WILL CHOOSE BAT OR BALL RANDOMLY

        THEN USER WILL BAT OR BOWL ACCORDING TO THE CHOICE

        THEN MATCH WILL START

        IF USER SCORE IS GREATER THAN AI SCORE THEN USER WILL WIN THE MATCH

        IF AI SCORE IS GREATER THAN USER SCORE THEN AI WILL WIN THE MATCH

        IF USER SCORE IS EQUAL TO AI SCORE THEN MATCH WILL BE DRAW

        AFTER THAT PLAYER CAN PLAY AGAIN BY CLICKING ON PLAY AGAIN BUTTON

        IF PLAYER WANT TO CLOSE THE GAME THEN HE CAN CLOSE THE GAME BY CLICKING ON CLOSE BUTTON

        AT THE BOTTOM OF THE MAIN SCREEN THERE IS A BUTTON NAMED OVER

        IF PLAYER CLICK ON OVER BUTTON THEN HE CAN SEE THE OVERS AND BALLS

        IF PLAYER CLICK ON 5 OVER THEN MATCH WILL BE PLAYED AT 30 BALLS

        IF PLAYER CLICK ON 10 OVER THEN MATCH WILL BE PLAYED AT 60 BALLS

        IF PLAYER CLICK ON 20 OVER THEN MATCH WILL BE PLAYED AT 120 BALLS

"""


# START OF THE PROGRAM

# IMPORTING NECESSARY LIBRARIES

import pygame as srs # IMPORTED PYGAME LIBRARY AS srs FOR FAST TYPING

import random as rd # IMPORTED RANDOM LIBRARY AS rd FOR FAST TYPING

# INITIALIZING PYGAME

srs.init() # TYPPED AS srs BECAUSE PYGAME LIBRARY IS IMPORTED AS srs

# SCREEN SETTINGS

screen = srs.display.set_mode((800, 600)) # SCREEN WIDTH = 800, SCREEN HEIGHT = 600

srs.display.set_caption("HAND CRICKET") # TITLE OF THE SCREEN

# IMPORTED FONT FOR FORMATTING TEXT

font = srs.font.Font(None, 36) # FONT SIZE = 36. Only Font Size is given because Font Style is None

# INITIALIZING COLORS FOR EASY ACCESS

WHITE = (255, 255, 255)     # -----> WHITE COLOR

BLACK = (0, 0, 0)           # -----> BLACK COLOR

RED = (255, 0, 0)           # -----> RED COLOR

GREEN = (0, 255, 0)         # -----> GREEN COLOR

BLUE = (0, 0, 255)          # -----> BLUE COLOR

HOT_PINK = (255, 105, 180)  # -----> HOT PINK COLOR

CYAN = (0, 255, 255)        # -----> CYAN COLOR

YELLOW = (255, 255, 0)      # -----> YELLOW COLOR

ORANGE = (255, 165, 0)      # -----> ORANGE COLOR

# INITIALIZING TEAM LOGOS

AFG = srs.image.load("LOGO\\TEAM_LOGO\\AFG.png")   # -----> AFGHANISTAN TEAM LOGO

BAN = srs.image.load("LOGO\\TEAM_LOGO\\BD.png")    # -----> BANGLADESH TEAM LOGO

IND = srs.image.load("LOGO\\TEAM_LOGO\\IND.png")   # -----> INDIA TEAM LOGO

PAK = srs.image.load("LOGO\\TEAM_LOGO\\PAK.png")   # -----> PAKISTAN TEAM LOGO

SRI = srs.image.load("LOGO\\TEAM_LOGO\\SL.png")    # -----> SRI LANKA TEAM LOGO

# INITIALIZING BAT AND BALL LOGOS

BAT = srs.image.load("LOGO\\BATBALL_LOGO\\BAT.png")   # -----> BAT LOGO

BALL = srs.image.load("LOGO\\BATBALL_LOGO\\BALL.png") # -----> BALL LOGO

# INITIALIZING TOSS LOGOS

HEAD = srs.image.load("LOGO\\TOSS_LOGO\\HEAD.png")    # -----> HEAD LOGO

TAIL = srs.image.load("LOGO\\TOSS_LOGO\\TAIL.png")    # -----> TAIL LOGO

# INITIALIZING NECESSARY VARIABLES. THESE WILL BE USED IN THE PROGRAM LATER

# THESE ARE SCREEN FLAGS. THESE FLAGS WILL BE USED TO RUN THE SCREENS OR CLOSE THE SCREENS

Main_screen_running = True                  # MAIN SCREEN FLAG INITIALLY TRUE

Toss_screen_running = False                 # TOSS SCREEN FLAG INITIALLY FALSE

Bat_Ball_Choice_screen_running = False      # BAT BALL CHOICE SCREEN FLAG INITIALLY FALSE

Bat_screen_running = False                  # BAT SCREEN FLAG INITIALLY FALSE

Ball_screen_running = False                 # BALL SCREEN FLAG INITIALLY FALSE

Result_screen_running = False               # RESULT SCREEN FLAG INITIALLY FALSE

Over_screen_running = False                 # OVER SCREEN FLAG INITIALLY FALSE

user_toss_win = False # THIS WILL BE USED TO CHECK WHETHER USER WON THE TOSS OR NOT. INITIALLY MAKE IT FALSE

# THESE VARIABLES WILL BE USED TO STORE THE FEEDBACKS, TEAMS, ETC

# STRING VARIABLES ARE INITIALIZED AS EMPTY STRINGS

user_team = ""              # USER TEAM

ai_team = ""                # AI TEAM

ai_bat_ball_choice = ""     # AI BAT OR BALL CHOICE

user_feedback = ""          # USER FEEDBACK --> LIKE 1, 2, 3, 4, 5, 6, OUT

ai_feedback = ""            # AI FEEDBACK   --> LIKE 1, 2, 3, 4, 5, 6, OUT

result_feedback = ""        # RESULT FEEDBACK --> LIKE USER TEAM WON THE MATCH, AI TEAM WON THE MATCH, MATCH DRAW

# THESE VARIABLES WILL BE USED TO STORE THE SCORES, WICKETS, BALLS, TARGET, OVERS, ETC

# INTEGER VARIABLES ARE INITIALIZED AS 0

user_score = 0              # USER SCORE

ai_score = 0                # AI SCORE

user_wicket = 0             # USER WICKET

ai_wicket = 0               # AI WICKET

balles = 0                  # IT IS BALL COUNT IN VARIABLE NAMED BALLES CAUSED BALL IS USED AS A FUNCTION

target = 0                  # TARGET SCORE

overes = 30             # IT IS OVER COUNT CONVERTED TO BALLS IN VARIABLE NAMED OVERES CAUSE OVER IS USED AS A FUNCTION


# DRAW TEAM LOGOS
def draw_team_logo():
    screen.blit(AFG, (0, 50))       # AFGHANISTAN TEAM LOGO ---> WIDTH = 100, HEIGHT = 100  (0, 50) --> (X, Y)

    screen.blit(BAN, (700, 50))     # BANGLADESH TEAM LOGO  ---> WIDTH = 100, HEIGHT = 100  (700, 50) --> (X, Y)

    screen.blit(IND, (0, 200))      # INDIA TEAM LOGO       ---> WIDTH = 100, HEIGHT = 100  (0, 200) --> (X, Y)

    screen.blit(PAK, (700, 200))    # PAKISTAN TEAM LOGO    ---> WIDTH = 100, HEIGHT = 100  (700, 200) --> (X, Y)

    screen.blit(SRI, (350, 350))    # SRI LANKA TEAM LOGO   ---> WIDTH = 100, HEIGHT = 100  (350, 350) --> (X, Y)


# DRAW TOSS LOGOS
def draw_toss_logo():
    screen.blit(HEAD, (0, 250))     # HEAD LOGO ---> WIDTH = 100, HEIGHT = 100  (0, 250) --> (X, Y)

    screen.blit(TAIL, (700, 250))   # TAIL LOGO ---> WIDTH = 100, HEIGHT = 100  (700, 250) --> (X, Y)


# DRAW BAT AND BALL LOGOS
def draw_bat_ball_logo():
    screen.blit(BAT, (0, 250))      # BAT LOGO ---> WIDTH = 100, HEIGHT = 100  (0, 250) --> (X, Y)

    screen.blit(BALL, (650, 250))   # BALL LOGO ---> WIDTH = 100, HEIGHT = 100  (650, 250) --> (X, Y)


# SCORECARD FUNCTION
def draw_scorecard():
    # GLOBAL VARIABLES ARE USED TO ACCESS THE VARIABLES OUTSIDE THE FUNCTION

    global user_team, ai_team, user_score, ai_score, user_wicket, ai_wicket, balles, target, user_feedback, ai_feedback

    # USER TEAM LOGO
    if user_team == "AFG": # IF USER TEAM IS AFGHANISTAN THEN SCORECARD BACKGROUND WILL BE CYAN
        screen.blit(AFG, (0, 0))                            # AFGHANISTAN TEAM LOGO

        srs.draw.rect(screen, CYAN, (150, 0, 500, 100))     # SCORECARD BACKGROUND

        user_title = font.render(                               # USER TITLE
            f"SCORE: {user_score}/{user_wicket} | BALL: {balles} | TARGET: {target}",
            True,                                       # ANTIALIASING
            BLACK,                                              # TEXT COLOR
        )

        screen.blit(user_title, (200, 30))                  # USER TITLE POSITION

    elif user_team == "BAN": # IF USER TEAM IS BANGLADESH THEN SCORECARD BACKGROUND WILL BE RED
        screen.blit(BAN, (0, 0))                            # BANGLADESH TEAM LOGO

        srs.draw.rect(screen, RED, (150, 0, 500, 100))      # SCORECARD BACKGROUND

        user_title = font.render(                               # USER TITLE
            f"SCORE: {user_score}/{user_wicket} | BALL: {balles} | TARGET: {target}",
            True,                                       # ANTIALIASING
            BLACK                                               # TEXT COLOR
        )

        screen.blit(user_title, (200, 30))

    elif user_team == "IND": # IF USER TEAM IS INDIA THEN SCORECARD BACKGROUND WILL BE BLUE
        screen.blit(IND, (0, 0))

        srs.draw.rect(screen, BLUE, (150, 0, 500, 100))

        user_title = font.render(
            f"SCORE: {user_score}/{user_wicket} | BALL: {balles} | TARGET: {target}",
            True,
            BLACK
        )

        screen.blit(user_title, (200, 30))

    elif user_team == "PAK": # IF USER TEAM IS PAKISTAN THEN SCORECARD BACKGROUND WILL BE GREEN
        screen.blit(PAK, (0, 0))

        srs.draw.rect(screen, GREEN, (150, 0, 500, 100))

        user_title = font.render(
            f"SCORE: {user_score}/{user_wicket} | BALL: {balles} | TARGET: {target}",
            True,
            BLACK
        )

        screen.blit(user_title, (200, 30))

    elif user_team == "SRI": # IF USER TEAM IS SRI LANKA THEN SCORECARD BACKGROUND WILL BE YELLOW
        screen.blit(SRI, (0, 0))

        srs.draw.rect(screen, YELLOW, (150, 0, 500, 100))

        user_title = font.render(
            f"SCORE: {user_score}/{user_wicket} | BALL: {balles} | TARGET: {target}",
            True,
            BLACK
        )

        screen.blit(user_title, (200, 30))

    # AI TEAM LOGO
    if ai_team == "AFG": # IF AI TEAM IS AFGHANISTAN THEN SCORECARD BACKGROUND WILL BE CYAN
        screen.blit(AFG, (700, 500))

        srs.draw.rect(screen, CYAN, (150, 500, 500, 100))

        user_title = font.render(
            f"SCORE: {ai_score}/{ai_wicket} | BALL: {balles} | TARGET: {target}",
            True,
            BLACK
        )

        screen.blit(user_title, (200, 540))
    elif ai_team == "BAN": # IF AI TEAM IS BANGLADESH THEN SCORECARD BACKGROUND WILL BE RED
        screen.blit(BAN, (700, 500))

        srs.draw.rect(screen, RED, (150, 500, 500, 100))

        user_title = font.render(
            f"SCORE: {ai_score}/{ai_wicket} | BALL: {balles} | TARGET: {target}",
            True,
            BLACK
        )

        screen.blit(user_title, (200, 540))
    elif ai_team == "IND": # IF AI TEAM IS INDIA THEN SCORECARD BACKGROUND WILL BE BLUE
        screen.blit(IND, (700, 500))

        srs.draw.rect(screen, BLUE, (150, 500, 500, 100))

        user_title = font.render(
            f"SCORE: {ai_score}/{ai_wicket} | BALL: {balles} | TARGET: {target}",
            True,
            BLACK
        )

        screen.blit(user_title, (200, 540))
    elif ai_team == "PAK": # IF AI TEAM IS PAKISTAN THEN SCORECARD BACKGROUND WILL BE GREEN
        screen.blit(PAK, (700, 500))

        srs.draw.rect(screen, GREEN, (150, 500, 500, 100))

        user_title = font.render(
            f"SCORE: {ai_score}/{ai_wicket} | BALL: {balles} | TARGET: {target}",
            True,
            BLACK
        )

        screen.blit(user_title, (200, 540))
    elif ai_team == "SRI": # IF AI TEAM IS SRI LANKA THEN SCORECARD BACKGROUND WILL BE YELLOW
        screen.blit(SRI, (700, 500))

        srs.draw.rect(screen, YELLOW, (150, 500, 500, 100))

        user_title = font.render(
            f"SCORE: {ai_score}/{ai_wicket} | BALL: {balles} | TARGET: {target}",
            True,
            BLACK
        )

        screen.blit(user_title, (200, 540))

    # USER AND AI FEEDBACK

    srs.draw.circle(screen, ORANGE, (720, 60), 55)              # USER FEEDBACK CIRCLE

    user_feedback_surface = font.render(user_feedback, True, WHITE)  # USER FEEDBACK

    screen.blit(user_feedback_surface, (685, 50))                       # USER FEEDBACK SURFACE

    srs.draw.circle(screen, ORANGE, (80, 540), 55)               # AI FEEDBACK CIRCLE

    ai_feedback_surface = font.render(ai_feedback, True, WHITE)       # AI FEEDBACK

    screen.blit(ai_feedback_surface, (45, 530))                          # AI FEEDBACK SURFACE


# RESULT SCREEN
def Result_Screen():
    # GLOBAL VARIABLES ARE USED TO ACCESS THE VARIABLES OUTSIDE THE FUNCTION
    global Result_screen_running, overes, result_feedback, Toss_screen_running, Bat_Ball_Choice_screen_running, \
        Bat_screen_running, Ball_screen_running, user_score, ai_score, user_wicket, ai_wicket, balles, target, \
        user_toss_win, user_team, ai_team, user_feedback, ai_feedback, ai_bat_ball_choice

    # THIS FUNCTION WILL RUN UNTIL THE RESULT SCREEN IS RUNNING
    while Result_screen_running:
        screen.fill(HOT_PINK) # SCREEN BACKGROUND COLOR IS HOT PINK

        title_surface = font.render(result_feedback, True, BLACK) # RESULT FEEDBACK

        screen.blit(title_surface, (300, 200)) # WIDTH = 147 , HEIGHT = 24

        play_again = font.render("PLAY AGAIN", True, RED) # PLAY AGAIN BUTTON

        screen.blit(play_again, (300, 300)) # WIDTH = 147 , HEIGHT = 24

        for event in srs.event.get():                       # EVENT LOOP
            if event.type == srs.QUIT:                      # IF QUIT BUTTON IS PRESSED
                Result_screen_running = False               # RESULT SCREEN WILL BE CLOSED

            if event.type == srs.MOUSEBUTTONDOWN:           # IF MOUSE BUTTON IS PRESSED
                x, y = srs.mouse.get_pos()                  # GET THE POSITION OF MOUSE

                if 300 <= x <= 447 and 300 <= y <= 324:     # IF PLAY AGAIN BUTTON IS PRESSED
                    user_toss_win = False                   # USER TOSS WIN WILL BE FALSE

                    user_team = ""                          # USER TEAM WILL BE EMPTY

                    ai_team = ""                            # AI TEAM WILL BE EMPTY

                    ai_bat_ball_choice = ""                 # AI BAT BALL CHOICE WILL BE EMPTY

                    user_feedback = ""                      # USER FEEDBACK WILL BE EMPTY

                    ai_feedback = ""                        # AI FEEDBACK WILL BE EMPTY

                    result_feedback = ""                    # RESULT FEEDBACK WILL BE EMPTY

                    user_score = 0                          # USER SCORE WILL BE 0

                    ai_score = 0                            # AI SCORE WILL BE 0

                    user_wicket = 0                         # USER WICKET WILL BE 0

                    ai_wicket = 0                           # AI WICKET WILL BE 0

                    balles = 0                              # BALL WILL BE 0

                    target = 0                              # TARGET WILL BE 0

                    overes = 30                             # OVER WILL BE 30

                    Result_screen_running = False           # RESULT SCREEN WILL BE CLOSED

                    Toss_screen_running = False             # TOSS SCREEN WILL BE CLOSED

                    Bat_Ball_Choice_screen_running = False  # BAT BALL CHOICE SCREEN WILL BE CLOSED

                    Bat_screen_running = False              # BAT SCREEN WILL BE CLOSED

                    Ball_screen_running = False             # BALL SCREEN WILL BE CLOSED

                    Result_screen_running = False           # RESULT SCREEN WILL BE CLOSED

        srs.display.update()                                # UPDATE THE SCREEN


# BATTING LOGIC

def Batting(user_choice, ai_choice):
    # GLOBAL VARIABLES ARE USED TO ACCESS THE VARIABLES OUTSIDE THE FUNCTION
    global user_score, overes, ai_score, user_wicket, ai_wicket, balles, target, user_feedback, ai_feedback, \
        Bat_screen_running, Ball_screen_running, Result_screen_running, result_feedback

    if target == 0:                                          # IF TARGET IS 0 THEN USER WILL BAT
        if user_choice == ai_choice:           # IF USER CHOICE IS EQUAL TO AI CHOICE THEN AI WICKET WILL BE INCREASED
            user_wicket += 1                                 # USER WICKET WILL BE INCREASED

            user_feedback = "OUT!"                           # USER FEEDBACK WILL BE OUT!

            ai_feedback = "BOWLED!"                          # AI FEEDBACK WILL BE BOWLED!

        else:                              # IF USER CHOICE IS NOT EQUAL TO AI CHOICE THEN USER SCORE WILL BE INCREASED
            user_score += user_choice                        # USER SCORE WILL BE INCREASED

            user_feedback = f"{user_choice}"                 # USER FEEDBACK WILL BE USER CHOICE

            ai_feedback = f"{ai_choice}"                     # AI FEEDBACK WILL BE AI CHOICE

        balles += 1                                          # BALL WILL BE INCREASED

        if balles == overes or user_wicket == 10:     # IF BALLS ARE EQUAL TO OVERES OR USER WICKET IS EQUAL TO 10
            target = user_score + 1                          # TARGET WILL BE USER SCORE + 1

            balles = 0                                       # BALLS WILL BE 0

            user_score = 0                                   # USER SCORE WILL BE 0

            user_wicket = 0                                  # USER WICKET WILL BE 0

            ai_score = 0                                     # AI SCORE WILL BE 0

            ai_wicket = 0                                    # AI WICKET WILL BE 0

            user_feedback = ""                               # USER FEEDBACK WILL BE EMPTY

            ai_feedback = ""                                 # AI FEEDBACK WILL BE EMPTY

            Bat_screen_running = False                       # BAT SCREEN WILL BE CLOSED

            Ball_screen_running = True                       # BALL SCREEN WILL BE OPENED

            Ball_Screen()                                    # BALL SCREEN FUNCTION WILL BE CALLED

    else:                                                    # IF TARGET IS NOT 0 THEN AI WILL BAT

        if user_score >= target:                             # IF USER SCORE IS GREATER THAN OR EQUAL TO TARGET
            Bat_screen_running = False                       # BAT SCREEN WILL BE CLOSED

            Result_screen_running = True                     # RESULT SCREEN WILL BE OPENED

            result_feedback = f"{user_team} WON THE MATCH"   # RESULT FEEDBACK WILL BE USER TEAM WON THE MATCH

            Result_Screen()                                  # RESULT SCREEN FUNCTION WILL BE CALLED

        else:                                                # IF USER SCORE IS NOT GREATER THAN OR EQUAL TO TARGET

            if balles == overes or user_wicket == 10:    # IF BALLS ARE EQUAL TO OVERES OR USER WICKET IS EQUAL TO 10

                if user_score >= target:                     # IF USER SCORE IS GREATER THAN OR EQUAL TO TARGET
                    Bat_screen_running = False               # BAT SCREEN WILL BE CLOSED

                    Result_screen_running = True             # RESULT SCREEN WILL BE OPENED

                    result_feedback = f"{user_team} WON THE MATCH" # RESULT FEEDBACK WILL BE USER TEAM WON THE MATCH

                    Result_Screen()                          # RESULT SCREEN FUNCTION WILL BE CALLED

                elif user_score == target - 1:               # IF USER SCORE IS EQUAL TO TARGET - 1
                    Bat_screen_running = False               # BAT SCREEN WILL BE CLOSED

                    Result_screen_running = True             # RESULT SCREEN WILL BE OPENED

                    result_feedback = "SO CLOSE! MATCH DRAW" # RESULT FEEDBACK WILL BE SO CLOSE! MATCH DRAW

                    Result_Screen()                          # RESULT SCREEN FUNCTION WILL BE CALLED

                else:                                        # IF USER SCORE IS NOT GREATER THAN OR EQUAL TO TARGET
                    Bat_screen_running = False               # BAT SCREEN WILL BE CLOSED

                    Result_screen_running = True             # RESULT SCREEN WILL BE OPENED

                    result_feedback = f"{user_team} LOST THE MATCH" # RESULT FEEDBACK WILL BE USER TEAM LOST THE MATCH

                    Result_Screen()                          # RESULT SCREEN FUNCTION WILL BE CALLED

            else:                             # IF BALLS ARE NOT EQUAL TO OVERES OR USER WICKET IS NOT EQUAL TO 10

                if user_choice == ai_choice:  # IF USER CHOICE IS EQUAL TO AI CHOICE THEN USER WICKET WILL BE INCREASED
                    user_wicket += 1                         # USER WICKET WILL BE INCREASED

                    user_feedback = "OUT!"                   # USER FEEDBACK WILL BE OUT!

                    ai_feedback = "BOWLED!"                  # AI FEEDBACK WILL BE BOWLED!

                else:                      # IF USER CHOICE IS NOT EQUAL TO AI CHOICE THEN USER SCORE WILL BE INCREASED
                    user_score += user_choice                # USER SCORE WILL BE INCREASED

                    user_feedback = f"{user_choice}"         # USER FEEDBACK WILL BE USER CHOICE

                    ai_feedback = f"{ai_choice}"             # AI FEEDBACK WILL BE AI CHOICE

                balles += 1                                  # BALL WILL BE INCREASED


# BOWLING LOGIC

def Bowling(user_choice, ai_choice):
    # GLOBAL VARIABLES ARE USED TO ACCESS THE VARIABLES OUTSIDE THE FUNCTION
    global user_score, overes, ai_score, user_wicket, ai_wicket, balles, target, user_feedback, ai_feedback, \
        Bat_screen_running, Ball_screen_running, Result_screen_running, result_feedback

    if target == 0:                                          # IF TARGET IS 0 THEN AI WILL BAT

        if user_choice == ai_choice:            # IF USER CHOICE IS EQUAL TO AI CHOICE THEN AI WICKET WILL BE INCREASED
            ai_wicket += 1                                   # AI WICKET WILL BE INCREASED

            ai_feedback = "OUT!"                             # AI FEEDBACK WILL BE OUT!

            user_feedback = "BOWLED!"                        # USER FEEDBACK WILL BE BOWLED!

        else:                                # IF USER CHOICE IS NOT EQUAL TO AI CHOICE THEN AI SCORE WILL BE INCREASED
            ai_score += ai_choice                            # AI SCORE WILL BE INCREASED

            ai_feedback = f"{ai_choice}"                     # AI FEEDBACK WILL BE AI CHOICE

            user_feedback = f"{user_choice}"                 # USER FEEDBACK WILL BE USER CHOICE

        balles += 1                                          # BALL WILL BE INCREASED

        if balles == overes or ai_wicket == 10:              # IF BALLS ARE EQUAL TO OVERES OR AI WICKET IS EQUAL TO 10
            target = ai_score + 1                            # TARGET WILL BE AI SCORE + 1

            balles = 0                                       # BALLS WILL BE 0

            user_score = 0                                   # USER SCORE WILL BE 0

            user_wicket = 0                                  # USER WICKET WILL BE 0

            ai_score = 0                                     # AI SCORE WILL BE 0

            ai_wicket = 0                                    # AI WICKET WILL BE 0

            user_feedback = ""                               # USER FEEDBACK WILL BE EMPTY

            ai_feedback = ""                                 # AI FEEDBACK WILL BE EMPTY

            Bat_screen_running = True                        # BAT SCREEN WILL BE OPENED

            Ball_screen_running = False                      # BALL SCREEN WILL BE CLOSED

            Bat_Screen()                                     # BAT SCREEN FUNCTION WILL BE CALLED

    else:                                                    # IF TARGET IS NOT 0 THEN USER WILL BOWL

        if ai_score >= target:                               # IF AI SCORE IS GREATER THAN OR EQUAL TO TARGET
            Ball_screen_running = False                      # BALL SCREEN WILL BE CLOSED

            Result_screen_running = True                     # RESULT SCREEN WILL BE OPENED

            result_feedback = f"{user_team} LOST THE MATCH"  # RESULT FEEDBACK WILL BE USER TEAM LOST THE MATCH

            Result_Screen()                                  # RESULT SCREEN FUNCTION WILL BE CALLED

        else:                                                # IF AI SCORE IS NOT GREATER THAN OR EQUAL TO TARGET

            if balles == overes or ai_wicket == 10:        # IF BALLS ARE EQUAL TO OVERES OR AI WICKET IS EQUAL TO 10

                if ai_score >= target:                       # IF AI SCORE IS GREATER THAN OR EQUAL TO TARGET
                    Ball_screen_running = False              # BALL SCREEN WILL BE CLOSED

                    Result_screen_running = True             # RESULT SCREEN WILL BE OPENED

                    result_feedback = f"{user_team} LOST THE MATCH" # RESULT FEEDBACK WILL BE USER TEAM LOST THE MATCH

                    Result_Screen()                          # RESULT SCREEN FUNCTION WILL BE CALLED

                elif ai_score == target - 1:                 # IF AI SCORE IS EQUAL TO TARGET - 1
                    Ball_screen_running = False              # BALL SCREEN WILL BE CLOSED

                    Result_screen_running = True             # RESULT SCREEN WILL BE OPENED

                    result_feedback = "SO CLOSE! MATCH DRAW" # RESULT FEEDBACK WILL BE SO CLOSE! MATCH DRAW

                    Result_Screen()                          # RESULT SCREEN FUNCTION WILL BE CALLED

                else:                                        # IF AI SCORE IS NOT GREATER THAN OR EQUAL TO TARGET
                    Ball_screen_running = False              # BALL SCREEN WILL BE CLOSED

                    Result_screen_running = True             # RESULT SCREEN WILL BE OPENED

                    result_feedback = f"{user_team} WON THE MATCH" # RESULT FEEDBACK WILL BE USER TEAM WON THE MATCH

                    Result_Screen()                          # RESULT SCREEN FUNCTION WILL BE CALLED

            else:                                  # IF BALLS ARE NOT EQUAL TO OVERES OR AI WICKET IS NOT EQUAL TO 10

                if user_choice == ai_choice:  # IF USER CHOICE IS EQUAL TO AI CHOICE THEN AI WICKET WILL BE INCREASED
                    ai_wicket += 1                           # AI WICKET WILL BE INCREASED

                    ai_feedback = "OUT!"                     # AI FEEDBACK WILL BE OUT!

                    user_feedback = "BOWLED!"                # USER FEEDBACK WILL BE BOWLED!

                else:                       # IF USER CHOICE IS NOT EQUAL TO AI CHOICE THEN AI SCORE WILL BE INCREASED
                    ai_score += ai_choice                    # AI SCORE WILL BE INCREASED

                    ai_feedback = f"{ai_choice}"             # AI FEEDBACK WILL BE AI CHOICE

                    user_feedback = f"{user_choice}"         # USER FEEDBACK WILL BE USER CHOICE

                balles += 1                                  # BALL WILL BE INCREASED


# BAT SCREEN

def Bat_Screen():
    global Bat_screen_running  # GLOBAL VARIABLE IS USED TO ACCESS THE VARIABLE OUTSIDE THE FUNCTION

    while Bat_screen_running: # THIS FUNCTION WILL RUN UNTIL THE BAT SCREEN IS RUNNING
        screen.fill(BLACK)    # SCREEN BACKGROUND COLOR IS BLACK


        draw_scorecard()      # DRAW SCORECARD FUNCTION

        # DRAW BUTTONS TO HIT
        srs.draw.circle(screen, RED, (400, 200), 50)            # RED BUTTON

        srs.draw.circle(screen, GREEN, (200, 200), 50)          # GREEN BUTTON

        srs.draw.circle(screen, BLUE, (600, 200), 50)           # BLUE BUTTON

        srs.draw.circle(screen, HOT_PINK, (300, 300), 50)       # HOT PINK BUTTON

        srs.draw.circle(screen, CYAN, (500, 300), 50)           # CYAN BUTTON

        srs.draw.circle(screen, ORANGE, (400, 400), 50)         # ORANGE BUTTON


        # BUTTONS FONT

        RED_FONT = font.render("2", True, WHITE)                # RED BUTTON TEXTED AS 2

        screen.blit(RED_FONT, (390, 190))                               # RED BUTTON TEXT POSITION

        GREEN_FONT = font.render("1", True, WHITE)              # GREEN BUTTON TEXTED AS 1

        screen.blit(GREEN_FONT, (190, 190))                             # GREEN BUTTON TEXT POSITION

        BLUE_FONT = font.render("3", True, WHITE)               # BLUE BUTTON TEXTED AS 3

        screen.blit(BLUE_FONT, (590, 190))                              # BLUE BUTTON TEXT POSITION

        HOT_PINK_FONT = font.render("4", True, WHITE)           # HOT PINK BUTTON TEXTED AS 4

        screen.blit(HOT_PINK_FONT, (290, 290))                          # HOT PINK BUTTON TEXT POSITION

        CYAN_FONT = font.render("5", True, WHITE)               # CYAN BUTTON TEXTED AS 5

        screen.blit(CYAN_FONT, (490, 290))                              # CYAN BUTTON TEXT POSITION

        ORANGE_FONT = font.render("6", True, WHITE)             # ORANGE BUTTON TEXTED AS 6

        screen.blit(ORANGE_FONT, (390, 390))                            # ORANGE BUTTON TEXT POSITION

        # EVENT LOOP
        for event in srs.event.get():
            if event.type == srs.QUIT:                                      # IF QUIT BUTTON IS PRESSED
                Bat_screen_running = False                                  # BAT SCREEN WILL BE CLOSED

            if event.type == srs.MOUSEBUTTONDOWN:                           # IF MOUSE BUTTON IS PRESSED
                x, y = srs.mouse.get_pos()                                  # GET THE POSITION OF MOUSE

                if 150 <= x <= 250 and 150 <= y <= 250:                     # IF RED BUTTON IS PRESSED
                    Batting(1, rd.choice([1, 2, 3, 4, 5, 6]))    # BAT FUNCTION WILL BE CALLED

                if 350 <= x <= 450 and 150 <= y <= 250:                     # IF GREEN BUTTON IS PRESSED
                    Batting(2, rd.choice([1, 2, 3, 4, 5, 6]))    # BAT FUNCTION WILL BE CALLED

                if 550 <= x <= 650 and 150 <= y <= 250:                     # IF BLUE BUTTON IS PRESSED
                    Batting(3, rd.choice([1, 2, 3, 4, 5, 6]))    # BAT FUNCTION WILL BE CALLED

                if 250 <= x <= 350 and 250 <= y <= 350:                     # IF HOT PINK BUTTON IS PRESSED
                    Batting(4, rd.choice([1, 2, 3, 4, 5, 6]))    # BAT FUNCTION WILL BE CALLED

                if 450 <= x <= 550 and 250 <= y <= 350:                     # IF CYAN BUTTON IS PRESSED
                    Batting(5, rd.choice([1, 2, 3, 4, 5, 6]))    # BAT FUNCTION WILL BE CALLED

                if 350 <= x <= 450 and 350 <= y <= 450:                     # IF ORANGE BUTTON IS PRESSED
                    Batting(6, rd.choice([1, 2, 3, 4, 5, 6]))    # BAT FUNCTION WILL BE CALLED

        srs.display.update()                                                # UPDATE THE SCREEN


# BALL SCREEN

def Ball_Screen():
    # GLOBAL VARIABLES ARE USED TO ACCESS THE VARIABLES OUTSIDE THE FUNCTION
    global Ball_screen_running

    while Ball_screen_running:                               # THIS FUNCTION WILL RUN UNTIL THE BALL SCREEN IS RUNNING
        screen.fill(BLACK)                                      # SCREEN BACKGROUND COLOR IS BLACK


        draw_scorecard()                                        # DRAW SCORECARD FUNCTION

        # DRAW BUTTONS TO BOWL

        srs.draw.circle(screen, RED, (400, 200), 50)            # RED BUTTON

        srs.draw.circle(screen, GREEN, (200, 200), 50)          # GREEN BUTTON

        srs.draw.circle(screen, BLUE, (600, 200), 50)           # BLUE BUTTON

        srs.draw.circle(screen, HOT_PINK, (300, 300), 50)       # HOT PINK BUTTON

        srs.draw.circle(screen, CYAN, (500, 300), 50)           # CYAN BUTTON

        srs.draw.circle(screen, ORANGE, (400, 400), 50)         # ORANGE BUTTON


        # BUTTONS FONT

        RED_FONT = font.render("2", True, WHITE)                # RED BUTTON TEXTED AS 2

        screen.blit(RED_FONT, (390, 190))                               # RED BUTTON TEXT POSITION

        GREEN_FONT = font.render("1", True, WHITE)              # GREEN BUTTON TEXTED AS 1

        screen.blit(GREEN_FONT, (190, 190))                             # GREEN BUTTON TEXT POSITION

        BLUE_FONT = font.render("3", True, WHITE)               # BLUE BUTTON TEXTED AS 3

        screen.blit(BLUE_FONT, (590, 190))                              # BLUE BUTTON TEXT POSITION

        HOT_PINK_FONT = font.render("4", True, WHITE)           # HOT PINK BUTTON TEXTED AS 4

        screen.blit(HOT_PINK_FONT, (290, 290))                          # HOT PINK BUTTON TEXT POSITION

        CYAN_FONT = font.render("5", True, WHITE)               # CYAN BUTTON TEXTED AS 5

        screen.blit(CYAN_FONT, (490, 290))                              # CYAN BUTTON TEXT POSITION

        ORANGE_FONT = font.render("6", True, WHITE)             # ORANGE BUTTON TEXTED AS 6

        screen.blit(ORANGE_FONT, (390, 390))                            # ORANGE BUTTON TEXT POSITION

        for event in srs.event.get():                                        # EVENT LOOP
            if event.type == srs.QUIT:                                       # IF QUIT BUTTON IS PRESSED
                Ball_screen_running = False                                  # BALL SCREEN WILL BE CLOSED

            if event.type == srs.MOUSEBUTTONDOWN:                            # IF MOUSE BUTTON IS PRESSED
                x, y = srs.mouse.get_pos()                                   # GET THE POSITION OF MOUSE

                if 150 <= x <= 250 and 150 <= y <= 250:                      # IF RED BUTTON IS PRESSED
                    Bowling(1, rd.choice([1, 2, 3, 4, 5, 6]))      # BOWL FUNCTION WILL BE CALLED

                if 350 <= x <= 450 and 150 <= y <= 250:                      # IF GREEN BUTTON IS PRESSED
                    Bowling(2, rd.choice([1, 2, 3, 4, 5, 6]))      # BOWL FUNCTION WILL BE CALLED

                if 550 <= x <= 650 and 150 <= y <= 250:                      # IF BLUE BUTTON IS PRESSED
                    Bowling(3, rd.choice([1, 2, 3, 4, 5, 6]))      # BOWL FUNCTION WILL BE CALLED

                if 250 <= x <= 350 and 250 <= y <= 350:                      # IF HOT PINK BUTTON IS PRESSED
                    Bowling(4, rd.choice([1, 2, 3, 4, 5, 6]))      # BOWL FUNCTION WILL BE CALLED

                if 450 <= x <= 550 and 250 <= y <= 350:                      # IF CYAN BUTTON IS PRESSED
                    Bowling(5, rd.choice([1, 2, 3, 4, 5, 6]))      # BOWL FUNCTION WILL BE CALLED

                if 350 <= x <= 450 and 350 <= y <= 450:                      # IF ORANGE BUTTON IS PRESSED
                    Bowling(6, rd.choice([1, 2, 3, 4, 5, 6]))      # BOWL FUNCTION WILL BE CALLED

        srs.display.update()                                                 # UPDATE THE SCREEN


# BAT AND BALL CHOICE SCREEN

def Bat_Ball_Choice_Screen():
    # GLOBAL VARIABLES ARE USED TO ACCESS THE VARIABLES OUTSIDE THE FUNCTION
    global Bat_Ball_Choice_screen_running, ai_bat_ball_choice, user_toss_win, Bat_screen_running, Ball_screen_running

    while Bat_Ball_Choice_screen_running:        # THIS FUNCTION WILL RUN UNTIL THE BAT BALL CHOICE SCREEN IS RUNNING
        screen.fill(BLUE)                          # SCREEN BACKGROUND COLOR IS BLUE

        if user_toss_win == True:                  # IF USER WON THE TOSS

            draw_bat_ball_logo()                   # DRAW BAT AND BALL LOGOS

            title = font.render("YOU WON THE TOSS! CHOOSE BATTING OR BOWLING", True, HOT_PINK)  # TITLE

            screen.blit(title, (100, 0))                                                       # TITLE POSITION

            back = font.render("QUIT", True, RED)    # QUIT BUTTON

            screen.blit(back, (370, 550))                   # QUIT BUTTON POSITION

            for event in srs.event.get():                        # EVENT LOOP

                if event.type == srs.QUIT:                       # IF QUIT BUTTON IS PRESSED
                    Bat_Ball_Choice_screen_running = False       # BAT BALL CHOICE SCREEN WILL BE CLOSED

                if event.type == srs.MOUSEBUTTONDOWN:            # IF MOUSE BUTTON IS PRESSED
                    x, y = srs.mouse.get_pos()                   # GET THE POSITION OF MOUSE

                    if 0 <= x <= 150 and 250 <= y <= 400:        # IF BAT BUTTON IS PRESSED
                        Bat_screen_running = True                # BAT SCREEN WILL BE OPENED
                        Bat_Screen()                             # BAT SCREEN FUNCTION WILL BE CALLED

                    if 650 <= x <= 800 and 250 <= y <= 400:      # IF BALL BUTTON IS PRESSED
                        Ball_screen_running = True               # BALL SCREEN WILL BE OPENED
                        Ball_Screen()                            # BALL SCREEN FUNCTION WILL BE CALLED

                    if 370 <= x <= 430 and 550 <= y <= 574:      # IF QUIT BUTTON IS PRESSED
                        Bat_Ball_Choice_screen_running = False   # BAT BALL CHOICE SCREEN WILL BE CLOSED

            srs.display.update()                                 # UPDATE THE SCREEN

        else:                                                    # IF USER LOST THE TOSS

            if ai_bat_ball_choice == "BAT":                      # IF AI CHOOSED BAT
                screen.blit(BALL, (650, 250))               # BALL IMAGE

                title = font.render("AI CHOOSED BATTING", True, HOT_PINK)   # TITLE

                screen.blit(title, (265, 0))                                        # TITLE POSITION

                back = font.render("QUIT", True, RED)               # QUIT BUTTON

                screen.blit(back, (370, 550))                              # QUIT BUTTON POSITION

                for event in srs.event.get():                                   # EVENT LOOP

                    if event.type == srs.QUIT:                                  # IF QUIT BUTTON IS PRESSED
                        Bat_Ball_Choice_screen_running = False                # BAT BALL CHOICE SCREEN WILL BE CLOSED

                    if event.type == srs.MOUSEBUTTONDOWN:                       # IF MOUSE BUTTON IS PRESSED
                        x, y = srs.mouse.get_pos()                              # GET THE POSITION OF MOUSE

                        if 650 <= x <= 800 and 250 <= y <= 400:                 # IF BALL BUTTON IS PRESSED
                            Ball_screen_running = True                          # BALL SCREEN WILL BE OPENED
                            Ball_Screen()                                       # BALL SCREEN FUNCTION WILL BE CALLED

                        if 370 <= x <= 430 and 550 <= y <= 574:                 # IF QUIT BUTTON IS PRESSED
                            Bat_Ball_Choice_screen_running = False            # BAT BALL CHOICE SCREEN WILL BE CLOSED

                srs.display.update()                                            # UPDATE THE SCREEN

            elif ai_bat_ball_choice == "BALL":                                  # IF AI CHOOSED BALL
                screen.blit(BAT, (0, 250))                                 # BAT IMAGE

                title = font.render("AI CHOOSED BOWLING", True, HOT_PINK)   # TITLE

                screen.blit(title, (265, 0))                                       # TITLE POSITION

                back = font.render("QUIT", True, RED)               # QUIT BUTTON

                screen.blit(back, (370, 550))                              # QUIT BUTTON POSITION

                for event in srs.event.get():                                   # EVENT LOOP

                    if event.type == srs.QUIT:                                  # IF QUIT BUTTON IS PRESSED
                        Bat_Ball_Choice_screen_running = False                # BAT BALL CHOICE SCREEN WILL BE CLOSED

                    if event.type == srs.MOUSEBUTTONDOWN:                       # IF MOUSE BUTTON IS PRESSED
                        x, y = srs.mouse.get_pos()                              # GET THE POSITION OF MOUSE

                        if 0 <= x <= 150 and 250 <= y <= 400:                   # IF BAT BUTTON IS PRESSED
                            Bat_screen_running = True                           # BAT SCREEN WILL BE OPENED
                            Bat_Screen()                                        # BAT SCREEN FUNCTION WILL BE CALLED

                        if 370 <= x <= 430 and 550 <= y <= 574:                 # IF QUIT BUTTON IS PRESSED
                            Bat_Ball_Choice_screen_running = False            # BAT BALL CHOICE SCREEN WILL BE CLOSED

                srs.display.update()                                            # UPDATE THE SCREEN

            else:                                                               # IF AI CHOOSED NEITHER BAT NOR BALL
                print("ERROR")                                                  # PRINT ERROR

# TOSS SCREEN

def Toss_Screen():
    # GLOBAL VARIABLES ARE USED TO ACCESS THE VARIABLES OUTSIDE THE FUNCTION
    global Toss_screen_running, Bat_Ball_Choice_screen_running, ai_bat_ball_choice, user_toss_win

    while Toss_screen_running:                         # THIS FUNCTION WILL RUN UNTIL THE TOSS SCREEN IS RUNNING
        screen.fill(WHITE)                             # SCREEN BACKGROUND COLOR IS WHITE

        draw_toss_logo()                               # WIDTH = 100, HEIGHT = 100

        title = font.render("CHOOSE HEAD OR TAIL", True, HOT_PINK)  # TITLE

        screen.blit(title, (265, 0))                                        # TITLE POSITION

        back = font.render("QUIT", True, RED)                       # QUIT BUTTON

        screen.blit(back, (370, 550))                                       # QUIT BUTTON POSITION

        for event in srs.event.get():                                           # EVENT LOOP

            if event.type == srs.QUIT:                                          # IF QUIT BUTTON IS PRESSED
                Toss_screen_running = False                                     # TOSS SCREEN WILL BE CLOSED

            if event.type == srs.MOUSEBUTTONDOWN:                               # IF MOUSE BUTTON IS PRESSED
                x, y = srs.mouse.get_pos()                                      # GET THE POSITION OF MOUSE

                if 0 <= x <= 100 and 250 <= y <= 350:                           # IF HEAD BUTTON IS PRESSED
                    ai_choose_toss = rd.choice(["HEAD", "TAIL"])                # AI CHOOSE TOSS

                    if ai_choose_toss == "HEAD":                                # IF AI CHOOSED HEAD
                        Bat_Ball_Choice_screen_running = True                 # BAT BALL CHOICE SCREEN WILL BE OPENED

                        user_toss_win = True                                    # USER TOSS WIN WILL BE TRUE

                        Bat_Ball_Choice_Screen()                     # BAT BALL CHOICE SCREEN FUNCTION WILL BE CALLED

                    else:                                                       # IF AI CHOOSED TAIL
                        ai_bat_ball_choice = rd.choice(["BAT", "BALL"])         # AI CHOOSE BAT OR BALL

                        Bat_Ball_Choice_screen_running = True                 # BAT BALL CHOICE SCREEN WILL BE OPENED

                        user_toss_win = False                                   # USER TOSS WIN WILL BE FALSE

                        Bat_Ball_Choice_Screen()                     # BAT BALL CHOICE SCREEN FUNCTION WILL BE CALLED

                if 700 <= x <= 800 and 250 <= y <= 350:                         # IF TAIL BUTTON IS PRESSED
                    ai_choose_toss = rd.choice(["HEAD", "TAIL"])                # AI CHOOSE TOSS

                    if ai_choose_toss == "TAIL":                                # IF AI CHOOSED TAIL
                        Bat_Ball_Choice_screen_running = True                 # BAT BALL CHOICE SCREEN WILL BE OPENED

                        user_toss_win = True                                    # USER TOSS WIN WILL BE TRUE

                        Bat_Ball_Choice_Screen()                     # BAT BALL CHOICE SCREEN FUNCTION WILL BE CALLED

                    else:                                                       # IF AI CHOOSED HEAD
                        ai_bat_ball_choice = rd.choice(["BAT", "BALL"])       # AI CHOOSE BAT OR BALL

                        Bat_Ball_Choice_screen_running = True                 # BAT BALL CHOICE SCREEN WILL BE OPENED

                        user_toss_win = False                                 # USER TOSS WIN WILL BE FALSE

                        Bat_Ball_Choice_Screen()                     # BAT BALL CHOICE SCREEN FUNCTION WILL BE CALLED

                if 370 <= x <= 430 and 550 <= y <= 574:                         # IF QUIT BUTTON IS PRESSED
                    Toss_screen_running = False                                 # TOSS SCREEN WILL BE CLOSED

        srs.display.update()                                                    # UPDATE THE SCREEN


# OVER SCREEN
def over_screen():                                                              # OVER SCREEN FUNCTION
    # GLOBAL VARIABLES ARE USED TO ACCESS THE VARIABLES OUTSIDE THE FUNCTION
    global Over_screen_running, overes

    while Over_screen_running:                         # THIS FUNCTION WILL RUN UNTIL THE OVER SCREEN IS RUNNING

        screen.fill(YELLOW)                            # SCREEN BACKGROUND COLOR IS YELLOW

        title = font.render("PLEASE SELECT YOUR OVER", True, HOT_PINK)  # TITLE

        screen.blit(title, (270, 0))                                            # TITLE POSITION

        back = font.render("QUIT", True, RED)                           # QUIT BUTTON

        screen.blit(back, (370, 550))                                           # QUIT BUTTON POSITION

        over1 = font.render("5", True, BLUE)                            # OVER 5

        screen.blit(over1, (370, 100))                                          # OVER 5 POSITION

        over2 = font.render("10", True, BLUE)                            # OVER 10

        screen.blit(over2, (370, 200))                                          # OVER 10 POSITION

        over3 = font.render("20", True, BLUE)                           # OVER 20

        screen.blit(over3, (370, 300))                                          # OVER 20 POSITION

        for event in srs.event.get():                                               # EVENT LOOP

            if event.type == srs.QUIT:                                              # IF QUIT BUTTON IS PRESSED
                Over_screen_running = False                                         # OVER SCREEN WILL BE CLOSED

            if event.type == srs.MOUSEBUTTONDOWN:                                   # IF MOUSE BUTTON IS PRESSED
                x, y = srs.mouse.get_pos()                                          # GET THE POSITION OF MOUSE

                if 370 <= x <= 430 and 100 <= y <= 124:                             # IF OVER 5 BUTTON IS PRESSED
                    overes = 30                                                     # OVER WILL BE 30
                    Over_screen_running = False                                     # OVER SCREEN WILL BE CLOSED

                if 370 <= x <= 430 and 200 <= y <= 224:                             # IF OVER 10 BUTTON IS PRESSED
                    overes = 60                                                     # OVER WILL BE 60
                    Over_screen_running = False                                     # OVER SCREEN WILL BE CLOSED

                if 370 <= x <= 430 and 300 <= y <= 324:                             # IF OVER 20 BUTTON IS PRESSED
                    overes = 120                                                    # OVER WILL BE 120
                    Over_screen_running = False                                     # OVER SCREEN WILL BE CLOSED

                if 370 <= x <= 430 and 550 <= y <= 574:                             # IF QUIT BUTTON IS PRESSED
                    Over_screen_running = False                                     # OVER SCREEN WILL BE CLOSED

        srs.display.update()                                                        # UPDATE THE SCREEN

# MAIN SCREEN

while Main_screen_running:                             # THIS FUNCTION WILL RUN UNTIL THE MAIN SCREEN IS RUNNING
    screen.fill(BLACK)                                 # SCREEN BACKGROUND COLOR IS BLACK

    # TEAM LOGOS
    draw_team_logo() # WIDTH = 100, HEIGHT = 100

    title = font.render("CHOOSE YOUR TEAM", True, HOT_PINK)         # TITLE

    screen.blit(title, (270, 0))                                            # TITLE POSITION

    # QUIT BUTTON
    back = font.render("QUIT", True, RED)           # WIDTH = 60, HEIGHT = 24

    screen.blit(back, (370, 550))                           # QUIT BUTTON POSITION

    # OVER BUTTON
    over = font.render("OVER", True, BLUE)          # WIDTH = 60, HEIGHT = 24

    screen.blit(over, (370, 500))                           # OVER BUTTON POSITION

    for event in srs.event.get():                                   # EVENT LOOP

        if event.type == srs.QUIT:                                  # IF QUIT BUTTON IS PRESSED
            Main_screen_running = False                             # MAIN SCREEN WILL BE CLOSED

        if event.type == srs.MOUSEBUTTONDOWN:                       # MOUSE CLICK ON TEAM LOGO
            x, y = srs.mouse.get_pos()                              # GET THE POSITION OF MOUSE

            if 0 <= x <= 100 and 50 <= y <= 150:                    # IF AFGHANISTAN LOGO IS PRESSED
                user_team = "AFG"                                   # USER TEAM WILL BE AFGHANISTAN

                ai_team_choice = rd.choice(["BAN", "IND", "PAK", "SRI"])    # AI TEAM WILL BE RANDOMLY CHOSEN

                ai_team = ai_team_choice                            # AI TEAM WILL BE AI TEAM CHOICE

                Toss_screen_running = True                          # TOSS SCREEN WILL BE OPENED

                Toss_Screen()                                       # TOSS SCREEN FUNCTION WILL BE CALLED

            if 700 <= x <= 800 and 50 <= y <= 150:                  # IF BANGLADESH LOGO IS PRESSED
                user_team = "BAN"                                   # USER TEAM WILL BE BANGLADESH

                ai_team_choice = rd.choice(["AFG", "IND", "PAK", "SRI"])    # AI TEAM WILL BE RANDOMLY CHOSEN

                ai_team = ai_team_choice                            # AI TEAM WILL BE AI TEAM CHOICE

                Toss_screen_running = True                          # TOSS SCREEN WILL BE OPENED

                Toss_Screen()                                       # TOSS SCREEN FUNCTION WILL BE CALLED

            if 0 <= x <= 100 and 200 <= y <= 300:                   # IF INDIA LOGO IS PRESSED
                user_team = "IND"                                   # USER TEAM WILL BE INDIA

                ai_team_choice = rd.choice(["AFG", "BAN", "PAK", "SRI"])    # AI TEAM WILL BE RANDOMLY CHOSEN

                ai_team = ai_team_choice                            # AI TEAM WILL BE AI TEAM CHOICE

                Toss_screen_running = True                          # TOSS SCREEN WILL BE OPENED

                Toss_Screen()                                       # TOSS SCREEN FUNCTION WILL BE CALLED

            if 700 <= x <= 800 and 200 <= y <= 300:                 # IF PAKISTAN LOGO IS PRESSED
                user_team = "PAK"                                   # USER TEAM WILL BE PAKISTAN

                ai_team_choice = rd.choice(["AFG", "BAN", "IND", "SRI"])    # AI TEAM WILL BE RANDOMLY CHOSEN

                ai_team = ai_team_choice                            # AI TEAM WILL BE AI TEAM CHOICE

                Toss_screen_running = True                          # TOSS SCREEN WILL BE OPENED

                Toss_Screen()                                       # TOSS SCREEN FUNCTION WILL BE CALLED

            if 350 <= x <= 450 and 350 <= y <= 450:                 # IF SRI LANKA LOGO IS PRESSED
                user_team = "SRI"                                   # USER TEAM WILL BE SRI LANKA

                ai_team_choice = rd.choice(["AFG", "BAN", "IND", "PAK"])    # AI TEAM WILL BE RANDOMLY CHOSEN

                ai_team = ai_team_choice                            # AI TEAM WILL BE AI TEAM CHOICE

                Toss_screen_running = True                          # TOSS SCREEN WILL BE OPENED

                Toss_Screen()                                       # TOSS SCREEN FUNCTION WILL BE CALLED

            if 370 <= x <= 430 and 500 <= y <= 524:                 # IF OVER BUTTON IS PRESSED
                Over_screen_running = True                          # OVER SCREEN WILL BE OPENED

                over_screen()                                       # OVER SCREEN FUNCTION WILL BE CALLED

            if 370 <= x <= 430 and 550 <= y <= 574:                 # IF QUIT BUTTON IS PRESSED
                Main_screen_running = False                         # MAIN SCREEN WILL BE CLOSED

    srs.display.update()                                            # UPDATE THE SCREEN

srs.quit()                                                          # QUIT THE GAME

# END OF THE PROGRAM