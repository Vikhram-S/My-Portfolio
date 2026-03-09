import streamlit as st

st.set_page_config(
    page_title="Vikhram S | AI Researcher",
    page_icon="🧠",
    layout="wide"
)

# ---------- STYLE ----------
st.markdown("""
<style>

body {
background: linear-gradient(135deg,#020617,#0f172a);
color:white;
}

.title{
font-size:48px;
font-weight:700;
}

.subtitle{
font-size:22px;
color:#94a3b8;
margin-bottom:10px;
}

.profileline{
font-size:18px;
color:#cbd5f5;
margin-bottom:15px;
}

.metric{
background: linear-gradient(135deg,#6366f1,#9333ea);
padding:25px;
border-radius:14px;
text-align:center;
font-size:20px;
color:white;
}

.card{
background:#111827;
padding:20px;
border-radius:14px;
border:1px solid #1f2937;
margin-bottom:15px;
}

.section{
font-size:30px;
margin-top:20px;
margin-bottom:10px;
font-weight:600;
}

.icons img{
margin-right:18px;
transition:0.3s;
}

.icons img:hover{
transform:scale(1.15);
}

</style>
""", unsafe_allow_html=True)

# ---------- HERO ----------
st.markdown('<div class="title">Vikhram S</div>', unsafe_allow_html=True)

st.markdown(
'<div class="subtitle">AI Researcher | Multimodal AI | Vision-Language Models</div>',
unsafe_allow_html=True
)

st.markdown(
'<div class="profileline">Advisor – Machine Learning, Tech Society | Saveetha Engineering College</div>',
unsafe_allow_html=True
)

st.write(
"Final-year Electronics and Communication Engineering student working on "
"multimodal AI, explainable machine learning, and healthcare AI systems."
)

# ---------- SOCIAL ICONS ----------
st.markdown("""
<div class="icons">

<a href="https://www.linkedin.com/in/vikhram-s/" target="_blank">
<img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="36">
</a>

<a href="https://github.com/Vikhram-S" target="_blank">
<img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="36">
</a>

<a href="https://huggingface.co/Vikhram-S" target="_blank">
<img src="https://huggingface.co/front/assets/huggingface_logo.svg" width="36">
</a>

<a href="mailto:vikhrams@saveetha.ac.in">
<img src="https://cdn-icons-png.flaticon.com/512/732/732200.png" width="36">
</a>

</div>
""", unsafe_allow_html=True)

st.divider()

# ---------- METRICS ----------
c1,c2,c3,c4 = st.columns(4)

with c2:
    st.markdown('<div class="metric">21K+<br>Python Library Downloads</div>', unsafe_allow_html=True)

with c3:
    st.markdown('<div class="metric">Springer<br>LNNS Publication</div>', unsafe_allow_html=True)
    
with c1:
    st.markdown(
        '<div class="metric">India AI Impact Summit 2026<br>Compendium Author<br><small>AI & Gender Empowerment</small></div>',
        unsafe_allow_html=True
    )

with c4:
    st.markdown('<div class="metric">Multimodal<br>AI Research</div>', unsafe_allow_html=True)

st.divider()

# ---------- TABS ----------
tab1,tab2,tab3,tab4 = st.tabs([
"Research Projects",
"Publications",
"Recognition",
"Contact"
])

# ---------- PROJECTS ----------
with tab1:

    st.markdown('<div class="section">Research Projects</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>ExplainableVLM-Rad</h3>
    Vision–Language framework for automated radiology report generation using interpretable multimodal AI.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>mimic-vit-biogpt</h3>
    Multimodal medical model combining ViT vision encoder and BioGPT language model.
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "View HuggingFace Model",
        "https://huggingface.co/Vikhram-S/mimic-vit-biogpt"
    )

    st.markdown("""
    <div class="card">
    <h3>IndianConstitution</h3>
    NLP-based Python library for programmatic analysis of the Constitution of India with 21K+ downloads.
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "View Python Library (PyPI)",
        "https://pypi.org/project/IndianConstitution/"
    )

# ---------- PUBLICATIONS ----------
with tab2:

    st.markdown('<div class="section">Publications</div>', unsafe_allow_html=True)

    st.write(
    "**Explainable SLM-Guided Vision-Language Models for Multi-Class Skin Lesion Recognition**"
    )

    st.write(
    "Accepted at International Conference on Innovative Computing and Communications 2026 "
    "and appearing in Springer Lecture Notes in Networks and Systems."
    )

# ---------- RECOGNITION ----------
with tab3:

    st.markdown('<div class="section">AI Impact Summit Recognition</div>', unsafe_allow_html=True)

    st.write(
    "Lead author of the NariRaksha case study featured in the AI and Gender Empowerment "
    "Casebook released during the India AI Impact Summit 2026 by MeitY and UN Women."
    )

    st.link_button(
        "View Casebook Publication",
        "https://d19ob9sqegt2wc.cloudfront.net/stage/uploads/AI_Empowerment_Case_Study_Web_a09fbf83c9.pdf"
    )

    st.image(
        "ai_summit.jpg",
        caption="AI Impact Summit 2026 – Casebook Launch",
        use_container_width=True
    )

# ---------- CONTACT ----------
with tab4:

    st.markdown('<div class="section">Contact</div>', unsafe_allow_html=True)

    st.markdown("""
📧 **Email:** vikhrams@saveetha.ac.in  

💻 **GitHub:** https://github.com/Vikhram-S  

🤗 **HuggingFace:** https://huggingface.co/Vikhram-S  

🔗 **LinkedIn:** https://www.linkedin.com/in/vikhram-s/
""")
