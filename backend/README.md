# Mental Health Journal API

This project is a mental health journal application that provides a platform for users to create, manage, and reflect on their journal entries. The application is built using Django for the backend and React for the frontend.

## Backend

The backend is developed using Django and provides a RESTful API for managing journal entries. Below are the key components of the backend:

- **manage.py**: A command-line utility for interacting with the Django project.
- **journal_api**: The main Django application containing settings, URL routing, and WSGI configuration.
- **journal**: A Django app that handles the journal entries, including models, views, serializers, and URL routing.

### Setup Instructions

1. **Install Dependencies**: Make sure you have Python and Django installed. You can install the required packages using pip:
   ```
   pip install -r requirements.txt
   ```

2. **Database Migrations**: Run the following command to apply database migrations:
   ```
   python manage.py migrate
   ```

3. **Run the Development Server**: Start the Django development server with:
   ```
   python manage.py runserver
   ```

4. **Access the API**: The API will be available at `http://localhost:8000/api/`.

## Frontend

The frontend is developed using React and provides a user-friendly interface for interacting with the journal API. Key components include:

- **App.js**: The main component that sets up routing and renders the application layout.
- **JournalEntry.js**: A component for displaying and managing individual journal entries.
- **Home.js**: The home page component that displays a list of journal entries or a form to create a new entry.

### Setup Instructions

1. **Install Dependencies**: Navigate to the frontend directory and install the required packages using npm:
   ```
   npm install
   ```

2. **Run the Development Server**: Start the React development server with:
   ```
   npm start
   ```

3. **Access the Application**: The application will be available at `http://localhost:3000/`.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.