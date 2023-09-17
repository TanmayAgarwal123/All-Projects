import pyautogui as pg
import time

messages = ['Hii', 'Hii 2','Hii 3', 'Hii again', 'Hii returns', 'Hii: wrath of a greeting','Hii: Lost in space','The Hii never die','The Hii never die 9','The Hii 10',
            'The Hii reborn','The Hii strike out','Hii: the last bomb','Hii: the untold story','Hii endgame','The last Hii','Hii- The Unreplied Story','Hii endgame 4','The Hii stricks back','Hii the last truth',
            'Hii rebirth','Hii: the never ending','The immortal Hii','The birth of Hey','The rise of Hey','Hey: The war begins','Hii vs Hey: The war of greatings','Hey: 4','Hey: 5','Death of Hey'
            'Hey revival','Hey vs Hii: the civil war','Hey vs Hii: The start of infinite war','The birth of bye','The pending Hii','Hii vs Hey: The remaining story','Hey vs Hii: the last war','Hello: the child of Hii and Hey','Hello 2','Hello 3'
            'Bye 2','Bye: The worst enemy','Hello 4','Hello 5','Bye returns','Bye forever','Hello vs Bye: The new war','Hello vs Bye: The ending','Whats up: The new hero in town','Howdy: the secret'
            'Hello returns','Ta-ta the new enemy','Mummy dat rahi hai: the horror','The horror returns','The remembrance of Hii','Greetings United','Greatings United 2','The lost Greatings','Greatings The end','Chal ab thak gaya 😂','Chal ab thak gaya 😂 2']
time.sleep(5)
print(len(messages))
for message in messages:
    pg.write(message)
    pg.press("enter")
    time.sleep(60)
