import streamlit as st
from datetime import date
from streamlit_chess import chess

# إعدادات الصفحة
st.set_page_config(page_title="المعسكر النهائي 2008", layout="centered", page_icon="🔥")

# التنسيق العربي
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [data-testid="stSidebar"], .st-emotion-cache-10trblm {
        direction: RTL; text-align: right; font-family: 'Cairo', sans-serif;
    }
    .countdown-box { background-color: #1a1a1a; padding: 20px; border-radius: 15px; text-align: center; color: white; border: 2px solid #ff4b4b; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔥 المعسكر النهائي 2008")

# العداد التنازلي
target_date = date(2026, 6, 25)
days_left = (target_date - date.today()).days
st.markdown(f'<div class="countdown-box"><h3>⏳ متبقي على الوزاري</h3><h1>{days_left} يوم</h1></div>', unsafe_allow_html=True)

# زر الشطرنج
if "play" not in st.session_state: st.session_state.play = False
if st.button("🎮 اضغط للعب الشطرنج"):
    st.session_state.play = not st.session_state.play

if st.session_state.play:
    st.markdown("### ♟️ لوحة التحدي (2D)")
    chess(key="my_chess")

st.divider()

# كود المهام (الرياضيات، الأحياء...)
subjects = {"الرياضيات": 70, "الأحياء": 60, "علوم الأرض": 48, "التربية الإسلامية": 48}
sel = st.selectbox("اختر المادة:", list(subjects.keys()))
total = subjects[sel]

if f"d_{sel}" not in st.session_state: st.session_state[f"d_{sel}"] = []
done = st.session_state[f"d_{sel}"]

st.metric(f"إنجاز {sel}", f"{len(done)} من {total}")
st.progress(len(done)/total)

# عرض أول 10 مهام كمثال للتجربة
for i in range(1, 11):
    if st.checkbox(f"مهمة {i}", value=(i in done), key=f"{sel}_{i}"):
        if i not in done: 
            done.append(i)
            st.rerun()
