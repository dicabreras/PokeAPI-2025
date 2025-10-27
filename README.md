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

Follow these five steps to get the Pokedex running locally:

| Step | Command | Purpose |
| :--- | :--- | :--- |
| **1. Clone Repository** | `git clone https://github.com/dicabreras/PokeAPI-2025.git` | Downloads the project files to your local machine. |
| **2. Navigate & Create VENV** | `cd PokeAPI-2025`<br>`python -m venv venv` | Enters the project directory and creates an isolated environment. |
| **3. Activate VENV** | `.\venv\Scripts\activate` (Windows)<br>or `source venv/bin/activate` (Linux/macOS) | Activates the virtual environment to manage dependencies. |
| **4. Install Dependencies** | `pip install -r requirements.txt` | Installs all necessary Python libraries (e.g., Django, requests). |
| **5. Start Server** | `python manage.py runserver` | Starts the Django development server, typically accessible at `http://127.0.0.1:8000`. |
