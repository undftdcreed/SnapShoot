# SnapShoot

SnapShoot is a web application that allows users to find unique accommodations for film productions in the Las Vegas Valley. Users can browse listings, book locations, and manage their bookings. This project is built using Django, a Python web framework.

## Live Site on Render 
https://snapshoot-fobr.onrender.com/

sometimes the server will shut itself off so let me know if i need to restart the server
## Features

- Browse listings: Users can view a list of available locations for film productions.
- Listing details: Users can see detailed information about a specific listing, including images, description, and pricing.
- Booking: Users can book a location for a specific date and time.
- User authentication: Users can sign up, log in, and log out of their accounts.
- Listing management: Authorized users can create, update, and delete listings.

## Technologies Used
Django
Python
Bootstrap
Trello
Render
HTML
CSS


## Screenshots
<img width="1425" alt="Screenshot 2023-07-19 at 1 39 26 PM" src="https://github.com/undftdcreed/SnapShoot/assets/122516652/fbea73f7-3748-4a9b-af09-25448b8709f6">
<img width="1423" alt="Screenshot 2023-07-19 at 1 39 38 PM" src="https://github.com/undftdcreed/SnapShoot/assets/122516652/2888434f-7da6-4e9d-a4f8-cb1542f64ead">

<img width="1421" alt="Screenshot 2023-07-19 at 1 39 57 PM" src="https://github.com/undftdcreed/SnapShoot/assets/122516652/235ac410-7b5f-4480-84ac-143336fc32a3">
<img width="1429" alt="Screenshot 2023-07-19 at 1 40 08 PM" src="https://github.com/undftdcreed/SnapShoot/assets/122516652/f21b4b94-bbfb-493f-a734-1602cc2c43ba">
<img width="1423" alt="Screenshot 2023-07-19 at 1 40 21 PM" src="https://github.com/undftdcreed/SnapShoot/assets/122516652/1d4361b3-20d6-49e4-b706-e747fc371514">



## Installation

1. Clone the repository: `git clone https://github.com/your-username/snapshoot.git`
2. Navigate to the project directory: `cd snapshoot`
3. Create a virtual environment: `python -m venv env`
4. Activate the virtual environment:
   - Windows: `env\Scripts\activate`
   - macOS/Linux: `source env/bin/activate`
5. Install the dependencies: `pip install -r requirements.txt`
6. Apply the database migrations: `python manage.py migrate`
7. Start the development server: `python manage.py runserver`

The application should now be running on `http://localhost:8000/`.

## Configuration

- Database: By default, the project is configured to use SQLite as the database. You can modify the database settings in the `settings.py` file if you prefer to use a different database engine.
- Static files: The project uses Django's static files handling. During development, make sure to run `python manage.py collectstatic` to collect and serve the static files properly.

## Contributing

Contributions to SnapShoot are welcome! If you find any issues or have suggestions for improvements, please submit an issue or pull request on the GitHub repository.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
