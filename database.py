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
                    # Marvel Heroes
                    ('Spider-Man', 'Peter Parker, bitten by a radioactive spider, swings through New York with web-based agility.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/133.jpg', 
                    'https://www.youtube.com/embed/AZtwzbF0Jhw'),
                    ('Iron Man', 'Tony Stark, genius billionaire, fights in a high-tech suit of armor.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/85.jpg', 
                    'https://www.youtube.com/embed/Ke1Y3P9D0Bc'),
                    ('Captain America', 'Steve Rogers, enhanced by super-soldier serum, wields a vibranium shield.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/274.jpg', 
                    'https://www.youtube.com/embed/cs8rF8dR8gY'),
                    ('Thor', 'God of Thunder from Asgard, wields Mjolnir to control lightning.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/140.jpg', 
                    'https://www.youtube.com/embed/JOddp-nlNvQ'),
                    ('Hulk', 'Bruce Banner transforms into a green giant with immense strength when angry.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/83.jpg', 
                    'https://www.youtube.com/embed/ZyJ3k6jBRcs'),
                    ('Black Panther', 'T Challa, king of Wakanda, uses vibranium tech and enhanced abilities.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/247.jpg', 
                    'https://www.youtube.com/embed/xjDjIWPwcPU'),
                    ('Wolverine', 'Mutant with healing factor and adamantium claws, fights with feral intensity.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/161.jpg', 
                    'https://www.youtube.com/embed/Div0iP65aZo'),
                    ('Doctor Strange', 'Master of the mystic arts, manipulates time and reality.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/12.jpg', 
                    'https://www.youtube.com/embed/Lt-U_t2pUHI'),
                    ('Scarlet Witch', 'Wanda Maximoff wields chaos magic, altering reality with immense power.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/444.jpg', 
                    'https://www.youtube.com/embed/sj9J2ecsSpo'),
                    ('Deadpool', 'Wade Wilson, the Merc with a Mouth, has rapid healing and a sharp wit.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/835.jpg', 
                    'https://www.youtube.com/embed/ONHBaC-pfsk'),
                    ('Black Widow', 'Natasha Romanoff, elite spy with unmatched combat skills.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/217.jpg', 
                    'https://www.youtube.com/embed/ybLTDShQfOY'),
                    ('Hawkeye', 'Clint Barton, expert marksman with trick arrows.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/88.jpg', 
                    'https://www.youtube.com/embed/5VYb3B1ETlk'),
                    ('Ant-Man', 'Scott Lang shrinks and grows using Pym Particles, with insect-like agility.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/857.jpg', 
                    'https://www.youtube.com/embed/pWdKf3MneyI'),
                    ('Captain Marvel', 'Carol Danvers, powered by cosmic energy, flies with super strength.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/112.jpg', 
                    'https://www.youtube.com/embed/Z1BCujX3pw8'),
                    ('Storm', 'Ororo Munroe controls weather with mutant powers, an X-Men leader.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/135.jpg', 
                    'https://www.youtube.com/embed/7p6MHO0hRY4'),
                    ('Vision', 'Synthetic being powered by the Mind Stone, with density manipulation.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/271.jpg', 
                    'https://www.youtube.com/embed/1yDZaY_kf3Q'),
                    ('Daredevil', 'Matt Murdock, blind lawyer with enhanced senses, fights crime in Hell’s Kitchen.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/70.jpg', 
                    'https://www.youtube.com/embed/jAy6NJ_D5vU'),
                    ('Ghost Rider', 'Johnny Blaze, bonded with a demon, wields hellfire and a fiery motorcycle.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/74.jpg', 
                    'https://www.youtube.com/embed/L0CK69f0YpU'),
                    ('Silver Surfer', 'Norrin Radd, cosmic herald with power cosmic, surfs the stars.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/127.jpg', 
                    'https://www.youtube.com/embed/5xY3S9S9f9g'),
                    ('Namor', 'Prince of Atlantis, with aquatic strength and flight abilities.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/142.jpg', 
                    'https://www.youtube.com/embed/8zQvk2L8dMo'),
                    ('Jean Grey', 'Mutant with telepathy and telekinesis, hosts the Phoenix Force.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/151.jpg', 
                    'https://www.youtube.com/embed/6XBs1N-1U8o'),
                    ('Star-Lord', 'Peter Quill, leader of the Guardians of the Galaxy, with cosmic gear.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/10353.jpg', 
                    'https://www.youtube.com/embed/d96cjJhvlMA'),
                    ('Gamora', 'Deadly assassin and Guardian, with superhuman strength and agility.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/165.jpg', 
                    'https://www.youtube.com/embed/2Svi37Z28KM'),
                    ('Rocket Raccoon', 'Genetically enhanced raccoon, expert tactician and sharpshooter.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/10038.jpg', 
                    'https://www.youtube.com/embed/jiGkrGGk9q0'),
                    ('Groot', 'Tree-like hero with regenerative powers, says “I am Groot.”', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/10037.jpg', 
                    'https://www.youtube.com/embed/D54rCcc2C4c'),
                    # DC Heroes
                    ('Superman', 'Kal-El from Krypton, with super strength, flight, and x-ray vision.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/791.jpg', 
                    'https://www.youtube.com/embed/T6DJcgm3wNY'),
                    ('Batman', 'Bruce Wayne, the Dark Knight, uses gadgets and martial arts to fight crime.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/639.jpg', 
                    'https://www.youtube.com/embed/rgH2w2N4zEA'),
                    ('Wonder Woman', 'Diana Prince, Amazon princess, wields strength and a Lasso of Truth.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/807.jpg', 
                    'https://www.youtube.com/embed/VSB4wGIdDwo'),
                    ('The Flash', 'Barry Allen, the Scarlet Speedster, runs at superhuman speeds.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/892.jpg', 
                    'https://www.youtube.com/embed/Yj0l7drA9f4'),
                    ('Aquaman', 'Arthur Curry, king of Atlantis, commands the seas and super strength.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/277.jpg', 
                    'https://www.youtube.com/embed/WDkg3h8PCVU'),
                    ('Green Lantern', 'Hal Jordan, wielding a power ring, creates energy constructs.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/698.jpg', 
                    'https://www.youtube.com/embed/FrkM3QpT7kY'),
                    ('Shazam', 'Billy Batson transforms into a magical hero with godlike powers.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/838.jpg', 
                    'https://www.youtube.com/embed/go6GEIrcvFY'),
                    ('Nightwing', 'Dick Grayson, former Robin, excels in acrobatics and combat.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/853.jpg', 
                    'https://www.youtube.com/embed/1o-4aV5nJZs'),
                    ('Cyborg', 'Victor Stone, part human, part machine, with advanced tech abilities.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/672.jpg', 
                    'https://www.youtube.com/embed/rCyY09V0VGA'),
                    ('Green Arrow', 'Oliver Queen, master archer, fights crime with precision.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/696.jpg', 
                    'https://www.youtube.com/embed/4p-E_2RaNvg'),
                    ('Martian Manhunter', 'Jonn Jonzz, Martian with shape-shifting and telepathy.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/733.jpg', 
                    'https://www.youtube.com/embed/ueZwv1bW5ng'),
                    ('Hawkman', 'Carter Hall, reincarnated warrior with winged flight and strength.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/706.jpg', 
                    'https://www.youtube.com/embed/9eY-P1V0n0Q'),
                    ('Hawkgirl', 'Shiera Sanders, winged heroine with combat skills and Nth metal.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/707.jpg', 
                    'https://www.youtube.com/embed/8kS7A_3Zm4o'),
                    ('Zatanna', 'Magician with spell-casting powers, member of Justice League Dark.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/809.jpg', 
                    'https://www.youtube.com/embed/2X7V2wusI4Y'),
                    ('Blue Beetle', 'Jaime Reyes, bonded with alien scarab, gains armor and weapons.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/864.jpg', 
                    'https://www.youtube.com/embed/v3evsR2KDiY'),
                    ('Firestorm', 'Ronnie Raymond and Martin Stein merge to control nuclear energy.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/704.jpg', 
                    'https://www.youtube.com/embed/5kS2b7v3f0o'),
                    ('Atom', 'Ray Palmer shrinks to microscopic sizes with advanced tech.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/717.jpg', 
                    'https://www.youtube.com/embed/4kS2b7v3f0o'),
                    ('Black Canary', 'Dinah Lance, martial artist with sonic scream abilities.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/667.jpg', 
                    'https://www.youtube.com/embed/4kS2b7v3f0o'),
                    ('Red Tornado', 'Android with wind manipulation powers, Justice League member.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/1103.jpg', 
                    'https://www.youtube.com/embed/4kS2b7v3f0o'),
                    # Other Publishers (Image, Dark Horse, etc.)
                    ('Invincible', 'Mark Grayson, young hero with super strength and flight.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/10866.jpg', 
                    'https://www.youtube.com/embed/-bfAVpuko5o'),
                    ('Omni-Man', 'Superhero from planet Viltrum, with immense power and speed.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/10867.jpg', 
                    'https://www.youtube.com/embed/3eU7bSc2U8o'),
                    ('Spawn', 'Al Simmons, resurrected with hellish powers, fights supernatural threats.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/790.jpg', 
                    'https://www.youtube.com/embed/0kS2b7v3f0o'),
                    ('Hellboy', 'Demon raised to fight evil, with strength and occult knowledge.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/1026.jpg', 
                    'https://www.youtube.com/embed/dt5g5_1cKVk'),
                    ('The Tick', 'Comedic hero with super strength and near-invulnerability.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/1082.jpg', 
                    'https://www.youtube.com/embed/4kS2b7v3f0o'),
                    ('Savage Dragon', 'Green-skinned hero with super strength, fights crime in Chicago.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/1081.jpg', 
                    'https://www.youtube.com/embed/4kS2b7v3f0o'),
                    ('ShadowHawk', 'Vigilante with armored suit and enhanced strength.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/1083.jpg', 
                    'https://www.youtube.com/embed/4kS2b7v3f0o'),
                    ('Witchblade', 'Sara Pezzini, bonded with mystical artifact, gains combat powers.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/1084.jpg', 
                    'https://www.youtube.com/embed/4kS2b7v3f0o'),
                    ('The Maxx', 'Homeless hero with dream-world powers, fights surreal threats.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/1085.jpg', 
                    'https://www.youtube.com/embed/4kS2b7v3f0o'),
                    ('Atom Eve', 'Invincible’s ally, manipulates matter at the atomic level.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/10868.jpg', 
                    'https://www.youtube.com/embed/3eU7bSc2U8o'),
                    ('SuperPatriot', 'Cyborg hero with enhanced strength and weaponry.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/1087.jpg', 
                    'https://www.youtube.com/embed/4kS2b7v3f0o'),
                    ('Battle Beast', 'Warrior from Invincible, with immense strength and combat skill.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/10869.jpg', 
                    'https://www.youtube.com/embed/3eU7bSc2U8o'),
                    ('Firebreather', 'Half-human, half-dragon with fire-based powers.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/1088.jpg', 
                    'https://www.youtube.com/embed/4kS2b7v3f0o'),
                    ('Kid Omni-Man', 'Young Viltrumite with super strength and flight.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/10870.jpg', 
                    'https://www.youtube.com/embed/3eU7bSc2U8o'),
                    ('Darkwing', 'Vigilante hero with stealth and combat prowess.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/1089.jpg', 
                    'https://www.youtube.com/embed/4kS2b7v3f0o'),
                    ('Noble Causes', 'Superhero family with varied powers, fighting for legacy.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/1090.jpg', 
                    'https://www.youtube.com/embed/4kS2b7v3f0o'),
                    ('Dynamo 5', 'Team of siblings with diverse superpowers, protecting Tower City.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/1091.jpg', 
                    'https://www.youtube.com/embed/4kS2b7v3f0o'),
                    ('Invincible Iron Man', 'Alternate Tony Stark with advanced armor tech.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/1004.jpg', 
                    'https://www.youtube.com/embed/Ke1Y3P9D0Bc'),
                    ('War Machine', 'James Rhodes, Iron Man’s ally, in a militarized suit.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/149.jpg', 
                    'https://www.youtube.com/embed/Ke1Y3P9D0Bc'),
                    ('Falcon', 'Sam Wilson, flies with winged suit and Redwing drone.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/73.jpg', 
                    'https://www.youtube.com/embed/8zQvk2L8dMo'),
                    ('Ms. Marvel', 'Kamala Khan, shape-shifting teen with polymorphic powers.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/10366.jpg', 
                    'https://www.youtube.com/embed/m9EX0f6V11Y'),
                    ('Moon Knight', 'Marc Spector, empowered by Khonshu, fights with lunar strength.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/94.jpg', 
                    'https://www.youtube.com/embed/x7KR88i1Z-o'),
                    ('Blade', 'Eric Brooks, vampire hunter with superhuman strength.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/48.jpg', 
                    'https://www.youtube.com/embed/4kS2b7v3f0o'),
                    ('Iron Fist', 'Danny Rand, martial artist with chi-powered fist.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/84.jpg', 
                    'https://www.youtube.com/embed/f9OKL5no-S0'),
                    ('Luke Cage', 'Power Man, with unbreakable skin and super strength.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/90.jpg', 
                    'https://www.youtube.com/embed/ytkjQvSkNqo'),
                    ('Nova', 'Richard Rider, cosmic hero with Nova Force powers.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/105.jpg', 
                    'https://www.youtube.com/embed/4kS2b7v3f0o'),
                    ('She-Hulk', 'Jennifer Walters, gamma-powered lawyer with super strength.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/125.jpg', 
                    'https://www.youtube.com/embed/u7JsKhI2An0'),
                    ('Sentry', 'Robert Reynolds, with the power of a million exploding suns.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/123.jpg', 
                    'https://www.youtube.com/embed/4kS2b7v3f0o'),
                    ('Human Torch', 'Johnny Storm, Fantastic Four member, controls flames.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/82.jpg', 
                    'https://www.youtube.com/embed/4kS2b7v3f0o'),
                    ('Invisible Woman', 'Sue Storm, creates force fields and turns invisible.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/81.jpg', 
                    'https://www.youtube.com/embed/4kS2b7v3f0o'),
                    ('Mr. Fantastic', 'Reed Richards, stretches his body with super elasticity.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/95.jpg', 
                    'https://www.youtube.com/embed/4kS2b7v3f0o'),
                    ('Thing', 'Ben Grimm, rock-like hero with immense strength.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/139.jpg', 
                    'https://www.youtube.com/embed/4kS2b7v3f0o'),
                    ('Cyclops', 'Scott Summers, X-Men leader with optic energy blasts.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/66.jpg', 
                    'https://www.youtube.com/embed/7p6MHO0hRY4'),
                    ('Iceman', 'Bobby Drake, mutant with ice manipulation powers.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/153.jpg', 
                    'https://www.youtube.com/embed/7p6MHO0hRY4'),
                    ('Beast', 'Hank McCoy, X-Men scientist with animal-like strength.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/43.jpg', 
                    'https://www.youtube.com/embed/7p6MHO0hRY4'),
                    ('Colossus', 'Piotr Rasputin, transforms into organic steel with super strength.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/61.jpg', 
                    'https://www.youtube.com/embed/Div0iP65aZo'),
                    ('Rogue', 'Mutant with power absorption through touch.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/121.jpg', 
                    'https://www.youtube.com/embed/7p6MHO0hRY4'),
                    ('Kitty Pryde', 'Phases through objects with mutant intangibility.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/89.jpg', 
                    'https://www.youtube.com/embed/7p6MHO0hRY4'),
                    ('Starfire', 'Tamaranean princess with energy blasts and flight.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/1105.jpg', 
                    'https://www.youtube.com/embed/4kS2b7v3f0o'),
                    ('Raven', 'Daughter of Trigon, with empathic and magical abilities.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/1104.jpg', 
                    'https://www.youtube.com/embed/4kS2b7v3f0o'),
                    ('Beast Boy', 'Changes into any animal with shape-shifting powers.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/1106.jpg', 
                    'https://www.youtube.com/embed/4kS2b7v3f0o'),
                    ('Robin', 'Tim Drake, detective and martial artist, Batman’s protégé.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/850.jpg', 
                    'https://www.youtube.com/embed/1o-4aV5nJZs'),
                    ('Supergirl', 'Kara Zor-El, Superman’s cousin with Kryptonian powers.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/792.jpg', 
                    'https://www.youtube.com/embed/4kS2b7v3f0o'),
                    ('Power Girl', 'Alternate Kara Zor-L, with Kryptonian strength and flight.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/763.jpg', 
                    'https://www.youtube.com/embed/4kS2b7v3f0o'),
                    ('Booster Gold', 'Time-traveling hero with advanced tech and energy blasts.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/668.jpg', 
                    'https://www.youtube.com/embed/4kS2b7v3f0o'),
                    ('Vixen', 'Mari McCabe, channels animal powers via mystical totem.', 
                    'https://www.superherodb.com/pictures2/portraits/10/100/803.jpg', 
                    'https://www.youtube.com/embed/4kS2b7v3f0o')
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