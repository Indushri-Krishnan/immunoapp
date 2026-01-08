import streamlit as st

# ---------- Page Config ----------
st.set_page_config(
    page_title="IMMUNO APP",
    page_icon="🩺",
    layout="centered"
)

# ---------- Custom CSS ----------
st.markdown("""
<style>
.main {
    background-color: #f4f8fb;
}
h1, h2, h3 {
    color: #0b4f6c;
}
.card {
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}
.footer {
    font-size: 13px;
    color: gray;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown("<h1 style='text-align:center;'>🩺 IMMUNO App</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>(Real-time medical diagnosis screening)</p>", unsafe_allow_html=True)

# ---------- Input Section ----------
st.markdown("<div class='card'><h3>Biosensed inputs</h3>", unsafe_allow_html=True)

cd19 = st.number_input("CD19 (cells/µL)", min_value=0.0)
cd34 = st.number_input("CD34 (cells/µL)", min_value=0.0)

anti_ccp = st.number_input("Anti-CCP (U/mL)", min_value=0.0)
rf = st.number_input("Rheumatoid Factor (U/mL)", min_value=0.0)

il6 = st.number_input("IL-6 (pg/mL)", min_value=0.0)
tnf = st.number_input("TNF-α (pg/mL)", min_value=0.0)

testosterone = st.number_input("Testosterone (ng/dL)", min_value=0.0)
lh_fsh = st.number_input("LH : FSH Ratio", min_value=0.0)
amh = st.number_input("AMH", min_value=0.0)

gfap = st.number_input("GFAP (pg/mL)", min_value=0.0)

st.markdown("</div>", unsafe_allow_html=True)

# ---------- Analyze Button ----------
st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
analyze = st.button("🔍 Analyze Health Risk")
st.markdown("</div>", unsafe_allow_html=True)

# ---------- Results ----------
if analyze:
    st.markdown("<div class='card'><h3>📊 Screening Results</h3>", unsafe_allow_html=True)

    # CD19
    if cd19 > 1000:
        st.error("CD19: Abnormal-Blood cancer risk")
    elif 100 <= cd19 <= 500:
        st.success("CD19: Normal Range")
    else:
        st.warning("CD19: Below Normal")

    # CD34
    if cd34 < 50:
        st.success("CD34: Normal")
    else:
        st.warning("CD34: Elevated-Blood cancer risk")

    st.divider()

    # RA
    if anti_ccp >= 60:
        st.error("Anti-CCP: High Positive-RA Risk")
    elif 40 <= anti_ccp < 60:
        st.warning("Anti-CCP: Moderate Positive")
    elif 20 <= anti_ccp < 40:
        st.info("Anti-CCP: Weak Positive")
    else:
        st.success("Anti-CCP: Negative")

    if rf > 60:
        st.error("Rheumatoid Factor: Positive")
    else:
        st.success("Rheumatoid Factor: Normal")

    st.divider()

    # Osteoarthritis / Inflammation
    if il6 > 5:
        st.warning("IL-6: Elevated-OA risk")
    else:
        st.success("IL-6: Normal")

    if tnf > 29.4:
        st.warning("TNF-α: Elevated-OA risk")
    else:
        st.success("TNF-α: Normal")

    st.divider()

    # PCOD
    if testosterone < 15 or testosterone > 70:
        st.warning("Testosterone: Abnormal-PCOD Risk")
    else:
        st.success("Testosterone: Normal")

    if abs(lh_fsh - 1.0) < 0.2:
        st.success("LH:FSH Ratio: Normal")
    else:
        st.warning("LH:FSH Ratio: Hormonal Imbalance")

    if amh > 5.8 < 8.17:
        st.warning("AMH: High-PCOD Risk")
    else:
        st.success("AMH: Normal")

    st.divider()

    # GFAP
    if gfap > 30:
        st.error("GFAP: Elevated-Cardiac Risk")
    else:
        st.success("GFAP: Normal")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------- Footer ----------
st.markdown("""
<div class="footer">
⚠ Disclaimer: This app is for academic & screening purposes only.<br>
It must be linked with implantable chip for real-time monitoring.
</div>
""", unsafe_allow_html=True)
