import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="Study Planner", layout="centered")

st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 10px; background-color: #333; color: white; }
    .stCheckbox { padding: 5px; background-color: #1e1e1e; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎓 Study Tasks Planner")

# البيانات
subjects = {
    "Mathematics": 70,
    "Biology": 60,
    "Religion": 48,
    "Earth Science": 48
}

selected_sub = st.selectbox("Select Subject:", list(subjects.keys()))

# حفظ الحالة في المتصفح
if f"done_{selected_sub}" not in st.session_state:
    st.session_state[f"done_{selected_sub}"] = []

total = subjects[selected_sub]
done_list = st.session_state[f"done_{selected_sub}"]

# الإحصائيات
st.metric("Progress", f"{len(done_list)} / {total}", f"{total - len(done_list)} Remaining")
st.progress(len(done_list) / total)

st.divider()

# عرض المهام
for i in range(1, total + 1):
    cols = st.columns([0.8, 0.2])
    is_done = i in done_list
    
    with cols[0]:
        st.write(f"Task {i} {'✅' if is_done else '⏳'}")
    with cols[1]:
        if st.checkbox("", value=is_done, key=f"chk_{selected_sub}_{i}"):
            if i not in done_list:
                st.session_state[f"done_{selected_sub}"].append(i)
                st.rerun()
        else:
            if i in done_list:
                st.session_state[f"done_{selected_sub}"].remove(i)
                st.rerun()
