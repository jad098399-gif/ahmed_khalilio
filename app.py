import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="المعسكر النهائي 2008", layout="centered")

# كود CSS لتنسيق الواجهة ودعم اللغة العربية وحقوق الملكية
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [data-testid="stSidebar"], .st-emotion-cache-10trblm {
        direction: RTL;
        text-align: right;
        font-family: 'Cairo', sans-serif;
    }
    .stMetric { text-align: right; }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: transparent;
        color: grey;
        text-align: center;
        font-size: 12px;
        padding: 10px;
    }
    </style>
    <div class="footer">
        جميع الحقوق محفوظة لـ adam fayiz @mshqabi ©
    </div>
    """, unsafe_allow_html=True)

st.title("🔥 المعسكر النهائي 2008")

# تعريف المواد مع عدد المهام والاختصار الخاص بكل مادة
subjects_info = {
    "الرياضيات": {"total": 70, "prefix": "ADV"},
    "الأحياء": {"total": 60, "prefix": "BIO"},
    "علوم الأرض": {"total": 48, "prefix": "GEO"},
    "التربية الإسلامية": {"total": 48, "prefix": "ISL"}
}

selected_sub = st.selectbox("اختر المادة لتفقد المهام:", list(subjects_info.keys()))

# جلب بيانات المادة المختارة
prefix = subjects_info[selected_sub]["prefix"]
total_tasks = subjects_info[selected_sub]["total"]

# حفظ حالة الإنجاز في ذاكرة المتصفح
if f"done_{selected_sub}" not in st.session_state:
    st.session_state[f"done_{selected_sub}"] = []

done_list = st.session_state[f"done_{selected_sub}"]

# الإحصائيات
st.metric("نسبة الإنجاز في " + selected_sub, f"{len(done_list)} من {total_tasks}", f"متبقي {total_tasks - len(done_list)}")
st.progress(len(done_list) / total_tasks)

st.divider()

# عرض المهام بالاختصارات الجديدة (مثلاً ADV 1, BIO 1)
for i in range(1, total_tasks + 1):
    cols = st.columns([0.8, 0.2])
    task_name = f"{prefix} {i}"
    is_done = i in done_list
    
    with cols[0]:
        # عرض اسم المهمة بالاختصار
        st.write(f"**{task_name}** {'✅' if is_done else '⏳'}")
    with cols[1]:
        if st.checkbox("", value=is_done, key=f"chk_{prefix}_{i}"):
            if i not in done_list:
                st.session_state[f"done_{selected_sub}"].append(i)
                st.rerun()
        else:
            if i in done_list:
                st.session_state[f"done_{selected_sub}"].remove(i)
                st.rerun()
