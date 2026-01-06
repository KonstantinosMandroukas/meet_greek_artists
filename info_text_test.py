import customtkinter
import tkinter as tk

root = customtkinter.CTk()
root.geometry("1500x900")
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure((2, 3), weight=0)
root.grid_rowconfigure((0, 1, 2), weight=1)


tabs = customtkinter.CTkTabview( root, width=1100, height=750)
artist_text = tabs.add("Text")
artist_photo = tabs.add("Photos")
artist_listen = tabs.add("Listen/Plays")


tabs.grid(row=0, column=1, padx=(20,0), pady=(50,40))

text = customtkinter.CTkLabel(artist_text, text="PUT THE DAMN TEXT HERE", font=("Arial", 16))
text.grid(row=1, column=0)


frame = customtkinter.CTkFrame(root, width=250, height=900) 
frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
frame.grid_rowconfigure(4, weight=1)

select_label = customtkinter.CTkLabel(frame, text="Select an artist", font=("Arial", 20)) 
# select_label.place(x=30, y= 2)
select_label.grid(row=0,column=0)

home_button = customtkinter.CTkButton( frame, text="Home")
home_button.grid(row=1,column=0, padx=(10,100), pady=(50,0))

select_artist_category_values = ["Actors", "Singers"]
select_artist_category = customtkinter.CTkComboBox( frame, values=select_artist_category_values)
select_artist_category.grid(row=2, column=0, padx=(10,100), pady=(30,0))

scrolable_frame = customtkinter.CTkScrollableFrame(frame, width=200, height=350)
scrolable_frame.grid(row=3, column=0, padx=(20, 50), pady=(30, 0), sticky="s")
scrolable_frame.grid_columnconfigure(0, weight=1)

#set theme/scaling
set_theme_values = ["Light", "Dark", "System"]
set_theme = customtkinter.CTkComboBox( root, values=set_theme_values)
set_theme.grid(row=4, column=0, padx=(0,80), pady=(5,50))

scaling_optionemenu = customtkinter.CTkComboBox( root, values=["80%", "90%", "100%", "110%", "120%"])
scaling_optionemenu.grid(row=5, column=0, padx=(0,80), pady=(0,70))


#search frame widgets

search_frame = customtkinter.CTkFrame( root, width=700, height=80)
search_frame.grid(row=0, column=1, pady=(0,80), padx=(0,100), sticky="n")

search = customtkinter.CTkEntry( search_frame, placeholder_text="Search an artist (Example: 'Konstantinos Argiros')", width=310, height=40, corner_radius=45)
search.grid(row=0, column=0, padx=(200,50))

search_button = customtkinter.CTkButton(search_frame, text="Search")
search_button.grid(row=0,column=2)

clear = customtkinter.CTkButton( search_frame, text="Clear")

option_frame = customtkinter.CTkFrame(master = root, width=1000, height=50)
option_frame.grid_rowconfigure(4, weight=1)


























root.mainloop()