# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the project

```bash
# Run the desktop GUI (requires tkinter, included with macOS Python)
python tictactoe.py

# Run the browser version (open directly in any browser)
open tictactoe.html

# Run the test file
python test.py
```

## Git workflow

All meaningful changes must be committed with a clean message and pushed to GitHub:

- Remote: https://github.com/Javiermb1983/claude-code-first-project
- Branch: `main`
- Stage specific files only — never `git add -A` (excludes `.DS_Store`, `.vscode/`, `.claude/`)
- Commit message format: short subject line (imperative mood) + blank line + body explaining what and why

## Architecture

The game logic is implemented twice, in two independent versions that share the same design language (dark navy palette, X in red `#e94560`, O in teal `#a8dadc`):

- **`tictactoe.py`** — desktop app using `tkinter`. All state and UI live in the `TicTacToe` class. Board is a flat 9-element list; win detection iterates the `WINS` constant (8 winning triplets).
- **`tictactoe.html`** — single-file browser app. Same game logic in vanilla JS, no dependencies. CSS, HTML, and JS are all inline in one file.

Both versions track persistent scores (X wins, O wins, draws) across rounds within a session. "New Game" resets the board but not the scores.
