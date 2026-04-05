import streamlit as st
from datetime import date
import base64

# إعدادات الصفحة
st.set_page_config(page_title="المعسكر النهائي 2008", layout="centered", page_icon="🔥")

# --- دالة لتحويل الصورة لـ Base64 لدمجها في CSS ---
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# الكود يحتاج لصورة متحركة (GIF) باسم 'chase.gif' في نفس المجلد على GitHub.
# سأقوم بإنشاء التصميم البكسلي لك وحفظه كـ GIF.
# حتى ترفع الصورة، سأستخدم رابطاً مثالياً لصورة بكسلية متحركة لعداء وتنين.
# استبدل الرابط أدناه برابط صورتك الـ GIF بعد رفعها على GitHub.
pixel_gif_url = "https://raw.githubusercontent.com/jad098399-gif/ahmed_khalilio/main/chase.gif"

# التنسيق العربي وحقوق الملكية وتنسيق الإشعار الجديد وصندوق العد التنازلي البكسلي
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [data-testid="stSidebar"], .st-emotion-cache-10trblm {{
        direction: RTL; text-align: right; font-family: 'Cairo', sans-serif;
        background-color: #f4f4f9;
    }}
    .footer {{ position: fixed; left: 0; bottom: 0; width: 100%; color: grey; text-align: center; font-size: 12px; padding: 10px; background: rgba(255,255,255,0.8); }}
    
    /* تنسيق صندوق العد التنازلي البكسلي المشوق */
    .countdown-box {{
        background-image: url('{pixel_gif_url}');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        border: 4px solid #333; /* إطار بكسلي داكن */
        margin-bottom: 20px;
        color: white; /* لون النص فوق الصورة */
        text-shadow: 2px 2px 4px rgba(0,0,0,0.8); /* ظل للنص لوضوحه */
        position: relative;
        overflow: hidden;
    }}
    .countdown-box h3 {{ margin: 0; font-size: 18px; font-weight: bold; }}
    .countdown-box h1 {{ margin: 10px 0; font-size: 48px; color: #ff4b4b; font-family: 'Courier New', monospace; }} /* خط مونو للرقم البكسلي */
    .countdown-box::after {{
        content: 'الوزاري 🔥 🏃‍♂️ أنت';
        position: absolute;
        bottom: 5px;
        left: 10px;
        font-size: 10px;
        color: rgba(255,255,255,0.7);
        font-family: 'Courier New', monospace;
    }}

    /* تنسيق زر الإشعار الواقعي */
    .stButton > button {{
        width: 100%;
        background-color: #ff4b4b;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 15px;
        font-weight: bold;
        font-size: 18px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: background-color 0.3s, transform 0.2s;
    }}
    .stButton > button:hover {{
        background-color: #ff3333;
        transform: scale(1.02);
    }}
    .stButton > button:active {{
        background-color: #cc0000;
        transform: scale(0.98);
    }}
    </style>
    <div class="footer">جميع الحقوق محفوظة لـ adam fayiz @mshqabi ©</div>
    """, unsafe_allow_html=True)

st.title("🔥 المعسكر النهائي 2008")

# --- إضافة العد التنازلي البكسلي المشوق ---
# تاريخ الامتحان الوزاري المتوقع لجيل 2008 (سنة ثانية)
target_date = date(2026, 6, 25) 
today = date.today()
days_left = (target_date - today).days

if days_left > 0:
    st.markdown(f"""
        <div class="countdown-box">
            <h3>👾 الهروب التوجيهي الكبير 👾</h3>
            <h3>متبقي على الهجوم الوزاري</h3>
            <h1>{days_left} يوم</h1>
        </div>
    """, unsafe_allow_html=True)
else:
    st.error("🚀 بدأت المعركة النهائية! قاتل يا وحش ⚔️")
# ----------------------------------------

# --- إضافة زر الإشعار الواقعي ---
if st.button("📞 99+ مكالمة فائتة"):
    st.warning("⚠️ الوزاري يتصل بكة :")
# -------------------------------

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

