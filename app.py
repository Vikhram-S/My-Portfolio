import streamlit as st

st.set_page_config(page_title="Vikhram S | AI Researcher", layout="wide")

st.title("Vikhram S")
st.subheader("AI Researcher | Multimodal AI | Vision-Language Models")

st.write("""
Final-year Electronics and Communication Engineering student at Saveetha Engineering College.
My research focuses on multimodal AI, explainable machine learning, and healthcare AI systems.
""")

st.divider()

st.header("Key Achievements")

st.markdown("""
- Paper accepted at **International Conference on Innovative Computing and Communications 2026**
- Publication in **Springer Lecture Notes in Networks and Systems**
- Lead Author – **NariRaksha Case Study** in *AI and Gender Empowerment Casebook*
- Featured at **India AI Impact Summit 2026** by MeitY and UN Women
""")

st.divider()

st.header("Research Projects")

st.subheader("ExplainableVLM-Rad")
st.write("Vision-Language Model for automated radiology report generation.")

st.subheader("mimic-vit-biogpt")
st.write("Multimodal medical AI model combining ViT and BioGPT.")

st.link_button(
    "View Model",
    "https://huggingface.co/Vikhram-S/mimic-vit-biogpt"
)

st.subheader("IndianConstitution")
st.write("""
NLP-based Python library for analysing the Constitution of India.
**21,000+ downloads**
""")

st.divider()

st.header("Open Source")

st.markdown("""
- GitHub
- Hugging Face
- Python Libraries
""")

st.divider()

st.header("Recognition")

st.write("""
Lead author of the **NariRaksha** case study featured in the *AI and Gender Empowerment Casebook* released at the India AI Impact Summit 2026 by MeitY and UN Women.
""")

st.divider()

st.header("Contact")

st.markdown("""
- GitHub: https://github.com/Vikhram-S
- HuggingFace: https://huggingface.co/Vikhram-S
- LinkedIn: https://www.linkedin.com/in/vikhram-s/
""")
