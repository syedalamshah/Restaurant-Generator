import streamlit as st
import langchain_helper

st.set_page_config(
    page_title="Restaurant Generator",
    page_icon="",
    layout="centered"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@300;400;500;600&display=swap');

    * { font-family: 'Inter', sans-serif; }

    .stApp { background-color: #0a1628; }

    .hero-title {
        font-family: 'Playfair Display', serif;
        font-size: 3rem;
        font-weight: 700;
        color: #e8f4f8;
        text-align: center;
        letter-spacing: -0.5px;
        margin-bottom: 8px;
    }

    .hero-subtitle {
        font-size: 0.95rem;
        color: #64899e;
        text-align: center;
        margin-bottom: 40px;
        font-weight: 300;
        letter-spacing: 0.5px;
    }

    .restaurant-name {
        font-family: 'Playfair Display', serif;
        font-size: 2rem;
        font-weight: 600;
        color: #e8f4f8;
        text-align: center;
        padding: 32px;
        background: #0f2035;
        border-radius: 16px;
        border: 1px solid #1e3a5f;
        margin: 20px 0;
        letter-spacing: 0.3px;
    }

    .menu-item {
        background: #0f2035;
        padding: 14px 22px;
        border-radius: 10px;
        margin: 6px 0;
        border: 1px solid #1e3a5f;
        color: #a8c5d6;
        font-size: 0.95rem;
        font-weight: 400;
    }

    .section-title {
        font-size: 0.75rem;
        font-weight: 600;
        color: #4a7a96;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin: 24px 0 12px 0;
    }

    div[data-testid="stSelectbox"] label {
        color: #4a7a96;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    div[data-testid="stSelectbox"] > div {
        background: #0f2035;
        border: 1px solid #1e3a5f;
        border-radius: 10px;
        color: #e8f4f8;
    }

    .stButton > button {
        background: #1a6b9a;
        color: #ffffff;
        border: none;
        border-radius: 10px;
        padding: 12px 32px;
        font-weight: 600;
        font-size: 0.95rem;
        width: 100%;
        letter-spacing: 0.5px;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        background: #1e85be;
        color: #ffffff;
    }

    hr { border-color: #1e3a5f; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='hero-title'>Restaurant Generator</div>", unsafe_allow_html=True)
st.divider()

cuisine = st.selectbox("Cuisine Type", ("Indian", "Italian", "Mexican", "Arabic", "American", "Chinese", "Pakistani"))

st.markdown("<br>", unsafe_allow_html=True)

if st.button("Generate"):
    with st.spinner("Generating..."):
        response = langchain_helper.generate_restaurant_name_and_items(cuisine)

        st.markdown(f"<div class='restaurant-name'>{response['restaurant_name'].strip()}</div>", unsafe_allow_html=True)

        st.markdown("<div class='section-title'>Menu Items</div>", unsafe_allow_html=True)

        menu_items = response['menu_items'].strip().split(",")
        for item in menu_items:
            st.markdown(f"<div class='menu-item'>{item.strip()}</div>", unsafe_allow_html=True)