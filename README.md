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
