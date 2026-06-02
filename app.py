import streamlit as st
from pypdf import PdfReader, PdfWriter
import io

# إعداد الصفحة لتكون باسم eipdf
st.set_page_config(page_title="eipdf - منصة أدوات PDF", layout="centered")

st.markdown("""
    <h1 style='text-align: center; color: #ff4b4b;'>🚀 منصة eipdf</h1>
    <p style='text-align: center;'>كل أدوات الـ PDF التي تحتاجها في مكان واحد</p>
    <hr>
""", unsafe_allow_html=True)

# القائمة الجانبية باسم eipdf
menu = st.sidebar.radio("📋 أدوات eipdf", ["الرئيسية", "دمج ملفات", "تقسيم ملفات", "تدوير الصفحات"])

if menu == "الرئيسية":
    st.info("💡 اختر أداة من القائمة الجانبية للبدء.")
    st.write("مرحباً بك في eipdf، منصتك المتكاملة لمعالجة ملفات الـ PDF بسرعة وسهولة.")

elif menu == "دمج ملفات":
    st.subheader("🔗 دمج ملفات PDF")
    files = st.file_uploader("ارفع الملفات", accept_multiple_files=True, type=['pdf'])
    if st.button("دمج الملفات"):
        if files:
            writer = PdfWriter()
            for f in files: writer.append(f)
            output = io.BytesIO()
            writer.write(output)
            st.success("تم الدمج بنجاح!")
            st.download_button("تحميل الملف المدمج", output.getvalue(), "merged.pdf", "application/pdf")

elif menu == "تقسيم ملفات":
    st.subheader("✂️ تقسيم ملفات PDF")
    file = st.file_uploader("ارفع الملف", type=['pdf'])
    page_num = st.number_input("رقم الصفحة المطلوبة", min_value=1, step=1)
    if st.button("استخراج الصفحة"):
        if file:
            reader = PdfReader(file)
            writer = PdfWriter()
            writer.add_page(reader.pages[page_num-1])
            output = io.BytesIO()
            writer.write(output)
            st.download_button("تحميل الصفحة", output.getvalue(), f"page_{page_num}.pdf", "application/pdf")

elif menu == "تدوير الصفحات":
    st.subheader("🔄 تدوير ملفات PDF")
    file = st.file_uploader("ارفع الملف", type=['pdf'])
    angle = st.selectbox("اختر الزاوية", [90, 180, 270])
    if st.button("تدوير الملف"):
        if file:
            reader = PdfReader(file)
            writer = PdfWriter()
            for page in reader.pages:
                page.rotate(angle)
                writer.add_page(page)
            output = io.BytesIO()
            writer.write(output)
            st.download_button("تحميل الملف المدور", output.getvalue(), "rotated.pdf", "application/pdf")
