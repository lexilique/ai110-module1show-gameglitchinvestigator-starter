# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  1) Whenever I guessed a number the hint the game provided was the complete opposite of the truth. For example, if I guessed 50 when the correct number was 20, it would tell me to guess higher when it should be telling me to guess lower.
  2) After each attempt you would expect the attempts left counter to decrease. However this number wouldn't update until after my second guess
  3) Each time I tried to run a new game it would give me an error. I would have to refresh the whole page in order to play a new game, instead of using the restart button.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1) The New Game button did not work and you would have to refresh the page in order to play a new game.
  2) The number of attempts left counter wouldn't start until after your second guess. This meant that by the time you run out of attempts, the counter still tells you that you have 1 attempt left.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior          | Actual Behavior | Console Output / Error   |
|-------|----------------------------|-----------------|--------------------------|
|   50  |      Go Lower              |   Go Higher     |    Go HIGHER!            |
|   75  | Decrement attempts counter |Decrements after attempt| Attempts left: 6|
|New Game|  restart new game         | Error message   | "Game over. Start a new game to try again."|



---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  I used Claude for this project
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
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
