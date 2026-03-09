import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Vikhram S | AI Researcher",
    page_icon="🧠",
    layout="wide"
)

# ---------- CURSOR REACTIVE AI NETWORK BACKGROUND ----------

components.html("""
<!DOCTYPE html>
<html>
<head>
<style>

canvas{
position:fixed;
top:0;
left:0;
z-index:-1;
}

body{
margin:0;
overflow:hidden;
background:#020617;
}

</style>
</head>

<body>

<canvas id="network"></canvas>

<script>

const canvas = document.getElementById("network");
const ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let mouse = {x:null,y:null};

window.addEventListener("mousemove", function(e){
mouse.x = e.x;
mouse.y = e.y;
});

let nodes = [];
let nodeCount = 80;

for(let i=0;i<nodeCount;i++){
nodes.push({
x:Math.random()*canvas.width,
y:Math.random()*canvas.height,
vx:(Math.random()-0.5)*0.6,
vy:(Math.random()-0.5)*0.6
});
}

function draw(){

ctx.clearRect(0,0,canvas.width,canvas.height);

for(let i=0;i<nodes.length;i++){

let n = nodes[i];

n.x += n.vx;
n.y += n.vy;

if(n.x<0||n.x>canvas.width) n.vx*=-1;
if(n.y<0||n.y>canvas.height) n.vy*=-1;

ctx.beginPath();
ctx.arc(n.x,n.y,2,0,Math.PI*2);
ctx.fillStyle="#6366f1";
ctx.fill();

for(let j=i+1;j<nodes.length;j++){

let m = nodes[j];

let dx = n.x-m.x;
let dy = n.y-m.y;
let dist = Math.sqrt(dx*dx+dy*dy);

if(dist<120){

ctx.beginPath();
ctx.moveTo(n.x,n.y);
ctx.lineTo(m.x,m.y);
ctx.strokeStyle="rgba(99,102,241,0.15)";
ctx.stroke();

}

}

if(mouse.x && mouse.y){

let dx = n.x-mouse.x;
let dy = n.y-mouse.y;
let dist = Math.sqrt(dx*dx+dy*dy);

if(dist<150){

ctx.beginPath();
ctx.moveTo(n.x,n.y);
ctx.lineTo(mouse.x,mouse.y);
ctx.strokeStyle="rgba(168,85,247,0.35)";
ctx.stroke();

}

}

}

requestAnimationFrame(draw);

}

draw();

</script>

</body>
</html>
""", height=0, width=0)

# ---------- CSS ----------

st.markdown("""
<style>

.block-container{
max-width:1100px;
margin:auto;
padding-top:2rem;
padding-left:1rem;
padding-right:1rem;
}

.title{
font-size:clamp(36px,5vw,52px);
font-weight:700;
background: linear-gradient(90deg,#6366f1,#a855f7,#22d3ee);
-webkit-background-clip:text;
color:transparent;
}

.subtitle{
font-size:clamp(18px,2.5vw,24px);
color:#cbd5f5;
}

.profile{
font-size:15px;
color:#94a3b8;
margin-bottom:20px;
}

.icons{
display:flex;
gap:18px;
margin-top:10px;
margin-bottom:20px;
flex-wrap:wrap;
}

.icons img{
width:34px;
transition:0.3s;
}

.icons img:hover{
transform:scale(1.2);
}

.metric-grid{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(200px,1fr));
gap:16px;
margin-top:20px;
margin-bottom:30px;
}

.metric{
background:rgba(255,255,255,0.05);
border:1px solid rgba(255,255,255,0.1);
border-radius:16px;
backdrop-filter:blur(14px);
height:140px;
display:flex;
flex-direction:column;
justify-content:center;
align-items:center;
text-align:center;
transition:0.3s;
}

.metric:hover{
transform:translateY(-4px);
box-shadow:0 10px 25px rgba(0,0,0,0.5);
}

.metric b{
font-size:28px;
}

.card{
background:rgba(255,255,255,0.05);
border:1px solid rgba(255,255,255,0.1);
border-radius:16px;
padding:22px;
margin-bottom:18px;
backdrop-filter:blur(14px);
}

.timeline{
border-left:2px solid #6366f1;
padding-left:18px;
}

.timeline-item{
margin-bottom:18px;
}

@media (max-width:600px){

.metric-grid{
grid-template-columns:1fr;
}

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

# ---------- METRICS ----------

st.markdown("""
<div class="metric-grid">

<div class="metric">
<b>AI Summit 2026</b>
Compendium Author
AI & Gender Empowerment
</div>

<div class="metric">
<b>21K+</b>
Python Library
Downloads
</div>

<div class="metric">
<b>Springer</b>
LNNS
Publication
</div>

<div class="metric">
<b>Multimodal</b>
AI Research
</div>

</div>
""", unsafe_allow_html=True)

# ---------- TABS ----------

tab1,tab2,tab3,tab4 = st.tabs([
"Research",
"Publications",
"Recognition",
"GitHub"
])

# ---------- PROJECTS ----------

with tab1:

    st.markdown("""
    <div class="card">
    <h3>ExplainableVLM-Rad</h3>
    Vision-Language framework for interpretable radiology report generation.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>mimic-vit-biogpt</h3>
    Multimodal medical model combining ViT and BioGPT.
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "View HuggingFace Model",
        "https://huggingface.co/Vikhram-S/mimic-vit-biogpt"
    )

    st.link_button(
        "View Python Library",
        "https://pypi.org/project/IndianConstitution/"
    )

# ---------- PUBLICATIONS TIMELINE ----------

with tab2:

    st.markdown("""
    <div class="timeline">

    <div class="timeline-item">
    <b>2026</b><br>
    Explainable SLM-Guided Vision-Language Models for Skin Lesion Recognition<br>
    Springer LNNS
    </div>

    </div>
    """, unsafe_allow_html=True)

# ---------- RECOGNITION ----------

with tab3:

    st.markdown("""
    <div class="card">

    Lead author of **NariRaksha case study** featured in  
    India AI Impact Summit 2026 casebook.

    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "View Casebook",
        "https://d19ob9sqegt2wc.cloudfront.net/stage/uploads/AI_Empowerment_Case_Study_Web_a09fbf83c9.pdf"
    )

    st.image(
        "ai_summit.jpg",
        caption="India AI Impact Summit 2026",
        use_container_width=True
    )

# ---------- GITHUB HEATMAP ----------

with tab4:

    st.markdown("### GitHub Activity")

    components.html("""
    <img src="https://ghchart.rshah.org/Vikhram-S" width="100%">
    """, height=200)
