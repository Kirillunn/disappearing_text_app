from tkinter import *

# Constants
BG_COLOR = "#E2F4C5"
TEXT_ZONE_COLOR="#A8CD9F"
FONT_COLOR = "#496989"
TIMER = 10

# Check when user is typing - on each click timer resets
def typing(event):
    global TIMER
    TIMER = 10


# Start count down when user stops typing
def start_countdown():
    global TIMER
    if TIMER > 0:
        text_zone.configure(state="normal")
        timer_label.config(text=TIMER)
        TIMER -= 1
        timer_label.after(1000, start_countdown)
    # When timer is 0, delete all text and disable text zone
    elif TIMER == 0:
        timer_label.config(text=TIMER)
        text_zone.delete('1.0', 'end')
        text_zone.configure(state="disabled")


# UI Setup
window = Tk()
window.title(string="BlinkWrite")
window.config(background=BG_COLOR)

# Logo
logo_field = Canvas(height=78, width=128, background="white", highlightthickness=0)
logo = PhotoImage(file="logo.png")
logo_field.create_image(64, 39, image=logo)
logo_field.grid(column=0, row=0)

label = Label(text="Type your text here...", background=BG_COLOR, foreground=FONT_COLOR,
              font=("Helvetica", 40, "bold"))
label.grid(column=1, row=0)

# Timer
timer_label = Label(text=TIMER, background=BG_COLOR, foreground=FONT_COLOR,
                    font=("Helvetica", 40, "bold"))
timer_label.grid(column=0, row=1)

# Text zone
text_zone = Text(height=20, width=50, bg=TEXT_ZONE_COLOR, state="disabled",
                 highlightthickness=0, foreground=FONT_COLOR, font=("Helvetica", 18))
text_zone.grid(column=1, row=1)
text_zone.focus_set()
text_zone.bind("<Key>", typing)

# Start button
start_button = Button(text="START", width=10, height=2,
                      foreground=FONT_COLOR, font=("Helvetica", 18, "bold"), command=start_countdown)
start_button.grid(column=1, row=2)

window.mainloop()