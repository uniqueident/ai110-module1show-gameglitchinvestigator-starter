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
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User selects a difficulty (defaults to normal)
2. User guesses between the ranges given, lets say 1, 100 is the range.
   1. The user chose to guess 50
3. Game returns "Too High"
4. User enters a Guess of 1
5. Game returns "Too Low"
6. User continues guessing until they are correct or out of guesses.
7. Game continues responding with Too High or Too Low until the user is correct or out of guesses.
8. Repeat 6-7 until done.
9. IF the user guesses correct, they are congratulated.
10. IF the user does not guess correctly in their amount of guesses, they lose and can choose to try again.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
======================================================================================================== test session starts ========================================================================================================
platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0
rootdir: /home/uniqueident/gameglitch/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.14.0
collected 13 items                                                                                                                                                                                                                  

tests/test_game_logic.py .............                                                                                                                                                                                        [100%]

======================================================================================================== 13 passed in 0.03s =========================================================================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
