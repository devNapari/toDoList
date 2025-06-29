# To-Do List Flask Application

This is a simple To-Do List application built using Flask and SQLite. The application allows users to manage their tasks by adding new tasks, deleting individual tasks, and clearing all tasks.

## Project Structure

```
toDoList-flask-app
├── app
│   ├── main.py          # Main entry point of the Flask application
│   ├── templates
│   │   └── index.html   # HTML template for displaying tasks
│   └── static
│       └── style.css    # CSS styles for the application
├── requirements.txt      # List of dependencies
└── README.md             # Project documentation
```

## Requirements

To run this application, you need to have Python installed on your machine. You also need to install the required packages listed in `requirements.txt`.

## Installation

1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Install the required packages using pip:

```
pip install -r requirements.txt
```

## Running the Application

1. Make sure you have created the `todo.db` file in the same directory as `main.py` or adjust the path accordingly.
2. Run the application:

```
python app/main.py
```

3. Open your web browser and go to `http://127.0.0.1:5000/` to access the To-Do List application.

## Features

- View the list of tasks
- Add new tasks
- Delete individual tasks
- Clear all tasks

## License

This project is open-source and available under the MIT License.