# Quiz-Game

A quiz game implemented in Python using Object-Oriented Programming principles. The game presents users with True/False questions and tracks their score through an interactive graphical interface.

## Features

- Multiple True/False questions
- Score tracking
- Question numbering
- Immediate visual feedback on answers
- Final score summary
- Graphical User Interface
- Interactive buttons for True/False responses
- Visual feedback with correct/incorrect indicators

## Concepts implemented
- Object-Oriented Programming
- Classes and Inheritance
- Methods and Attributes
- Tkinter GUI Programming
- Event Handling
- List Operations
- for Loop, while Loop

## Project Structure

- `main.py`: Main game logic and execution
- `question_model.py`: Question class definition
- `quiz_brain.py`: QuizBrain class handling game mechanics
- `data.py`: Question data stored in dictionary format
- `ui.py`: User interface implementation using Tkinter
- `images/`: Directory containing UI assets
  - `true.png`: Image for true button
  - `false.png`: Image for false button

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

### QuizInterface
- Handles the graphical user interface
- Features:
  - Dynamic question display
  - Interactive True/False buttons
  - Visual feedback for answers
  - Score display
  - Automatic question progression

## How to Play

1. Run the `main.py` script
2. Click the True or False button to answer each question
3. Receive immediate visual feedback on your answer
4. Watch your score update in real-time
5. Continue until all questions are answered

## Dependencies

- Python 3.x
- Tkinter (included in standard Python installation)
