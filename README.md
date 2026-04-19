
# Chess Puzzles from Lichess

A streamlined tool designed to fetch and manage tactical puzzles from the [Lichess Open Database]([https://database.lichess.org/#puzzles](https://huggingface.co/datasets/Lichess/chess-puzzles)). This project allows users to retrieve high-quality chess tactics for analysis, training, or application development.

## 🚀 Features

- **puzzles_fetcher.py**: A dedicated script to automate the process of downloading and filtering puzzle data directly from Lichess.
- **Ready-to-Use Data**: Includes an initial set of **20 curated puzzles** to get you started immediately without any configuration.
- **Detailed Metadata**: Each puzzle includes FEN strings, solution moves, Elo ratings, and tactical themes.

## 🛠 Installation

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/omar-codeplay/Chess-puzzles-from-lichess.git](https://github.com/omar-codeplay/Chess-puzzles-from-lichess.git)
   cd Chess-puzzles-from-lichess

```
 2. **(Optional) Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   
   ```
 3. **Install Dependencies**:
   *(If you have a requirements file)*
   ```bash
   pip install requests

   ```
## 📖 Usage
### Fetching New Puzzles
To run the fetcher and update your local puzzle set, execute:
```bash
python puzzles_fetcher.py

```
### Exploring the Sample Set
The repository comes pre-loaded with **20 puzzles**. You can find these in the project directory (e.g., puzzles.csv or data/), ready for parsing or manual study.
## 📁 Project Structure
```text
├── puzzles_fetcher.py   # Main script for data retrieval
├── puzzles.csv          # Initial set of 20 sample puzzles
├── src/                 # (Optional) Core logic and utility scripts
├── requirements.txt     # List of required Python packages
└── README.md            # Project documentation

```
## ♟️ About Lichess Puzzles
All puzzles are sourced from Lichess.org. These puzzles are:
 * Generated from real games played on Lichess.
 * Verified by Stockfish for accuracy.
 * Released under the **CC0 (Creative Commons Public Domain)** license.
## 🤝 Contributing
Contributions are welcome! If you want to add more features to the fetcher or improve the data handling, feel free to:
 1. Fork the repository.
 2. Create a feature branch.
 3. Submit a Pull Request.
*Maintained with ❤️ by omar-codeplay*
```

```
