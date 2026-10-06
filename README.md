# Mini Games – BDD & TDD

This project contains small games developed and tested using **Behaviour Driven Development (BDD)** and **Test Driven Development (TDD)**.

## Games

The project contains:

* Number Guessing Game
* Hangman
* Game Hub Menu

## BDD

The expected behaviour of the games is described using BDD scenarios following the:

* **Given** – the starting situation
* **When** – an action is performed
* **Then** – the expected result

The scenarios are used as a guide when creating the automated tests.

## TDD

The development follows the TDD cycle:

1. Write a test for a behaviour.
2. Run the test and confirm that it fails.
3. Implement the functionality.
4. Run the test again and confirm that it passes.
5. Refactor when needed while keeping the tests passing.

The Git history and branches are used to demonstrate this process.

## Testing

The tests are written using `pytest`.

Run the tests with:

```bash
pytest
```

## Project Structure

```text
mini-games-tdd/
├── mini_games.py
├── tests/
│   ├── test_number_guessing.py
│   ├── test_hangman.py
│   └── test_game_hub.py
└── README.md
```

## Git Branches

The project will contain two branches demonstrating the TDD process:

* **tests** – contains the tests before the functionality is implemented. The tests run but fail.
* **tdd** – contains the implementation together with the tests. The tests run and pass.
