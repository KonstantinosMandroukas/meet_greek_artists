#THIS IS NOT USABLE ANYMORE

'''libraries'''
import customtkinter
import tkinter as tk
from PIL import Image, ImageTk
from time import *
import os




''' app apearance'''
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


singers = ['Alkistis Protopsalti', 'Anna Vissi', 'Antonis Remos', 'Atzela Dimitriou', 'Basilis Papakonstantinou', 'Despoina Vandi', 'Dimitra Galani', 'Dimitris Mitropanos', 'Dionisis Sxoinas', 'Dionisys Savopoulos', 'Eleftheria Arvanitaki', 'Elena Paparizou', 'Eleni Foureira', 'Elli Kokkinou', 'Giannis Kotsiras', 'Giannis Ploutarxos', 'Giorgos Dalaras', 'Giorgos Mazonakis', 'Giorgos Sabanis', 'Haris Alexiou', 'Hmiskoumpria', 'Ivi Adamou', 'Konstantinos Argiros', 'Kostis Maravelias', 'Lavredis Maxairitsas', 'Lefteris Pantazis', 'Maria Farantouri', 'Marinela', 'Melisses', 'Mixalis Hatziganns', 'Natasa Mpofiliou', 'Natasa Theodoridou', 'Nikos Oikonomopoulos', 'Nikos Vertis', 'Nikos Xiloiris', 'Notis Sfakianakis', 'Panos Kiamos', 'Panos Mouzourakis', 'Pix Lax', 'Sakis Rouvas', 'Stamatis Gonidis', 'Stavento', 'Stelios Rokkos', 'Stratos Dionisiou', 'Tamta', 'Themis Adamantidis', 'Vaggelis Kakouriotis', 'Vasilis Karras']

actors = ["Giannis Bezos", "Markos Seferlis", "Vaso Laskaraki"]

''' app layout '''


root = customtkinter.CTk()
root.title("Meet greek artists")
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()
root.geometry("1500x900")
# root.geometry(f"{screen_width-10}x{screen_height-10}")
# root.resizable(False, False)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure((2, 3), weight=0)
root.grid_rowconfigure((0, 1, 2), weight=1)



'''tab view'''


tabs = customtkinter.CTkTabview( root, width=1100, height=750)
artist_text = tabs.add("Text")
artist_photo = tabs.add("Photos")
artist_listen = tabs.add("Listen/Plays")

def clear_tab(tab):
    for widget in tab.winfo_children():
        widget.grid_forget()
        
tabs.winfo_children

def Clear_tabs():
    clear_tab(artist_photo)
    clear_tab(artist_text)
    clear_tab(artist_listen)
    

'''app icon'''


# icon_path = "C:/Users/konma/Documents/vs code-programming/meet greek artists/artist_images/logo.ico"

# root.wm_iconbitmap(icon_path)
    


''' artist functions'''

def Rouvas():
    Clear_tabs()
    tabs.grid(row=0, column=1, padx=(20,0), pady=(50,40))
    rouvas_label.grid(row=0, column=0)
    rouvas_text.grid(row=1, column=0)
    # image_rouvas_res.place(x=0, y = 10)
    visit_spot.grid(row=0, column=0, padx=50)
    visit_yt.grid(row=0, column=2)
    # rouvas_youtube.place(x=300, y=30)
    # rouvas_spotify.place(x=0, y=30)
    root_label.grid_forget()

def Argiros():
    Clear_tabs()
    tabs.grid(row=0, column=1, padx=(20,0), pady=(50,40))
    argiros_label.grid(row=0,column=0)
    argiros_text.grid(row=1, column=0)
    # image_argiros_res.place(x=200, y=200)
    visit_spot.grid(row=0, column=0, padx=50)
    visit_yt.grid(row=0, column=2)
    # argiros_spotify.place(x=0,y=30)
    # argiros_youtube.place(x=300,y=30)
    root_label.grid_forget()
     
        
def Bezos():
    Clear_tabs()
    tabs.grid(row=0, column=1, padx=(20,0), pady=(50,40))
    bezos_label.grid(row=0, column=0)
    bezos_text.grid(row=1, column=0, padx=(0,80), pady=(0,80))
    # image_bezos_res.place(x=0, y=0)
    visit.grid(row=0,column=0)
    go.grid(row=1,column=0)
    root_label.grid_forget()
    
def Seferlis():
    Clear_tabs()
    tabs.grid(row=0, column=1, padx=(20,0), pady=(50,40))
    seferlis_label.grid(row=0, column=0)
    seferlis_text.grid(row=1, column=0, padx=(0,80), pady=(0,80))
    # image_seferlis_res.place(x=0, y=0)
    visit.grid(row=0,column=0)
    go.grid(row=1,column=0)
    root_label.grid_forget()
    
    
    
    
'''general functions'''    


def change_scaling_event(new_scaling: str):
    new_scaling_float = int(new_scaling.replace("%", "")) / 100
    customtkinter.set_widget_scaling(new_scaling_float)
    
# def change_scaling_event(scaling: str):
#     customtkinter.set_widget_scaling(scaling)


    
def Select_artist_category(category):
    Clear_tabs()
    if category == "Singers":
        '''place'''
        rouvas.grid(padx=3, pady=0)
        argiros.grid(padx=3, pady=10)
        bezos.grid_forget()
        seferlis.grid_forget()

        option_1.place_forget()
        root_label.grid_forget()
        go.place_forget()
        visit.place_forget()
    elif category == "Actors":
        '''place'''
        bezos.grid(padx=3, pady=0)
        seferlis.grid(padx=3, pady=10)
        '''place forget'''
        rouvas.grid_forget()
        argiros.grid_forget()


        option_1.place_forget()
        root_label.grid_forget()
        go.place_forget()
        visit.place_forget()

    
 

def Set_Themes(choise):
    customtkinter.set_appearance_mode(choise)


def Search():
    tabs.grid_forget()
    root_label.grid_forget()
    search_text = search.get().lower()
    clear.grid(row=0, column=0, padx=(0,500))

    
    def Go():
        
        option_1.grid_forget()

        
        choise = search_text
        if choise == "sakis rouvas" or choise == "rouvas":
            Rouvas()
        elif choise == "konstantinos argiros" or choise == "argiros":
            Argiros()
        elif choise == "giannis bezos" or choise == "bezos":
            Bezos()
        elif choise == "markos seferlis" or choise == "seferlis":
            Seferlis()     

    if "sakis rouvas" in search_text or "rouvas" in search_text:
        option_1.grid(row=0, column=1)
        label_argiros.place_forget()
        label_rouvas.place(x=1, y=1)
        label_bezos.place_forget()
        label_seferlis.place_forget()
        go = customtkinter.CTkButton( option_1, text="Go", command=Go)
        go.place(x=850, y=1)
        
    elif "konstantinos argiros" in search_text or "argiros" in search_text:
        label.place_forget()
        label_rouvas.place_forget()
        label_argiros.place(x=1, y=1)
        label_seferlis.place_forget()
        label_bezos.place_forget()
        go = customtkinter.CTkButton( option_1, text="Go", command=Go)
        go.place(x=850, y=1)
        
    elif "giannis bezos" in search_text or "bezos" in search_text:
        label.place_forget()
        label_argiros.place_forget()
        label_rouvas.place_forget()
        label_bezos.place(x=1, y=1)
        label_seferlis.place_forget()
        go = customtkinter.CTkButton( option_1, text="Go", command=Go)
        go.place(x=850, y=1)
        
    elif "markos seferlis" in search_text or "seferlis" in search_text:
        label.place_forget()
        label_bezos.place_forget()
        label_rouvas.place_forget()
        label_argiros.place_forget()
        label_seferlis.place(x=1, y=1)
        go = customtkinter.CTkButton( option_1, text="Go", command=Go)
        go.place(x=850, y=1)
        
    else:
        label_argiros.place_forget()
        label_rouvas.place_forget()
        label_bezos.place_forget()
        label_seferlis.place_forget()
        option_1.grid(row=0, column=1)
        label.place(x=1, y=1)

        
        

def open_website(url):
    # Construct the appropriate command based on the operating system
    if os.name == 'nt':  # For Windows
        os.system(f'start {url}')
    elif os.name == 'posix':  # For Linux, macOS, etc.
        os.system(f'xdg-open {url}')
    else:
        raise Exception("Unsupported operating system")

def Go():
    open_website("https://www.more.com/")

def yt_link(link:str):
    open_website(link)
def spotify_link(link:str):
    open_website(link)
    



        
def Clear():
    search.delete(0, tk.END)
    option_1.place_forget()



def Home_button():
    root_label.grid(row=1, column=1, padx=(0,80), pady=(0,20))
    tabs.grid_forget()
    bezos.grid_forget()
    rouvas.grid_forget()
    argiros.grid_forget()
    seferlis.grid_forget()
    option_1.grid_forget()




'''general '''

#side frame widgets

frame = customtkinter.CTkFrame(root, width=250, height=900) 
frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
frame.grid_rowconfigure(4, weight=1)

select_label = customtkinter.CTkLabel(frame, text="Select an artist", font=("Arial", 20)) 
select_label.place(x=30, y= 2)

home_button = customtkinter.CTkButton( frame, text="Home", command=Home_button)
home_button.grid(row=1,column=0, padx=(10,100), pady=(50,0))

select_artist_category_values = ["Actors", "Singers"]
select_artist_category = customtkinter.CTkComboBox( frame, values=select_artist_category_values, command=Select_artist_category)
select_artist_category.grid(row=2, column=0, padx=(10,100), pady=(30,0))

scrolable_frame = customtkinter.CTkScrollableFrame(frame, width=200, height=350)
scrolable_frame.grid(row=3, column=0, padx=(20, 50), pady=(30, 0), sticky="s")
scrolable_frame.grid_columnconfigure(0, weight=1)

set_theme_values = ["Light", "Dark", "System"]
set_theme = customtkinter.CTkComboBox( root, values=set_theme_values , command=Set_Themes)
set_theme.grid(row=4, column=0, padx=(0,80), pady=(5,50))

scaling_optionemenu = customtkinter.CTkComboBox( root, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=change_scaling_event)
scaling_optionemenu.grid(row=5, column=0, padx=(0,80), pady=(0,70))





#search frame widgets

search_frame = customtkinter.CTkFrame( root, width=700, height=80)
search_frame.grid(row=0, column=1, pady=(0,80), padx=(0,100), sticky="n")
# search_frame.grid_columnconfigure(0, weight=1)

search = customtkinter.CTkEntry( search_frame, placeholder_text="Search an artist (Example: 'Konstantinos Argiros')", width=310, height=40, corner_radius=45)
search.grid(row=0, column=0, padx=(200,50))

search_button = customtkinter.CTkButton(search_frame, text="Search", command=Search)
search_button.grid(row=0,column=2)

clear = customtkinter.CTkButton( search_frame, text="Clear", command=Clear)

option_1 = customtkinter.CTkFrame(master = root, width=1000, height=50)
option_1.grid_rowconfigure(4, weight=1)

label = customtkinter.CTkLabel( option_1, text="No results found.")

#root widgets

root_label = customtkinter.CTkLabel( root, text="Select an artist and learn more about him/her", font=("Arial", 20)) 
root_label.grid(row=1, column=1, padx=(0,80), pady=(0,20))



#artist's general widgets

# spotify_image = customtkinter.CTkImage(dark_image= Image.open("C:/Users/konma/Documents/vs code-programming/meet greek artists/artist_images/spotify.png"), light_image= Image.open("C:/Users/konma/Documents/vs code-programming/meet greek artists/artist_images/spotify.png"), size=(200, 200))
# youtube_image = customtkinter.CTkImage(dark_image=Image.open("C:/Users/konma/Documents/vs code-programming/meet greek artists/artist_images/youtube.png"), light_image=Image.open("C:/Users/konma/Documents/vs code-programming/meet greek artists/artist_images/youtube.png"), size=(200, 200))

visit_spot = customtkinter.CTkLabel( artist_listen, text="Visit Spotify:", font=("Arial", 25, "bold"))
visit_yt = customtkinter.CTkLabel( artist_listen, text="Visit YouTube:", font=("Arial", 25, "bold"))


go = customtkinter.CTkButton( artist_listen, text="Go", command=Go, width=100,height=30)

visit = customtkinter.CTkLabel( artist_listen, text="You can visit 'more.com' to learn more \nabout current plays where the artist might be performing on.", font=("Aria",20,"bold"))




'''artist buttons'''

#actors
bezos = customtkinter.CTkButton( scrolable_frame, text="Giannis Bezos", command=Bezos)
bezos_text = customtkinter.CTkLabel( artist_text, text="Bezos")
# image_bezos = customtkinter.CTkImage(light_image=Image.open("C:/Users/konma/Documents/vs code-programming/meet greek artists/artist_images/bezos.png"), dark_image=Image.open("C:/Users/konma/Documents/vs code-programming/meet greek artists/artist_images/bezos.png"), size=(800, 450))
# image_bezos_res = customtkinter.CTkLabel(  artist_photo, text=" ", image=image_bezos)
bezos_label = customtkinter.CTkLabel( artist_text, text="Giannis Bezos", font=("Aria", 30, "bold"))

label_bezos = customtkinter.CTkLabel( option_1, text="Are you looking for: Giannis Bezos")

seferlis = customtkinter.CTkButton( scrolable_frame, text="Markos Seferlis", command=Seferlis)
seferlis_text = customtkinter.CTkLabel( artist_text, text="Seferlis")
# image_seferlis = customtkinter.CTkImage(light_image=Image.open("C:/Users/konma/Documents/vs code-programming/meet greek artists/artist_images/seferlis.jpg"), dark_image=Image.open("C:/Users/konma/Documents/vs code-programming/meet greek artists/artist_images/seferlis.jpg"), size=(1200, 700))
# image_seferlis_res = customtkinter.CTkLabel( artist_photo, text=" ", image=image_seferlis)
seferlis_label = customtkinter.CTkLabel( artist_text, text="Markos Seferlis", font=("Arial", 30, "bold"))

label_seferlis = customtkinter.CTkLabel( option_1, text="Are you looking for: Markos Seferlis")

#singers

rouvas = customtkinter.CTkButton( scrolable_frame, text="Sakis Rouvas", command=Rouvas)
rouvas_text = customtkinter.CTkLabel( artist_text, text="Born and raised in the island of Corfu, Sakis Rouvas started his music career in 1991, at the Thessaloniki Song Festival. \nSince then, he has steadily been at the top of the Greek music scene and show-biz with numerous distinctions among different fields, \nas he has received the Best New Singer, Best Song and the “Karolos Koun” Award for Best Stage Performance, \nas well as many other national and international awards.\nHis multitalented personality has been demonstrated through his leading roles in cinema, ancient drama and Hollywood movies, \nas well as through his participation in popular TV shows and large-scale events, including the 2004 Athens Olympics Closing Ceremony and the \nEurovision Song Contest, \nwhere he successfully represented Greece in 2004 and 2009. \nParallel to his career, Sakis has participated in several initiatives that aim to raise awareness for the protection of the environment \nand has demonstrated a long-term commitment to supporting children in need, while being himself a caring father of four.", font=("Arial", 17))
# image_rouvas = customtkinter.CTkImage(light_image=Image.open("C:/Users/konma/Documents/vs code-programming/meet greek artists/artist_images/rouvas.png"), dark_image=Image.open("C:/Users/konma/Documents/vs code-programming/meet greek artists/artist_images/rouvas.png"), size=(400, 400))
# image_rouvas_res = customtkinter.CTkLabel( artist_photo, text=" ", image=image_rouvas)
rouvas_label = customtkinter.CTkLabel(master = artist_text, text="Sakis Rouvas", font=("Arial", 30, "bold"))
label_rouvas = customtkinter.CTkLabel( option_1, text="Are you looking for: Sakis Rouvas")
# rouvas_spotify = customtkinter.CTkButton( artist_listen, text=" ", command=lambda:spotify_link("https://open.spotify.com/artist/0VuyN0xzSqykiDB2MxihTe"), width=-1000, height=-1000, image=spotify_image, fg_color="#153f25", hover_color="#1d5833", corner_radius=100)
# rouvas_youtube = customtkinter.CTkButton( artist_listen, text=" ", image=youtube_image, fg_color="#9c2f21", hover_color="#B54537", corner_radius=100, command=lambda:yt_link("https://www.youtube.com/@SakisRouvas"))






argiros = customtkinter.CTkButton( scrolable_frame, text="Konstantinos Argiros", command=Argiros)
argiros_text = customtkinter.CTkLabel( artist_text, text="argiros", font=("Arial", 17))
# image_argiros = customtkinter.CTkImage(light_image=Image.open("C:/Users/konma/Documents/vs code-programming/meet greek artists/artist_images/argiros.png"), dark_image=Image.open("C:/Users/konma/Documents/vs code-programming/meet greek artists/artist_images/argiros.png"), size=(350, 400))
# image_argiros_res = customtkinter.CTkLabel( artist_photo, text=" ", image=image_argiros)
argiros_label = customtkinter.CTkLabel(master = artist_text, text="Konstantinos Argiros", font=("Arial", 30, "bold"))

label_argiros = customtkinter.CTkLabel( option_1, text="Are you looking for: Konstantinos Argiros")
# argiros_spotify = customtkinter.CTkButton( artist_listen, text=" ", command=lambda:spotify_link("https://open.spotify.com/artist/5YquORfLTx6nWMlBzJstx7"), width=-1000, height=-1000, image=spotify_image, fg_color="#153f25", hover_color="#1d5833", corner_radius=100)
# argiros_youtube = customtkinter.CTkButton( artist_listen, text=" ", image=youtube_image, fg_color="#9c2f21", hover_color="#B54537", corner_radius=100, command=lambda:yt_link("https://www.youtube.com/channel/UCcvaYRhzNq5wUo9Ssbw6KUQ"))











root.mainloop()