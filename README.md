# ♟️ Checkers AI – Minimax with Alpha-Beta Pruning

A Python-based Checkers game with two AI bots competing in a strategic turn-based environment. One bot uses a heuristic evaluation function, while the other implements the Minimax algorithm with alpha-beta pruning for intelligent decision-making. The game features a PyQt5 GUI for real-time visual gameplay.

## 🧠 Features

- Minimax AI with alpha-beta pruning (depth-limited)
- Heuristic evaluation: piece value, kings, and mobility
- PyQt5-based GUI for board rendering
- Bot-vs-Bot gameplay simulation
- Modular design with dynamic method loading
- Real-time execution and performance timing

## 🛠️ Tech Stack

- **Language**: Python 3.12
- **GUI**: PyQt5
- **AI**: Minimax + Alpha-Beta Pruning
- **Structure**: Dynamic import of bot methods (`group1`, `group2`)

## 🚀 How to Run

1. Install dependencies:
   ```bash
   pip install PyQt5
2. Run the game:

bash
Copy
Edit
python main.py

3. Choose AI bots (group1, group2) from the dropdowns and click Play.

## 📁 Project Structure

.
├── main.py             # Launches GUI and game loop
├── group1.py           # Heuristic-based bot
├── group2.py           # Minimax bot (your AI)
├── checkers.py         # Evaluation and game simulation helpers
├── components/         # Contains compiled logic (.pyc)
├── resources/          # GUI assets (images, icons)

## 🤖 Bot Summary
group1: Uses static evaluation with no lookahead

group2: Uses Minimax (depth=3) with alpha-beta pruning for move search

Evaluation factors:

Regular pieces vs kings

Remaining legal moves (mobility)

Material balance
