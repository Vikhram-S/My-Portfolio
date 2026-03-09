import streamlit as st
import streamlit.components.v1 as components
import requests
import feedparser

st.set_page_config(page_title="Vikhram S | AI Researcher", page_icon="🧠", layout="wide")

# -------- AI PARTICLE BACKGROUND --------

components.html("""
<canvas id="bg"></canvas>
<style>
canvas{position:fixed;top:0;left:0;z-index:-1}
body{margin:0;background:#020617}
</style>

<script>
const c=document.getElementById("bg")
const x=c.getContext("2d")
c.width=window.innerWidth
c.height=window.innerHeight

let p=[]
for(let i=0;i<90;i++){
p.push({x:Math.random()*c.width,y:Math.random()*c.height,
vx:(Math.random()-.5)*.6,vy:(Math.random()-.5)*.6})
}

function draw(){
x.clearRect(0,0,c.width,c.height)

for(let i=0;i<p.length;i++){
let a=p[i]
a.x+=a.vx
a.y+=a.vy

if(a.x<0||a.x>c.width)a.vx*=-1
if(a.y<0||a.y>c.height)a.vy*=-1

x.beginPath()
x.arc(a.x,a.y,2,0,Math.PI*2)
x.fillStyle="#6366f1"
x.fill()

for(let j=i+1;j<p.length;j++){
let b=p[j]
let dx=a.x-b.x
let dy=a.y-b.y
let d=Math.sqrt(dx*dx+dy*dy)

if(d<120){
x.beginPath()
x.moveTo(a.x,a.y)
x.lineTo(b.x,b.y)
x.strokeStyle="rgba(99,102,241,.2)"
x.stroke()
}
}
}
requestAnimationFrame(draw)
}
draw()
</script>
""", height=0)

# -------- STYLES --------

st.markdown("""
<style>

.block-container{max-width:1100px;margin:auto}

.title{
font-size:50px;
font-weight:700;
background:linear-gradient(90deg,#6366f1,#a855f7,#22d3ee);
-webkit-background-clip:text;
color:transparent;
}

.icons img{width:32px;margin-right:14px}

.metric-grid{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(200px,1fr));
gap:16px;margin-top:20px
}

.metric{
background:rgba(255,255,255,.05);
border:1px solid rgba(255,255,255,.1);
padding:20px;border-radius:14px;
text-align:center
}

.card{
background:rgba(255,255,255,.05);
border:1px solid rgba(255,255,255,.1);
padding:20px;border-radius:14px;margin-bottom:15px
}

.timeline{border-left:2px solid #6366f1;padding-left:15px}

</style>
""", unsafe_allow_html=True)

# -------- HEADER --------

st.markdown('<div class="title">Vikhram S</div>', unsafe_allow_html=True)
st.write("AI Researcher | Multimodal AI | Vision-Language Models")
st.caption("Advisor – Machine Learning, Tech Society | Saveetha Engineering College")

# -------- SOCIAL --------

st.markdown(f"""
<a href="https://www.linkedin.com/in/vikhram-s/"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png"></a>
<a href="https://github.com/Vikhram-S"><img src="https://cdn-icons-png.flaticon.com/512/25/25231.png"></a>
<a href="https://huggingface.co/Vikhram-S"><img src="https://huggingface.co/front/assets/huggingface_logo.svg"></a>
<a href="mailto:vikhrams@saveetha.ac.in"><img src="https://cdn-icons-png.flaticon.com/512/732/732200.png"></a>
""", unsafe_allow_html=True)

# -------- METRICS --------

st.markdown("""
<div class="metric-grid">

<div class="metric">
<b>India AI Impact Summit 2026</b><br>
Compendium Author<br>
AI & Gender Empowerment
</div>

<div class="metric">
<b>21K+</b><br>
Python Library Downloads
</div>

<div class="metric">
<b>Springer</b><br>
LNNS Publication
</div>

<div class="metric">
<b>Multimodal</b><br>
AI Research
</div>

</div>
""", unsafe_allow_html=True)

# -------- TABS --------

tab1,tab2,tab3,tab4 = st.tabs(["Research","Publications","Recognition","GitHub"])

# -------- RESEARCH --------

with tab1:

    st.markdown("""
<div class="card">
<b>ExplainableVLM-Rad</b><br>
Explainable multimodal radiology report generation.
</div>
""", unsafe_allow_html=True)

    st.link_button("HuggingFace Model",
    "https://huggingface.co/Vikhram-S/mimic-vit-biogpt")

    st.link_button("Python Library",
    "https://pypi.org/project/IndianConstitution/")

# -------- GOOGLE SCHOLAR --------

with tab2:

    scholar_id="YOUR_SCHOLAR_ID"

    feed = feedparser.parse(
    f"https://scholar.googleusercontent.com/scholar?q=author:{scholar_id}&output=rss"
    )

    st.subheader("Latest Publications")

    for entry in feed.entries[:5]:
        st.markdown(f"- {entry.title}")

# -------- RECOGNITION --------

with tab3:

    st.link_button(
    "View AI & Gender Empowerment Casebook",
    "https://d19ob9sqegt2wc.cloudfront.net/stage/uploads/AI_Empowerment_Case_Study_Web_a09fbf83c9.pdf"
    )

    st.image("ai_summit.jpg", width="stretch")

# -------- GITHUB HEATMAP --------

with tab4:

    components.html("""
<img src="https://ghchart.rshah.org/Vikhram-S" width="100%">
""", height=200)

# -------- DOWNLOAD CV --------

with open("vikhram_cv.pdf","rb") as f:
    st.download_button(
        "Download CV",
        f,
        file_name="Vikhram_S_CV.pdf"
    )
