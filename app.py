import streamlit as st

# Agent Profile
agent_name = "Halo"
specialization = "Internet Safety for Children"
age_range = "Up to Age 13"
mission = "To protect, educate, and empower children with safe and smart online behaviors."
skills = [
    "Online privacy education",
    "Cyberbullying prevention",
    "Parental control guidance",
    "Safe social media habits",
    "Digital citizenship training"
]
brand_voice = "Empowering, educational, and friendly"
affiliation = "SHE CAN DO I.T.™ Movement"

# Streamlit App Layout
st.set_page_config(page_title="Meet Halo", layout="centered")

st.title("🛡️ Meet Halo")
st.subheader("Your Digital Safety Ally for Kids")

st.markdown(f"**Agent Name:** {agent_name}")
st.markdown(f"**Specialization:** {specialization}")
st.markdown(f"**Target Audience:** Children ({age_range})")
st.markdown(f"**Mission:** {mission}")

st.markdown("### 👩🏾‍💻 Core Skills")
for skill in skills:
    st.markdown(f"- {skill}")

st.markdown(f"**Brand Voice:** {brand_voice}")
st.markdown(f"**Affiliation:** {affiliation}")

st.success("Halo is here to make the internet a safer place for every child.")

# Optional: Add image or branding
# st.image("halo_logo.png", caption="Halo – Empowering Kids Online", use_column_width=True)
