import tkinter as tk 
from tkinter import PhotoImage 
from tkinter import messagebox 
import socket 
from time import sleep 
import threading 
# MAIN GAME WINDOW 
window_main = tk.Tk() 
window_main.title("Game Client") 
your_name = "" 
opponent_name = "" 
game_round = 0 
game_timer = 4 
your_choice = "" 
opponent_choice = "" 
TOTAL_NO_OF_ROUNDS = 5 
your_score = 0 
opponent_score = 0 
# network client 
client = None 
HOST_ADDR = "192.168.222.1" 
HOST_PORT = 8080 
top_welcome_frame = tk.Frame(window_main) 
lbl_name = tk.Label(top_welcome_frame, text="Name:") 
lbl_name.pack(side=tk.LEFT) 
ent_name = tk.Entry(top_welcome_frame) 
ent_name.pack(side=tk.LEFT) 
btn_connect = tk.Button(top_welcome_frame, text="Connect", command=lambda: 
connect()) 
btn_connect.pack(side=tk.LEFT) 
top_welcome_frame.pack(side=tk.TOP) 
top_message_frame = tk.Frame(window_main) 
lbl_line = tk.Label( 
 top_message_frame, 
 text="***********************************************************", 
).pack() 
lbl_welcome = tk.Label(top_message_frame, text="") 
lbl_welcome.pack() 
lbl_line_server = tk.Label( 
 top_message_frame, 
 text="***********************************************************",) 
lbl_line_server.pack_forget() 
top_message_frame.pack(side=tk.TOP) 
top_frame = tk.Frame(window_main) 
top_left_frame = tk.Frame( 
 top_frame, highlightbackground="green", highlightcolor="green", 
highlightthickness=1) 
lbl_your_name = tk.Label( 
 top_left_frame, text="Your name: " + your_name, font="Helvetica 13 bold") 
lbl_opponent_name = tk.Label(top_left_frame, text="Opponent: " + opponent_name) 
lbl_your_name.grid(row=0, column=0, padx=5, pady=8) 
lbl_opponent_name.grid(row=1, column=0, padx=5, pady=8) 
top_left_frame.pack(side=tk.LEFT, padx=(10, 10)) 
top_right_frame = tk.Frame( 
 top_frame, highlightbackground="green", highlightcolor="green", 
highlightthickness=1) 
lbl_game_round = tk.Label( 
 top_right_frame, 
 text="Game round (x) starts in", 
 foreground="blue", 
 font="Helvetica 14 bold",) 
lbl_timer = tk.Label( 
 top_right_frame, text=" ", font="Helvetica 24 bold", foreground="blue") 
lbl_game_round.grid(row=0, column=0, padx=5, pady=5) 
lbl_timer.grid(row=1, column=0, padx=5, pady=5) 
top_right_frame.pack(side=tk.RIGHT, padx=(10, 10)) 
top_frame.pack_forget() 
middle_frame = tk.Frame(window_main) 
lbl_line = tk.Label( 
 middle_frame, 
text="***********************************************************" 
).pack() 
lbl_line = tk.Label( 
 middle_frame, text="**** GAME LOG ****", font="Helvetica 13 bold", 
foreground="blue" 
).pack() 
lbl_line = tk.Label( 
 middle_frame, 
text="***********************************************************" 
).pack() 
round_frame = tk.Frame(middle_frame) 
lbl_round = tk.Label(round_frame, text="Round") 
lbl_round.pack() 
lbl_your_choice = tk.Label( 
 round_frame, text="Your choice: " + "None", font="Helvetica 13 bold") 
lbl_your_choice.pack() 
lbl_opponent_choice = tk.Label(round_frame, text="Opponent choice: " + "None") 
lbl_opponent_choice.pack() 
lbl_result = tk.Label( 
 round_frame, text=" ", foreground="blue", font="Helvetica 14 bold") 
lbl_result.pack() 
round_frame.pack(side=tk.TOP) 
final_frame = tk.Frame(middle_frame) 
lbl_line = tk.Label( 
 final_frame, 
text="***********************************************************").pack() 
lbl_final_result = tk.Label( 
 
final_frame, text=" ", font="Helvetica 13 bold", foreground="blue") 
lbl_final_result.pack() 
lbl_line = tk.Label( 
 final_frame, 
text="***********************************************************" 
).pack() 
final_frame.pack(side=tk.TOP) 
 # Start the timer 
 threading._start_new_thread(count_down, (game_timer, "")) 
 sck.close() 
window_main.mainloop()
