# Tic-tac-toe
# Overview
This is a simple Tic Tac Toe game for two players, built using Python.
It is a console-based game where two users take turns marking cells with 'X' and 'O' on a 3×3 grid.
The first player to place three marks in a row — horizontally, vertically, or diagonally — wins.

# Features
Two-player terminal-based gameplay

Simple and readable board layout

Input validation to ensure correct moves

Win and draw condition detection

No external libraries required

# How to Play
Players take turns choosing a cell numbered from 1 to 9.

A move is valid only if the chosen cell is not already taken.

The game ends when a player wins or all cells are filled (draw).

# Code Structure
print_board(board) — Displays the current game board

check_winner(board, player) — Checks for a winning condition

is_full(board) — Checks if the board is full

play_game() — Main loop that controls gameplay logic

# Requirements
Python 3.x
