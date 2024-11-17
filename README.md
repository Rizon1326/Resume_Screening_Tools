# Resume Screening App 📄

This is a **Resume Screening App** built with **Streamlit** that uses AI to predict the job category from an uploaded resume. It leverages **TF-IDF** vectorization and a **pre-trained classification model** to analyze resumes.

---

## Features ✨

- **AI-Powered Resume Analysis**: Upload your resume and get a predicted job category instantly.
- **Customizable UI**: Includes a modern, responsive design with custom CSS for a professional look.
- **Fun Facts and Tips**: Displays category-specific fun facts or tips.
- **Background Support**: Easily add a custom background image.

---

## How It Works 🔍

1. **Resume Upload**: Upload your resume file (`.txt` or `.pdf`).
2. **Processing**: 
   - Cleans the resume text (removes special characters, URLs, etc.).
   - Transforms the cleaned text using TF-IDF.
   - Predicts the job category using a pre-trained model.
3. **Results**: The app displays the predicted job category along with a fun fact or tip.

---

## Installation 🛠️

### Clone the Repository
```bash
git clone https://github.com/your-username/resume-screening-app.git
cd resume-screening-app
```
## Install Dependencies
bash
Copy code
## Run the App
streamlit run app.py
## File Structure 📁
```bash
.
├── app.py                # Main application script
├── clf.pkl               # Pre-trained classification model
├── tfidf.pkl             # TF-IDF vectorizer model
├── requirements.txt      # List of Python dependencies
├── README.md             # Project documentation
└── background.png        # Optional background image
```
## Pre-requisites 🧰
Python 3.7+
Required Libraries: Streamlit, nltk, scikit-learn, Pillow
To install the dependencies, use:

pip install -r requirements.txt
## Customization 🖌️
Background Image:

Replace background.png with your desired image and uncomment the set_background() function in the code.
Fun Facts:

Add or modify the fun_facts dictionary in app.py to include your own fun facts or tips.
## Built With ❤️ By Rizon

