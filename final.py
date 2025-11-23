import time
import random

# List of questions
# Keys: q = question, o = options, a = correct answer text
# More questions can be added later (T_T)
questions = [
    {"q": "If NAME is coded as MZLD, how is PEON coded?", "o": ["ODNM", "ODMN", "ONDM", "OMND"], "a": "ODNM"},
    {"q": "If P=16 and TAP=37, then CUP=?", "o": ["40", "38", "36", "39"], "a": "40"},
    {"q": "Adhar goes 4km straight, turns right (3km), then right (2km). Direction?", "o": ["North", "South", "East", "West"], "a": "East"},
    {"q": "Series: 2, 8, 18, 32, 50, ?", "o": ["64", "72", "70", "68"], "a": "72"},
    {"q": "Missing Code: Z9A, X7D, ?, T3J", "o": ["W6F", "S3H", "G9V", "V5G"], "a": "V5G"},
    {"q": "Angle of clock hands at 9:30?", "o": ["75 deg", "90 deg", "105 deg", "120 deg"], "a": "105 deg"},
    {"q": "Math: If '+' is 'x', '-' is '+'. Solve: 21 / 8 + 2 - 12 x 3", "o": ["14", "9", "13.5", "11"], "a": "9"},
    {"q": "12cm cube cut into 3cm cubes. Total small cubes?", "o": ["16", "64", "128", "32"], "a": "64"},
    {"q": "Cube Slicing: Total corner (vertex) cubes?", "o": ["4", "8", "12", "16"], "a": "8"},
    {"q": "Product of 3 consecutive integers is 210. Sum of smaller two?", "o": ["13", "11", "12", "18"], "a": "11"},
    {"q": "Logic Matrix: A, D, H ... F, L, M ... ?, N, R", "o": ["K", "N", "O", "P"], "a": "K"},
    {"q": "Number Logic: 2->4, 3->27, 4->?", "o": ["56", "49", "45", "64"], "a": "64"}
]

def update_leaderboard(player, points):
    # Appending to file
    try:
        f = open("leaderboard.txt", "a")
        f.write(player + "," + str(points) + "\n")
        f.close()
    except:
        print("Could not save score.")

def print_top_scores():
    print("\n------------------------------")
    print("   TOP 5 PLAYERS")
    print("------------------------------")
    
    try:
        f = open("leaderboard.txt", "r")
        content = f.readlines()
        f.close()
        
        scores = []
        for line in content:
            clean_line = line.strip()
            # check if line has data
            if "," in clean_line:
                data = clean_line.split(",")
                name = data[0]
                # convert score to int
                sc = int(data[1])
                scores.append([name, sc])
        
        # Sort desc
        scores.sort(key=lambda x: x[1], reverse=True)
        
        count = 1
        # only shows the top 5
        for s in scores[:5]:
            print(str(count) + ". " + s[0] + " - " + str(s[1]))
            count += 1
            
    except:
        print("No records found.")
    
    print("------------------------------\n")

def run_quiz():
    print("==================================================")
    print("           MAT SKILL TEST - BRAINSTORM")
    print("==================================================")
    
    p_name = input("Enter Player Name: ")
    
    # Shuffle list
    random.shuffle(questions)
    # Pick first 10
    my_quiz = questions[:10]
    # THESE ARE THE RULES:-
    print("\nHello " + p_name + "!")
    print("Instructions:")
    print("1. You have 10 questions.")
    print("2. Time Limit: 60 seconds per question.")
    print("3. +10 points for correct answer.")
    print("4. +5 BONUS points if answered in under 10 seconds.")
    input("\n>> Press ENTER to Begin <<")
    score = 0
    report_card = []
    
    i = 1
    for q in my_quiz:
        print("\nQ" + str(i) + ": " + q['q'])
        
        # copy and shuffle options
        opts = q['o'][:]
        random.shuffle(opts)
        
        # print options 1-4
        k = 1
        for o in opts:
            print(str(k) + ") " + o)
            k += 1
            
        # find where the answer is
        ans_text = q['a']
        ans_index = opts.index(ans_text)
        # correct choice number (string)
        correct_choice = str(ans_index + 1)
        
        # Timing
        start = time.time()
        try:
            user_ans = input("Answer (1-4): ")
        except:
            user_ans = "0" # invalid
        end = time.time()
        
        t_taken = int(end - start)
        
        # Scoring logic
        res = "Wrong"
        pts = 0
        bonus = 0
        
        if t_taken > 60:
            print("Time Up! Too slow.")
            res = "Timeout"
        elif user_ans == correct_choice:
            print("Correct!")
            res = "Correct"
            pts = 10
            # bonus check
            if t_taken < 10:
                print("Speed Bonus! +5")
                bonus = 5
        else:
            print("Wrong. Correct was: " + ans_text)
            
        # calc totals
        total_pts = pts + bonus
        score += total_pts
        
        # save stats
        stats = {
            "n": i,
            "res": res,
            "t": t_taken,
            "p": pts,
            "b": bonus,
            "tot": total_pts
        }
        report_card.append(stats)
        
        i += 1
        print("-" * 30)

    # End Stats
    print("\n========================================")
    print(" RESULTS FOR: " + p_name)
    print("========================================")
    # Simple tabs instead of complex formatting
    print("Q#\tResult\tTime\tBase\tBonus\tTotal")
    
    for r in report_card:
        print(str(r['n']) + "\t" + r['res'] + "\t" + str(r['t']) + "s\t" + str(r['p']) + "\t" + str(r['b']) + "\t" + str(r['tot']))
        
    print("----------------------------------------")
    print("FINAL SCORE: " + str(score))
    
    update_leaderboard(p_name, score)
    print_top_scores()
#finally game over :)
if __name__ == "__main__":
    run_quiz()
