# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
   The purpose of this game is to have users guess a number within a certain number of attempts. It also gives the user hints after they make a guess (Ex. if their guess was too high or too low). It also keeps track of the user's score and how many attempts they have left.
- [ ] Detail which bugs you found.
   One bug I found was the number of attempts was delayed and wouldn't decrease until after your second guess. I also noticed that the hints the game provided were the compelte opposite of what it should have given. The third bug I saw was that whenever you wanted to start a new game you would get an error message, and the only way to start a new game was to refresh the page.
- [ ] Explain what fixes you applied.
   I implemented fixes in the hints logic and the attempts conunter. I fixed the bug that gave the wrong hints by changing the logic. I also fixed the attempts counter by setting the inital attempts counter to 0 instead of 1 so the user can get the full number of attempts.  

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User selects a difficulty by accessing the left side panel. In this demo we select Normal difficulty
2. User enters a guess of 50
3. Game returns "Too High"
4. User enters a guess of 30 
5. Game returns "Too Low"
6. Score updates after each guess
7. User's number of attempts left decreases after each guess
8. Game ends either after user enters the correct guess or when they run out of attempts

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
