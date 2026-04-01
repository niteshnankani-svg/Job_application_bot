import streamlit as st
import os
from app import extract_text_from_pdf, run_job_application_bot

# Page config
st.set_page_config(
    page_title="Job Application Bot",
    page_icon="🤖",
    layout="wide"
)

# Title
st.title("🤖 Job Application Bot")
st.subheader("Upload JD and Resume → Get Cover Letter + Match Analysis")
st.divider()

# API Key
api_key = st.text_input("🔑 Enter OpenAI API Key", type="password")

# Two columns for uploads
col1, col2 = st.columns(2)

with col1:
    st.subheader("📄 Job Description")
    jd_file = st.file_uploader("Upload JD (PDF)", type="pdf")

with col2:
    st.subheader("📋 Your Resume")
    resume_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

st.divider()

# Analyze button
if st.button("🚀 Analyze & Generate Cover Letter", use_container_width=True):
    
    if not api_key:
        st.error("Please enter your OpenAI API key")
    elif not jd_file or not resume_file:
        st.error("Please upload both Job Description and Resume")
    else:
        os.environ["OPENAI_API_KEY"] = api_key
        
        with st.spinner("🔍 Reading documents..."):
            jd_text = extract_text_from_pdf(jd_file)
            resume_text = extract_text_from_pdf(resume_file)
        
        with st.spinner("🤖 AI Agents working... this may take a minute..."):
            results = run_job_application_bot(jd_text, resume_text)
        
        st.success("✅ Analysis Complete!")
        st.divider()
        
        # Show results in tabs
        tab1, tab2, tab3, tab4 = st.tabs([
            "📋 JD Analysis",
            "👤 Resume Analysis", 
            "🎯 Match Analysis",
            "✉️ Cover Letter"
        ])
        
        with tab1:
            st.subheader("Job Requirements")
            st.write(results['jd_analysis'])
        
        with tab2:
            st.subheader("Your Skills & Experience")
            st.write(results['resume_analysis'])
        
        with tab3:
            st.subheader("How Well You Match")
            st.write(results['match_analysis'])
        
        with tab4:
            st.subheader("Your Cover Letter")
            st.write(results['cover_letter'])
            st.download_button(
                label="📥 Download Cover Letter",
                data=results['cover_letter'],
                file_name="cover_letter.txt",
                mime="text/plain"
            )
