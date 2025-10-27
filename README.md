This project, a simple Pokedex viewer built with the Django web framework, serves as a practical exercise in backend development, data manipulation, and responsive frontend design.

🚀 Technologies Used
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Backend: Python 3 & Django

Data Source: External PokeAPI (consumed via synchronous HTTP requests)

Frontend: HTML5, Bootstrap 5 (for responsive design and styling) & Vanilla JavaScript (for interactivity)

Environment: Virtual Environments (venv)

🧠 Key Learning Outcomes & Features
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
This project allowed me to gain hands-on experience with several core concepts: <br>

API Integration	Consuming   &nbsp;--> parsing, and standardizing data from a third-party REST API (pokeapi.co). <br>

Data Transformation	       &nbsp; --> Implementing server-side data manipulation logic, including filtering Pokémon based on criteria (Weight, Type, Height) and performing custom string operations (e.g., reversing Pokémon names).<br>

Django Views & Context     &nbsp; -->	Managing Django's flow control, processing data within views.py, and passing structured data (context) to templates.<br>

Advanced Filtering	       &nbsp; --> Implementing complex filters in the service layer to handle multiple conditions simultaneously (e.g., "Type X AND Height > Y").<br>

Client-Side Interactivity	 &nbsp; --> Using Vanilla JavaScript to enhance the UX, specifically by adding a persistent Dark Mode toggle and a feature to optionally show/hide a table column via DOM manipulation.<br>

Responsive Design	        &nbsp;  --> Styling complex, scrollable data tables using Bootstrap 5 to ensure usability across different screen sizes.
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
