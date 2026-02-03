import streamlit as st

# ------------------ Page Config ------------------
st.set_page_config(
    page_title="Video Editor Portfolio",
    page_icon="🎬",
    layout="wide"
)

# ------------------ Custom CSS ------------------
st.markdown("""
<style>
body {
    background-color: #0f0f0f;
}
.video-container {
    border-radius: 16px;
    overflow: hidden;
}
.title-text {
    font-size: 48px;
    font-weight: 700;
}
.subtitle-text {
    font-size: 20px;
    color: #bbbbbb;
}
.section-title {
    font-size: 32px;
    margin-top: 40px;
}
.footer {
    text-align: center;
    color: #777;
    margin-top: 60px;
}
</style>
""", unsafe_allow_html=True)

# ------------------ Hero Section ------------------
st.title("🎬 Savya Sanchi")
st.markdown("<div class='subtitle-text'>Video Editor  |  Motion Designer | Storyteller</div>", unsafe_allow_html=True)

st.markdown("---")

# ------------------ About Section ------------------
st.header("About Me")
st.write(
    "I’m a video editor specializing in cinematic edits, motion graphics, and storytelling. "
    "I work with Premiere Pro, After Effects, and DaVinci Resolve to craft engaging visuals "
    "for brands, creators, and personal projects."
)

st.markdown("---")
# ------------------ Showreel Section ------------------
st.header("Showreel")

col1, col2 = st.columns(2)

with col1:
    st.video("https://youtu.be/ex_Dcy_so6U")
    st.caption("🎥 Real Estate Edit")

with col2:
    st.video("https://youtu.be/zoycIE0ZVpk")
    st.caption("⚡ Talking Head Edit")

col3, col4 = st.columns(2)

with col3:
    st.video("https://youtu.be/OV89V6QA-8Y")
    st.caption("🎨 Social media Edit")

with col4:
    st.video("https://www.youtube.com/watch?v=VIDEO_LINK_4")
    st.caption("🎶 UI Saas Explainer Edit")

st.markdown("---")

# ------------------ Skills Section ------------------
st.header("Skills")


skills = [
    "Adobe Premiere Pro",
    "After Effects",
    "DaVinci Resolve",
    "Motion Graphics",
    "Color Grading",
    "Storytelling"
]
st.markdown("<div class='subtitle-text'>" +" | ".join(skills) + "</div>", unsafe_allow_html=True)

st.markdown("---")

# ------------------ Contact Section ------------------
st.header("Contact")

st.write("📧 Email: mssanchi15@gmail.com")

st.markdown("---")

# ------------------ Footer ------------------
st.markdown("<div class='footer'>© 2026 Savya Sanchi | Built with Streamlit</div>", unsafe_allow_html=True)
