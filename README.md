Vivek's URL Shortener
A sleek and simple URL Shortener Web App built using Python Flask. Just paste your long URL, click shorten, and get a compact version with a copy-to-clipboard feature.

🚀 Features
🔧 Built with Flask and PyShorteners

🧠 Uses TinyURL API to generate short URLs

🎨 Responsive UI with HTML + CSS

📋 Copy to Clipboard functionality

📱 Mobile-friendly layout

⚡ Deployed on Render

📁 Project Structure
csharp
Copy
Edit
project-folder/
├── app.py                  # Main Flask backend
├── requirements.txt        # Python dependencies
├── Procfile                # For Render deployment
├── templates/
│   └── home.html           # Main UI template
└── static/
    └── style.css           # Styling file
🛠️ Installation
Clone the repository

bash
Copy
Edit
git clone https://github.com/Itzvivek18/url-shortener.git
cd url-shortener
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run locally

bash
Copy
Edit
python app.py
Visit http://localhost:5000 in your browser.

🌐 Deployed Version
Check out the live version here:
[https://your-render-url.onrender.com](https://url-c1ri.onrender.com)

📦 Deployment (Render)
Push the project to GitHub.

Go to Render and create a new Web Service.

Connect your repo and configure:

Build Command: pip install -r requirements.txt

Start Command: python app.py

Port: Use os.environ.get('PORT') in your code

👨‍💻 Developer
Vivek Kumar
📧 vivekumar454@gmail.com
📱 +91-8847302071

📌 Project Description
This project helps users shorten long URLs easily and share them quickly. It showcases a minimal, responsive design with clean UI, suitable for portfolio projects or learning Flask basics.
