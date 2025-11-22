# BrainStorm: MAT Skill Test

## Overview
BrainStorm is a CLI-based quiz application that tests Mental Ability (MAT). It features random question selection, a strict timer, speed bonuses, and a detailed statistical report at the end of every game.

## Features
* **Input:** User selects options 1-4.
* **Processing:** Calculates time taken.
    * Assigns 10 points for correct answer.
    * Assigns 5 bonus points if time < 10s
* **Detailed Statistics:** Displays a breakdown of base points, bonus points, and time taken for every single question.
* **Leaderboard:** Saves top scores to a `leaderboard.txt` file.
* **Randomization:** Shuffles questions so no two quizzes are the same.While also shuffling the options themselves.
* **Zero Dependencies:** Uses only standard Python libraries (`random`, `time`).

## How to Run
1.  Download `final.py`.
2.  Run command: `python final.py`
