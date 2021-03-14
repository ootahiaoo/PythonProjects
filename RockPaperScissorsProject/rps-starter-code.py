#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.my_move = 'rock'

    def move(self):
        return self.my_move

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def learn(self, my_move, their_move):
        self.my_move = their_move


class CyclePlayer(Player):
    def learn(self, my_move, their_move):
        previous_move = moves.index(my_move)
        if previous_move + 1 < len(moves):
            self.my_move = moves[previous_move + 1]
        else:
            self.my_move = moves[0]


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Rock, paper, scissors? > ").lower()
            if move in moves:
                break
        return move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You played {move1}, Player Two played {move2}.")
        if move1 == move2:
            print("** TIE **")
        else:
            if beats(move1, move2):
                print("** PLAYER ONE WINS **")
                self.p1_score += 1
            else:
                print("** PLAYER TWO WINS **")
                self.p2_score += 1

        print(f"-- Score: \nPlayer One: {self.p1_score} / "
              f"Player Two: {self.p2_score}\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        # Play until one player is ahead by three points
        round = 0
        while True:
            print(f"--- Round {round}: ---")
            self.play_round()
            round += 1
            if self.p1_score == 3:
                print("** PLAYER ONE WON THE GAME **")
                break
            if self.p2_score == 3:
                print("** PLAYER TWO WON THE GAME **")
                break
        print("--- Final Score: ---\n"
              f"Player One: {self.p1_score} / "
              f"Player Two: {self.p2_score}\n")
        print("Thank you for playing!\n")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
