from pathlib import Path
from html import escape
from textwrap import dedent

import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="NEXUS AI | News Intelligence",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# --------------------------------------------------
# MODEL LOADING
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Hugging Face model repository
MODEL_ID = "atharva1405/NEXUS-News-Summarizer"


@st.cache_resource
def load_model():

    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_ID
    )

    model = AutoModelForSeq2SeqLM.from_pretrained(
        MODEL_ID
    )

    model.eval()

    return tokenizer, model


try:
    tokenizer, model = load_model()

except Exception as error:
    st.error(f"Could not load the summarization model: {error}")
    st.stop()


# --------------------------------------------------
# CUSTOM STYLING
# --------------------------------------------------

st.markdown(
    dedent(
        """
        <style>
        .stApp {
            background:
                radial-gradient(ellipse at 10% 0%,
                    rgba(36, 76, 180, 0.16), transparent 38%),
                #080B12;
            color: #F0F3FA;
            font-family: Inter, sans-serif;
        }

        #MainMenu, footer { visibility: hidden; }
        [data-testid="stHeader"] { background: transparent; }

        .block-container {
            max-width: 1150px;
            padding-top: 1.5rem;
            padding-bottom: 3rem;
        }

        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 22px;
            margin-bottom: 48px;
            background: rgba(18, 23, 36, 0.8);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 16px;
        }

        .brand {
            font-size: 21px;
            font-weight: 800;
            letter-spacing: 2px;
            color: #FFFFFF;
        }
        .brand span { color: #7194FF; }

        .nav-tag {
            font-size: 11px;
            color: #A5B4FC;
            letter-spacing: 1.5px;
            border: 1px solid rgba(113,148,255,0.3);
            padding: 7px 12px;
            border-radius: 20px;
            background: rgba(113,148,255,0.08);
        }

        .hero {
            text-align: center;
            margin: 0 auto 44px auto;
        }

        .eyebrow {
            display: inline-block;
            color: #A5B4FC;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 3px;
            padding: 9px 15px;
            border-radius: 30px;
            border: 1px solid rgba(113,148,255,0.25);
            background: rgba(113,148,255,0.07);
            margin-bottom: 20px;
        }

        .hero h1 {
            font-size: clamp(38px, 6vw, 66px);
            font-weight: 850;
            letter-spacing: -2.5px;
            line-height: 1.08;
            color: #FFFFFF;
            margin: 0;
        }

        .gradient-text {
            background: linear-gradient(100deg,
                #8EA8FF 0%, #B9A1FF 45%, #75DEFF 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hero p {
            max-width: 610px;
            margin: 22px auto 0 auto;
            color: #929CB3;
            font-size: 16px;
            line-height: 1.8;
        }

        .section-label {
            font-size: 12px;
            font-weight: 700;
            color: #C5CEE0;
            letter-spacing: 1.5px;
            margin-bottom: 12px;
        }

        [data-testid="stTextArea"] textarea {
            background: #101522 !important;
            color: #F3F5FB !important;
            border: 1px solid #273149 !important;
            border-radius: 15px !important;
            padding: 18px !important;
            font-size: 15px !important;
            line-height: 1.8 !important;
        }

        [data-testid="stTextArea"] textarea:focus {
            border-color: #7896FF !important;
            box-shadow: 0 0 0 3px rgba(120,150,255,0.12) !important;
        }

        [data-testid="stTextArea"] textarea::placeholder {
            color: #66718A !important;
        }

        .stButton > button, .stDownloadButton > button {
            width: 100%;
            min-height: 50px;
            color: white !important;
            font-weight: 750 !important;
            font-size: 15px !important;
            border: none !important;
            border-radius: 12px !important;
            background: linear-gradient(100deg, #496EFF, #8666F8) !important;
            box-shadow: 0 8px 30px rgba(86,103,255,0.2);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .stButton > button:hover, .stDownloadButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 12px 35px rgba(86,103,255,0.35);
        }

        .result-card {
            background: linear-gradient(145deg,
                rgba(20,28,46,0.98), rgba(13,18,30,0.98));
            border: 1px solid rgba(125,151,255,0.24);
            border-radius: 18px;
            padding: 26px;
            margin-top: 10px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.2);
        }

        .result-heading {
            font-size: 12px;
            color: #A5B4FC;
            font-weight: 800;
            letter-spacing: 2px;
            margin-bottom: 16px;
        }

        .result-text {
            color: #E5EAF5;
            font-size: 17px;
            line-height: 1.9;
            white-space: pre-wrap;
            overflow-wrap: anywhere;
        }

        .info-card {
            background: rgba(17,23,37,0.8);
            border: 1px solid #202A3D;
            border-radius: 14px;
            padding: 19px;
            min-height: 100px;
        }

        .info-number {
            color: #FFFFFF;
            font-size: 23px;
            font-weight: 800;
        }

        .info-caption {
            color: #8995AD;
            font-size: 12px;
            margin-top: 7px;
        }

        hr {
            border-color: #20283A !important;
            margin-top: 30px !important;
            margin-bottom: 30px !important;
        }

        .footer {
            text-align: center;
            color: #647089;
            font-size: 12px;
            line-height: 2;
            padding-top: 30px;
        }
        .footer strong { color: #A5B4FC; }

        @media (max-width: 650px) {
            .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
            }
            .hero h1 { letter-spacing: -1px; }
            .navbar { margin-bottom: 32px; }
            .result-card { padding: 20px; }
        }
        </style>
        """
    ),
    unsafe_allow_html=True,
)


# --------------------------------------------------
# NAVIGATION
# --------------------------------------------------

st.markdown(
    dedent(
        """
        <div class="navbar">
            <div class="brand">✦ NEXUS<span>AI</span></div>
            <div class="nav-tag">NEWS INTELLIGENCE</div>
        </div>
        """
    ),
    unsafe_allow_html=True,
)


# --------------------------------------------------
# HERO
# --------------------------------------------------

st.markdown(
    dedent(
        """
        <div class="hero">
            <div class="eyebrow">✦ INTELLIGENCE, WITHOUT THE NOISE</div>
            <h1>
                Read less.<br>
                <span class="gradient-text">Understand more.</span>
            </h1>
            <p>
                Transform lengthy news articles into concise,
                meaningful summaries using an AI-powered
                text summarization model.
            </p>
        </div>
        """
    ),
    unsafe_allow_html=True,
)


# --------------------------------------------------
# ARTICLE INPUT
# --------------------------------------------------

st.markdown(
    '<div class="section-label">01 &nbsp; / &nbsp; YOUR SOURCE</div>',
    unsafe_allow_html=True,
)

article = st.text_area(
    "Article",
    height=260,
    placeholder=(
        "Paste your news article here...\n\n"
        "Politics, technology, sports, business — "
        "bring any story into focus."
    ),
    label_visibility="collapsed",
    key="article_input",
)

word_count = len(article.split())
col1, col2 = st.columns([3, 1])

with col1:
    st.markdown(
        f"""
        <div style="color:#75819A; font-size:12px; padding-top:12px;">
            ◈ &nbsp; {word_count:,} words detected
            &nbsp; · &nbsp; T5 SUMMARIZATION ENGINE
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    summarize_clicked = st.button(
        "✦  Generate Summary",
        use_container_width=True,
    )


# --------------------------------------------------
# GENERATE SUMMARY
# --------------------------------------------------

if summarize_clicked:
    if not article.strip():
        st.warning("Please paste a news article first.")
    else:
        with st.spinner("Reading your article and generating insights..."):
            try:
                inputs = tokenizer(
                    article,
                    return_tensors="pt",
                    max_length=512,
                    truncation=True,
                )

                summary_ids = model.generate(
                    **inputs,
                    max_length=128,
                    num_beams=4,
                    early_stopping=True,
                )

                summary = tokenizer.decode(
                    summary_ids[0],
                    skip_special_tokens=True,
                ).strip()

                st.session_state["generated_summary"] = summary
                st.session_state["summary_source"] = article

            except Exception as error:
                st.error(f"Unable to generate the summary: {error}")


# --------------------------------------------------
# SUMMARY RESULTS
# --------------------------------------------------

if st.session_state.get("generated_summary"):
    summary = st.session_state["generated_summary"]
    source_article = st.session_state.get("summary_source", "")
    summary_words = len(summary.split())
    original_words = len(source_article.split())

    reduction = (
        (1 - summary_words / original_words) * 100
        if original_words > 0
        else 0
    )

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(
        '<div class="section-label">02 &nbsp; / &nbsp; THE ESSENTIALS</div>',
        unsafe_allow_html=True,
    )

    # Keep the HTML unindented after dedent so Markdown does not show tags as code.
    summary_html = dedent(
        f"""
        <div class="result-card">
            <div class="result-heading">✦ &nbsp; AI-GENERATED SUMMARY</div>
            <div class="result-text">{escape(summary)}</div>
        </div>
        """
    ).strip()

    st.markdown(summary_html, unsafe_allow_html=True)
    st.write("")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            dedent(
                f"""
                <div class="info-card">
                    <div class="info-number">{original_words:,}</div>
                    <div class="info-caption">Original words</div>
                </div>
                """
            ),
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            dedent(
                f"""
                <div class="info-card">
                    <div class="info-number">{summary_words:,}</div>
                    <div class="info-caption">Summary words</div>
                </div>
                """
            ),
            unsafe_allow_html=True,
        )

    with c3:
        st.markdown(
            dedent(
                f"""
                <div class="info-card">
                    <div class="info-number">{reduction:.0f}%</div>
                    <div class="info-caption">Word count reduction</div>
                </div>
                """
            ),
            unsafe_allow_html=True,
        )

    st.write("")
    st.download_button(
        label="↓  Download Summary",
        data=summary,
        file_name="news_summary.txt",
        mime="text/plain",
        use_container_width=True,
    )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown(
    dedent(
        """
        <div class="footer">
            <strong>✦ NEXUS AI</strong><br>
            Powered by a fine-tuned T5 Transformer model.<br>
            Built for clearer, faster news consumption.
        </div>
        """
    ),
    unsafe_allow_html=True,
)
