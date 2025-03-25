import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st
from datetime import datetime

# === ONION RIVER INC. STYLED HEADER ===
st.set_page_config(page_title="Onion River Inc. | AI Real Estate Agent", layout="wide")
st.markdown("""
    <div style='display: flex; justify-content: space-between; align-items: center;'>
        <div style='display: flex; align-items: center;'>
            <img src='https://onionriverinc.streamlit.app/A_modern,_corporate-style_logo_for_a_commercial_re.png' width='60' style='margin-right: 15px;'>
            <div style='font-size: 32px; font-weight: bold;'>
                <span style='color: #2a5d84;'>▲</span> Onion River Inc.
            </div>
        </div>
        <div style='text-align: right; font-size: 14px;'>
            Michael Juniper Burke, CEO<br>
            onionriverinc@gmail.com<br>
            41 Darwin Ave., Hastings-On-Hudson, NY 10706<br>
            2930 Dugar Brook Rd., Calais, VT 05648
        </div>
    </div>
    <hr>
""", unsafe_allow_html=True)

# === SIDEBAR NAVIGATION ===
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", [
    "🏠 Home",
    "📊 Deal Analyzer",
    "📈 Rent Growth Forecast",
    "🤝 JV & Lender Contacts",
    "📈 Stock / REIT Tracker",
    "📋 About"
])

# === PAGE: HOME ===
if page == "🏠 Home":
    st.title("AI Investment Agent Dashboard")
    st.write("Welcome to Onion River Inc.'s AI-powered platform. Analyze deals, track rent trends, monitor REITs, and manage your contacts—all in one place.")

# === PAGE: DEAL ANALYZER ===
elif page == "📊 Deal Analyzer":
    st.header("Multifamily Deal Analyzer")
    purchase_price = st.number_input("Purchase Price ($)", 100000, 10000000, 1200000)
    monthly_rent = st.number_input("Monthly Rent Per Unit ($)", 500, 5000, 2200)
    units = st.number_input("Number of Units", 1, 100, 6)
    vacancy_rate = st.slider("Vacancy Rate (%)", 0.0, 10.0, 5.0)
    expenses = st.number_input("Monthly Operating Expenses ($)", 0, 50000, 4000)

    effective_gross = monthly_rent * units * (1 - vacancy_rate / 100)
    noi = effective_gross - expenses
    cap_rate = (noi * 12) / purchase_price * 100

    st.subheader("Results")
    st.write(f"**Effective Gross Income:** ${effective_gross:,.2f}/mo")
    st.write(f"**NOI:** ${noi:,.2f}/mo")
    st.write(f"**Cap Rate:** {cap_rate:.2f}%")

# === PAGE: RENT GROWTH FORECAST ===
elif page == "📈 Rent Growth Forecast":
    st.header("Rent Growth Forecast - Prosper, TX")
    base_rent = st.number_input("Current Average Rent ($)", 1000, 5000, 2962)
    annual_growth_rate = st.slider("Expected Annual Growth (%)", -5.0, 10.0, 1.5)
    years = st.slider("Forecast Horizon (years)", 1, 10, 5)

    st.subheader("Projected Rent Over Time")
    forecast = [base_rent * (1 + annual_growth_rate/100) ** year for year in range(years + 1)]
    st.line_chart(forecast)

# === PAGE: JV / LENDER CONTACTS ===
elif page == "🤝 JV & Lender Contacts":
    st.header("Preferred JV Partners & Lenders")
    st.subheader("Commercial Real Estate Agent")
    st.write("**Name:** Eagle Ledge\n**Phone:** 347-324-7140\n**Email:** onionriverinc@gmail.com")

    st.subheader("Investment Agent")
    st.write("**Name:** Log Town\n**Phone:** 347-324-7140\n**Email:** onionriverinc@gmail.com")

    st.info("Send updates to onionriverinc@gmail.com to add new contacts.")

# === PAGE: STOCK / REIT TRACKER ===
elif page == "📈 Stock / REIT Tracker":
    st.header("REIT & Dividend Stock Tracker")
    st.write("Coming soon: live REIT metrics, dividend income tracking, and market alerts using Alpha Vantage API.")
    st.success("Beta version launching Q2 2025.")

# === PAGE: ABOUT ===
elif page == "📋 About":
    st.header("About Onion River Inc.")
    st.write("""
    **Onion River Inc.** is a commercial real estate acquisitions firm focused on mid-market, value-add investments in Westchester County and Manhattan. 

    This platform is your AI-powered assistant to help with deal analysis, market intelligence, and investor/lender engagement.
    """)
