import tkinter as tk
####
WINS = [
    [0,1,2],[3,4,5],[6,7,8],
    [0,3,6],[1,4,7],[2,5,8],
    [0,4,8],[2,4,6]
]

BG       = "#1a1a2e"
CELL_BG  = "#16213e"
HOVER_BG = "#0f3460"
WIN_BG   = "#0f3460"
X_COLOR  = "#e94560"
O_COLOR  = "#a8dadc"
BTN_COLOR = "#e94560"
BTN_HOVER = "#c73652"

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.configure(bg=BG)
        self.root.resizable(False, False)

        self.scores = {"X": 0, "O": 0, "draw": 0}
        self._build_ui()
        self.init()

    def _build_ui(self):
        tk.Label(self.root, text="Tic Tac Toe", bg=BG, fg=X_COLOR,
                 font=("Segoe UI", 28, "bold")).pack(pady=(24, 8))

        score_frame = tk.Frame(self.root, bg=BG)
        score_frame.pack(pady=(0, 8))
        self.x_lbl   = tk.Label(score_frame, text="X: 0",     bg=BG, fg=X_COLOR, font=("Segoe UI", 12, "bold"))
        self.d_lbl   = tk.Label(score_frame, text="Draws: 0", bg=BG, fg="#aaaaaa", font=("Segoe UI", 12, "bold"))
        self.o_lbl   = tk.Label(score_frame, text="O: 0",     bg=BG, fg=O_COLOR, font=("Segoe UI", 12, "bold"))
        self.x_lbl.pack(side="left", padx=20)
        self.d_lbl.pack(side="left", padx=20)
        self.o_lbl.pack(side="left", padx=20)

        self.status_lbl = tk.Label(self.root, text="", bg=BG, fg=O_COLOR, font=("Segoe UI", 13))
        self.status_lbl.pack(pady=(0, 12))

        board_frame = tk.Frame(self.root, bg=BG)
        board_frame.pack()
        self.buttons = []
        for i in range(9):
            btn = tk.Button(
                board_frame, text="", width=4, height=2,
                bg=CELL_BG, activebackground=HOVER_BG,
                relief="flat", bd=0, font=("Segoe UI", 28, "bold"),
                cursor="hand2",
                command=lambda idx=i: self.click(idx)
            )
            btn.grid(row=i//3, column=i%3, padx=5, pady=5, ipadx=8, ipady=8)
            btn.bind("<Enter>", lambda e, b=btn: self._on_enter(b))
            btn.bind("<Leave>", lambda e, b=btn: self._on_leave(b))
            self.buttons.append(btn)

        reset_btn = tk.Button(
            self.root, text="New Game",
            bg=BTN_COLOR, fg="white", activebackground=BTN_HOVER,
            relief="flat", bd=0, font=("Segoe UI", 11),
            cursor="hand2", padx=24, pady=8,
            command=self.init
        )
        reset_btn.pack(pady=20)

    def init(self):
        self.board    = [""] * 9
        self.current  = "X"
        self.game_over = False
        for btn in self.buttons:
            btn.config(text="", bg=CELL_BG, fg="white", state="normal")
        self.status_lbl.config(text="X's turn")

    def _on_enter(self, btn):
        if btn["text"] == "" and not self.game_over:
            btn.config(bg=HOVER_BG)

    def _on_leave(self, btn):
        if btn["bg"] == HOVER_BG and btn["text"] == "":
            btn.config(bg=CELL_BG)

    def click(self, i):
        if self.game_over or self.board[i]:
            return
        self.board[i] = self.current
        color = X_COLOR if self.current == "X" else O_COLOR
        self.buttons[i].config(text=self.current, fg=color, state="disabled",
                                disabledforeground=color)

        result = self.check_winner()
        if result:
            self.game_over = True
            if result.get("winner"):
                for j in result["line"]:
                    self.buttons[j].config(bg=WIN_BG)
                self.status_lbl.config(text=f"{result['winner']} wins!")
                self.scores[result["winner"]] += 1
            else:
                self.status_lbl.config(text="It's a draw!")
                self.scores["draw"] += 1
            self._update_scores()
        else:
            self.current = "O" if self.current == "X" else "X"
            self.status_lbl.config(text=f"{self.current}'s turn")

    def check_winner(self):
        for a, b, c in WINS:
            if self.board[a] and self.board[a] == self.board[b] == self.board[c]:
                return {"winner": self.board[a], "line": [a, b, c]}
        if all(self.board):
            return {"winner": None, "draw": True}
        return None

    def _update_scores(self):
        self.x_lbl.config(text=f"X: {self.scores['X']}")
        self.d_lbl.config(text=f"Draws: {self.scores['draw']}")
        self.o_lbl.config(text=f"O: {self.scores['O']}")


if __name__ == "__main__":
    root = tk.Tk()
    TicTacToe(root)
    root.mainloop()
