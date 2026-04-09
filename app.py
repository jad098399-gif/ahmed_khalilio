import streamlit as st
from datetime import date

# إعدادات الصفحة - تأكد أنها أول سطر برمجي
st.set_page_config(page_title="Adam's page", layout="centered", page_icon="🤙")

# التنسيق العربي وحقوق الملكية
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [data-testid="stSidebar"], .st-emotion-cache-10trblm {
        direction: RTL; text-align: right; font-family: 'Cairo', sans-serif;
    }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; color: grey; text-align: center; font-size: 12px; padding: 10px; background: rgba(255,255,255,0.8); }
    .countdown-box { background-color: #1a1a1a; padding: 20px; border-radius: 15px; text-align: center; color: white; border: 2px solid #ff4b4b; margin-bottom: 20px; }
    </style>
    <div class="footer">جميع الحقوق محفوظة لـ adam fayiz @mshqabi ©</div>
    """, unsafe_allow_html=True)

st.title("nothing...")

# --- العداد التنازلي ---
target_date = date(2026, 6, 25)
days_left = (target_date - date.today()).days
if days_left > 0:
    st.markdown(f'<div class="countdown-box"><h3>⏳ متبقي على الوزاري</h3><h1>{days_left} يوم</h1></div>', unsafe_allow_html=True)


# --- زر الشطرنج الاحترافي (حل مشكلة السطر 3) ---
st.divider()
st.markdown("### ♟️ chess ")
# هذا الزر يفتح لك لوحة شطرنج 2D احترافية في صفحة جديدة دون أن يعطل موقعك
chess_url = "https://lichess.org/repro" 
st.link_button("🎮 بدأ ", chess_url, use_container_width=True)
st.caption("جميع الحقوق محفوظة لـ adam fayiz @mshqabi ")

st.divider()
st.markdown("### absi kick 💚 ")

chess_url = "https://kick.com/absi" 
st.link_button(" دخول عالبث 🥇 ", chess_url, use_container_width=True)

st.divider()

