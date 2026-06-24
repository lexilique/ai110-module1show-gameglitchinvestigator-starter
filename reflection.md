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
    One AI suggestion that was correct was changing the inital value of attempt counter from 1 to 0. I verified this result by running through the game again and paying attention to the number of attempts. I also verified this change with pytests.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
    An example of an AI suggestion that was misleading was when I was troubleshooting my test cases. I initally wasn't able to run the pytest command so I asked Claude to help me figure out the problem. It suggested to create a new file to reorder the import path. However, after I did some research and reprompting I could have simply used a different command.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
    I first made sure that the logic of the fix bug made sense. Then I checked to see that each test case for that specific bug passed. To make sure, I also ran through the game myself and tested any edge cases. 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
    One test I ran manually was the attempt counter. I tested each counter on every difficulty to make sure they all decremented correctly.
- Did AI help you design or understand any tests? How?
    The AI I used helped me design the attempt counter tests. I asked it to create a pytest and gave it some context to what the inital bug was so it could test any edge cases.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
    Each time you rerun your Streamlit app, it creates a new session. When a user updates any part of this app, session state stores these changes. Without session state, these changes would not be saved and the app would rerun each variable's values to their inital value when you first started the app.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
    One habit from this project I want to reuse in future labs and projects is to give more context when prompting. Before I would usually copy and paste my problem to an LLM without telling it what exactly happened.
- What is one thing you would do differently next time you work with AI on a coding task?
    One thing I would do differently the next time I work with AI on a coding task is actively review and fact check the suggestions it gives. I should also be more comfortable with starting new chats/redoing prompts if the AI's suggestions aren't accurate enough.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
    This project helped me see that AI generated code isn't terrible to use, but you just have to be careful and fact check what it suggests.

