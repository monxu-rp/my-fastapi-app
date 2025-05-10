# Practice Project with Python and Hexagonal Architecture

This project is designed to practice and experiment with various concepts and tools in Python, such as:

- **Hexagonal Architecture**: Implementing the architecture to promote a clean and flexible structure within the application.
- **FastAPI**: Building a fast and efficient API using FastAPI.
- **Unit Tests**: Including unit tests to ensure the proper functionality of each component in the system.
- **Integration Tests**: Adding integration tests to verify that the different components of the application interact correctly.
- **And whatever comes up...**: As the project progresses, other technologies and techniques are explored as well.

## Objectives

The main goal of this project is to enhance skills in Python development while applying principles of clean architecture and good software development practices.

## Requirements

- Python 3.x
- FastAPI
- Uvicorn
- pytest
- httpx (for integration tests)
- coverage (for test coverage reports)

## Installation


1. Clone the repository:

   ```bash
   git clone https://github.com/username/project.git
   ```

1. Create a virtual environment (optional but recommended):

   ```bash
    python -m venv .venv
   ```

   1. On Windows, use this command to activate the virtual environment:

       ```bash
       .\.venv\Scripts\activate
       ```
   1. On macOS/Linux, use this command to activate:

       ```bash
       source .venv/bin/activate
       ```

1. Install dependencies:
   1. For production:
       ```bash
       pip install -r requirements.txt
       ```
   1. For development:
      ```bash
      pip install -r dev-requirements.txt
      ```
1. Run the application:

   ```bash
    uvicorn app.main:app --reload
   ```

1. Run the tests:

   ```bash
   pytest
   ```
1. Run the tests with coverage:

   ```bash
   coverage run -m pytest
   coverage report
   coverage html  # Genera un informe visual en htmlcov/index.html
   ```

1. To destroy the virtual environment, use this command:

    ```bash
    deactivate
    ```