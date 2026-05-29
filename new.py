import customtkinter
import tkinter as tk
from PIL import Image, ImageTk, UnidentifiedImageError, ImageOps
import os
import requests
from io import BytesIO
from CTkMessagebox import CTkMessagebox
import psycopg
from mail import Send_Email
from dotenv import load_dotenv

''' app apearance'''
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

''' app layout '''
root = customtkinter.CTk()
root.title("Meet greek artists")
root.geometry("1500x900")
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure((2, 3), weight=0)
root.grid_rowconfigure((0, 1, 2), weight=1)


load_dotenv()

'''Database connection'''
db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('DB_PORT')
db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASS')
db_name = os.environ.get('DB_NAME')




mydb = psycopg.connect(
    host = db_host,
    user = db_user,
    password = db_pass,
    dbname = db_name,
    port = db_port,
    sslmode='require'
) 

cursor = mydb.cursor()



#old-host: db.tznssyoujmjylijfqevh.supabase.co
    

'''app icon'''
icon_path = "C:/Users/konma/Documents/vs code-programming/meet greek artists/artist_images/logo.ico"
root.wm_iconbitmap(icon_path)

'''Tab View'''
tabs = customtkinter.CTkTabview(root, width=1100, height=750)
artist_text = tabs.add("Text")
artist_photo = tabs.add("Photos")
artist_listen = tabs.add("Listen/Plays")

'''funtions'''

def open_website(url): #To open websites/connected to buttons
    # Construct the appropriate command based on the operating system
    if os.name == 'nt':  # For Windows
        os.system(f'start {url}')
    elif os.name == 'posix':  # For Linux, macOS, etc.
        os.system(f'xdg-open {url}')
    else:
        raise Exception("Unsupported operating system")
    

def Send_mail(action, window,**info):
    if action == 'report':
        txt_mail = Send_Email(f"Problem: {info['problem']}", action)
    elif action == 'request':
        txt_mail = Send_Email(f"name = {info['name']}\ncategory = {info['category']}", action)
    txt_mail.send()
    window.destroy() 
    
    
def report_problem():
    win = customtkinter.CTkToplevel()
    win.title('Report a problem')
    win.geometry('400x400')
    win.resizable(False, False)
    win.lift()
    win.focus_force()
    win.attributes('-topmost', True)
    
    label = customtkinter.CTkLabel(master=win, text='Describe the problem in the field below:')
    label.pack()
    entry = customtkinter.CTkTextbox(master=win,width=300, height=200)
    entry.pack()
    button = customtkinter.CTkButton(master=win, text='Send Problem', command=lambda:Send_mail(action='report', window=win, problem = entry.get()))
    button.pack(pady=50)    
    
def request_artist():
    win = customtkinter.CTkToplevel()
    win.title('Request an artist')
    win.geometry('400x400')
    win.resizable(False, False)
    win.lift()
    win.focus_force()
    win.attributes('-topmost',True)
    
    name_label = customtkinter.CTkLabel(win, text="Enter artist's name:")
    name_label.pack()
    name_entry = customtkinter.CTkEntry(win, placeholder_text='Name')
    name_entry.pack()
    artist_category_label = customtkinter.CTkLabel(win, text="Select the artist's category")
    artist_category_label.pack()
    artist_category_values = ["Actor", "Singer"]
    artist_category = customtkinter.CTkComboBox(win, values=artist_category_values)
    artist_category.pack()
    choise = artist_category.get()
    # category = 'actor' if choise == 'actor' else category == 'singer'
    btn_ok = customtkinter.CTkButton(win, text='Send Request', command=lambda:Send_mail(action='request',window=win,name=name_entry.get(), category=choise))
    btn_ok.pack(pady=100)
    
def fit_image(image_path, target_width, target_height):
    with Image.open(image_path) as img:
        # Contain resizes the image to fit inside the bounding box
        resized_img = ImageOps.contain(img, (target_width, target_height))
        return resized_img
 
def Get_infoAndDisplay(bt_val:str): #Displaying info (text / photo / yt or spotify links)
    Clear_tabs()
    not_found_label.configure(text='')
    tabs.grid(row=0, column=1, padx=(20,0), pady=(50,40))
    option_frame.grid_forget()
    root_label.grid_forget()

    # robust parsing: support "First Last" and single-name artists
    parts = bt_val.split()
    if len(parts) >= 2:
        first_name = parts[0]
        last_name = parts[-1]
    else:
        first_name = parts[0]
        last_name = None
        

    '''display text'''
    if last_name:
        sq = "SELECT info FROM artists_all WHERE first_name = %s AND last_name = %s"
        cursor.execute(sq, (first_name, last_name))
    else:
        sq = "SELECT info FROM artists_all WHERE first_name = %s"
        val = [(first_name)]
        cursor.execute(sq, val)
    results = cursor.fetchall()
    if results and results[0][0]:
        text_label = customtkinter.CTkLabel(artist_text, text=(results[0][0]), font=("Arial", 16))
        text_label.grid(row=1, column=0)
    else:
        text_label = customtkinter.CTkLabel(artist_text, text=(f"No text found for {bt_val}. Please contact the creator for more information"), font=("Arial", 16))
        text_label.grid(row=1, column=1)
    name_label.configure(text=f"You are currently looking at\n{bt_val}")
    '''display other info'''
    sq = "SELECT * FROM artists_all WHERE id = 'singer' AND first_name = %s AND last_name = %s"
    # val = [(bt_val)]
    cursor.execute(sq,(first_name, last_name))
    results = cursor.fetchall()
    if len(results) > 0: 
        #Get Spotify links
        sq = "SELECT spotify_link FROM artists_all WHERE first_name = %s AND last_name = %s"
        # val = [(bt_val)]
        cursor.execute(sq, (first_name, last_name))
        results = cursor.fetchall()
        results_str = results[0][0] if results and results[0] else None
        if results_str:
            spotify_text = customtkinter.CTkLabel(artist_listen, text="Spotify", font=("Arial", 20, "bold"))
            spotify_text.grid(row=0, column=0)
            spotify = customtkinter.CTkButton(artist_listen, text=" ", command=lambda:open_website(results_str), width=-1000, height=-1000, fg_color="#153f25", hover_color="#1d5833", corner_radius=100, image=customtkinter.CTkImage(dark_image= Image.open("C:/Users/konma/Documents/vs code-programming/meet greek artists/artist_images/spotify.png"), light_image= Image.open("C:/Users/konma/Documents/vs code-programming/meet greek artists/artist_images/spotify.png"), size=(200, 200)))
            spotify.grid(row=1, column=0)

        #Get Yt Links
        sq = "SELECT yt_link FROM artists_all WHERE first_name = %s AND last_name = %s"
        val = [(bt_val)]
        cursor.execute(sq, (first_name, last_name))
        results = cursor.fetchall()
        results_str2 = results[0][0] if results and results[0] else None
        if results_str2:
            youtube_text = customtkinter.CTkLabel(artist_listen, text="YouTube", font=("Arial", 20, "bold"))
            youtube_text.grid(row=0, column=1)
            youtube = customtkinter.CTkButton(artist_listen, text=" ", command=lambda:open_website(results_str2), width=-1000, height=-1000, fg_color="#9c2f21", hover_color="#B54537", corner_radius=100, image=customtkinter.CTkImage(dark_image= Image.open("C:/Users/konma/Documents/vs code-programming/meet greek artists/artist_images/youtube.png"), light_image= Image.open("C:/Users/konma/Documents/vs code-programming/meet greek artists/artist_images/youtube.png"), size=(200, 200)))
            youtube.grid(row=1, column=1)

        morecom_text = customtkinter.CTkLabel(artist_listen, text="More.com", font=("Arial", 20, "bold"))
        morecom_text.grid(row=0, column=2)
        morecom = customtkinter.CTkButton(artist_listen, text=" ", command=lambda:open_website("https://www.more.com/el/tickets/music/"), width=-100, height=-100, fg_color="#C4E816", hover_color="#A2C10F", image=customtkinter.CTkImage(dark_image = Image.open("C:/Users/konma/Documents/vs code-programming/meet greek artists/artist_images/more.jpg"),light_image = Image.open("C:/Users/konma/Documents/vs code-programming/meet greek artists/artist_images/more.jpg"), size=(200,200)))
        morecom.grid(row=1, column=2)
    else:
        morecom_text = customtkinter.CTkLabel(artist_listen, text="For more information about plays that the artist\nmight be performing on visit more.com", font=("Arial", 20))
        morecom_text.grid(row=0, column=1)
        morecom = customtkinter.CTkButton(artist_listen, text=" ", command=lambda:open_website("https://www.more.com/el/tickets/theatre/"), width=-100, height=-100, fg_color="#C4E816", hover_color="#A2C10F", image=customtkinter.CTkImage(dark_image = Image.open("C:/Users/konma/Documents/vs code-programming/meet greek artists/artist_images/more.jpg"),light_image = Image.open("C:/Users/konma/Documents/vs code-programming/meet greek artists/artist_images/more.jpg"), size=(200,200)))
        morecom.grid(row=1, column=1)
    '''display image'''
    # Get image link from database (handle single-name artists as well)
    if last_name:
        sq = "SELECT image_link FROM artists_all WHERE first_name = %s AND last_name = %s"
        cursor.execute(sq, (first_name, last_name))
    else:
        sq = "SELECT image_link FROM artists_all WHERE first_name = %s"
        cursor.execute(sq, (first_name,))
    results2 = cursor.fetchall()

    if not results2 or not results2[0] or not results2[0][0]:
        no_img_found_label.configure(text=f'There is not an available image for {bt_val} right now.')
        no_img_found_label.grid(row=0, column=0)
    else:
        image_path = str(results2[0][0]).strip()
        try:
            # If the path is a URL, fetch it; otherwise treat it as local file path.
            if image_path.lower().startswith(("http://", "https://")):
                response = requests.get(image_path, timeout=5)
                response.raise_for_status()
                img = Image.open(BytesIO(response.content))
            else:
                # Make relative paths absolute to the script directory
                if not os.path.isabs(image_path):
                    base_dir = os.path.dirname(__file__)
                    image_path = os.path.join(base_dir, image_path)
                img = Image.open(image_path)

            # Use actual widget sizes (fallback to sensible defaults if small)
            # width, height = tabs.winfo_width(), tabs.winfo_height()
            # if width < 50:
            #     width = 600
            # if height < 50:
            #     height = 400 
        
            width, height = img.width, img.height
            if (width > tabs.winfo_width() and height > tabs.winfo_height()) or (width > tabs.winfo_width() or height > tabs.winfo_height()):
                width  = width / 2
                height = height / 2         
                
            artist_image = customtkinter.CTkImage(light_image=img, dark_image=img, size=(width, height))
            image_res = customtkinter.CTkLabel(artist_photo, image=artist_image, text="")
            image_res.grid(row=0, column=0)
        except (requests.exceptions.RequestException, UnidentifiedImageError, OSError) as e:
            not_found_label.configure(text=f'Unable to load the image for {bt_val}. Please check the path or your internet connection.')
            not_found_label.grid(row=1, column=1)
            CTkMessagebox(title="Image Error", message="Cannot load image — please check the path or your connection.")
            return None  # Stop further processing when image loading fails

def clear_frame(frame):  #customtkinter.CTkFrame or customtkinter.CTkScrollableFrame #clears a specific frame
    for widget in frame.winfo_children():
        widget.grid_forget()

def clear_tab(tab): #customtkinter.CTkTabView #clears a specific tab
    for widget in tab.winfo_children():
        widget.grid_forget()

def Clear_tabs():   #clears the tabview all together
    clear_tab(artist_photo)
    clear_tab(artist_text)
    clear_tab(artist_listen)
        
def Clear(): #clears the search bar
    search.delete(0, tk.END)

def change_scaling_event(new_scaling: str):  #changes the scaling of the app
    new_scaling_float = int(new_scaling.replace("%", "")) / 100
    customtkinter.set_widget_scaling(new_scaling_float)
    
def Select_artist_category(choise): #depends on the users selection. It connects to the database and gets the actors or the singers.
    name_label.configure(text='')
    clear_frame(scrolable_frame)
    Clear_tabs()
    if choise == "Singers":
        clear_frame(scrolable_frame)
        sq = "SELECT first_name, last_name FROM artists_all WHERE id = 'singer'"
        cursor.execute(sq)
        results = cursor.fetchall()
        results.sort(key=lambda x: (x[0], x[1]))
        counter = 0
        rowx = 1
        columny = 0
        paddx = 10
        paddy = 10

        for first_name, last_name in results:
            full_name = f"{first_name} {last_name}"
            button = customtkinter.CTkButton(scrolable_frame, text=full_name, command=lambda bt_val=full_name: Get_infoAndDisplay(bt_val))
            button.grid(row=rowx, column=columny, padx=paddx, pady=paddy)
            rowx += 4
            counter += 1
            
        req_button = customtkinter.CTkButton(scrolable_frame, text='Request and artist', fg_color='red', command=lambda:request_artist())
        req_button.grid(row=rowx, column=columny, padx=paddx, pady=paddy)
        
        
        
    elif choise == "Actors":
        clear_frame(scrolable_frame)
        sq = "SELECT first_name, last_name FROM artists_all WHERE id = 'actor'"
        cursor.execute(sq)
        results = cursor.fetchall()
        results.sort(key=lambda x: (x[0], x[1]))
        
                
        counter = 0
        rowx = 1
        columny = 0
        paddx = 10
        paddy = 10

        for first_name, last_name in results:
            full_name = f"{first_name} {last_name}"
            button = customtkinter.CTkButton(scrolable_frame, text=full_name, command=lambda bt_val=full_name: Get_infoAndDisplay(bt_val))
            button.grid(row=rowx, column=columny, padx=paddx, pady=paddy)
            rowx += 4
            counter += 1
            
        req_button = customtkinter.CTkButton(scrolable_frame, text='Request and artist', fg_color='red',hover_color='red', command=lambda:request_artist())
        req_button.grid(row=rowx, column=columny, padx=paddx, pady=paddy)
            
def Search(): #handles the searching   
    tabs.grid_forget()
    root_label.grid_forget()
    clear.grid(row=0, column=0, padx=(0,500))
    user_input = search.get().strip()
    option_frame.grid(row=0, column=1, sticky="s")
    if not user_input:
        return

    clear_frame(option_frame)

    parts = user_input.split()
    first = parts[0].lower()
    last = parts[-1].lower() 
    full_name = f"{first} {last}"

    def add_buttons(rows):
        option_frame.grid(row=0, column=1, sticky="s")
        for i, (fn, ln) in enumerate(rows):
            # build full name safely (handle None or empty last names)
            full_name = fn if not ln else f"{fn} {ln}"
            btn = customtkinter.CTkButton(
                option_frame,
                text=full_name,
                command=lambda: Get_infoAndDisplay(full_name)
            )
            btn.grid(row=1 + i, column=1, pady=5)

    # normalize to lowercase for case-insensitive matching in SQL
    if len(parts) >= 2:
        name = parts[0].lower()
         # allow middle names by taking last token as last name
        sq = "SELECT first_name, last_name FROM artists_all WHERE LOWER(first_name) = %s AND LOWER(last_name) = %s"
        cursor.execute(sq, (first,last))
        results = cursor.fetchall()

        if results:
            add_buttons(results)
        else:
            # fallback: search by last name in artist_search
            sq = "SELECT first_name, last_name FROM artists_all WHERE LOWER(last_name) = %s"
            cursor.execute(sq, last)
            results = cursor.fetchall()
            if results:
                add_buttons(results)
            else:
                not_found_label.configure(text=f"No artist found for '{user_input}'")
                not_found_label.grid(row=0, column=0)
    
    else:
        # single-word search: try first name or last name
        name = parts[0].lower()
        sq = "SELECT first_name, last_name FROM artists_all WHERE LOWER(first_name) = %s OR LOWER(last_name) = %s"
        cursor.execute(sq, (first, last))
        results = cursor.fetchall()
        if results:
            # normalize None last names to empty string so add_buttons builds names correctly
            normalized = [(fn, ln if ln is not None else "") for fn, ln in results]
            add_buttons(normalized)
        else:
            not_found_label.configure(text=f"No artist found for '{user_input}'")
            not_found_label.grid(row=0, column=0)
            
     
def Set_Themes(choise): #changes the theme of the app
    customtkinter.set_appearance_mode(choise)

def Home_button():
    Clear()#Resets everything to its first appearance
    clear_frame(scrolable_frame)
    tabs.grid_forget()
    root_label.grid(row=1, column=1, padx=(0,80), pady=(0,20))
    option_frame.grid_forget()
    name_label.configure(text="")

'''general'''

#side frame widgets

frame = customtkinter.CTkFrame(root, width=250, height=900) 
frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
frame.grid_rowconfigure(4, weight=1)

select_label = customtkinter.CTkLabel(frame, text="Select an artist", font=("Arial", 20)) 
select_label.grid(row=0,column=0)

home_button = customtkinter.CTkButton( frame, text="Home", command=Home_button)
home_button.grid(row=1,column=0, padx=(10,100), pady=(50,0))

select_artist_category_values = ["Actors", "Singers"]
select_artist_category = customtkinter.CTkComboBox( frame, values=select_artist_category_values, command=Select_artist_category)
select_artist_category.grid(row=2, column=0, padx=(10,100), pady=(30,0))

scrolable_frame = customtkinter.CTkScrollableFrame(frame, width=200, height=350)
scrolable_frame.grid(row=3, column=0, padx=(20, 50), pady=(30, 0), sticky="s")
scrolable_frame.grid_columnconfigure(0, weight=1)

#set theme/scaling
set_theme_values = ["Light", "Dark", "System"]
set_theme = customtkinter.CTkComboBox( root, values=set_theme_values , command=Set_Themes)
set_theme.grid(row=4, column=0, padx=(0,80), pady=(5,50))

scaling_optionemenu = customtkinter.CTkOptionMenu( root, values=["80%", "90%", "100%", "110%", "120%","130%"], command=change_scaling_event, dynamic_resizing=False)
scaling_optionemenu.grid(row=5, column=0, padx=(0,80), pady=(0,70))


report_button = customtkinter.CTkButton(root, text='⚠️ Report a problem', command=lambda:report_problem())
report_button.grid(row=5, column=0, padx=(0,80), pady=(50,10))

#search frame widgets

search_frame = customtkinter.CTkFrame( root, width=700, height=80)
search_frame.grid(row=0, column=1, pady=(0,80), padx=(0,100), sticky="n")

search = customtkinter.CTkEntry( search_frame, placeholder_text="Search an artist (e.g: 'Sakis Rouvas')", width=310, height=40, corner_radius=45)
search.grid(row=0, column=0, padx=(200,50))
search.bind("<Return>", lambda e: Search()) #when user presses 'enter' the search happens

search_button = customtkinter.CTkButton(search_frame, text="Search", command=Search)
search_button.grid(row=0,column=2)

clear = customtkinter.CTkButton( search_frame, text="Clear", command=Clear)

option_frame = customtkinter.CTkFrame(master = root, width=1000, height=50)
option_frame.grid_rowconfigure(4, weight=1)

#root widgets

root_label = customtkinter.CTkLabel( root, text="Select an artist and learn more about them", font=("Arial", 20)) 
root_label.grid(row=1, column=1, padx=(0,80), pady=(0,20))

#display artist name

name_label = customtkinter.CTkLabel(frame, text=f"")
name_label.grid(row=4,column=0)

#general labels
not_found_label = customtkinter.CTkLabel(option_frame,text='', font=('Arial',16)) #for when there is not an image for an artist
not_found_label.grid(row=0,column=0)

no_img_found_label = customtkinter.CTkLabel(artist_photo,text='', font=('Arial',16)) #for when there is not an image for an artist
no_img_found_label.grid(row=0,column=0)



root.mainloop()
