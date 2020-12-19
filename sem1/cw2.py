# flappy game

# This game is using 1280x720 for main game and 1920x1080 for boss key (a full screen)
# different size is used as I suppose there is no need for a full screen as this game

from tkinter import *
from time import sleep
from random import randint


# constants

# width between pillars
PILLAR_H = {1: 120, 2: 180, 3: 230, 4: 290, 5: 350, 6: 390}
PILLAR_W = 300
HEIGHT = 170
CHEAT = 120
CHEAT_HEIGHT = 500
# character size
CHARACTER_WIDTH = 120
CHARACTER_HEIGHT = 60


# initial variables
chance = 0
score = 950  # (15+30+50)*10--10 scores for each pillar (collide once cause losing 10 scores)

# ******************************** define function ***************************************


def window_configure():
    window.title("flappy funny")
    # window.iconbitmap("icon.ico")


# jump in home page --- jump and move left & right
def char_jump(event):
    # global funny
    pos0 = game_place.coords(funny0)
    global inverse
    if pos0[0] > 900 or pos0[0] < 10.0:
        inverse += 1
    if inverse == 0 or inverse % 2 == 0:
        jmp_x = 1.5
    else:
        jmp_x = -1.5

    for i in range(26):
        game_place.move(funny0, jmp_x, -2)
        sleep(0.008)
        game_place.update()
    for i in range(26):
        game_place.move(funny0, jmp_x, 2)
        sleep(0.008)
        game_place.update()


# jump in game ---jump and move pillars
def jump_game(event):
    global end, pos_c, bak, pause
    end = 0
    pos_c = game_place.coords(funny)
    if pause == 1:
        window.wait_window(bak)
    for i in range(26):
        if end == 1:
            break
        pillar_move()
        game_place.move(funny, 0, -2)
        sleep(0.0025)
        game_place.update()
        pos_c = game_place.coords(funny)
    for i in range(26):
        if end == 1:
            break
        pillar_move()
        game_place.move(funny, 0, 2)
        sleep(0.0025)
        game_place.update()
        pos_c = game_place.coords(funny)


# buttons-active
def active_button(event):
    x = event.x
    y = event.y
    if 410 < x < 600 and 410 > y > 360:
        game_place.move(btn1, 5, 5)
    elif 720 < x < 921 and 410 > y > 360:
        game_place.move(btn2, 5, 5)
    elif 410 < x < 600 and 530 > y > 490:
        game_place.move(btn3, 5, 5)
    elif 720 < x < 921 and 530 > y > 490:
        game_place.move(btn0, 5, 5)
    elif 568 < x < 752 and 650 > y > 570:
        game_place.move(btn5, 5, 5)


# buttons-inactive-animation
def inactive_button(event):
    x = event.x
    y = event.y
    if 410 < x < 600 and 410 > y > 360:
        game_place.move(btn1, -5, -5)
        return new_game()
    elif 720 < x < 921 and 410 > y > 360:
        game_place.move(btn2, -5, -5)
        return game_continue()
    elif 410 < x < 600 and 530 > y > 490:
        game_place.move(btn3, -5, -5)
        return helpinfo()
    elif 720 < x < 921 and 530 > y > 490:
        game_place.move(btn0, -5, -5)
        return window.quit()
    elif 568 < x < 752 and 650 > y > 570:
        game_place.move(btn5, -5, -5)
        return score_view()


# button to start new game
def new_game():
    global new_pg, text_s, entry_s, btn_start, btn_close, \
        player_level, player_name, btn_s, btn_c
    text_start = " Please create a player name: \n (words & numbers only!)"
    new_pg = game_place.create_rectangle(290, 30, 1000, 330, fill="#9EFFCC")
    text_s = game_place.create_text(630, 90, text=text_start, font="Bold, 20")
    player_name = Entry(window, width=30, borderwidth=2, font="Arial, 15", fg="grey")
    player_name.insert(0, "Enter player name")
    entry_s = game_place.create_window(630, 200, window=player_name)
    btn_start = Button(window, text="Start Now", font="Arial 15", command=get_new)
    btn_s = game_place.create_window(630, 300, window=btn_start)

    btn_close = Button(window, text=" x ", font="Arial 15", activebackground="red",
                       activeforeground="white", command=close1)
    btn_c = game_place.create_window(1002, 50, window=btn_close, anchor="e")
    player_level = 1


# button to continue previous game
def game_continue():
    global new_pg, text_s, entry_s, btn_start, btn_close, player_name, \
        btn_s, btn_c, name_tried, tried
    tried = []
    name_tried = 0
    new_pg = game_place.create_rectangle(290, 30, 1000, 330, fill="#9EFFCC")
    text_continue = " Please enter your player name: "
    text_s = game_place.create_text(630, 90, text=text_continue, font="Bold, 20")
    player_name = Entry(window, width=30, borderwidth=2, font="Arial, 15", fg="grey")
    player_name.insert(0, "Enter player name")
    entry_s = game_place.create_window(630, 200, window=player_name)
    btn_start = Button(window, text="Continue", font="Arial 15", command=get_player)

    btn_s = game_place.create_window(630, 300, window=btn_start)

    btn_close = Button(window, text=" x ", font="Arial 15", activebackground="red",
                       activeforeground="white", command=close1)
    btn_c = game_place.create_window(1002, 50, window=btn_close, anchor="e")


# button to the help page
def helpinfo():
    global otherpage, other_info1, btn_c, btn_close, other_info2
    otherpage = game_place.create_rectangle(290, 30, 1000, 330, fill="#f8ffb0")
    info = "Press 'New Start' to start as new player.\nPress 'Continue' to " \
           "continue as a previous player\nPress 'Customise' to add key of jump\n" \
           "For high scores and leader board, clink 'View Scores'"
    other_info1 = game_place.create_text(630, 100, text=info, font="Bold 12", anchor="center")
    about = "Funny is a famous emoji with the meaning of laugh at in a kind purpose\n" \
            "One day, Funny got a couple of wings! He flies and flies...\n" \
            "But...wait! Why are there many pillars!" \
            "\n(tab <space> to elude pillars " \
            "/space or other keys if you customised)"
    other_info2 = game_place.create_text(630, 180, text=about, font="Bold 12")
    btn_close = Button(window, text="Close", command=close2)
    btn_c = game_place.create_window(630, 300, window=btn_close)


def score_view():
    global otherpage, other_info1, btn_close, btn_c, content0, content, other_info2
    otherpage = game_place.create_rectangle(290, 30, 1000, 330, fill="#9EFFCC")
    try:
        with open("scores.txt", "r+") as file_score:
            label = "\nScore       ||       Leader\n"
            content0 = file_score.readlines()
            calculate_leader()
            score_available = label + "\n" + str(content)
    except FileNotFoundError:
        score_available = "Sorry, there is no scores available..."
    text_score = "Current score available:" + "\n" + str(score_available)
    try:
        with open("gameleaders.txt", "r+") as file_leader:
            text_leader = "leader history:\n" + file_leader.read()
    except FileNotFoundError:
        text_leader = "Sorry, there is no leaders currently...\nTry to do the first one to pass the game?"
    other_info1 = game_place.create_text(500, 170, text=text_score, font="Bold, 12")
    other_info2 = game_place.create_text(830, 160, text=text_leader, font="Bold 12")
    btn_close = Button(window, text="Close", command=close2)
    btn_c = game_place.create_window(630, 300, window=btn_close)


def get_player():
    global player, text_s2, player_name, player_level, score, name_tried
    player = player_name.get()
    try:
        with open(player + ".txt", "r+") as player_file:
            current_player = player_file.readlines()
            player = current_player[0]
            player = player.replace("\n", "")
            player_level = int(current_player[1])
            score = int(current_player[2])
            return start()
    except FileNotFoundError:
        name_tried += 1
        text_notfound = "Sorry, your player name seems to be not found,\nplease try again: "
        text_s2 = game_place.create_text(630, 150, text=text_notfound, font="Bold, 15")
        tried.append(text_s2)


def get_new():
    global player, player_name
    player = player_name.get()
    return start()


# clear start page & continue page
def close1():
    game_place.delete(new_pg, text_s, entry_s, btn_s, btn_c)
    btn_start.destroy()
    btn_close.destroy()
    try:
        for i in range(name_tried):
            game_place.delete(tried[i])
    except NameError:
        pass


# clear help page
def close2():
    game_place.delete(otherpage, other_info1, btn_c, other_info2)
    btn_close.destroy()


# deal with levels
def start():
    global funny, pos_c, btn_cheat, btn_pause, chance, score, btn_qt, player_level

    game_place.delete("all")
    btn_start.destroy()
    btn_close.destroy()

    # unbind mouse clink (as used images as buttons)
    game_place.unbind("<Button-1>")
    game_place.unbind("<ButtonRelease-1>")

    # stuff on the game page
    btn_pal = Button(window, text="II", font="Arial 15", command=stp, bg="#FF9C97")
    btn_pause = game_place.create_window(1250, 17, window=btn_pal, anchor="w")
    btn_cht = Button(window, text="cheat", font="Arial 12", command=cheat, bg="#FF9C97")
    btn_cheat = game_place.create_window(1160, 15, window=btn_cht, anchor="w")
    btn_qu = Button(window, text="Quit", font="Arial 12", command=quit_game, bg="#FF9C97")
    btn_qt = game_place.create_window(1070, 15, window=btn_qu, anchor="w")

    funny = game_place.create_image(170, 600, image=character)
    # in case pos_c is not defined (haven't jump and have a collision)
    pos_c = game_place.coords(funny)
    window.bind("<space>", jump_game)

    # showing score
    if chance != 0:
        score -= 10
        chance = 0
    showscore = "Current score: " + str(score) + "\t"
    showlevel = "Level: " + str(player_level)
    game_place.create_text(150, 16, text=showscore + showlevel, font="Arial 17", fill="white",
                           activefill="black")
    game_place.create_text(120, 50, text="(lose once for 10 scores)",
                           font="Arial 15", fill="white", activefill="black")
    game_place.create_text(600, 17, text="Go for it, " + player + "!",
                           font="Arial 15", fill="white", activefill="black")
    return level(player_level)


# pillars used for each level & assign pillar passed
def level(arg):
    global num_pillar, p_pass
    p_pass = 0
    if arg == 1:
        num_pillar = 20
        return assign_plr()
    elif arg == 2:
        num_pillar = 30
        return assign_plr()
    elif arg == 3:
        num_pillar = 50
        return assign_plr()
    else:
        num_pillar = 0   # in case
        return win_pg()


# assign pillars
def assign_plr():
    global pl, plr_no, cht
    pl = []  # list of images
    plr_no = []  # list of the pillar index
    # for the use of cheat code
    cht = 0

    # select a random image from list pillar for num_pillar times
    for i in range(num_pillar):
        plr_i = randint(1, 6)
        plr_no.append(plr_i)
        num = plr_i - 1
        pl.append(game_place.create_image(905 + PILLAR_W * (i - 1), 362, image=pillars[num]))
    return plr_start()


# move pillars (while)
def plr_start():
    global end, pause, backhome
    pause = 0
    end = 0
    backhome = 0
    while True:
        if end == 1:
            break
        else:
            pillar_move()
            game_place.update()
    return end_level()


# detect collision
def collision():
    global end, cht
    # cheat or not
    if cht == 0:
        plr_n = plr_no[id_p]
        plr_interval = PILLAR_H[plr_n]
        height = HEIGHT
    else:
        plr_interval = CHEAT
        height = CHEAT_HEIGHT

    if pos_c[1]-CHARACTER_HEIGHT/2 < plr_interval or pos_c[1]+CHARACTER_HEIGHT/2\
            > plr_interval + height:
        end = 1


# move pillar(not in a while loop)
def pillar_move():
    global bak, pause
    # for pause use
    if pause == 1:
        window.wait_window(bak)
        pause = 0

    for i in range(num_pillar):
        global pos_p, p_pass
        pos_p = game_place.coords(pl[i])
        try:
            if i == num_pillar - 1:
                if pos_p[0] < 15:
                    global end
                    end = 1
            if 170 + CHARACTER_WIDTH/2 > pos_p[0] > 170 - CHARACTER_WIDTH/2:
                global id_p
                id_p = i
                collision()
            if pos_p[0] < 15:
                game_place.delete(pl[i])
                p_pass += 1
                continue
            # elif pos_p[0]
        except IndexError:
            continue
        game_place.move(pl[i], -1, 0)
    sleep(0.0025)


def end_level():
    if p_pass == num_pillar:
        return you_win()
    elif backhome == 1:
        return 0
    else:
        return game_over()


def you_win():
    global player_level, btn_hm, btn_home, wn_btn, win_1, win_2
    player_level += 1
    win_1 = game_place.create_text(600, 350, text="You Win!!", font="Arial 100", fill="white",
                                   activefill="black")
    wn_btn = Button(window, text=">>", font="bold 60", command=start, fg="#05008A")
    win_2 = game_place.create_window(1050, 350, window=wn_btn)
    btn_hm = Button(window, text="Back to Home", font="Arial 17", command=home_if_save)
    btn_home = game_place.create_window(600, 500, window=btn_hm)



def game_over():
    global chance, btn_hm, btn_home, ls_btn, loss_tx, loss_bn
    loss_tx = game_place.create_text(600, 330, text="Game Over", font="Arial 100", fill="white",
                                     activefill="black")
    ls_btn = Button(window, text="Try again...", font="Arial 25", command=start,
                    bg="#05008A", fg="white")
    chance += 1
    loss_bn = game_place.create_window(600, 490, window=ls_btn)
    btn_hm = Button(window, text="Back to Home", font="Arial 17", command=home_if_save)
    btn_home = game_place.create_window(600, 560, window=btn_hm)


# tap space to jump and elude pillars
def win_pg():
    global btn_hm, btn_home, win_1, win_2
    congrats1 = "Congratulations!"
    congrats2 = "You passed\nall the levels!!"
    win_1 = game_place.create_text(600, 290, text=congrats1, font="Arial 57", fill="white",
                                   activefill="black")
    win_2 = game_place.create_text(600, 390, text=congrats2, font="Arial 35", fill="white",
                                   activefill="black")
    score_show = Button(window, text="view scores", font="Arial 15", bg="#06008A", fg="white", command=score_view)
    game_place.create_window(600, 500, window=score_show)
    btn_hm = Button(window, text="Home", font="Arial 17", command=home_if_save)
    btn_home = game_place.create_window(600, 560, window=btn_hm)

    total_scores = str(score)+"     "+player
    try:
        with open("scores.txt", "a") as score_file:
            score_file.write("\n"+total_scores)
    except FileNotFoundError:
        file_sc = open("scores.txt", "w")
        file_sc.write(total_scores)


# boss key
# if boss key---
def boss_key(event):
    top = Toplevel()
    top.title("Black board")
    canvas = Canvas(top, bg="#000000", width=1920, height=1080)
    canvas.create_image(770, 380, image=bos_ky)
    canvas.pack()
    stp()


# cheat code
def cheat():
    global end, p_pass, cht
    cht = 1

    # delete pillars on the window
    for i in range(num_pillar):
        pos_p = game_place.coords(pl[i])
        try:
            if pos_p[0] > 15:
                game_place.delete(pl[i])
        except IndexError:
            continue

    # use other pictures of remaining pillars (huge interval)
    for i in range(num_pillar-p_pass):
        pl[p_pass + i] = (game_place.create_image(905 + 250 * (i - 1), 360, image=pillar0))
    return plr_start()


def stp():
    global pos_window, pos_txt, back_b, toquit, bak, pause, qt, btn_hm, btn_home
    pause = 1
    pos_window = game_place.create_rectangle(200, 170, 800, 500, fill="white")
    pos_txt = game_place.create_text(500, 250, text="Paused now...\n You can do:", font="bold 30")
    bak = Button(window, text="Back", font="Arial 20", command=back)
    back_b = game_place.create_window(300, 380, window=bak)
    qt = Button(window, text="Quit", font="Arial 20", command=delete_btns)
    toquit = game_place.create_window(650, 380, window=qt)
    btn_hm = Button(window, text="Home", font="Arial 17", command=home_if_save)
    btn_home = game_place.create_window(500, 380, window=btn_hm)

def back():
    game_place.delete(pos_window, pos_txt)
    bak.destroy()
    qt.destroy()
    btn_hm.destroy()


def delete_btns():
    bak.destroy()
    qt.destroy()
    btn_hm.destroy()
    return quit_game()


def home_if_save():
    global qt, qt_txt, qtb_ye, pause, bak, qtb_no, backhome, end
    game_place.delete(btn_home)
    try:
        qt.destroy()
        bak.destroy()
        game_place.delete(pos_txt, back_b, toquit)
    except NameError:
        pass
    try:
        ls_btn.destroy()
        game_place.delete(loss_tx, loss_bn)
    except NameError:
        pass
    try:
        wn_btn.destroy()
        game_place.delete(win_1, win_2)
    except NameError:
        pass
    btn_hm.destroy()
    backhome = 1
    pause = 1
    end = 1
    qt_txt = game_place.create_text(500, 250, text="Save or not ??", font="bold 30")
    qtb_ye = Button(window, text="Save", font="Arial 20", command=save)
    game_place.create_window(300, 380, window=qtb_ye)
    qtb_no = Button(window, text="No, thanks", font="Arial 20", command=nosave)
    game_place.create_window(650, 380, window=qtb_no)


def quit_game():
    global qt, qt_txt, qtb_ye, pause, bak, qtb_no
    pause = 1
    qt = game_place.create_rectangle(200, 170, 800, 500, fill="white")
    qt_txt = game_place.create_text(500, 250, text="Do you want to save?", font="bold 30")
    qtb_ye = Button(window, text="Yes", font="Arial 20", command=save)
    game_place.create_window(300, 380, window=qtb_ye)
    qtb_no = Button(window, text="No", font="Arial 20", command=nosave)
    game_place.create_window(650, 380, window=qtb_no)
    bak = Button(window, text="Back to game", font="Arial 15", command=back_qt)
    game_place.create_window(510, 200, window=bak)


def back_qt():
    game_place.delete(qt, qt_txt)
    qtb_ye.destroy()
    qtb_no.destroy()
    bak.destroy()


def nosave():
    global end
    if backhome == 1:
        return home_page()
    else:
        end = 1
        bak.destroy()
        return window.quit()


def save():
    global end
    file = open(player + ".txt", "w")
    file.write(player + "\n" + str(player_level) + "\n" + str(score))
    if backhome == 1:
        return home_page()
    else:
        end = 1
        bak.destroy()
        return window.quit()


def calculate_leader():
    global content, content0
    content0 = sorted(content0, reverse=True)
    content = ""
    for i in range(len(content0)):
        content0[i] = content0[i].replace("\n", "")
        if content0[0][0:3] == content0[i][0:3]:
            try:
                with open("gameleaders.txt", "r") as file_leader_r:
                    l_list = file_leader_r.readlines()
                    for n in range(len(l_list)):
                        l_list[n] = l_list[n].replace("\n", "")
                    if content0[i] not in l_list:
                        with open("gameleaders.txt", "a") as file_leader_a:
                            file_leader_a.write(content0[i] + "\n")
            except FileNotFoundError:
                file_ldr = open("gameleaders.txt", "w")
                file_ldr.write(content0[i])
            content0[i] += " *Current Leader(s)* "
    if len(content0) > 12:
        for i in range(12):
            content += content0[i] + "\n"
    else:
        for i in content0:
            content += i + "\n"
    content.replace("[", " ").replace("]", " ").replace("\n", "")


def customise():
    global new_pg, text_s, entry_s, btn_start, btn_close, btn_s, btn_c, player_cus
    info = "Currently you can only add the key to jump inside game\n" \
           "(default is space)\n" \
           "\nYou must ensure the key you entered is in right form if you\n" \
           " want to add and not a right clink or an <Up>(Up is the boss key) \n"\
           "\nplease enter which key on keyboard you want to use:"
    new_pg = game_place.create_rectangle(350, 15, 800, 330, fill="#f8ffb0")
    text_s = game_place.create_text(581, 100, text=info, font="Arial 12")
    player_cus = Entry(window, width=30, borderwidth=2, font="Arial, 15", fg="grey")
    entry_s = game_place.create_window(530, 200, window=player_cus)
    btn_start = Button(window, text=" Ok ", font="Arial 15", command=custom_bind)
    btn_s = game_place.create_window(530, 300, window=btn_start)
    btn_close = Button(window, text=" x ", font="Arial 15", activebackground="red",
                       activeforeground="white", command=close1)
    btn_c = game_place.create_window(800, 35, window=btn_close, anchor="e")


def custom_bind():
    cust_bind = player_cus.get()
    window.bind(cust_bind, jump_game)
    return close1()


def home_page():
    global inverse, btn1, btn2, btn3, btn0, btn5, info_text, customised_btn, funny0

    game_place.delete("all")
    window.unbind("all")

    game_place.create_image(680, 360, image=Img)
    funny0 = game_place.create_image(170, 300, image=character0)

    game_place.bind("<Button-1>", active_button)
    game_place.bind("<ButtonRelease-1>", inactive_button)
    inverse = 0
    window.bind("<space>", char_jump)
    window.bind("<Up>", boss_key)

    # startting buttons

    btn1 = game_place.create_image(500, 380, image=start_btn1)
    btn2 = game_place.create_image(830, 380, image=continue_btn2)
    btn3 = game_place.create_image(500, 510, image=help_btn3)
    btn0 = game_place.create_image(830, 509, image=quit_btn0)
    btn5 = game_place.create_image(660, 600, image=score_btn)
    info_text = game_place.create_text(660, 680, text="please tap space to jump",
                                       font="Arial, 25", fill="#05008A", activefill="white")
    cus_btn = Button(window, text="Customise", bg="orange", font="Arial 15", command=customise)
    customised_btn = game_place.create_window(60, 690, window=cus_btn)


# ********************************** end of define function part **************************

# open tkinter

window = Tk()
window_configure()

# create canvas
game_place = Canvas(window, bg="#89CAFD", width=1280, height=720)


# *********************************** start page ******************************************

# background
Img = PhotoImage(file="gamepage.gif")  # Figure 1


# character images
character0 = PhotoImage(file="character0.gif")  # Figure 2
character = PhotoImage(file="character.gif")


# homepage button images
start_btn1 = PhotoImage(file="001.gif")  # Figure 10
continue_btn2 = PhotoImage(file="002.gif")  # Figure 11
help_btn3 = PhotoImage(file="003.gif")  # Figure 12
quit_btn0 = PhotoImage(file="004.gif")  # Figure 13
score_btn = PhotoImage(file="005.gif")  # Figure 14

# pillar images
pillar1 = PhotoImage(file="pillar1.gif")  # Figure 3
pillar2 = PhotoImage(file="pillar2.gif")  # Figure 4
pillar3 = PhotoImage(file="pillar3.gif")  # Figure 5
pillar4 = PhotoImage(file="pillar4.gif")  # Figure 6
pillar5 = PhotoImage(file="pillar5.gif")  # Figure 7
pillar6 = PhotoImage(file="pillar6.gif")  # Figure 8
# list of pillars
pillars = [pillar1, pillar2, pillar3, pillar4, pillar5, pillar6]

# used for cheat code
pillar0 = PhotoImage(file="pillar0.gif")  # Figure 9

# used for boss_key
bos_ky = PhotoImage(file="bk.gif")
# ************************** bind stuff **********************************************


home_page()
# ******************************* display ****************************************
game_place.pack()
window.mainloop()

# ***********************************************************************************
# reference list for all images

# pillar_origional, Nintendo(2020) [diagram],
# Available at:https://www.clipartkey.com/view/xxiRxx_super-mario-pipe-png/
#                                                 (Accessed: 20 November 2020)

# funny, wing, emoji of Baidu Tieba(2020) [diagram], Available at: https://tieba.baidu.com/
#                                               (Accessed: 1 December 2020)
#  (as both are emojis, the link is direct to home page of Baidu Tieba

# Figure 1.gamepage.gif: self edited with "pillar_origional.png"

# Figure 2.self edited with "funny.png" and "wings.png"

# Figure 3-9. self edited with "pillar_origional.png"

# Figure 10-14. self drawn picture
