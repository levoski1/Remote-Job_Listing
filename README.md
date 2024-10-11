
# Remote Job Opportunities Website

## Project Overview
The **Remote Job Opportunities Website** is a web application designed to help companies post remote job listings and provide a platform for job seekers to find relevant job opportunities. This project targets companies seeking ALX graduates and other remote job seekers, facilitating an easy job posting and searching process.

### Key Features:
- Company dashboard for managing job listings.
- Ability to post, edit, and delete job listings.
- Separation of active and expired job listings.
- Search functionality for job seekers (yet to be implemented in MVP).
- Responsive design for both mobile and desktop devices.

## Table of Contents
- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites:
- Python 3.7 or higher
- SQLite (since we are using SQLite as the database)
- Flask and other dependencies (listed in `requirements.txt`)

### Steps to Install:
1. Clone the repository:
    ```bash
    git clone https://github.com/levoski1/Remote-Job_Listing.git
    cd Remote-Job_Listing
    ```

2. Set up a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask app:
    ```bash
    flask run
    ```

5. Visit `http://127.0.0.1:5000/` to view the website locally.


6. Default Email and Password:
    ```
    levibliss20@gmail.com
    aaaaa
    ```

## Usage

### For Companies:
1. Register as a company by visiting `/company-register`.
2. After registration, log in at `/company-login`.
3. Access your dashboard at `/company-dashboard` to:
   - Post new jobs.
   - View active and expired job listings.
   - Edit or delete job listings.

### For Job Seekers:
- The search and filter features will be included in the future iterations.

### Database:
- The project uses **SQLite** for local development. A production-ready deployment should switch to a cloud-hosted database.

## Folder Structure

```
remote-job-listing/
│
├── app/
│   ├── __init__.py           # Initialize the Flask app and register Blueprints
│   ├── jobs/                 # Blueprint for job-related functionality
│   │   ├── __init__.py       # Initialize the Jobs Blueprint
│   │   ├── routes.py         # Routes for jobs (listing, posting)
│   │   └── models.py         # Job model
│   ├── users/                # Blueprint for user-related functionality
│   │   ├── __init__.py       # Initialize the Users Blueprint
│   │   ├── routes.py         # Routes for users (login, registration)
│   │   └── models.py         # User model (for companies)
│   ├── static/               # Static files (CSS, JS, images)
│   └── templates/            # HTML files (Jinja templates)
├── config.py                 # Configuration settings (e.g., SQLite URI)
├── run.py                    # Entry point for running the Flask application
├── requirements.txt          # Python dependencies (Flask, etc.)
└── README.md                 # This README file
```

## Technologies Used
- **Backend**: Flask (Python)
- **Database**: SQLite
- **Frontend**: HTML5, CSS3 (Base structure provided, further styling required)
- **Cloud Deployment**: AWS or Heroku (to be implemented)

## Contributing

Contributions are welcome! Here’s how you can help:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. Make your changes and commit them with descriptive messages:
    ```bash
    git commit -m "[feature] Added new feature"
    ```
4. Push to your branch:
    ```bash
    git push origin feature/your-feature-name
    ```
5. Create a pull request on GitHub.

## License
This project is licensed under the MIT License. You can find more information in the `LICENSE` file.
