import streamlit as st

st.set_page_config(page_title="eipdf - منصة أدوات PDF", layout="wide")

# CSS لتجميل البطاقات
st.markdown("""
    <style>
    .card { background-color: #f8f9fa; padding: 20px; border-radius: 10px; border: 1px solid #ddd; text-align: center; }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 eipdf - أدوات PDF المجانية")
st.write("---")

# تقسيم الصفحة لأعمدة لعرض الأدوات كبطاقات
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='card'><h3>🔗 دمج</h3><p>دمج عدة ملفات في ملف واحد</p></div>", unsafe_allow_html=True)
    if st.button("اذهب لدمج ملفات"): st.session_state.page = "دمج"

with col2:
    st.markdown("<div class='card'><h3>✂️ تقسيم</h3><p>استخراج صفحات من PDF</p></div>", unsafe_allow_html=True)
    if st.button("اذهب لتقسيم ملفات"): st.session_state.page = "تقسيم"

with col3:
    st.markdown("<div class='card'><h3>🔄 تدوير</h3><p>تدوير صفحات ملف PDF</p></div>", unsafe_allow_html=True)
    if st.button("اذهب لتدوير الملف"): st.session_state.page = "تدوير"

# منطق التنقل بين الأدوات
if "page" not in st.session_state: st.session_state.page = "الرئيسية"

# هنا نضع كود الأدوات بناءً على الصفحة المختارة (نفس المنطق القديم)
