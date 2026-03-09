import streamlit as st

st.set_page_config(
    page_title="Vikhram S | AI Researcher",
    page_icon="🧠",
    layout="wide"
)

# ---------- STYLE ----------
st.markdown("""
<style>

/* PAGE BACKGROUND */

body{
background: linear-gradient(135deg,#020617,#0f172a);
color:white;
}

/* MAIN CONTAINER */

.block-container{
padding-top:2rem;
padding-left:5%;
padding-right:5%;
}

/* GRADIENT TITLE */

.title{
font-size:clamp(36px,5vw,54px);
font-weight:700;
background: linear-gradient(90deg,#6366f1,#a855f7,#22d3ee);
-webkit-background-clip:text;
color:transparent;
}

/* SUBTITLE */

.subtitle{
font-size:clamp(18px,2.5vw,24px);
color:#cbd5f5;
margin-bottom:8px;
}

/* PROFILE LINE */

.profile{
font-size:16px;
color:#94a3b8;
margin-bottom:20px;
}

/* SOCIAL ICONS */

.icons{
display:flex;
gap:18px;
margin-top:10px;
margin-bottom:15px;
}

.icons img{
width:36px;
transition:0.3s;
}

.icons img:hover{
transform:scale(1.2);
}

/* GLASS CARDS */

.card{
background:rgba(255,255,255,0.05);
border:1px solid rgba(255,255,255,0.1);
backdrop-filter:blur(14px);
border-radius:16px;
padding:22px;
margin-bottom:18px;
transition:0.3s;
}

.card:hover{
transform:translateY(-6px);
box-shadow:0 10px 25px rgba(0,0,0,0.6);
}

/* METRIC CARDS */

.metric{
background:rgba(255,255,255,0.05);
border:1px solid rgba(255,255,255,0.1);
backdrop-filter:blur(14px);
border-radius:16px;
height:140px;
display:flex;
flex-direction:column;
justify-content:center;
align-items:center;
font-size:18px;
transition:0.3s;
}

.metric:hover{
box-shadow:0 10px 30px rgba(99,102,241,0.6);
transform:translateY(-4px);
}

/* BIG METRIC NUMBER */

.metric b{
font-size:28px;
}

/* SECTION HEADINGS */

.section{
font-size:28px;
font-weight:600;
margin-top:25px;
margin-bottom:10px;
background:linear-gradient(90deg,#22d3ee,#a855f7);
-webkit-background-clip:text;
color:transparent;
}

/* MOBILE */

@media (max-width:768px){

.icons{
justify-content:center;
}

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
'<div class="profile">Advisor – Machine Learning, Tech Society | Saveetha Engineering College</div>',
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
<img src="https://cdn-icons-png.flaticon.com/512/174/174857.png">
</a>

<a href="https://github.com/Vikhram-S" target="_blank">
<img src="https://cdn-icons-png.flaticon.com/512/25/25231.png">
</a>

<a href="https://huggingface.co/Vikhram-S" target="_blank">
<img src="https://huggingface.co/front/assets/huggingface_logo.svg">
</a>

<a href="mailto:vikhrams@saveetha.ac.in">
<img src="https://cdn-icons-png.flaticon.com/512/732/732200.png">
</a>

</div>
""", unsafe_allow_html=True)

st.divider()

# ---------- METRICS ----------

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="metric">
    <b>AI Summit 2026</b>
    Compendium Author
    <small>AI & Gender Empowerment</small>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="metric">
    <b>21K+</b>
    Python Library
    Downloads
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="metric">
    <b>Springer</b>
    LNNS
    Publication
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="metric">
    <b>Multimodal</b>
    AI Research
    </div>
    """, unsafe_allow_html=True)

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
    Vision-Language framework for automated radiology report generation
    using interpretable multimodal AI.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>mimic-vit-biogpt</h3>
    Multimodal medical model combining ViT vision encoder
    and BioGPT language model.
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "View HuggingFace Model",
        "https://huggingface.co/Vikhram-S/mimic-vit-biogpt"
    )

    st.markdown("""
    <div class="card">
    <h3>IndianConstitution</h3>
    NLP-based Python library for programmatic analysis of the Constitution
    of India with 21K+ downloads.
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "View Python Library",
        "https://pypi.org/project/IndianConstitution/"
    )

# ---------- PUBLICATIONS ----------

with tab2:

    st.markdown('<div class="section">Publications</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">

    **Explainable SLM-Guided Vision-Language Models for Multi-Class Skin Lesion Recognition**

    Accepted at *International Conference on Innovative Computing and Communications 2026*  
    Appearing in **Springer Lecture Notes in Networks and Systems (LNNS)**.

    </div>
    """, unsafe_allow_html=True)

# ---------- RECOGNITION ----------

with tab3:

    st.markdown('<div class="section">AI Impact Summit Recognition</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">

    Lead author of the **NariRaksha case study** featured in the  
    **AI & Gender Empowerment Casebook** released during the  
    **India AI Impact Summit 2026** by MeitY and UN Women.

    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "View Casebook",
        "https://d19ob9sqegt2wc.cloudfront.net/stage/uploads/AI_Empowerment_Case_Study_Web_a09fbf83c9.pdf"
    )

    st.image(
        "ai_summit.jpg",
        caption="AI Impact Summit 2026",
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
