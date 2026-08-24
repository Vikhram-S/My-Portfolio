import streamlit as st

st.set_page_config(
    page_title="Vikhram S | AI Researcher",
    page_icon=None,
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Hide all Streamlit UI chrome
st.markdown("""
<style>
    #MainMenu, footer, header, [data-testid="stToolbar"] {
        visibility: hidden !important;
        height: 0px !important;
    }
    .stApp {
        background-color: #0b0f19;
    }
    .block-container {
        max-width: 680px;
        padding-top: 6.5rem;
        padding-bottom: 4rem;
    }
</style>
""", unsafe_allow_html=True)

TARGET = "https://vikhram-s.github.io/"

# Primary redirect method
st.markdown(
    f'<meta http-equiv="refresh" content="2.5;url={TARGET}">',
    unsafe_allow_html=True
)

# Main content
st.markdown(f"""
<div style="
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    color: #e2e8f0;
    text-align: center;
">

    <div style="
        font-size: 2.75rem;
        font-weight: 650;
        letter-spacing: -0.03em;
        margin-bottom: 0.6rem;
        background: linear-gradient(90deg, #a5b4fc, #c4b5fd);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    ">
        Vikhram S
    </div>

    <div style="
        font-size: 1.15rem;
        color: #94a3b8;
        font-weight: 400;
        margin-bottom: 3.2rem;
        letter-spacing: 0.01em;
    ">
        AI Researcher · Multimodal Intelligence · Medical AI · Public-Interest Technology
    </div>

    <div style="
        background: rgba(30, 41, 59, 0.45);
        border: 1px solid rgba(148, 163, 184, 0.12);
        border-radius: 14px;
        padding: 2.4rem 2rem;
        margin-bottom: 2.8rem;
    ">
        <p style="
            font-size: 1.08rem;
            line-height: 1.65;
            color: #e2e8f0;
            margin: 0 0 0.7rem 0;
        ">
            This page has permanently moved.
        </p>
        <p style="
            font-size: 0.98rem;
            color: #94a3b8;
            margin: 0;
            line-height: 1.5;
        ">
            You are being redirected to the official research website.
        </p>
    </div>

    <a href="{TARGET}" style="
        display: inline-block;
        background: #6366f1;
        color: #ffffff;
        text-decoration: none;
        padding: 0.9rem 2.1rem;
        border-radius: 9px;
        font-size: 1rem;
        font-weight: 500;
        letter-spacing: 0.01em;
        transition: background 0.2s ease;
    ">
        Continue to Official Website
    </a>

    <div style="
        margin-top: 3.8rem;
        font-size: 0.88rem;
        color: #64748b;
        line-height: 1.6;
    ">
        Permanent address<br>
        <a href="{TARGET}" style="color: #818cf8; text-decoration: none;">
            {TARGET}
        </a>
    </div>

</div>
""", unsafe_allow_html=True)

# Reliable JavaScript fallback
st.markdown(f"""
<script>
    setTimeout(function() {{
        window.location.replace("{TARGET}");
    }}, 2500);
</script>
""", unsafe_allow_html=True)
