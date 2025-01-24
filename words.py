import random


WORDS = ["Virtunexa","Python", "Programming", "Developer", "Encyclopedia", "Rhythm"]

def main():
    score = 0
    print("Welcome to the Spelling Game!")
    
    while True:
        word = random.choice(WORDS)
        print(f"Spell the word: {word}")
        user_input = input("Your spelling: ").strip()
        
        if user_input.lower() == word.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct spelling is: {word}")
        
        print(f"Your current score is: {score}")
        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break
    
    print(f"Thank you for playing! Your final score is: {score}")

if __name__ == "__main__":
    main()