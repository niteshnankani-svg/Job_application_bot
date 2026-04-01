import streamlit as st
from crewai import Agent, Task, Crew
from pypdf import PdfReader
import os

# Page setup
st.title("🤖 Job Application Bot")
st.subheader("Upload JD and Resume → Get Cover Letter")

# API Key input
api_key = st.text_input("Enter OpenAI API Key", type="password")

# File uploads
jd_file = st.file_uploader("Upload Job Description (PDF)", type="pdf")
resume_file = st.file_uploader("Upload Your Resume (PDF)", type="pdf")

# Analyze button
if st.button("Analyze & Generate Cover Letter"):
    
    if not api_key:
        st.error("Please enter your OpenAI API key")
    elif not jd_file or not resume_file:
        st.error("Please upload both files")
    else:
        os.environ["OPENAI_API_KEY"] = api_key
        
        # Extract text from JD
        with st.spinner("Reading Job Description..."):
            jd_reader = PdfReader(jd_file)
            jd_text = ""
            for page in jd_reader.pages:
                jd_text += page.extract_text()
        
        # Extract text from Resume
        with st.spinner("Reading Resume..."):
            resume_reader = PdfReader(resume_file)
            resume_text = ""
            for page in resume_reader.pages:
                resume_text += page.extract_text()
        
        # Create Agents
        with st.spinner("AI Agents Working..."):
            
            job_analyzer = Agent(
                role='Job Requirements Analyst',
                goal='Analyze job descriptions and extract key requirements',
                backstory='You are an expert recruiter who deeply understands what companies look for in AI and ML candidates.',
                verbose=False
            )
            
            writer = Agent(
                role='Cover Letter Writer',
                goal='Write a personalized and compelling cover letter',
                backstory='You are an expert career coach who writes amazing cover letters that get candidates hired.',
                verbose=False
            )
            
            # Create Tasks
            analyze_task = Task(
                description=f'Analyze this job description and extract top 5 requirements: {jd_text}',
                agent=job_analyzer,
                expected_output='A list of top 5 key requirements for this job.'
            )
            
            write_task = Task(
                description=f'Write a cover letter based on this resume: {resume_text} for this job: {jd_text}',
                agent=writer,
                expected_output='A professional cover letter ready to send.'
            )
            
            # Run Crew
            crew = Crew(
                agents=[job_analyzer, writer],
                tasks=[analyze_task, write_task],
                verbose=False
            )
            
            result = crew.kickoff()
        
        # Show Results
        st.success("Done! 🎉")
        st.subheader("Your Cover Letter")
        st.write(str(result))