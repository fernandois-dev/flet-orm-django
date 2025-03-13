# CRUD Flet-Django Data Management Application

This project is a web application built using [Flet](https://flet.dev/) for the frontend and likely [Django](https://www.djangoproject.com/) for the backend. It provides a dynamic and interactive interface for managing data, featuring functionalities like searching, filtering, pagination, editing, and deleting records.
Design based on Flet's sample gallery <3, 

## Features

*   **Dynamic Data Display:**  Displays data in a user-friendly table format.
*   **Search and Filtering:** Allows users to search and filter data based on various criteria.
*   **Pagination:** Implements pagination to handle large datasets efficiently.
*   **Sorting:** Enables sorting of data by clicking on column headers.
*   **CRUD Operations:** Supports Create, Read, Update, and Delete (CRUD) operations on data records.
*   **Customizable Actions:** Provides a menu for performing actions on selected records, such as deleting or deactivating.
*   **Responsive Design:** Adapts to different screen sizes, ensuring a consistent user experience.
*   **Confirmation Dialogs:** Uses confirmation dialogs for critical actions like deletion.
*   **Error Handling:** Includes error handling to gracefully manage unexpected situations.
* **Customizable Forms:** Allows to create custom forms for each model.
* **Customizable Buttons:** Allows to create custom buttons for each model.

## Technologies Used

*   **Flet:** A real-time Python framework for building interactive web, desktop, and mobile apps.
*   **Django:** A high-level Python web framework for rapid development. (Assumed based on the code structure)
*   **Python:** The primary programming language.
*   **Django ORM:** For database interactions.
* **Custom Components:** The project uses custom components like `CustomButtonCupertino`, `NotDataTable`, `DlgConfirm`, and `DlgAlert`.

## Project Structure

The project is organized as follows:

*   **`pages/generic_page.py`:** Contains the core logic for the generic data management page. This file handles:
    *   Data loading and display.
    *   Search and filtering.
    *   Pagination.
    *   Row selection and actions.
    *   Form display for editing/creating records.
    *   Deletion of records.
*   **`components/`:**  Directory for reusable UI components.
    *   `custom_buttons.py`: Contains custom button implementations.
    *   `not_data_table.py`: Contains the custom data table implementation.
    * `custom_dialogs.py`: Contains custom dialogs implementations.
*   **`data/`:** Directory for data related functions.
    * `search.py`: Contains the search function.
*   **`models.py`:** (Likely in a Django app) Defines the data models.
*   **`views.py`:** (Likely in a Django app) Handles the views and logic.
*   **`urls.py`:** (Likely in a Django app) Defines the URL patterns.
* **Other files:** Other files related to the project.

## Getting Started

### Prerequisites

*   Python 3.7+
*   Flet installed (`pip install flet`)
*   Django installed (`pip install django`)
*   A database (e.g., SQLite, PostgreSQL, MySQL) configured for Django.

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/fernandois-dev/flet-orm-django.git
    cd flet-orm-django
    ```
2. Create a virtual environment (recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt # if you have a requirements.txt file
    # or
    pip install flet django
    ```
4.  Set up the Django - database:
    ```bash
    python sincronization.py
    ```
5. Run the Flet app:
    ```bash
    flet run main.py # or the name of your main file

## Usage

1.  Open your web browser and go to the URL where the Flet app is running (usually `http://localhost:8550`).
2.  You should see the data management interface.
3.  Use the search bar to filter data.
4.  Click on column headers to sort data.
5.  Select rows to perform actions like deleting or editing.
6. Click on the "New" button to create a new record.


## Contact

Fernando de la Fuente - delafuentecarrasco@gmail.com  - https://github.com/fernandois-dev

## Acknowledgements

*   Flet
*   Django
*   Any other libraries or resources you used.
