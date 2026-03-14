import mysql.connector


# Creating connection object 
#credentials for local db connection
mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "admin123",
    database = "meet_greek_artists"
)

cursor = mydb.cursor()
# actors = ['Adreas Barkoulis', 'Alekos Alexandrakis', 'Alexandros Mpourdoumis', 'Aliki Vougiouklaki', 'Alina Kotsovoulou', 'Anna Panagiotopoulou', 'Antonis Antoniou', 'Antonis Loudaros', 'Argiris Aggelou', 'Dimitris Papamixahl', 'Dionisis Papagianopoulos', 'Efi Papathoeodorou', 'Eirini Koumarianou', 'Eleni Kokkidou', 'Eleni Rantou', 'Elisavet Konstantinidou', 'Giannis Tsimitselis', 'Giorgos Kapoutzidis', 'Giorgos Konstantinou', 'Katerina Geronikolou', 'Katerina Lexou', 'Kostas Voutsas', 'Kostas Xatzichristos', 'Labros Konstantaras', 'Melina Merkouri', 'Michalis Reppas', 'Mimis Fotopoulos', 'Mirka Papakonstantinou', 'Nikos Kourkoulos', 'Nikos Rizos', 'Ntinos Iliopoulos', 'Orestis Makris', 'Paulos Orkopoulos', 'Renia Louizidou', 'Smaragda Karidi', 'Stamatis Fasoulis', 'Tasos Giannopoulos', 'Thanasis Tsaltabasis', 'Thansis Veggos', 'Thodoris Atheridis', 'Vasilis Avlonitis', 'Vasilis Logothetidis', 'Viki Stavropoulou', 'Vladimiros Kiriakidis']


# singers = ['Alkistis Protopsalti', 'Anna Vissi', 'Antonis Remos', 'Atzela Dimitriou', 'Basilis Papakonstantinou', 'Despoina Vandi', 'Dimitra Galani', 'Dimitris Mitropanos', 'Dionisis Sxoinas', 'Dionisys Savopoulos', 'Eleftheria Arvanitaki', 'Elena Paparizou', 'Eleni Foureira', 'Elli Kokkinou', 'Giannis Kotsiras', 'Giannis Ploutarxos', 'Giorgos Dalaras', 'Giorgos Mazonakis', 'Giorgos Sabanis', 'Haris Alexiou', 'Hmiskoumpria', 'Ivi Adamou', 'Konstantinos Argiros', 'Kostis Maravelias', 'Lavredis Maxairitsas', 'Lefteris Pantazis', 'Maria Farantouri', 'Marinela', 'Melisses', 'Mixalis Hatziganns', 'Natasa Mpofiliou', 'Natasa Theodoridou', 'Nikos Oikonomopoulos', 'Nikos Vertis', 'Nikos Xiloiris', 'Notis Sfakianakis', 'Panos Kiamos', 'Panos Mouzourakis', 'Pix Lax', 'Sakis Rouvas', 'Stamatis Gonidis', 'Stavento', 'Stelios Rokkos', 'Stratos Dionisiou', 'Tamta', 'Themis Adamantidis', 'Vaggelis Kakouriotis', 'Vasilis Karras']
# text = "Born and raised in the island of Corfu, Sakis Rouvas started his music career in 1991, at the Thessaloniki Song Festival. \nSince then, he has steadily been at the top of the Greek music scene and show-biz with numerous distinctions among different fields, \nas he has received the Best New Singer, Best Song and the “Karolos Koun” Award for Best Stage Performance, \nas well as many other national and international awards.\nHis multitalented personality has been demonstrated through his leading roles in cinema, ancient drama and Hollywood movies, \nas well as through his participation in popular TV shows and large-scale events, including the 2004 Athens Olympics Closing Ceremony and the \nEurovision Song Contest, \nwhere he successfully represented Greece in 2004 and 2009. \nParallel to his career, Sakis has participated in several initiatives that aim to raise awareness for the protection of the environment \nand has demonstrated a long-term commitment to supporting children in need, while being himself a caring father of four."
# new = ["Manolis Mitsias"]
'''get values from db'''
# sq = "SELECT Name FROM artist_info VALUES (%s)"
# cursor.execute(sq)
# results = cursor.fetchall()



'''show databeses'''
# cursor.execute("SHOW DATABASES")

# for x in cursor:
#   print(x)

'''create and show tables'''
# cursor.execute("CREATE TABLE artists (name VARCHAR(255), last_name VARCHAR(255))")
# cursor.execute("SHOW TABLES")

# for i in cursor:
#   print(i)

'''insert in rows'''
# for i in new:
#     sql = "INSERT INTO artist_info (Name) VALUES (%s)"
#     val =[(i)] 
#     cursor.execute(sql, val)
#     mydb.commit()

# mydb.close()
    
# sql = "INSERT INTO artist_info (Name) VALUES ('Dimitris Chorn', 'Elli Lampeti', 'Tzeni Karezi', 'Nikos Stavridis', 'Christophoros Papakaliatis', 'Maro Kontou', 'Maria Kavogianni', 'Kostas Koklas', 'Aggeliki Lampri', 'Elisavet Konstantinidou', 'Meletis Ilias', 'Giannis Drakopoulos', 'Nora Valsami', 'Melpo Zarokosta', 'Georgia Vasiliadou', 'Mairi Aroni', 'Hro Mane', 'Eleni Krita', 'Adreas Barkoulis', 'Tzois Evidi')"
# cursor.execute(sql)
# mydb.commit()


# .executemany		

# ident = "Singer"


'''this way you will be able to insert things to artits'''
# sql = "UPDATE artist_info SET Identifier = (%s) WHERE Name =''"
# val = [(ident)]
# cursor.execute(sql, val)
# mydb.commit()

# sql = "UPDATE artist_info SET Spotify_url = (%s) WHERE Name ='Sakis Rouvas'"
# val = [(url)]
# cursor.execute(sql, val)
# mydb.commit()


# UPDATE tablename
# SET ="new value"
# WHERE ="old value";


'''select'''
# sq = "SELECT * FROM artists"
# print (cursor.execute(sq))

# print(cursor.rowcount, "details inserted")


'''delete row'''
# query = "DELETE FROM artist_info WHERE Name = 'Stratos Dionisiou'"
# cursor.execute(query)
# mydb.commit()

'''important everytime you try to do something'''
# mydb.commit()

# disconnecting from server
# mydb.close()


