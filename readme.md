# 🪓 Hangman Game — Python CLI

A beginner-friendly **command-line Hangman game** developed in Python.  
The player must guess the hidden word letter by letter before the hangman is fully drawn.

This project is designed with **clean logic, simple structure, and clear ASCII visuals**, making it perfect for students and beginners learning Python fundamentals.

---

## 🎯 Project Overview

- A random word is selected from a predefined list
- The player guesses one letter at a time
- Each wrong guess reduces a life and updates the hangman drawing
- The game ends when the word is guessed correctly or all lives are lost

---

## ✨ Key Features

- 🎲 **Random word selection** using Python’s `random` module  
- 🎨 **ASCII hangman stages** that visually represent remaining lives  
- 🔁 **Input validation** to prevent:
  - Non-alphabet characters
  - Multiple-character inputs
  - Repeated guesses  
- ❤️ **Lives-based system** linked directly to hangman stages  
- 🧠 **Beginner-friendly logic** using loops, sets, and strings  

---

## 📚 Concepts Covered

By building this project, you’ll learn:

- Working with **lists, sets, and strings**
- Using **while loops** for continuous gameplay
- Handling **user input safely**
- Implementing **game state management**
- Writing **readable and maintainable Python code**

---

## ▶️ How to Run the Game

1. Install **Python 3.x**
2. Save the file as `hangman.py`
3. Open a terminal and run:


python hangman.py

---

word_list = [
    "mango", "apple", "banana", "papaya", "peach",
    "grapes", "orange", "kiwi", "watermelon", "strawberry"
]
# 🪜 Hangman Stages
The game uses multiple ASCII art stages to represent incorrect guesses, gradually completing the hangman figure as lives decrease.

🏁 Game Outcomes

✅ Win: All letters are guessed before lives run out

❌ Lose: Lives reach zero and the correct word is revealed

# 👨‍💻 Author
  Gaurang Sharma

BTech AI/ML Student
Python & Problem-Solving Enthusiast