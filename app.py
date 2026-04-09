import streamlit as st
from datetime import date

# 1. إعدادات الصفحة (يجب أن يكون أول سطر)
st.set_page_config(page_title="Adam's page", layout="centered", page_icon="🤙")

# 2. التنسيق العربي وحقوق الملكية
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [data-testid="stSidebar"], .st-emotion-cache-10trblm {
        direction: RTL; text-align: right; font-family: 'Cairo', sans-serif;
    }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; color: grey; text-align: center; font-size: 12px; padding: 10px; background: rgba(255,255,255,0.8); z-index: 100; }
    .countdown-box { 
        background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%); 
        padding: 25px; 
        border-radius: 15px; 
        text-align: center; 
        color: white; 
        border: 2px solid #ff4b4b; 
        margin-bottom: 20px; 
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }
    /* تحسين مظهر الأزرار لتبدو احترافية */
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; }
    </style>
    <div class="footer">جميع الحقوق محفوظة لـ adam fayiz @mshqabi ©</div>
    """, unsafe_allow_html=True)

st.title("Adam's World 🤙")

# --- العداد التنازلي ---
target_date = date(2026, 6, 25)
today = date.today()
days_left = (target_date - today).days

if days_left > 0:
    st.markdown(f'''
        <div class="countdown-box">
            <h3 style="margin:0;">⏳ متبقي على الوزاري</h3>
            <h1 style="margin:0; color:#ff4b4b;">{days_left} يوم</h1>
        </div>
    ''', unsafe_allow_html=True)
else:
    st.balloons()
    st.success("حان وقت الإبداع! بالتوفيق في الامتحانات الوزارية 🚀")

# --- الروابط السريعة ---

# قسم الشطرنج
st.divider()
st.markdown("### ♟️ Chess Zone")
st.link_button("🎮 ابدأ اللعب (Lichess)", "https://lichess.org/repro", use_container_width=True)

# قسم عبسي Kick
st.divider()
st.markdown("### 💚 Absi on Kick")
st.link_button("🥇 دخول البث المباشر", "https://kick.com/absi", use_container_width=True)

# قسم الإنستقرام
st.divider()
st.markdown("### 📷 Instagram")
st.link_button("💤 متابعة على الإنستا", "https://www.instagram.com/mshqabi/", use_container_width=True)

# التذييل النهائي
st.divider()
st.caption("جميع الحقوق محفوظة لـ adam fayiz @mshqabi")
