# paper-scissors-rock

**Paper Scissors Rock** is a game for two players. Each player simultaneously opens his/her
hand to display a symbol:

- Fist equals rock,
- Open hand equals paper,
- Showing the index and middle finger equals scissors.

The winner is determined by the following schema:

- paper beats (wraps) rock,
- rock beats (blunts) scissors,
- scissors beats (cuts) paper

This program enables a user to play **Paper Scissors Rock** against a computer.

## Getting Started

Install Python 3.7.x or newer. You can download the Anaconda Python distribution [here](https://www.anaconda.com/products/individual).

Clone this repository, then open a command prompt and navigate to the project directory (\*/paper-scissors-rock).

Install requirements:

`pip install -r requirements.txt`

Run the program!

`python run.py`


## Notes

### Repository Structure

```
paper-scissors-rock
├── src
│   ├── __init.py__
│   ├── game.py
│   ├── helpers.py
│   ├── main.py
│   ├── player.py
│   ├── robot.py
│   └── round.py
├── tests
│   ├── __init.py__
│   ├── game_test.py
│   ├── helpers_test.py
│   ├── main.py
│   ├── player_test.py
│   ├── robot_test.py
│   └── round_test.py
├── .gitignore
├── readme.md
├── requirements.txt
└── run.py
```

### Classes

The code-base is comprised of four main classes:

- Player class. A player is a participant that makes moves (via user input) in each round of a game.
- Robot class (inherits Player class). A robot is a player that makes moves autonamously in each round of a game.
- Round class. A round consists of one move each from two players and then a winner is determined.
- Game class. A game consists of two participants (players and/or robots). The participants compete for an aribitrary number of rounds. The results across all completed rounds can be tallied at any point.

### Tests

Unit tests have been implemented using the Python [unittest](https://docs.python.org/3/library/unittest.html) library.

All methods for all classes have an associated set of test cases.

Unit tests can be run by navigating to the project directory and then running:

`python -m tests.main`
