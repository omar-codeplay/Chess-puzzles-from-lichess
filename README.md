# ♟️ Ultimate Lichess Offline Puzzle Trainer

A high-performance, offline-first chess puzzle trainer. This repository provides a massive database of over 40,000 Lichess puzzles, categorized and split into optimized JSON chunks for instant web loading.

## 🚀 Features
- **Offline First:** No API calls needed during gameplay. 
- **Massive Database:** 40,000+ puzzles included in `data/` (2,000 per file).
- **Adaptive Difficulty:** Automatically increases puzzle rating as you solve.
- **Theme Filtering:** Practice specific tactics (Forks, Pins, Mates, etc.).
- **Mistake Animation:** High-fidelity experience—watch the opponent blunder before you move.

## 📂 Project Structure
- `/index.html` - The trainer interface.
- `/js/app.js` - The ultimate puzzle engine.
- `/puzzles/` - Directory containing `puzzles_part_1.json` through `puzzles_part_20.json`.
- `/scripts/downloader.py` - The Python script to fetch more puzzles or refresh the database.

## 🛠️ How to Use
1. Clone the repository.
2. Ensure `puzzles_part_X.json` files are in the root or a designated folder.
3. Because browsers restrict local file access (CORS), run a local server:
   ```bash
   # If you have Python
   python -m http.server 8000
