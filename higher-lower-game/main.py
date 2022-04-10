from game_data import data
import art
import random


score=0
print(art.logo)

continue_playing = 1
page_a=random.choice(data)
page_b=random.choice(data)
while continue_playing:
    page_a = page_b
    page_b = random.choice(data)

    while page_a == page_b:
        page_b = random.choice(data)

    print(f'A: {page_a["name"]}, a {page_a["description"]} from {page_a["country"]}')
    print(art.vs)
    print(f'B: {page_b["name"]}, a {page_b["description"]} from {page_b["country"]}')
    if page_a["follower_count"]>page_b["follower_count"]:
        higher ='A'
    else:
        higher = 'B'
    guess = input("Who has more followers? ").upper()
    if guess==higher:
        score+=1
        print(f"That's right! :) \n Score: {score}")
        
        
    else:
        continue_playing=0
        print(f"Oops, Game Over :( \n Final Score: {score}")

    
