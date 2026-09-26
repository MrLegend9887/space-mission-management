# Space Mission Management System

A Python-based Space Mission Management System built using Object-Oriented Programming (OOP).

The project manages astronauts, missions, astronaut assignments, mission status, mission capacity, searching, reporting, validation, and data consistency.

## Features

- Create and manage space missions
- Register and manage astronauts
- Search missions by ID, destination, and status
- Update mission information
- Manage mission status transitions
- Assign astronauts to missions
- Unassign astronauts from missions
- Track astronaut availability
- Enforce mission astronaut capacity
- Generate mission and astronaut reports
- Validate mission and astronaut operations
- Handle invalid operations and edge cases
- Automated testing using Python's built-in `unittest` framework

## Project Structure

    P3_Space_Mission_Management/
    │
    ├── main.py
    ├── astronaut.py
    ├── mission.py
    ├── mission_manager.py
    │
    └── tests/
        └── test_mission_manager.py

## Modules

### `astronaut.py`

Contains the `Astronaut` class.

The class represents an astronaut and stores information such as:

- Astronaut ID
- Name
- Date of birth
- Country
- Height
- Specialization
- Assigned mission

It also provides methods for updating astronaut information.

### `mission.py`

Contains the `Mission` class.

The class represents a space mission and manages:

- Mission ID
- Mission name
- Launch date
- Destination
- Mission status
- Assigned astronauts
- Mission capacity

It also handles astronaut assignment, removal, status changes, and mission information updates.

### `mission_manager.py`

Contains the `MissionManager` class.

The manager acts as the central system responsible for:

- Managing missions
- Managing the astronaut registry
- Finding missions and astronauts
- Assigning and unassigning astronauts
- Searching and filtering missions
- Generating reports and statistics
- Validating operations
- Managing mission capacity

### `main.py`

Acts as the application's entry point.

It creates the required objects and demonstrates the functionality of the system.

## Architecture

The project separates responsibilities into different modules.

    main.py
       │
       ▼
    MissionManager
       /       \
      /         \
     ▼           ▼
    Mission   Astronaut

### Responsibility Flow

- `Astronaut` represents an individual astronaut.
- `Mission` represents a space mission and its assigned astronauts.
- `MissionManager` coordinates missions and astronauts.
- `main.py` acts as the entry point of the application.

The modules are separated to keep the code organized and reduce unnecessary dependencies.

## Requirements

- Python 3.x
- No external Python packages are required.

## How to Run

Clone the repository and navigate to the project directory.

Run:

    python main.py

## Running Tests

The project uses Python's built-in `unittest` framework.

Run all tests with:

    python -m unittest discover -s tests -v

The current test suite contains 22 automated tests covering mission management, astronaut registration, assignment, validation, capacity, and status transitions.

## Validation & Error Handling

The system validates several operations before modifying its data.

Examples include:

- Preventing duplicate mission registration
- Preventing duplicate astronaut registration
- Rejecting assignments to unknown missions
- Rejecting assignments of unknown astronauts
- Preventing an astronaut from being assigned to multiple missions
- Preventing assignments when a mission is full
- Preventing invalid mission status values
- Preventing invalid mission status transitions
- Handling invalid dates
- Validating astronaut unassignment operations

## Testing

Automated tests are used to verify the behavior of the `MissionManager`.

The tests cover:

- Mission creation and removal
- Mission lookup
- Mission searching
- Mission status transitions
- Astronaut registration
- Astronaut lookup
- Astronaut assignment
- Astronaut unassignment
- Mission capacity
- Validation and edge cases

Current test result:

    22 tests
    22 passed

## Current Limitations

The current version is an in-memory Python application.

Data is not persisted to a database or external storage, so information is lost when the application terminates.

The project currently focuses on the core domain logic and does not provide a graphical user interface or web interface.

## Learning Goals

This project was developed to practice software engineering concepts including:

- Object-Oriented Programming
- Class design
- Object relationships
- Separation of responsibilities
- Validation
- Error handling
- Automated testing
- Refactoring
- Modular project structure
- Git and GitHub workflow