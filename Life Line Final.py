import random 
# Intialising the dictionary
Quiz ={
    'Questions':[],
    'Options':[],
    'Answers':[]
}
# Cateogory 1 (Questions, Options, Actual Answer)
Educational =[
    "Q1. How many bones are in the adult human body?",
    "Q2. Which part of the brain is responsible for memory and learning?",
    "Q3. Which mineral is important for regulating blood pressure?",
    "Q4. Which mental health condition is most commonly associated with an overactive 'fight or flight' response?",
    "Q5. Which of the following is a complete protein source that contains all nine essential amino acids?",
    "Q6. Which hormone is released in response to stress?",
    "Q7. What is the body's natural sleep-wake cycle called?",
    "Q8. Which of the following is a core principle of mindfulness meditation?",
    "Q9. Which organ is responsible for filtering waste from the blood?",
    "Q10. Which of the following foods contains the highest concentration of beta-carotene?",
    "Q11. What is the primary benefit of cardiovascular exercise?",
    "Q12. Which system controls the body's response to stress?",
    "Q13. What is the recommended daily intake of water for an adult?",
    "Q14. Which of the following exercises is best for building cardiovascular endurance?",
    "Q15. Which mineral is most commonly found to be deficient in the diets of women of childbearing age, leading to an increased risk of anemia?"
]
Edu_Options = [
    ['A: 206', 'B: 210'],
    ['A: Medulla', 'B: Hippocampus'],
    ['A: Potassium', 'B: Magnesium'],
    ['A: Anxiety disorder', 'B: Schizophrenia'],
    ['A: Lentils', 'B: Quinoa'],
    ['A: Cortisol', 'B: Dopamine', 'C: Melatonin'],
    ['A: Circadian rhythm', 'B: REM cycle', 'C: Resting phase'],
    ['A: Focus on clearing your mind completely', 'B: Avoid any thoughts or emotions', 'C: Focus on the present moment and accept thoughts non-judgmentally'],
    ['A: Lungs', 'B: Liver', 'C: Kidneys'],
    ['A: Sweet potatoes', 'B: Spinach', 'C: Tomatoes'],
    ['A: Building muscle mass', 'B: Improving flexibility', 'C: Increasing endurance', 'D: Strengthening bones'],
    ['A: Respiratory system', 'B: Nervous system', 'C: Digestive system', 'D: Immune system'],
    ['A: 2 cups', 'B: 4 cups', 'C: 6-8 cups', 'D: 10-12 cups'],
    ['A: Weightlifting', 'B: Running', 'C: Squats', 'D: Stretching'],
    ['A: Calcium', 'B: Iron', 'C: Potassium', 'D: Magnesium']
]
Edu_Ans = ["A", "B", "A", "A", "B", "A", "A", "C", "C", "A", "C", "B", "C", "B", "B"]
# Cateogory 2 (Questions, Options, Actual Answer)
Entertainment = [
    "Q1: Which rapper’s real name is Aubrey Drake Graham?",
    "Q2: Which 2020 Netflix series stars Zendaya and Jacob Elordi?",
    "Q3: Which artist's 2019 album included hits like 'Sunflower'?",
    "Q4: Which movie features a team of astronauts who travel through a wormhole to find a new home for humanity?",
    "Q5: Which 2021 film, starring Timothée Chalamet, is based on a science fiction novel and set on the desert planet Arrakis?",
    "Q6: Which animated series features the characters Finn the Human and Jake the Dog?",
    "Q7: Who played Lara Jean Covey in the Netflix film series To All the Boys I've Loved Before?",
    "Q8: Which Netflix original series centres around a charming yet obsessive stalker named Joe Goldberg?",
    "Q9: Which video game became the most downloaded game in 2020, with elements of social deception?",
    "Q10: Which K-pop group became the first to top the Billboard Hot 100 with the song 'Dynamite'?",
    "Q11: Which 2019 animated film features the voice of Chris Pratt as the main character, Ian Lightfoot?",
    "Q12: Which 2021 Netflix series, starring Millie Bobby Brown, is based on the book series about the younger sister of a Consulting Detective?",
    "Q13: In Harry Potter, what is the name of Harry’s pet owl?",
    "Q14: What reality TV show features Kim, Kourtney, and Khloé?",
    "Q15: Which artist broke records with the 2021 single 'drivers license'?"
]
Ent_Options = [
    ['A: Drake', 'B: Travis Scott'],
    ['A: The Society', 'B: Euphoria'],
    ['A: Post Malone', 'B: Lil Nas X'],
    ['A: The Martian', 'B: Interstellar'],
    ['A: Blade Runner 2049', 'B: Dune'],
    ['A: Steven Universe', 'B: Gravity Falls', 'C: Adventure Time'],
    ['A: Hailee Steinfeld', 'B: Lana Condor', 'C: Olivia Rodrigo'],
    ['A: The Society', 'B: You', 'C: 13 Reasons Why'],
    ['A: Among Us', 'B: Fall Guys', 'C: Minecraft'],
    ['A: EXO', 'B: Twice', 'C: BTS'],
    ['A: Toy Story 4', 'B: Onward', 'C: Frozen II', 'D: Soul'],
    ['A: Stranger Things', 'B: Enola Holmes', 'C: The Witcher', 'D: 13 Reasons Why'],
    ['A: Crookshanks', 'B: Hedwig', 'C: Scabbers', 'D: Buckbeak'],
    ['A: The Real Housewives of Beverly Hills', 'B: Keeping Up with the Kardashians', 'C: Love Island', 'D: Selling Sunset'],
    ['A: Billie Eilish', 'B: Lorde', 'C: Olivia Rodrigo', 'D: Halsey']
]
Ent_Ans = ["A", "B", "A", "B", "B", "C", "B", "B", "A", "C", "B", "B", "B", "B", "C"]
# Intialising Variables
lives = 3
score =0
ans= ''
result = ''
topic =''
#                                                                           G A M E  B E G I N S 

# User selects Category
while topic.lower() != 'educational' and topic.lower() != 'entertainment' and topic.lower() != 'both':
    topic = input("Select your topic(s): Educational, Entertainment, Both. ")
if topic.lower() == 'educational':
    Quiz['Questions'] = Educational 
    Quiz['Options'] = Edu_Options 
    Quiz['Answers'] = Edu_Ans 
elif topic.lower() == 'entertainment':
    Quiz['Questions'] = Entertainment
    Quiz['Options'] = Ent_Options
    Quiz['Answers'] = Ent_Ans
elif topic.lower() == 'both':
    Quiz['Questions'] = Educational + Entertainment
    Quiz['Options'] = Edu_Options + Ent_Options
    Quiz['Answers'] = Edu_Ans + Ent_Ans
# Total Number of Questions to begin with (imp for final score)
TotalQuestions = len(Quiz['Questions'])
# Quiz Function
def Trivia():
    global Quiz, score, lives, ans, win, loss, rounds
    print()
    print(Quiz['Questions'][0]) # prints question
    for i in Quiz['Options'][0]: # prints options
        print(i, end = " ")
    print()
    Flag = False
    while Flag == False: 
        Guess = input("Enter the Alphabet of the option: ").upper() # takes user's guess
        for count in Quiz['Options'][0]:
            if count[0] == Guess:
                Flag = True
                break         
    if Quiz['Answers'][0] == Guess: # checks if user is right or not
        print("Lives: "  + str(lives))
        score += 1 # increments if ans is right
    else: #when user answers wrong
        print("Incorrect! You life is on the line, protect it!")
        rounds = 0
        while rounds != 1 and rounds != 3: # User chooses how many rounds of RPS to play
            rounds=input("Choose round(s) 1 or 3.")
            if rounds.isdigit() is False:
                rounds = 0
            else:
                rounds = int(rounds)
        win = 0
        loss = 0
        for x in range(rounds):
            if win != 2 and loss != 2: # if best 2/3 then RPS stops
                ans = input("Enter r for rock, p for paper, s for scissor: ").lower()
                result=rps_choice()
                print(result)
                if result=="You win!":
                    win+=1
                else:
                    loss+=1 
            else:
                break
        if loss>win: # decrements lives
            lives=lives-1
        print("Lives:", lives)
    Quiz['Questions'].pop(0) # removes first elements from the dictionary
    Quiz['Options'].pop(0)
    Quiz['Answers'].pop(0)

def auto_rps(): # Recursive/helper for computer generated RPS
    global ans
    auto = random.choice(["R", "P", "S"])
    print("Player 2 chose:", auto)
    if auto!=ans.upper(): # checks for Draw
        return auto
    ans = input("Draw!! Enter R for rock, P for paper, S for scissor: ").lower()
    return auto_rps() # repeats until not a draw

def rps_choice(): # Compares User and Computer for RPS result
    global ans
    auto= auto_rps() # calls Helper Function
    if ans=="r" and auto=="P":
        return "You lose!"
    elif ans=="r" and auto=="S":
        return "You win!"
    elif ans=="p" and auto=="R":
        return "You win!"
    elif ans=="p" and auto=="S":
        return "You lose!"
    elif ans=="s" and auto=="P":
        return "You win!"
    elif ans=="s" and auto=="R":
        return "You lose!"
    else:
        ans = input("Incorrect Input!  Enter R for rock, P for paper, S for scissor: ").lower() 
        return rps_choice() # returns until a win or a loss

while len(Quiz["Questions"]) != 0 and lives != 0: # calls function until end of game
    Trivia()
print("Final Score: " + str(score) + "/" + str(TotalQuestions)) # final score