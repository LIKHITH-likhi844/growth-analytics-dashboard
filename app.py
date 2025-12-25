import streamlit as st
import pandas as pd

st.set_page_config(page_title="Growth Analytics Dashboard", layout="wide")

st.title("📈 Growth Analytics Dashboard")
st.caption("Built for tracking acquisition, conversion & funnel performance")

# Sample growth data
data = pd.DataFrame({
    "Channel": ["Google Ads", "Facebook Ads", "Organic", "Referral"],
    "Visits": [1200, 950, 1600, 700],
    "Leads": [240, 190, 320, 140],
    "Conversions": [96, 76, 144, 49]
})

data["Lead Conversion Rate (%)"] = (data["Leads"] / data["Visits"]) * 100
data["Final Conversion Rate (%)"] = (data["Conversions"] / data["Visits"]) * 100

st.subheader("📊 Channel Performance")
st.dataframe(data)

st.subheader("📈 Conversion Rate by Channel")
st.bar_chart(
    data.set_index("Channel")[["Lead Conversion Rate (%)", "Final Conversion Rate (%)"]]
)

st.subheader("🧠 Insights")
st.markdown("""
- Organic traffic has the **highest conversion rate**
- Paid channels can be optimized through **better targeting and creatives**
- Funnel drop-offs can be reduced with **landing page A/B testing**
""")
