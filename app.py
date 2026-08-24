import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Vikhram S | AI Researcher",
    page_icon=None,          # no emoji / no icon
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------- Minimal dark network background (subtle, professional) ----------
components.html("""
<!DOCTYPE html>
<html>
<head>
<style>
canvas {
    position: fixed;
    top: 0;
    left: 0;
    z-index: -1;
}
body {
    margin: 0;
    overflow: hidden;
    background: #020617;
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

let nodes = [];
const nodeCount = 55;
for (let i = 0; i < nodeCount; i++) {
    nodes.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        vx: (Math.random() - 0.5) * 0.35,
        vy: (Math.random() - 0.5) * 0.35
    });
}

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    for (let i = 0; i < nodes.length; i++) {
        let n = nodes[i];
        n.x += n.vx;
        n.y += n.vy;
        if (n.x < 0 || n.x > canvas.width) n.vx *= -1;
        if (n.y < 0 || n.y > canvas.height) n.vy *= -1;

        ctx.beginPath();
        ctx.arc(n.x, n.y, 1.4, 0, Math.PI * 2);
        ctx.fillStyle = "rgba(99, 102, 241, 0.55)";
        ctx.fill();

        for (let j = i + 1; j < nodes.length; j++) {
            let m = nodes[j];
            let dx = n.x - m.x;
            let dy = n.y - m.y;
            let dist = Math.sqrt(dx * dx + dy * dy);
            if (dist < 110) {
                ctx.beginPath();
                ctx.moveTo(n.x, n.y);
                ctx.lineTo(m.x, m.y);
                ctx.strokeStyle = "rgba(99, 102, 241, 0.08)";
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
/* Hide Streamlit chrome */
#MainMenu, footer, header {visibility: hidden !important;}
.stApp {background: transparent;}

.block-container {
    max-width: 720px;
    padding-top: 4.5rem;
    padding-bottom: 3rem;
}

.main-title {
    font-size: clamp(2.4rem, 5vw, 3.2rem);
    font-weight: 650;
    letter-spacing: -0.02em;
    background: linear-gradient(90deg, #818cf8, #c084fc, #67e8f9);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.4rem;
    text-align: center;
}

.subtitle {
    font-size: 1.15rem;
    color: #94a3b8;
    text-align: center;
    margin-bottom: 2.8rem;
    font-weight: 400;
}

.card {
    background: rgba(15, 23, 42, 0.65);
    border: 1px solid rgba(148, 163, 184, 0.12);
    border-radius: 16px;
    padding: 2rem 1.8rem;
    backdrop-filter: blur(12px);
    text-align: center;
    margin-bottom: 2rem;
}

.card p {
    color: #e2e8f0;
    font-size: 1.05rem;
    line-height: 1.6;
    margin: 0 0 0.6rem 0;
}

.card .secondary {
    color: #94a3b8;
    font-size: 0.95rem;
}

.redirect-btn {
    display: inline-block;
    background: linear-gradient(90deg, #6366f1, #8b5cf6);
    color: white !important;
    text-decoration: none;
    padding: 0.85rem 2rem;
    border-radius: 10px;
    font-weight: 500;
    font-size: 1rem;
    letter-spacing: 0.01em;
    transition: all 0.25s ease;
    border: none;
}

.redirect-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(99, 102, 241, 0.35);
}

.footer-note {
    text-align: center;
    color: #64748b;
    font-size: 0.85rem;
    margin-top: 2.5rem;
}

.footer-note a {
    color: #818cf8;
    text-decoration: none;
}
</style>
""", unsafe_allow_html=True)

TARGET = "https://vikhram-s.github.io/"

# Meta refresh (primary, works without JS)
st.markdown(
    f'<meta http-equiv="refresh" content="2.2; url={TARGET}">',
    unsafe_allow_html=True
)

# ---------- Content ----------
st.markdown('<div class="main-title">Vikhram S</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">AI Researcher · Multimodal Intelligence · Medical AI · Public-Interest Technology</div>',
    unsafe_allow_html=True
)

st.markdown(f"""
<div class="card">
    <p>This page has permanently moved to the official research website.</p>
    <p class="secondary">You will be redirected automatically in a moment.</p>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div style="text-align: center;">
    <a href="{TARGET}" class="redirect-btn">
        Continue to Official Website
    </a>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="footer-note">
    Permanent address:<br>
    <a href="{TARGET}">{TARGET}</a>
</div>
""", unsafe_allow_html=True)

# JavaScript fallback (highly reliable)
st.markdown(f"""
<script>
    setTimeout(function() {{
        window.location.replace("{TARGET}");
    }}, 2200);
</script>
""", unsafe_allow_html=True)
