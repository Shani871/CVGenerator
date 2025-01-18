# CV Generator

A Django-based web application for creating and generating professional CVs.

## Features
- User-friendly form for entering personal details
- Stores CV data in a database
- Generates a downloadable PDF CV
- Built using Django framework

## Technologies Used
- Python
- Django
- HTML/CSS
- SQLite3

## Project Structure
```
CVGenerator/
├── migrations/
├── templates/
│   ├── pdf/
│   │   ├── accept.html
│   │   └── resume.html
├── static/
│   └── styles.css
├── models.py
├── views.py
├── urls.py
├── db.sqlite3
├── manage.py
└── README.md
```

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project folder:
   ```bash
   cd CVGenerator
   ```
3. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```
4. Install the required packages:
   ```bash
   pip install django
   ```
5. Run migrations:
   ```bash
   python manage.py migrate
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```
7. Open the application in your browser: `http://127.0.0.1:8000`

## Usage
- Fill in the CV details form.
- Submit the form to save the data.
- A downloadable PDF CV will be generated based on the data.

## Contributing
Feel free to fork this repository and make contributions! If you encounter any issues, please open a pull request.

## License
This project is open source and available under the MIT License.
