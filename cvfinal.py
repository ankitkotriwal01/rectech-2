

# App ready to deploy 


import streamlit as st
import io
from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Pt, RGBColor
import pandas as pd
import os
import openai
import time

# Create a new Word document
doc = Document()

# Default font settings
default_font_name = 'Calibri'
default_font_size = Pt(12)
default_paragraph_alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
default_font_color = RGBColor(0, 0, 0)

# Apply styles to the Normal style
normal_style = doc.styles['Normal']
normal_style.font.name = default_font_name
normal_style.font.size = default_font_size
normal_style.paragraph_format.alignment = default_paragraph_alignment
normal_style.font.color.rgb = default_font_color

# Streamlit app title and introduction
st.title("Resume Generator")

# Initialize session state variables
if 'prof_exp_rows' not in st.session_state:
    st.session_state.prof_exp_rows = 0
if 'edu_rows' not in st.session_state:
    st.session_state.edu_rows = 0
if 'skills_rows' not in st.session_state:
    st.session_state.skills_rows = 0
if 'cert_rows' not in st.session_state:
    st.session_state.cert_rows = 0
if 'projects_rows' not in st.session_state:
    st.session_state.projects_rows = 0
if 'prof_mem_rows' not in st.session_state:
    st.session_state.prof_mem_rows = 0
if 'languages_rows' not in st.session_state:
    st.session_state.languages_rows = 0
if 'volunteer_rows' not in st.session_state:
    st.session_state.volunteer_rows = 0

# Function to create a table in Streamlit
def create_table_with_predefined_size(rows, cols, key_prefix):
    data = []
    for row in range(rows):
        row_data = [st.text_input(f"Enter value for row {row + 1}, column {col + 1}:", key=f"{key_prefix}-{row}-{col}") for col in range(cols)]
        data.append(row_data)

    df = pd.DataFrame(data, columns=[f"Column {col + 1}" for col in range(cols)])
    st.table(df)

# Function to get user input for string values
def get_user_input(prompt):
    return st.text_input(prompt).strip()

# Section header (Title)
st.write("We need some basic information to generate your resume.")

# Get user input for personal details
full_name = get_user_input("Enter your full name:")
phone_number = get_user_input("Enter your phone number:")
email_address = get_user_input("Enter your email address:")
linkedin_profile = get_user_input("Enter your LinkedIn profile (if applicable):")
portfolio_website = get_user_input("Enter your professional website or portfolio (if applicable):")

# Page numbers in the footer
for section in doc.sections:
    footer = section.footer
    p = footer.paragraphs[0]
    p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    run = p.add_run("Page ")
    run.bold = False

# Resume section
st.header("Resume")
st.write("Please enter your professional details.")


doc.add_paragraph(f"Full Name: {full_name}")
doc.add_paragraph(f"Phone Number: {phone_number}")
doc.add_paragraph(f"Email Address: {email_address}")
doc.add_paragraph(f"LinkedIn Profile: {linkedin_profile}")
doc.add_paragraph(f"Professional Website/Portfolio: {portfolio_website}")

# Resume Summary or Objective
st.subheader("Resume Summary or Objective")
resume_summary = st.text_area("Enter your resume summary or objective:")
doc.add_heading("Resume Summary or Objective", level=2)
doc.add_paragraph(resume_summary)

# Professional Experience
st.subheader("Professional Experience")
num_prof_exp_rows1 = st.number_input("Enter the number of rows for Professional Experience:", min_value=0, value=3, key="unique_key_for_prof_exp_rows1")
create_table_with_predefined_size(num_prof_exp_rows1, 4, 1)  # Specify the number of columns as needed


# Education
st.subheader("Education")
num_prof_exp_rows2 = st.number_input("Enter the number of rows for Education:", min_value=0, value=3, key="unique_key_for_prof_exp_rows2")
create_table_with_predefined_size(num_prof_exp_rows2, 4, 2)  # Specify the number of columns as needed


# Skills
st.subheader("Skills")
num_prof_exp_rows3 = st.number_input("Enter the number of rows for Skills:", min_value=0, value=3, key="unique_key_for_prof_exp_rows3")
create_table_with_predefined_size(num_prof_exp_rows3, 4, 3)  # Specify the number of columns as needed


# Certifications and Training
st.subheader("Certifications and Training")
num_prof_exp_rows4 = st.number_input("Enter the number of rows for Certifications and Training:", min_value=0, value=3, key="unique_key_for_prof_exp_rows4")
create_table_with_predefined_size(num_prof_exp_rows4, 4, 4)  # Specify the number of columns as needed


# Achievements and Awards
st.subheader("Achievements and Awards")
achievements = st.text_area("Enter your achievements and awards:")

# Projects
st.subheader("Projects")
num_prof_exp_rows5 = st.number_input("Enter the number of rows for Projects:", min_value=0, value=3, key="unique_key_for_prof_exp_rows5")
create_table_with_predefined_size(num_prof_exp_rows5, 4, 5)  # Specify the number of columns as needed

# Publications/Presentations
st.subheader("Publications/Presentations")
publications = st.text_area("Enter your publications or presentations:")

# Professional Memberships
st.subheader("Professional Memberships")
num_prof_exp_rows6 = st.number_input("Enter the number of rows for Professional Memberships:", min_value=0, value=3, key="unique_key_for_prof_exp_rows6")
create_table_with_predefined_size(num_prof_exp_rows6, 4, 6)  # Specify the number of columns as needed

# Languages
st.subheader("Languages")
num_prof_exp_rows7 = st.number_input("Enter the number of rows for Languages:", min_value=0, value=3, key="unique_key_for_prof_exp_rows7")
create_table_with_predefined_size(num_prof_exp_rows7, 4, 7)  # Specify the number of columns as needed

# Volunteer Work
st.subheader("Volunteer Work")
num_prof_exp_rows8 = st.number_input("Enter the number of rows for Volunteer Work:", min_value=0, value=3, key="unique_key_for_prof_exp_rows8")
create_table_with_predefined_size(num_prof_exp_rows8, 4, 8)  # Specify the number of columns as needed

# Hobbies and Interests
st.subheader("Hobbies and Interests")
hobbies_interests = st.text_area("Enter your hobbies and interests:")

# References
st.subheader("References")
references = st.text_area("Enter your references information:")

doc.add_heading("Summary or Objective", level=2)
doc.add_paragraph(resume_summary)

# Define a function to add a table to the document
def add_table_to_doc(heading, rows, cols, session_state_key):
    doc.add_heading(heading, level=2)
    table = doc.add_table(rows=rows + 1, cols=cols)
    table.autofit = False

    # Add header row
    header_cells = table.rows[0].cells
    for col in range(cols):
        header_cells[col].text = f"Column {col + 1}"

    # Add data rows
    for row in range(rows):
        row_cells = table.rows[row + 1].cells
        for col in range(cols):
            value = st.session_state[f"{session_state_key}-{row}-{col}"]
            row_cells[col].text = value

# Professional Experience
add_table_to_doc("Professional Experience", num_prof_exp_rows1, 4, 1)

# Education
add_table_to_doc("Education", num_prof_exp_rows2, 4, 2)

# Skills
add_table_to_doc("Skills", num_prof_exp_rows3, 4, 3)

# Certifications and Training
add_table_to_doc("Certifications and Training", num_prof_exp_rows4, 4, 4)

# Achievements and Awards
doc.add_heading("Achievements and Awards", level=2)
doc.add_paragraph(achievements)

# Projects
add_table_to_doc("Projects", num_prof_exp_rows5, 4, 5)

# Publications/Presentations
doc.add_heading("Publications/Presentations", level=2)
doc.add_paragraph(publications)

# Professional Memberships
add_table_to_doc("Professional Memberships", num_prof_exp_rows6, 4, 6)

# Languages
add_table_to_doc("Languages", num_prof_exp_rows7, 4, 7)

# Volunteer Work
add_table_to_doc("Volunteer Work", num_prof_exp_rows8, 4, 8)

# Hobbies and Interests
doc.add_heading("Hobbies and Interests", level=2)
doc.add_paragraph(hobbies_interests)

# References
doc.add_heading("References", level=2)
doc.add_paragraph(references)


file_name = st.text_input("Enter the file name for saving the resume")

if file_name:
    file_path = f"{file_name}.docx"

    # Download button
    def main():
        output = io.BytesIO()
        doc.save(output)
        output.seek(0)
        st.download_button("Download DOCX", data=output.getvalue(), file_name=file_name)

    main()

