# # import streamlit as st
# # import joblib
# # import numpy as np
# #
# # st.set_page_config(page_title="CreditWise", page_icon="🏦")
# #
# # model  = joblib.load("loan_model.pkl")
# # scaler = joblib.load("scaler.pkl")
# #
# # st.title("🏦 CreditWise")
# # st.subheader("Loan Approval Prediction System")
# # st.markdown("---")
# #
# # col1, col2 = st.columns(2)
# #
# # with col1:
# #     applicant_income   = st.number_input("Applicant Income", min_value=0, value=50000)
# #     age                = st.number_input("Age", min_value=18, max_value=80, value=30)
# #     savings            = st.number_input("Savings", min_value=0, value=100000)
# #     loan_amount        = st.number_input("Loan Amount", min_value=0, value=200000)
# #     credit_score       = st.number_input("Credit Score", min_value=300, max_value=900, value=700)
# #     dti_ratio          = st.number_input("DTI Ratio", min_value=0.0, max_value=1.0, value=0.3, step=0.01)
# #
# # with col2:
# #     coapplicant_income = st.number_input("Co-Applicant Income", min_value=0, value=0)
# #     dependents         = st.number_input("Dependents", min_value=0, value=0)
# #     collateral_value   = st.number_input("Collateral Value", min_value=0, value=0)
# #     loan_term          = st.number_input("Loan Term (months)", min_value=12, value=360, step=12)
# #     existing_loans     = st.number_input("Existing Loans", min_value=0, value=0)
# #     education_level    = st.selectbox("Education Level", ["Graduate", "Not Graduate", "Post Graduate"])
# #
# # col3, col4 = st.columns(2)
# #
# # with col3:
# #     employment_status  = st.selectbox("Employment Status", ["Salaried", "Self-employed", "Unemployed"])
# #     employer_category  = st.selectbox("Employer Category", ["Government", "MNC", "Private", "Unemployed"])
# #
# # with col4:
# #     property_area      = st.selectbox("Property Area", ["Rural", "Semiurban", "Urban"])
# #     loan_purpose       = st.selectbox("Loan Purpose", ["Car", "Education", "Home", "Personal"])
# #     marital_status     = st.selectbox("Marital Status", ["Married", "Single"])
# #     gender             = st.selectbox("Gender", ["Female", "Male"])
# #
# # st.markdown("---")
# #
# # if st.button("Check Loan Eligibility", use_container_width=True):
# #     edu_map = {"Graduate": 0, "Not Graduate": 1, "Post Graduate": 2}
# #     edu_encoded = edu_map[education_level]
# #
# #     dti_sq    = dti_ratio ** 2
# #     credit_sq = credit_score ** 2
# #
# #     features = np.array([[
# #         applicant_income, coapplicant_income, age, dependents,
# #         existing_loans, savings, collateral_value, loan_amount,
# #         loan_term, edu_encoded,
# #         1 if employment_status=="Salaried" else 0,
# #         1 if employment_status=="Self-employed" else 0,
# #         1 if employment_status=="Unemployed" else 0,
# #         1 if employer_category=="Government" else 0,
# #         1 if employer_category=="MNC" else 0,
# #         1 if employer_category=="Private" else 0,
# #         1 if employer_category=="Unemployed" else 0,
# #         1 if property_area=="Semiurban" else 0,
# #         1 if property_area=="Urban" else 0,
# #         1 if loan_purpose=="Car" else 0,
# #         1 if loan_purpose=="Education" else 0,
# #         1 if loan_purpose=="Home" else 0,
# #         1 if loan_purpose=="Personal" else 0,
# #         1 if marital_status=="Single" else 0,
# #         1 if gender=="Male" else 0,
# #         dti_sq, credit_sq
# #     ]])
# #
# #     features_scaled = scaler.transform(features)
# #     prediction = model.predict(features_scaled)[0]
# #
# #     if prediction == 1:
# #         st.success("✅ Loan Approved! Congratulations!")
# #         st.balloons()
# #     else:
# #         st.error("❌ Loan Not Approved.")
#
# import streamlit as st
# import joblib
# import numpy as np
#
# model  = joblib.load(r"C:\Users\deepu\PycharmProjects\MLProject\loan_model.pkl")
# scaler = joblib.load(r"C:\Users\deepu\PycharmProjects\MLProject\scaler.pkl")
#
# # ── Custom CSS ────────────────────────────────────────────
# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
#
# * { font-family: 'Poppins', sans-serif; }
#
# .stApp {
#     background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
#     min-height: 100vh;
# }
#
# /* Hero Header */
# .hero {
#     text-align: center;
#     padding: 40px 20px 20px;
# }
# .hero h1 {
#     font-size: 3.5rem;
#     font-weight: 700;
#     background: linear-gradient(90deg, #f7971e, #ffd200);
#     -webkit-background-clip: text;
#     -webkit-text-fill-color: transparent;
#     margin-bottom: 5px;
# }
# .hero p {
#     color: #aaa;
#     font-size: 1.1rem;
#     margin-top: 0;
# }
#
# /* Cards */
# .card {
#     background: rgba(255,255,255,0.05);
#     border: 1px solid rgba(255,255,255,0.1);
#     border-radius: 16px;
#     padding: 25px;
#     margin-bottom: 20px;
#     backdrop-filter: blur(10px);
# }
# .card-title {
#     color: #ffd200;
#     font-size: 1.1rem;
#     font-weight: 600;
#     margin-bottom: 15px;
#     letter-spacing: 1px;
#     text-transform: uppercase;
# }
#
# /* Input labels */
# label { color: #ccc !important; font-size: 0.85rem !important; }
#
# /* Number inputs & selects */
# .stNumberInput input, .stSelectbox select {
#     background: rgba(255,255,255,0.08) !important;
#     border: 1px solid rgba(255,255,255,0.15) !important;
#     border-radius: 10px !important;
#     color: white !important;
# }
#
# /* Button */
# .stButton > button {
#     background: linear-gradient(90deg, #f7971e, #ffd200) !important;
#     color: #1a1a2e !important;
#     font-weight: 700 !important;
#     font-size: 1.1rem !important;
#     border: none !important;
#     border-radius: 50px !important;
#     padding: 15px 40px !important;
#     width: 100% !important;
#     cursor: pointer !important;
#     transition: transform 0.2s !important;
#     margin-top: 10px !important;
# }
# .stButton > button:hover {
#     transform: scale(1.02) !important;
#     box-shadow: 0 8px 25px rgba(247,151,30,0.4) !important;
# }
#
# /* Result boxes */
# .result-approved {
#     background: linear-gradient(135deg, #11998e, #38ef7d);
#     border-radius: 16px;
#     padding: 30px;
#     text-align: center;
#     margin-top: 20px;
# }
# .result-rejected {
#     background: linear-gradient(135deg, #c0392b, #e74c3c);
#     border-radius: 16px;
#     padding: 30px;
#     text-align: center;
#     margin-top: 20px;
# }
# .result-title {
#     font-size: 2rem;
#     font-weight: 700;
#     color: white;
#     margin: 0;
# }
# .result-sub {
#     color: rgba(255,255,255,0.85);
#     font-size: 1rem;
#     margin-top: 8px;
# }
#
# /* Stats bar */
# .stat-box {
#     background: rgba(255,255,255,0.07);
#     border-radius: 12px;
#     padding: 15px;
#     text-align: center;
#     border: 1px solid rgba(255,255,255,0.1);
# }
# .stat-number {
#     font-size: 1.8rem;
#     font-weight: 700;
#     color: #ffd200;
# }
# .stat-label {
#     color: #aaa;
#     font-size: 0.8rem;
# }
#
# div[data-testid="stMarkdownContainer"] p { color: #ccc; }
# </style>
# """, unsafe_allow_html=True)
#
# # ── Hero Section ─────────────────────────────────────────
# st.markdown("""
# <div class="hero">
#     <h1>💳 CreditWise</h1>
#     <p>AI-Powered Loan Approval Prediction System</p>
# </div>
# """, unsafe_allow_html=True)
#
# # ── Stats Row ─────────────────────────────────────────────
# c1, c2, c3, c4 = st.columns(4)
# with c1:
#     st.markdown('<div class="stat-box"><div class="stat-number">95%</div><div class="stat-label">Accuracy</div></div>', unsafe_allow_html=True)
# with c2:
#     st.markdown('<div class="stat-box"><div class="stat-number">27</div><div class="stat-label">Features Analyzed</div></div>', unsafe_allow_html=True)
# with c3:
#     st.markdown('<div class="stat-box"><div class="stat-number">AI</div><div class="stat-label">Powered Model</div></div>', unsafe_allow_html=True)
# with c4:
#     st.markdown('<div class="stat-box"><div class="stat-number">⚡</div><div class="stat-label">Instant Result</div></div>', unsafe_allow_html=True)
#
# st.markdown("<br>", unsafe_allow_html=True)
#
# # ── Form ─────────────────────────────────────────────────
# st.markdown('<div class="card"><div class="card-title">👤 Personal Information</div>', unsafe_allow_html=True)
# col1, col2, col3 = st.columns(3)
# with col1:
#     applicant_income   = st.number_input("Applicant Income (₹)", min_value=0, value=50000)
# with col2:
#     coapplicant_income = st.number_input("Co-Applicant Income (₹)", min_value=0, value=0)
# with col3:
#     age                = st.number_input("Age", min_value=18, max_value=80, value=30)
#
# col4, col5, col6 = st.columns(3)
# with col4:
#     dependents         = st.number_input("Dependents", min_value=0, value=0)
# with col5:
#     gender             = st.selectbox("Gender", ["Female", "Male"])
# with col6:
#     marital_status     = st.selectbox("Marital Status", ["Married", "Single"])
# st.markdown('</div>', unsafe_allow_html=True)
#
# st.markdown('<div class="card"><div class="card-title">💼 Financial Details</div>', unsafe_allow_html=True)
# col7, col8, col9 = st.columns(3)
# with col7:
#     savings            = st.number_input("Savings (₹)", min_value=0, value=100000)
# with col8:
#     collateral_value   = st.number_input("Collateral Value (₹)", min_value=0, value=0)
# with col9:
#     existing_loans     = st.number_input("Existing Loans", min_value=0, value=0)
#
# col10, col11 = st.columns(2)
# with col10:
#     credit_score       = st.number_input("Credit Score", min_value=300, max_value=900, value=700)
# with col11:
#     dti_ratio          = st.number_input("DTI Ratio", min_value=0.0, max_value=1.0, value=0.3, step=0.01)
# st.markdown('</div>', unsafe_allow_html=True)
#
# st.markdown('<div class="card"><div class="card-title">🏦 Loan Details</div>', unsafe_allow_html=True)
# col12, col13, col14 = st.columns(3)
# with col12:
#     loan_amount        = st.number_input("Loan Amount (₹)", min_value=0, value=200000)
# with col13:
#     loan_term          = st.number_input("Loan Term (months)", min_value=12, value=360, step=12)
# with col14:
#     loan_purpose       = st.selectbox("Loan Purpose", ["Car", "Education", "Home", "Personal"])
# st.markdown('</div>', unsafe_allow_html=True)
#
# st.markdown('<div class="card"><div class="card-title">🏢 Employment Details</div>', unsafe_allow_html=True)
# col15, col16, col17 = st.columns(3)
# with col15:
#     employment_status  = st.selectbox("Employment Status", ["Salaried", "Self-employed", "Unemployed"])
# with col16:
#     employer_category  = st.selectbox("Employer Category", ["Government", "MNC", "Private", "Unemployed"])
# with col17:
#     property_area      = st.selectbox("Property Area", ["Rural", "Semiurban", "Urban"])
#
# education_level        = st.selectbox("Education Level", ["Graduate", "Not Graduate", "Post Graduate"])
# st.markdown('</div>', unsafe_allow_html=True)
#
# # ── Predict ───────────────────────────────────────────────
# if st.button("🔍 Check My Loan Eligibility"):
#     edu_map = {"Graduate": 0, "Not Graduate": 1, "Post Graduate": 2}
#     features = np.array([[
#         applicant_income, coapplicant_income, age, dependents,
#         existing_loans, savings, collateral_value, loan_amount,
#         loan_term, edu_map[education_level],
#         1 if employment_status=="Salaried" else 0,
#         1 if employment_status=="Self-employed" else 0,
#         1 if employment_status=="Unemployed" else 0,
#         1 if employer_category=="Government" else 0,
#         1 if employer_category=="MNC" else 0,
#         1 if employer_category=="Private" else 0,
#         1 if employer_category=="Unemployed" else 0,
#         1 if property_area=="Semiurban" else 0,
#         1 if property_area=="Urban" else 0,
#         1 if loan_purpose=="Car" else 0,
#         1 if loan_purpose=="Education" else 0,
#         1 if loan_purpose=="Home" else 0,
#         1 if loan_purpose=="Personal" else 0,
#         1 if marital_status=="Single" else 0,
#         1 if gender=="Male" else 0,
#         dti_ratio**2, credit_score**2
#     ]])
#
#     features_scaled = scaler.transform(features)
#     prediction = model.predict(features_scaled)[0]
#
#     if prediction == 1:
#         st.markdown("""
#         <div class="result-approved">
#             <div class="result-title">✅ Loan Approved!</div>
#             <div class="result-sub">Congratulations! Your loan application looks great. You qualify for the requested loan amount.</div>
#         </div>
#         """, unsafe_allow_html=True)
#         st.balloons()
#     else:
#         st.markdown("""
#         <div class="result-rejected">
#             <div class="result-title">❌ Loan Not Approved</div>
#             <div class="result-sub">Try improving your Credit Score, reducing DTI Ratio, or increasing your savings.</div>
#         </div>
#         """, unsafe_allow_html=True)
#


import streamlit as st
import joblib
import numpy as np

model  = joblib.load(r"C:\myproject\CreditWise_Loan\CreditWise__Loan_Aprroval\loan_model.pkl")
scaler = joblib.load(r"C:\myproject\CreditWise_Loan\CreditWise__Loan_Aprroval\scaler.pkl")
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

* { font-family: 'Poppins', sans-serif; }

.stApp {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    min-height: 100vh;
}

.hero { text-align: center; padding: 40px 20px 20px; }
.hero h1 {
    font-size: 3.5rem; font-weight: 700;
    background: linear-gradient(90deg, #f7971e, #ffd200);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    margin-bottom: 5px;
}
.hero p { color: #ccc; font-size: 1.1rem; margin-top: 0; }

.card {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 16px; padding: 25px; margin-bottom: 20px;
}
.card-title {
    color: #ffd200; font-size: 1rem; font-weight: 600;
    margin-bottom: 15px; letter-spacing: 1px; text-transform: uppercase;
}

.stat-box {
    background: rgba(255,255,255,0.07);
    border-radius: 12px; padding: 15px; text-align: center;
    border: 1px solid rgba(255,255,255,0.1);
}
.stat-number { font-size: 1.8rem; font-weight: 700; color: #ffd200; }
.stat-label { color: #aaa; font-size: 0.8rem; }

label, .stSelectbox label, .stNumberInput label {
    color: white !important;
    font-size: 0.9rem !important;
    font-weight: 500 !important;
}

.stNumberInput input {
    background-color: #1e1b4b !important;
    color: white !important;
    border: 1.5px solid #ffd200 !important;
    border-radius: 10px !important;
    font-size: 1rem !important;
}

.stSelectbox > div > div {
    background-color: #1e1b4b !important;
    color: white !important;
    border: 1.5px solid #ffd200 !important;
    border-radius: 10px !important;
}

.stSelectbox > div > div > div { color: white !important; }

.stNumberInput button {
    background-color: #302b63 !important;
    color: #ffd200 !important;
    border: 1px solid #ffd200 !important;
}

.stButton > button {
    background: linear-gradient(90deg, #f7971e, #ffd200) !important;
    color: #1a1a2e !important;
    font-weight: 700 !important;
    font-size: 1.1rem !important;
    border: none !important;
    border-radius: 50px !important;
    padding: 15px 40px !important;
    width: 100% !important;
    margin-top: 10px !important;
}
.stButton > button:hover {
    transform: scale(1.02) !important;
    box-shadow: 0 8px 25px rgba(247,151,30,0.4) !important;
}

.result-approved {
    background: linear-gradient(135deg, #11998e, #38ef7d);
    border-radius: 16px; padding: 30px; text-align: center; margin-top: 20px;
}
.result-rejected {
    background: linear-gradient(135deg, #c0392b, #e74c3c);
    border-radius: 16px; padding: 30px; text-align: center; margin-top: 20px;
}
.result-title { font-size: 2rem; font-weight: 700; color: white; }
.result-sub { color: rgba(255,255,255,0.85); font-size: 1rem; margin-top: 8px; }

div[data-testid="stMarkdownContainer"] p { color: #ccc; }
</style>
""", unsafe_allow_html=True)

# ── Hero ─────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <h1>💳 CreditWise</h1>
    <p>AI-Powered Loan Approval Prediction System</p>
</div>
""", unsafe_allow_html=True)

# ── Stats ─────────────────────────────────────────────────
c1, c2 = st.columns(2)
with c1:
    st.markdown('<div class="stat-box"><div class="stat-number">86.5%</div><div class="stat-label">Accuracy</div></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="stat-box"><div class="stat-number">78.3%</div><div class="stat-label">Precision</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Personal Info ─────────────────────────────────────────
st.markdown('<div class="card"><div class="card-title">👤 Personal Information</div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    applicant_income   = st.number_input("Applicant Income (₹)", min_value=0, value=50000)
with col2:
    coapplicant_income = st.number_input("Co-Applicant Income (₹)", min_value=0, value=0)
with col3:
    age                = st.number_input("Age", min_value=18, max_value=80, value=30)

col4, col5, col6 = st.columns(3)
with col4:
    dependents         = st.number_input("Dependents", min_value=0, value=0)
with col5:
    gender             = st.selectbox("Gender", ["Female", "Male"])
with col6:
    marital_status     = st.selectbox("Marital Status", ["Married", "Single"])
st.markdown('</div>', unsafe_allow_html=True)

# ── Financial Details ─────────────────────────────────────
st.markdown('<div class="card"><div class="card-title">💰 Financial Details</div>', unsafe_allow_html=True)
col7, col8, col9 = st.columns(3)
with col7:
    savings            = st.number_input("Savings (₹)", min_value=0, value=100000)
with col8:
    collateral_value   = st.number_input("Collateral Value (₹)", min_value=0, value=0)
with col9:
    existing_loans     = st.number_input("Existing Loans", min_value=0, value=0)

col10, col11 = st.columns(2)
with col10:
    credit_score       = st.number_input("Credit Score", min_value=300, max_value=900, value=700)
with col11:
    dti_ratio          = st.number_input("DTI Ratio", min_value=0.0, max_value=1.0, value=0.3, step=0.01)
st.markdown('</div>', unsafe_allow_html=True)

# ── Loan Details ──────────────────────────────────────────
st.markdown('<div class="card"><div class="card-title">🏦 Loan Details</div>', unsafe_allow_html=True)
col12, col13, col14 = st.columns(3)
with col12:
    loan_amount        = st.number_input("Loan Amount (₹)", min_value=0, value=200000)
with col13:
    loan_term          = st.number_input("Loan Term (months)", min_value=12, value=360, step=12)
with col14:
    loan_purpose       = st.selectbox("Loan Purpose", ["Car", "Education", "Home", "Personal"])
st.markdown('</div>', unsafe_allow_html=True)

# ── Employment Details ────────────────────────────────────
st.markdown('<div class="card"><div class="card-title">🏢 Employment Details</div>', unsafe_allow_html=True)
col15, col16, col17 = st.columns(3)
with col15:
    employment_status  = st.selectbox("Employment Status", ["Salaried", "Self-employed", "Unemployed"])
with col16:
    employer_category  = st.selectbox("Employer Category", ["Government", "MNC", "Private", "Unemployed"])
with col17:
    property_area      = st.selectbox("Property Area", ["Rural", "Semiurban", "Urban"])

education_level        = st.selectbox("Education Level", ["Graduate", "Not Graduate", "Post Graduate"])
st.markdown('</div>', unsafe_allow_html=True)

# ── Predict ───────────────────────────────────────────────
if st.button("🔍 Check My Loan Eligibility"):
    edu_map = {"Graduate": 0, "Not Graduate": 1, "Post Graduate": 2}
    features = np.array([[
        applicant_income, coapplicant_income, age, dependents,
        existing_loans, savings, collateral_value, loan_amount,
        loan_term, edu_map[education_level],
        1 if employment_status=="Salaried" else 0,
        1 if employment_status=="Self-employed" else 0,
        1 if employment_status=="Unemployed" else 0,
        1 if employer_category=="Government" else 0,
        1 if employer_category=="MNC" else 0,
        1 if employer_category=="Private" else 0,
        1 if employer_category=="Unemployed" else 0,
        1 if property_area=="Semiurban" else 0,
        1 if property_area=="Urban" else 0,
        1 if loan_purpose=="Car" else 0,
        1 if loan_purpose=="Education" else 0,
        1 if loan_purpose=="Home" else 0,
        1 if loan_purpose=="Personal" else 0,
        1 if marital_status=="Single" else 0,
        1 if gender=="Male" else 0,
        dti_ratio**2, credit_score**2
    ]])

    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)[0]

    if prediction == 1:
        st.markdown("""
        <div class="result-approved">
            <div class="result-title">✅ Loan Approved!</div>
            <div class="result-sub">Congratulations! Your application looks great. You qualify for the requested loan amount.</div>
        </div>
        """, unsafe_allow_html=True)
        st.balloons()
    else:
        st.markdown("""
        <div class="result-rejected">
            <div class="result-title">❌ Loan Not Approved</div>
            <div class="result-sub">Try improving your Credit Score, reducing DTI Ratio, or increasing your Savings.</div>
        </div>
        """, unsafe_allow_html=True)