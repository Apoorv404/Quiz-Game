# Quiz-Game

A text-based quiz game implemented in Python using Object-Oriented Programming principles. The game presents users with True/False questions and tracks their score.

## Features

- Multiple True/False questions
- Score tracking
- Question numbering
- Immediate feedback on answers
- Final score summary

## Concepts implemented
- Object-Oriented Programming
- Classes
- Methods
- Attributes
- List
- for Loop, while Loop

## Project Structure

- [`main.py`](main.py): Main game logic and execution
- [`question_model.py`](question_model.py): Question class definition
- [`quiz_brain.py`](quiz_brain.py): QuizBrain class handling game mechanics
- [`data.py`](data.py): Question data stored in dictionary format

## Classes

### Question
- Stores question text and correct answer
- Attributes:
  - `text`: The question text
  - `answer`: The correct answer (True/False)

### QuizBrain
- Manages quiz logic and scoring
- Methods:
  - `still_has_question()`: Checks if more questions remain
  - `next_question()`: Presents next question to user
  - `check_answer()`: Verifies user's answer and updates score

## How to Play

1. Run the `main.py` script
2. Answer each question with "True" or "False"
3. Get immediate feedback on your answer
4. See your current score after each question
5. View your final score when the quiz ends

## Example Usage

```python
Q.1: A slug's blood is green. (True/False): True
You got it right!
The correct answer was True
Your current score: 1/1

Q.2: The loudest animal is the African Elephant. (True/False): False
You got it right!
The correct answer was False
Your current score: 2/2

...

You've completed the quiz.
Your final score: 8/12
```

## Question Database

The quiz includes questions on various topics including:
- Animal facts
- Human anatomy
- Geography
- Technology
- History

## Dependencies

- Python 3.x
- No external libraries required
