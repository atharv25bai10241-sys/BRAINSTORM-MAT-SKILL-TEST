# BRAINSTORM: MAT Skill Test

## Project Overview

BRAINSTORM is an interactive command-line quiz application designed to assess and enhance quantitative reasoning, logical thinking, and problem-solving skills aligned with Management Aptitude Tests (MAT) and similar competitive examinations. The application presents randomized questions across multiple categories including coding patterns, mathematical reasoning, logical sequences, directional sense, and pattern recognition.

The platform provides an engaging quiz experience with time-based scoring, instant feedback, and a persistent leaderboard system to track top performers and encourage competitive learning.

## Problem Statement

Many students preparing for competitive management entrance exams (like MAT, CAT, XAT) struggle to find interactive, real-time feedback systems that help them practice and improve their quantitative and logical reasoning skills. Traditional static question papers lack:

- Interactive feedback and scoring
- Time management practice
- Performance tracking across multiple attempts
- Gamification elements to maintain engagement
- Randomized question sequencing to prevent memorization

BRAINSTORM addresses these gaps by providing a dynamic, user-friendly platform that simulates actual exam conditions while maintaining engagement through bonus scoring and leaderboard rankings.

## Target Users

- Students preparing for management entrance exams (MAT, CAT, XAT, GMAT)
- Competitive examination aspirants
- Educational institutions conducting aptitude assessments
- Self-learners looking to strengthen logical and quantitative reasoning
- Recruiters conducting preliminary screening tests

## Features

### Core Features

1. **Dynamic Question Bank**
   - 12 carefully curated questions covering diverse topics
   - Questions randomized on each game session
   - Covers coding logic, mathematical operations, directional reasoning, series completion, and pattern recognition

2. **Interactive Quiz Interface**
   - Clear command-line interface with formatted questions and options
   - Real-time user input with immediate feedback
   - Emoji-enhanced user experience (✅, ❌, ⚡)
   - Structured performance display

3. **Advanced Scoring System**
   - Base points: +10 for correct answers
   - Bonus points: +5 for answers completed in under 10 seconds
   - Time tracking per question (measured in seconds)
   - Maximum possible score: 150 points

4. **Time Management**
   - 60-second time limit per question
   - Real-time duration tracking
   - Auto-detection of timeout scenarios
   - Displays elapsed time for each question

5. **Randomized Options**
   - Options shuffled for each question session
   - Prevents pattern recognition from option positioning
   - Maintains question integrity while ensuring freshness

6. **Comprehensive Performance Report**
   - Detailed statistics table with Q#, Status, Time, Base Points, Bonus Points
   - Status indicators: CORRECT, WRONG, TIMEOUT
   - Individual and cumulative scoring display
   - Professional formatting with visual separators

7. **Persistent Leaderboard System**
   - Top 5 performers tracked across all sessions
   - Scores stored in external file for data persistence
   - Automatic ranking and sorting
   - Displays rank, player name, and total score

8. **Data Persistence**
   - Leaderboard saved to `leaderboard.txt`
   - Appends each new score to existing records
   - Enables long-term performance tracking

## Technologies & Tools Used

- **Programming Language**: Python 3.x
- **Core Libraries**:
  - `time` - For measuring response duration per question
  - `random` - For shuffling questions and options
- **File I/O**: Text file operations for leaderboard persistence
- **Data Structures**: Lists and dictionaries for question organization and statistics
- **Platform**: Cross-platform command-line application

## Installation & Setup

### Requirements

- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd brainstorm-mat-quiz
   ```

2. **Verify Python Installation**
   ```bash
   python --version
   ```

3. **Place the Script**
   Ensure `final.py` is in your desired working directory.

4. **Create Working Directory**
   ```bash
   mkdir -p quiz_data
   cd quiz_data
   ```

### Running the Project

**Method 1: Direct Execution**
```bash
python final.py
```

**Method 2: Using Python Launcher (Windows)**
```bash
py final.py
```

**Method 3: Make it Executable (Linux/Mac)**
```bash
chmod +x final.py
./final.py
```

The application will start immediately with the title screen and request for player name input.

## Instructions for Testing

### Manual Testing Procedure

1. **Launch Application**
   ```bash
   python final.py
   ```

2. **Input Player Name**
   - Enter any alphanumeric name when prompted
   - Example: `John`, `Player1`, `Alice123`

3. **Review Instructions**
   - Read the on-screen instructions carefully
   - Note the scoring system details
   - Press ENTER to proceed

4. **Answer Questions**
   - Read each question carefully
   - Review all 4 options
   - Enter your choice (1-4) within 60 seconds
   - Watch for real-time feedback

5. **Verify Scoring**
   - Confirm base points (+10 for correct)
   - Check for bonus points (+5 if under 10 seconds)
   - Monitor timeout detection after 60 seconds

6. **Review Performance Report**
   - Check the detailed statistics table
   - Verify final score (max 150 points)
   - Confirm player name is correctly displayed

7. **Check Leaderboard**
   - Review Top 5 rankings
   - Verify score persistence across sessions
   - Play multiple times and confirm rankings update

### Test Cases

**Test Case 1: Correct Answer (Under 10 seconds)**
- Expected: ✅ CORRECT! message + 15 total points (10 base + 5 bonus)

**Test Case 2: Correct Answer (Over 10 seconds, under 60)**
- Expected: ✅ CORRECT! message + 10 points

**Test Case 3: Incorrect Answer**
- Expected: ❌ WRONG! message with correct answer displayed + 0 points

**Test Case 4: Timeout (Over 60 seconds)**
- Expected: ❌ TIME UP! message + 0 points

**Test Case 5: Leaderboard Persistence**
- Expected: Score saved from previous session appears in new leaderboard

## Screenshots / Sample Output

### Game Start Screen
```
============================================================
          BRAINSTORM: MAT SKILL TEST          
============================================================
Enter your Name: Player1

Hello Player1!
Instructions:
1. You have 10 questions.
2. Time Limit: 60 seconds per question.
3. +10 points for correct answer.
4. +5 BONUS points if answered in under 10 seconds.
5. Options are shuffled every time. Watch carefully!

>> Press ENTER to Begin <<
```

### Question Display Sample
```
----------------------------------------
QUESTION 1
If NAME is coded as MZLD, how is PEON coded?
1) OMND
2) ODNM
3) ONDM
4) ODMN
Your Choice (1-4): 
```

### Performance Report Sample
```
============================================================
           PERFORMANCE REPORT: PLAYER1
============================================================
Q#   STATUS     TIME(s)  BASE   BONUS  TOTAL
------------------------------------------------------------
1    CORRECT    5        10     5      15
2    CORRECT    12       10     0      10
3    WRONG      8        0      0      0
4    CORRECT    4        10     5      15
5    TIMEOUT    62       0      0      0
6    CORRECT    9        10     5      15
7    WRONG      15       0      0      0
8    CORRECT    7        10     5      15
9    CORRECT    11       10     0      10
10   CORRECT    6        10     5      15
------------------------------------------------------------
FINAL SCORE: 110 / 150
============================================================
```

### Leaderboard Display
```
==============================
   🏆 TOP 5 LEADERBOARD 🏆
==============================
1. Atharv kala : 145 pts
2. qwerty : 140 pts
3. atharv : 135 pts
4. atharv6 : 130 pts
5. qwertyuiop : 125 pts
==============================
```

## Question Categories & Difficulty

The question bank includes 12 questions across the following categories:

1. **Coding & Pattern Logic** (Questions 1, 5)
   - Symbolic substitution and pattern matching

2. **Mathematical Reasoning** (Questions 2, 7, 10)
   - Numerical operations and algebraic calculations
   - Operator substitution logic

3. **Spatial & Directional Reasoning** (Question 3)
   - Navigation and directional sense
   - Coordinate-based problem solving

4. **Series & Sequence Analysis** (Question 4)
   - Number pattern completion
   - Mathematical progressions

5. **Geometric Reasoning** (Questions 6, 8, 9)
   - Time-based calculations (clock angles)
   - 3D spatial visualization and cutting logic
   - Cube-related computations

6. **Logical Matrix & Number Logic** (Questions 11, 12)
   - Alphabetic sequence logic
   - Function-based numerical patterns

## Scoring Methodology

### Point Allocation

| Criterion | Points |
|-----------|--------|
| Correct Answer | +10 |
| Speed Bonus (≤10 sec) | +5 |
| Wrong Answer | 0 |
| Timeout (>60 sec) | 0 |

### Score Calculation

- **Question Score** = Base Points + Bonus Points
- **Session Score** = Sum of all 10 question scores
- **Maximum Possible** = 150 points (10 questions × 10 base + 10 questions × 5 bonus)
- **Leaderboard Ranking** = By total score (descending order)

### Performance Levels

- 130-150: Excellent
- 110-129: Very Good
- 90-109: Good
- 70-89: Average
- Below 70: Needs Improvement

## Code Architecture

### File Structure
```
brainstorm-mat-quiz/
├── final.py                 # Main application script
├── leaderboard.txt          # Generated leaderboard data (auto-created)
├── README.md                # This file
└── statement.md             # Project statement
```

### Key Components

**1. Data Structure: Question Bank**
```python
question_bank = [
    {
        "q": "Question text",
        "options": ["Option1", "Option2", "Option3", "Option4"],
        "correct_text": "CorrectOption"
    }
]
```

**2. Helper Functions**

- `save_score_to_file(name, score)`: Appends player score to leaderboard.txt
- `show_leaderboard()`: Reads leaderboard file and displays Top 5 ranked players

**3. Main Logic Function**

- `start_game()`: Orchestrates entire quiz workflow including question display, user input, scoring, and report generation

**4. Core Features Implementation**

- Question randomization using `random.shuffle()`
- Option shuffling per question session
- Time measurement using `time.time()`
- Dynamic correct answer indexing after option shuffle
- Formatted output using f-strings and print formatting

## Challenges Faced & Solutions

### Challenge 1: Maintaining Correct Answer After Option Shuffling
**Problem**: After shuffling options, the correct answer position changes, but must still be identifiable.
**Solution**: Create a copy of options list, shuffle it, and then search for the correct text value in the shuffled list to determine its new position.

### Challenge 2: File I/O Error Handling
**Problem**: Leaderboard file might not exist on first run.
**Solution**: Implemented try-except blocks with FileNotFoundError handling to gracefully manage missing files.

### Challenge 3: Precise Time Measurement
**Problem**: Capturing exact response time while accounting for I/O operations.
**Solution**: Used `time.time()` immediately before and after input() to measure precise duration.

### Challenge 4: Formatting Output Cleanly
**Problem**: Aligning performance report data in readable columns.
**Solution**: Used Python f-strings with field width specifiers for consistent column alignment.

## Learnings & Key Takeaways

1. **Data Structure Design**: Dictionaries within lists provide flexible, scalable question organization
2. **File Persistence**: Understanding file I/O operations and error handling for data durability
3. **Time Measurement**: Practical application of timing functions in quiz/exam contexts
4. **User Experience**: Emoji and formatting enhance engagement in CLI applications
5. **Randomization**: Importance of shuffling algorithms in preventing pattern recognition
6. **Scoring Systems**: Gamification through bonus points increases user motivation
7. **Competitive Elements**: Leaderboards drive engagement and repeat usage

## Future Enhancements

1. **Question Difficulty Levels**
   - Implement Easy, Medium, Hard categories
   - Allow users to select difficulty level at start

2. **User Authentication & Profiles**
   - Create user accounts with password protection
   - Persistent user profiles with score history
   - Individual performance analytics

3. **Enhanced Database**
   - Replace text file with SQLite database
   - Support for complex queries and filtering
   - User statistics and trend analysis

4. **Question Management System**
   - Admin interface to add/edit/delete questions
   - Categorization by topic and difficulty
   - Dynamic question loading from database

5. **Analytics Dashboard**
   - Graphical performance charts
   - Question-wise success rate analysis
   - Time distribution statistics

6. **Multiplayer Mode**
   - Real-time competitive quizzes
   - Networking capabilities for simultaneous play

7. **Web Interface**
   - Convert CLI to web application using Flask/Django
   - Browser-based accessibility
   - Enhanced UI/UX with HTML/CSS/JavaScript

8. **Mobile Application**
   - Native mobile app development
   - Offline quiz capability
   - Push notifications for streak tracking

9. **Adaptive Difficulty**
   - AI-based question selection based on performance
   - Personalized learning paths

10. **Timed Challenges & Tournaments**
    - Special time-bound events
    - Seasonal leaderboards
    - Achievement badges and milestones

## References & Resources

1. **Python Documentation**: https://docs.python.org/3/
2. **Time Module**: https://docs.python.org/3/library/time.html
3. **Random Module**: https://docs.python.org/3/library/random.html
4. **Aptitude Test Resources**: MAT/CAT exam preparation guides
5. **File I/O Best Practices**: Python file handling documentation

## Author & Contact

**Project**: BRAINSTORM - MAT Skill Test  
**Version**: 1.0  
**Created**: 20/11/2025

For questions, suggestions, or contributions, please contact the developer(Atharv Kala) or submit issues through the GitHub repository.

## License

This project is for educational purposes as part of academic coursework in VITyarthi.

---

**Last Updated**: November 2025  
**Status**: Active & Maintained
