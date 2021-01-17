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

The codebase is comprised of four main classes:

- Player class. A player is a participant that makes moves (via user input) in each round of a game.
- Robot class (inherits Player class). A robot is a player that makes moves autonamously in each round of a game.
- Round class. A round consists of one move each from two players and then a winner is determined.
- Game class. A game consists of two participants (players and/or robots). The participants compete for an aribitrary number of rounds. The results across all completed rounds can be tallied at any point.

### Tests

Unit tests have been implemented using the Python [unittest](https://docs.python.org/3/library/unittest.html) library.

All methods for all classes have an associated set of test cases.

Where functions/methods require user inputs, the user inputs are mocked using a unittest [patch](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch) decorator.

Unit tests can be run by navigating to the project directory and then running:

`python -m tests.main`

### Exception Handling

At times the user will be prompted to enter information via the command line (e.g.: name, number of rounds to play, move to make, etc). Exception handling is used to capture and handle occasions when user inputs are invalid. This is done in two steps:
- First, the [get_input](https://github.com/davidconalrobinson/paper-scissors-rock/blob/d036c051e6f368ffe9fdec7a68d36acc56719374/src/helpers.py#L12) function will raise a valueError if the input is not in a set of specified values and/or if a non-numeric value is entered when a numeric value is expected.
- Second, in the event that an exception is raised, the [try_again](https://github.com/davidconalrobinson/paper-scissors-rock/blob/d036c051e6f368ffe9fdec7a68d36acc56719374/src/helpers.py#L27) function is used to print the exception error message and then prompt the user to try again.

### Extensibility

The codebase has been developed with extensibility in mind. In particular:
- New attributes and methods can be added to existing classes, or new classes can inherit existing classes.
- Modular components can be replaced or updated. For example, at initialisation a 'move model' is selected for any Robot object. This model will be invoked every time the robot makes a move. By default, the [Robot.simple_move_model()](https://github.com/davidconalrobinson/paper-scissors-rock/blob/d036c051e6f368ffe9fdec7a68d36acc56719374/src/robot.py#L26) will be selected - however, if new models are developed then these can be altenatively selected when a Robot object is initialised.

### Future Development

Some options for developing this program further:
- Containerise the program (e.g.: Docker) - will help to manage dependencies.
- Pattern recognition could be used to develop a robot move model that anticipates and responds to patterns in the users moves.
- Player and game information could be stored in a SQL database - this can be done quite easily by using the SQLAlchemy ORM to map existing classes to relational database objects.
- Build a simple web API around classes and methods (e.g.: using Flask) - this would enable lightweight web to be built that users could interact with remotely.
- Build a lightweight UI (e.g.: PyQT).
