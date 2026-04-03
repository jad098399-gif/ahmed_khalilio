import streamlit as st
from streamlit_javascript import st_javascript
import json

# إعدادات الصفحة
st.set_page_config(page_title="المعسكر النهائي 2008", layout="centered")

# كود التنسيق ودعم العربية وحقوق الملكية
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [data-testid="stSidebar"], .st-emotion-cache-10trblm {
        direction: RTL;
        text-align: right;
        font-family: 'Cairo', sans-serif;
    }
    .footer {
        position: fixed; left: 0; bottom: 0; width: 100%;
        color: grey; text-align: center; font-size: 12px; padding: 10px;
    }
    </style>
    <div class="footer">جميع الحقوق محفوظة لـ adam fayiz @mshqabi ©</div>
    """, unsafe_allow_html=True)

st.title("🔥 المعسكر النهائي 2008")

subjects_info = {
    "الرياضيات": {"total": 70, "prefix": "ADV"},
    "الأحياء": {"total": 60, "prefix": "BIO"},
    "علوم الأرض": {"total": 48, "prefix": "GEO"},
    "التربية الإسلامية": {"total": 48, "prefix": "ISL"}
}

selected_sub = st.selectbox("اختر المادة:", list(subjects_info.keys()))
prefix = subjects_info[selected_sub]["prefix"]
total_tasks = subjects_info[selected_sub]["total"]

# --- كود الحفظ الذكي (LocalStorage) ---
# جلب البيانات المحفوظة من متصفح الطالب
storage_key = f"tasks_storage_2008"
saved_data = st_javascript(f"parent.localStorage.getItem('{storage_key}')")

if f"done_dict" not in st.session_state:
    st.session_state.done_dict = {}

# تحديث الذاكرة المؤقتة من المتصفح
if saved_data and saved_data != "null":
    try:
        st.session_state.done_dict = json.loads(saved_data)
    except:
        pass

if selected_sub not in st.session_state.done_dict:
    st.session_state.done_dict[selected_sub] = []

done_list = st.session_state.done_dict[selected_sub]

# الإحصائيات
st.metric(f"إنجاز {selected_sub}", f"{len(done_list)} من {total_tasks}")
st.progress(len(done_list) / total_tasks)
st.divider()

# عرض المهام وحفظها فورياً عند الضغط
for i in range(1, total_tasks + 1):
    cols = st.columns([0.8, 0.2])
    task_id = i
    is_done = task_id in done_list
    
    with cols[0]:
        st.write(f"**{prefix} {i}** {'✅' if is_done else '⏳'}")
    with cols[1]:
        if st.checkbox("", value=is_done, key=f"c_{prefix}_{i}"):
            if task_id not in done_list:
                st.session_state.done_dict[selected_sub].append(task_id)
                # حفظ في متصفح الموبايل فوراً
                js_save = f"parent.localStorage.setItem('{storage_key}', '{json.dumps(st.session_state.done_dict)}')"
                st_javascript(js_save)
                st.rerun()
        else:
            if task_id in done_list:
                st.session_state.done_dict[selected_sub].remove(task_id)
                js_save = f"parent.localStorage.setItem('{storage_key}', '{json.dumps(st.session_state.done_dict)}')"
                st_javascript(js_save)
                st.rerun()
