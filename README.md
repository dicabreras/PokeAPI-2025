This project, a simple Pokedex viewer built with the Django web framework, serves as a practical exercise in backend development, data manipulation, and responsive frontend design.

## 🚀 Technologies Used

| Category | Technology & Component | Purpose |
| :--- | :--- | :--- |
| **Backend** | Python 3 & **Django** | Handles routing, views, and server-side logic. |
| **Data Source** | External **PokeAPI** | Data source, consumed via synchronous HTTP requests. |
| **Frontend** | HTML5, **Bootstrap 5** & **Vanilla JavaScript** | Structure, responsive design/styling, and client-side interactivity. |
| **Environment** | **Virtual Environments (venv)** | Ensures project dependency isolation. |


## 🧠 Key Learning Outcomes & Features

| Concept / Feature | Description |
| :--- | :--- |
| **API Integration** | Consuming, parsing, and standardizing data from a third-party REST API (`pokeapi.co`). |
| **Data Transformation** | Implementing server-side data manipulation logic, including filtering and performing custom string operations (e.g., **reversing Pokémon names**). |
| **Django Views & Context** | Managing Django's flow control, processing data within `views.py`, and passing structured data (`context`) to templates. |
| **Advanced Filtering** | Implementing complex filters in the service layer to handle multiple conditions simultaneously (e.g., "Type X AND Height > Y"). |
| **Client-Side Interactivity** | Using **Vanilla JavaScript** to enhance the UX (e.g., persistent **Dark Mode** toggle and optionally showing/hiding the 'Reversed Name' column via DOM manipulation). |
| **Responsive Design** | Styling complex, scrollable data tables using **Bootstrap 5** to ensure usability across different screen sizes. |
--------------------------------------
## 🛠️ Setup & Installation

To ensure smooth execution across all operating systems, the instructions below include a necessary step for Windows PowerShell security.

| Step | Command | Purpose |
| :--- | :--- | :--- |
| **1. Clone Repository** | `git clone https://github.com/dicabreras/PokeAPI-2025.git`<br>`cd PokeAPI-2025` | Downloads the project and navigates to the directory. |
| **2. Create VENV** | `python -m venv venv` | Creates an isolated environment, ensuring correct Windows structure (`Scripts`). |
| **3. Security Policy (Windows ONLY)** | **Run in the VENV terminal** and execute: <br>`Set-ExecutionPolicy RemoteSigned -Scope Process` | Temporarily overrides Windows security settings, allowing the VENV activation script to run. |
| **4. Activate VENV** | **Windows (PowerShell):** <br>`.\venv\Scripts\activate`<br>**Linux/macOS:** <br>`source venv/bin/activate` | Activates the virtual environment. |
| **5. Install Dependencies** | `pip install -r requirements.txt` | Installs Django, Requests, and all necessary libraries from the manifest. |
| **6. Apply Migrations** | `python manage.py migrate` | Sets up the database tables required by Django's core modules (admin, auth, sessions). |
| **7. Start Server** | `python manage.py runserver` | Starts the Django development server, accessible at `http://127.0.0.1:8000`. |
