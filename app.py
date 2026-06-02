import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="eipdf - كل أدوات PDF", layout="wide")

# تخصيص التصميم (CSS) لجعلها تشبه البطاقات
st.markdown("""
    <style>
    .card { background-color: #f0f2f6; padding: 20px; border-radius: 15px; text-align: center; height: 200px; }
    .card:hover { background-color: #e0e2e6; cursor: pointer; }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 eipdf - كل أدواتك في مكان واحد")
st.write("أدوات سهلة ومجانية لمعالجة ملفات PDF")

# وظيفة لعرض بطاقة أداة
def show_tool_card(title, description, icon):
    st.markdown(f"""
        <div class='card'>
            <h2>{icon}</h2>
            <h3>{title}</h3>
            <p>{description}</p>
        </div>
    """, unsafe_allow_html=True)

# تقسيم الصفحة إلى أعمدة (3 أعمدة في كل صف)
col1, col2, col3 = st.columns(3)

with col1:
    show_tool_card("دمج PDF", "دمج ملفات متعددة في ملف واحد", "🔗")
    if st.button("استخدم دمج PDF"): st.session_state.tool = "دمج"

with col2:
    show_tool_card("تقسيم PDF", "استخراج صفحات محددة من الملف", "✂️")
    if st.button("استخدم تقسيم PDF"): st.session_state.tool = "تقسيم"

with col3:
    show_tool_card("تدوير الصفحات", "تغيير اتجاه صفحات PDF", "🔄")
    if st.button("استخدم تدوير PDF"): st.session_state.tool = "تدوير"

# منطق تنفيذ الأداة المختارة
if "tool" in st.session_state:
    st.write("---")
    if st.session_state.tool == "دمج":
        st.subheader("🔗 دمج الملفات")
        # هنا تضع كود الدمج الخاص بك
    elif st.session_state.tool == "تقسيم":
        st.subheader("✂️ تقسيم الملفات")
        # هنا تضع كود التقسيم الخاص بك
