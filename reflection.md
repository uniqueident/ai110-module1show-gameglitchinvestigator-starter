# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

The game gave conflicting hints, being incorrect, and backwards.
It also listed the incorrect amount of attempts, and failed to write the actual range of numbers selected for the Easy, Medium, and Hard mode.


- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| guess of -1 | "Too Low":Hint | "Too High":Hint | none |
| 7 guesses on Normal | 8 guesses allowed | 7 guesses allowed | none |
| Easy mode selected (and new game selected)| Secret range between 1 to 20 | range from 1 to 100 | none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - One example of a sugession that was correct was about moving the functions over to a different file. I verified the result by looking over the diff, and running the game again. As such I only needed to see if the text was the same for the functions being moved over and the functions in the logic_utils.py file.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - Skimming through the testing, I noticed that the AI create two of the same test case, but labelled them differently, given that they both had the same assumptions and tests going on, but claimed to test different things, as such I had it remove the case, and create one that actually covered the `None` condition in python, instead of asserting that an empty string `""` and `None` are the same (they are not). This is Despite the fact that they are both falsy according to Python logic.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - I stepped through the conditional logic per "unit" function or method in this case. And Saw that if the individual units were working logistically with what should be expected from a simplistic application, I would consider it good. As such,
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
