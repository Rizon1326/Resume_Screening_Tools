import streamlit as st
import pickle
import re
import nltk
from PIL import Image     
import base64

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

# Loading models
clf = pickle.load(open('clf.pkl', 'rb'))
tfidfd = pickle.load(open('tfidf.pkl', 'rb'))


def clean_resume(resume_text):
    clean_text = re.sub('http\S+\s*', ' ', resume_text)  
    clean_text = re.sub('RT|cc', ' ', clean_text)
    clean_text = re.sub('#\S+', '', clean_text)
    clean_text = re.sub('@\S+', '  ', clean_text)
    clean_text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', clean_text)
    clean_text = re.sub(r'[^\x00-\x7f]', r' ', clean_text)
    clean_text = re.sub('\s+', ' ', clean_text) 
    return clean_text


def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)


def main():
    # Set page config
    st.set_page_config(page_title="Resume Screening App", page_icon="📄", layout="wide")

    # Set background image (replace 'background.png' with your image file)
    # set_background('background.png')

    # Custom CSS
    st.markdown("""
    <style>
    .big-font {
        font-size:50px !important;
        color: #1E88E5;
        font-weight: bold;
    }
    .result {
        font-size: 30px;
        font-weight: bold;
        color: #4CAF50;
    }
    .upload-box {
        border: 2px dashed #1E88E5;
        border-radius: 10px;
        padding: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    # App title
    st.markdown('<p class="big-font">Resume Screening App</p>', unsafe_allow_html=True)

    # Add a brief description
    st.write("Upload your resume and let AI predict your job category!")

    # File uploader
    with st.container():
        st.markdown('<div class="upload-box">', unsafe_allow_html=True)
        uploaded_file = st.file_uploader('Choose your resume file', type=['txt', 'pdf'])
        st.markdown('</div>', unsafe_allow_html=True)

    if uploaded_file is not None:
        try:
            resume_bytes = uploaded_file.read()
            resume_text = resume_bytes.decode('utf-8')
        except UnicodeDecodeError:
            resume_text = resume_bytes.decode('latin-1')

        with st.spinner("Analyzing your resume..."):
            cleaned_resume = clean_resume(resume_text)
            input_features = tfidfd.transform([cleaned_resume])
            prediction_id = clf.predict(input_features)[0]

        # Map category ID to category name
        category_mapping = {
            15: "Java Developer", 23: "Testing", 8: "DevOps Engineer",
            20: "Python Developer", 24: "Web Designing", 12: "HR",
            13: "Hadoop", 3: "Blockchain", 10: "ETL Developer",
            18: "Operations Manager", 6: "Data Science", 22: "Sales",
            16: "Mechanical Engineer", 1: "Arts", 7: "Database",
            11: "Electrical Engineering", 14: "Health and fitness",
            19: "PMO", 4: "Business Analyst", 9: "DotNet Developer",
            2: "Automation Testing", 17: "Network Security Engineer",
            21: "SAP Developer", 5: "Civil Engineer", 0: "Advocate",
        }

        category_name = category_mapping.get(prediction_id, "Unknown")

        # Display result with animation
        st.success("Analysis Complete!")
        st.markdown(f'<p class="result">Predicted Category: {category_name}</p>', unsafe_allow_html=True)

        # Add a fun fact or tip related to the predicted category
        fun_facts = {
            "Java Developer": "Did you know? Java was originally designed for interactive television, but it was too advanced for the digital cable television industry of the time.",
            "Python Developer": "Fun fact: Python is named after the British comedy group Monty Python, not the snake!",
            "Data Science": "Tip: Continuously updating your skills in machine learning and big data technologies can give you an edge in the data science field.",
            # Add more fun facts or tips for other categories
        }

        if category_name in fun_facts:
            st.info(fun_facts[category_name])

    # Add a footer
    st.markdown("---")
    st.markdown("Built with ❤️ by Your Name")


if __name__ == "__main__":
    main()