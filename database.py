import sqlite3

def create_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    # Creating a  Users table
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )''')
    # Create Superheroes table
    c.execute('''CREATE TABLE IF NOT EXISTS superheroes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        image_url TEXT NOT NULL,
        video_url TEXT NOT NULL
    )''')
    # Preloading the superheroes table since it is empty
    c.execute('SELECT COUNT(*) FROM superheroes')
    if c.fetchone()[0] == 0:
        heroes = [
            # Some Marvel Heroes
            ('Spider-Man', 'Peter Parker, bitten by a radioactive spider, swings through New York with web-based agility.', 
             'https://upload.wikimedia.org/wikipedia/en/2/21/Web_of_Spider-Man_Vol_1_100.jpg', 
             'https://www.youtube.com/embed/JfVOs4VSpmA'),
            ('Iron Man', 'Tony Stark, genius billionaire, fights in a high-tech suit of armor.', 
             'https://upload.wikimedia.org/wikipedia/en/e/e0/Iron_Man_bleeding_edge.jpg', 
             'https://www.youtube.com/embed/Ke1Y3P9D0Bc'),
            ('Captain America', 'Steve Rogers, enhanced by super-soldier serum, wields a vibranium shield.', 
             'https://upload.wikimedia.org/wikipedia/en/3/3b/Captain_America_The_First_Avenger_poster.jpg', 
             'https://www.youtube.com/embed/JerVrbLldXw'),
            ('Thor', 'God of Thunder from Asgard, wields Mjolnir to control lightning.', 
             'https://upload.wikimedia.org/wikipedia/en/f/fc/Thor_poster.jpg', 
             'https://www.youtube.com/embed/JOddp-nlNvQ'),
            ('Hulk', 'Bruce Banner transforms into a green giant with immense strength when angry.', 
             'https://upload.wikimedia.org/wikipedia/en/a/aa/Hulk_%282003_film%29_poster.jpg', 
             'https://www.youtube.com/embed/2v1l5OkgJHg'),
            ('Black Panther', 'T’Challa, king of Wakanda, uses vibranium tech and enhanced abilities.', 
             'https://upload.wikimedia.org/wikipedia/en/d/d6/Black_Panther_%28film%29_poster.jpg', 
             'https://www.youtube.com/embed/xjDjIWPwcPU'),
            ('Wolverine', 'Mutant with healing factor and adamantium claws, fights with feral intensity.', 
             'https://upload.wikimedia.org/wikipedia/en/3/37/X-Men_Origins_Wolverine_theatrical_poster.jpg', 
             'https://www.youtube.com/embed/QN6tSxkZzys'),
            ('Doctor Strange', 'Master of the mystic arts, manipulates time and reality.', 
             'https://upload.wikimedia.org/wikipedia/en/c/c7/Doctor_Strange_poster.jpg', 
             'https://www.youtube.com/embed/Lt-U_t2pUHI'),
            ('Scarlet Witch', 'Wanda Maximoff wields chaos magic, altering reality with immense power.', 
             'https://upload.wikimedia.org/wikipedia/en/c/c2/WandaVision_poster.jpg', 
             'https://www.youtube.com/embed/sj9J2ecsSpo'),
            ('Deadpool', 'Wade Wilson, the Merc with a Mouth, has rapid healing and a sharp wit.', 
             'https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg', 
             'https://www.youtube.com/embed/Xithigfg7dA'),
            ('Black Widow', 'Natasha Romanoff, elite spy with unmatched combat skills.', 
             'https://upload.wikimedia.org/wikipedia/en/9/96/Black_Widow_poster.jpg', 
             'https://www.youtube.com/embed/ybLTDShQfOY'),
            ('Hawkeye', 'Clint Barton, expert marksman with trick arrows.', 
             'https://upload.wikimedia.org/wikipedia/en/9/99/Hawkeye_%28TV_series%29_poster.jpg', 
             'https://www.youtube.com/embed/5VYb3B1ETlk'),
            # Some DC Heroes
            ('Superman', 'Kal-El from Krypton, with super strength, flight, and x-ray vision.', 
             'https://upload.wikimedia.org/wikipedia/en/3/35/Supermanflying.png', 
             'https://www.youtube.com/embed/T6DJcgm3wNY'),
            ('Batman', 'Bruce Wayne, the Dark Knight, uses gadgets and martial arts to fight crime.', 
             'https://upload.wikimedia.org/wikipedia/en/c/c6/Batman_v_Superman_Dawn_of_Justice_poster.jpg', 
             'https://www.youtube.com/embed/0WWzgGyAH6Y'),
            ('Wonder Woman', 'Diana Prince, Amazon princess, wields strength and a Lasso of Truth.', 
             'https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg', 
             'https://www.youtube.com/embed/VSB4wGIdDwo'),
            ('The Flash', 'Barry Allen, the Scarlet Speedster, runs at superhuman speeds.', 
             'https://upload.wikimedia.org/wikipedia/en/e/ed/The_Flash_%28film%29_poster.jpg', 
             'https://www.youtube.com/embed/r51cYVZWfrY'),
            ('Aquaman', 'Arthur Curry, king of Atlantis, commands the seas and super strength.', 
             'https://upload.wikimedia.org/wikipedia/en/1/1c/Aquaman_poster.jpg', 
             'https://www.youtube.com/embed/WDkg3h8PCVU'),
            ('Green Lantern', 'Hal Jordan, wielding a power ring, creates energy constructs.', 
             'https://upload.wikimedia.org/wikipedia/en/6/6b/Green_Lantern_poster.jpg', 
             'https://www.youtube.com/embed/8NWGlNE1R3Y'),
            ('Shazam', 'Billy Batson transforms into a magical hero with godlike powers.', 
             'https://upload.wikimedia.org/wikipedia/en/6/64/Shazam%21_theatrical_poster.jpg', 
             'https://www.youtube.com/embed/go6GEIrcvFY'),
            ('Nightwing', 'Dick Grayson, former Robin, excels in acrobatics and combat.', 
             'https://upload.wikimedia.org/wikipedia/en/9/9c/Nightwing_Vol_3_1.jpg', 
             'https://www.youtube.com/embed/6XBs1N-1U8o'),
            ('Cyborg', 'Victor Stone, part human, part machine, with advanced tech abilities.', 
             'https://upload.wikimedia.org/wikipedia/en/0/0c/Justice_League_%28film%29_poster.jpg', 
             'https://www.youtube.com/embed/rCyY09V0VGA'),
            ('Green Arrow', 'Oliver Queen, master archer, fights crime with precision.', 
             'https://upload.wikimedia.org/wikipedia/en/5/5c/Green_Arrow_Vol_6_1.jpg', 
             'https://www.youtube.com/embed/g8kS1o7B0-k'),
            ('Martian Manhunter', 'J’onn J’onzz, Martian with shape-shifting and telepathy.', 
             'https://upload.wikimedia.org/wikipedia/en/5/5d/Martian_Manhunter_0001.jpg', 
             'https://www.youtube.com/embed/ueZwv1bW5ng'),
        ]
        c.executemany('INSERT INTO superheroes (name, description, image_url, video_url) VALUES (?, ?, ?, ?)', heroes)
    conn.commit()
    conn.close()

def add_user(username, email, password):
    #connect to the databse
    #have an active cursor
    #execute instruction, I am adding a user so I will be using INSERT INTO user...etc
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    try:
        c.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
                  (username, email, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def check_user(email, password):
    #connect to the databse
    #have an active cursor
    #execute instruction, I am validating a user's credentials when they log in/sign in
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT id, username FROM users WHERE email = ? AND password = ?', (email, password))
    user = c.fetchone() #this returns a dictionary, and its now being assigned to a variable called user
    conn.close()
    if user:
        return {'id': user[0], 'username': user[1]}#this is for the session management
    return None

def get_all_superheroes():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT id, name, description, image_url FROM superheroes')
    #This is another way to write if statements in python, it's effiecient and saves time and space in the coding environment
    #it would have been 
    # for row in c.fetchall():
    #     id=row[0]
    #     name=row[1]
    #     desc=row[2]
    #     img=row[3]
    #     heroes={"id":id,"name":name,"desc":desc,"img":img} this is a dicionary
    heroes = [{'id': row[0], 'name': row[1], 'description': row[2], 'image_url': row[3]} for row in c.fetchall()]
    conn.close()
    return heroes

def get_superhero(hero_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT id, name, description, image_url, video_url FROM superheroes WHERE id = ?', (hero_id,))
    hero = c.fetchone()
    conn.close()
    if hero:
        return {'id': hero[0], 'name': hero[1], 'description': hero[2], 'image_url': hero[3], 'video_url': hero[4]}
    return None