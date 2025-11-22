import time
import random

# DICTIONARIES USED 
question_bank = [
    {
        "q": "If NAME is coded as MZLD, how is PEON coded?",
        "options": ["ODNM", "ODMN", "ONDM", "OMND"],
        "correct_text": "ODNM"
    },
    {
        "q": "If P=16 and TAP=37, then CUP=?",
        "options": ["40", "38", "36", "39"],
        "correct_text": "40"
    },
    {
        "q": "Adhar goes 4km straight, turns right (3km), then right (2km). Direction?",
        "options": ["North", "South", "East", "West"],
        "correct_text": "East"
    },
    {
        "q": "Series: 2, 8, 18, 32, 50, ?",
        "options": ["64", "72", "70", "68"],
        "correct_text": "72"
    },
    {
        "q": "Missing Code: Z9A, X7D, ?, T3J",
        "options": ["W6F", "S3H", "G9V", "V5G"],
        "correct_text": "V5G"
    },
    {
        "q": "Angle of clock hands at 9:30?",
        "options": ["75 deg", "90 deg", "105 deg", "120 deg"],
        "correct_text": "105 deg"
    },
    {
        "q": "Math: If '+' is 'x', '-' is '+'. Solve: 21 / 8 + 2 - 12 x 3",
        "options": ["14", "9", "13.5", "11"],
        "correct_text": "9"
    },
    {
        "q": "12cm cube cut into 3cm cubes. Total small cubes?",
        "options": ["16", "64", "128", "32"],
        "correct_text": "64"
    },
    {
        "q": "Cube Slicing: Total corner (vertex) cubes?",
        "options": ["4", "8", "12", "16"],
        "correct_text": "8"
    },
    {
        "q": "Product of 3 consecutive integers is 210. Sum of smaller two?",
        "options": ["13", "11", "12", "18"],
        "correct_text": "11"
    },
    {
        "q": "Logic Matrix: A, D, H ... F, L, M ... ?, N, R",
        "options": ["K", "N", "O", "P"],
        "correct_text": "K"
    },
    {
        "q": "Number Logic: 2->4, 3->27, 4->?",
        "options": ["56", "49", "45", "64"],
        "correct_text": "64"
    }
]

# HELPER FUNCTIONS

def save_score_to_file(name, score):
    try:
        file = open("leaderboard.txt", "a")
        file.write(name + "," + str(score) + "\n")
        file.close()
    except:
        print("Error saving score.")

def show_leaderboard():
    print("\n" + "="*30)
    print("   🏆 TOP 5 LEADERBOARD 🏆")
    print("="*30)
    
    try:
        file = open("leaderboard.txt", "r")
        lines = file.readlines()
        file.close()
        
        data = []
        for line in lines:
            line = line.strip()
            if "," in line:
                parts = line.split(",")
                p_name = parts[0]
                p_score = int(parts[1])
                data.append([p_name, p_score])
        data.sort(key=lambda x: x[1], reverse=True)
        
        rank = 1
        for entry in data[:5]:
            print(str(rank) + ". " + entry[0] + " : " + str(entry[1]) + " pts")
            rank = rank + 1
            
    except FileNotFoundError:
        print("No games played yet.")
    
    print("="*30 + "\n")

# MAIN QUIZ LOGIC 

def start_game():
    print("="*60)
    print("          BRAINSTORM: MAT SKILL TEST          ")
    print("="*60)
    
    name = input("Enter your Name: ")
    
    # Shuffle the Questions so the order is different every time
    random.shuffle(question_bank)
    
    # Select the first 10 questions
    quiz_questions = question_bank[:10]
    
    print("\nHello " + name + "!")
    print("Instructions:")
    print("1. You have 10 questions.")
    print("2. Time Limit: 60 seconds per question.")
    print("3. +10 points for correct answer.")
    print("4. +5 BONUS points if answered in under 10 seconds.")
    print("5. Options are shuffled every time. Watch carefully!")
    input("\n>> Press ENTER to Begin <<")
    
    total_score = 0
    stats_list = [] 
    
    q_number = 1
    
    for item in quiz_questions:
        print("\n" + "-"*40)
        print("QUESTION " + str(q_number))
        print(item['q'])
        
        # SHUFFLE OPTIONS LOGIC
        # 1. Create a COPY of options so we don't mess up the main list
        current_options = item['options'][:] 
        
        # 2. Shuffle this specific copy
        random.shuffle(current_options)
        
        # 3. Print Options with numbers 1-4
        index = 1
        for opt in current_options:
            print(str(index) + ") " + opt)
            index = index + 1
        
        # 4. Find which number (1-4) corresponds to the CORRECT text
        # We search for the correct text in the shuffled list
        correct_index = current_options.index(item['correct_text'])
        correct_number_str = str(correct_index + 1)
        
        # INPUT & TIMER
        start_time = time.time()
        user_input = input("Your Choice (1-4): ")
        end_time = time.time()
        
        duration = int(end_time - start_time)
        
        # SCORING 
        status = "WRONG"
        base_pts = 0
        bonus_pts = 0
        
        if duration > 60:
            print("❌ TIME UP! You took " + str(duration) + " seconds.")
            status = "TIMEOUT"
            
        # Check if user input matches the dynamic correct number
        elif user_input == correct_number_str:
            print("✅ CORRECT! (" + str(duration) + "s)")
            status = "CORRECT"
            base_pts = 10
            
            if duration < 10:
                print("   ⚡ FAST ANSWER BONUS! (+5 pts)")
                bonus_pts = 5
        else:
            print("❌ WRONG! The correct answer was: " + item['correct_text'])
        
        # Stats Update
        question_total = base_pts + bonus_pts
        total_score = total_score + question_total
        
        # Create a dictionary for the report
        record = {
            "num": q_number,
            "stat": status,
            "time": duration,
            "base": base_pts,
            "bonus": bonus_pts,
            "total": question_total
        }
        stats_list.append(record)
        q_number = q_number + 1
        
    # END SCREEN & REPORT
    print("\n" + "="*60)
    print("           PERFORMANCE REPORT: " + name.upper())
    print("="*60)
    
    # Header formatting
    print(f"{'Q#':<4} {'STATUS':<10} {'TIME(s)':<8} {'BASE':<6} {'BONUS':<6} {'TOTAL':<6}")
    print("-" * 60)
    
    # Print rows
    for row in stats_list:
        print(f"{row['num']:<4} {row['stat']:<10} {row['time']:<8} {row['base']:<6} {row['bonus']:<6} {row['total']:<6}")
        
    print("-" * 60)
    print("FINAL SCORE: " + str(total_score) + " / 150")
    print("="*60)
    
    save_score_to_file(name, total_score)
    show_leaderboard()

if __name__ == "__main__":
    start_game()