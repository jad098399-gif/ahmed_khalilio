import streamlit as st
from datetime import date

# إعدادات الصفحة
st.set_page_config(page_title="المعسكر النهائي 2008", layout="centered")

# التنسيق العربي وحقوق الملكية
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [data-testid="stSidebar"], .st-emotion-cache-10trblm {
        direction: RTL; text-align: right; font-family: 'Cairo', sans-serif;
    }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; color: grey; text-align: center; font-size: 12px; padding: 10px; }
    .countdown-box { background-color: #f0f2f6; padding: 15px; border-radius: 10px; text-align: center; border: 1px solid #ff4b4b; margin-bottom: 20px; }
    </style>
    <div class="footer">جميع الحقوق محفوظة لـ adam fayiz @mshqabi ©</div>
    """, unsafe_allow_html=True)

st.title("🔥 المعسكر النهائي 2008")

# --- إضافة العد التنازلي ---
target_date = date(2026, 6, 25)
today = date.today()
days_left = (target_date - today).days

if days_left > 0:
    st.markdown(f"""
        <div class="countdown-box">
            <h3 style="margin:0; color: #31333F;">ضايل الوزاري 💀</h3>
            <h1 style="margin:0; color: #ff4b4b;">{days_left} يوم</h1>
        </div>
    """, unsafe_allow_html=True)
else:
    st.error("🚀 بدأت الامتحانات! بالتوفيق يا وحش")
# --------------------------

subjects_info = {
    "الرياضيات": {"total": 70, "prefix": "ADV"},
    "الأحياء": {"total": 60, "prefix": "BIO"},
    "علوم الأرض": {"total": 48, "prefix": "GEO"},
    "التربية الإسلامية": {"total": 48, "prefix": "ISL"}
}

selected_sub = st.selectbox("اختر المادة:", list(subjects_info.keys()))
prefix = subjects_info[selected_sub]["prefix"]
total_tasks = subjects_info[selected_sub]["total"]

# استخدام Query Params للحفظ في الرابط
if f"done_{selected_sub}" not in st.session_state:
    # محاولة جلب البيانات من الرابط إذا وجدت
    query_data = st.query_params.get_all(f"d_{prefix}")
    st.session_state[f"done_{selected_sub}"] = [int(x) for x in query_data] if query_data else []

done_list = st.session_state[f"done_{selected_sub}"]

# الإحصائيات
st.metric(f"إنجاز {selected_sub}", f"{len(done_list)} من {total_tasks}")
st.progress(len(done_list) / total_tasks)


st.divider()

# عرض المهام
for i in range(1, total_tasks + 1):
    cols = st.columns([0.8, 0.2])
    is_done = i in done_list
    with cols[0]:
        st.write(f"**{prefix} {i}** {'✅' if is_done else '⏳'}")
    with cols[1]:
        if st.checkbox("", value=is_done, key=f"chk_{prefix}_{i}"):
            if i not in done_list:
                done_list.append(i)
                st.query_params[f"d_{prefix}"] = done_list
                st.rerun()
        else:
            if i in done_list:
                done_list.remove(i)
                st.query_params[f"d_{prefix}"] = done_list
                st.rerun()
