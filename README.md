# E-Library

This is a simple FastAPI project for managing a virtual library. It includes routes to perform CRUD (Create, Read, Update, Delete) operations on books.

## Features
- Create new books.
- Retrieve a list of all books or details of a specific book.
- Update book information partially or completely.
- Delete books.

## Requirements
To run this project, ensure you have the following installed:

- Python 3.8 or higher
- Virtual environment (optional but recommended)

## Setup

### 1. Clone the repository:
```bash
git clone <repository-url>
cd E-Library
```

### 2. Create a virtual environment:
```bash
python -m venv venv
```

### 3. Activate the virtual environment:
- On Windows:
  ```bash
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### 4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Start the Server
To start the FastAPI server, run:
```bash
uvicorn main:app --reload
```
The server will be available at `http://127.0.0.1:8000`.

### API Documentation
Interactive API documentation is available at:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Directory Structure
```
E-Library/
├── main.py          # Entry point of the FastAPI application
├── schemas          # Pydantic models for data validation
├── crud             # CRUD logic for managing books
├── routers          # API routes
├── requirements.txt # Project dependencies
├── README.md        # Project documentation
├── .gitignore       # Ignored files and directories
└── ...              # Other supporting files
```

## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

Feel free to modify and enhance this template as needed!

