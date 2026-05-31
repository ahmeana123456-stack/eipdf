import streamlit as st
from pypdf import PdfReader, PdfWriter
import io

st.title("موقع eipdf - أدوات PDF")

# القائمة الجانبية لتطوير الموقع
menu = st.sidebar.selectbox("اختر أداة", ["دمج ملفات PDF", "تقسيم PDF"])

# أداة الدمج
if menu == "دمج ملفات PDF":
    st.header("أداة دمج ملفات PDF")
    uploaded_files = st.file_uploader("اختر ملفات PDF لدمجها", accept_multiple_files=True, type=['pdf'])
    if st.button("دمج الملفات"):
        if uploaded_files:
            writer = PdfWriter()
            for file in uploaded_files:
                writer.append(file)
            output = io.BytesIO()
            writer.write(output)
            st.success("تم الدمج!")
            st.download_button("تحميل الملف المدمج", output.getvalue(), "merged.pdf", "application/pdf")

# أداة التقسيم (جديدة!)
elif menu == "تقسيم PDF":
    st.header("أداة تقسيم PDF")
    uploaded_file = st.file_uploader("ارفع ملف PDF لتقسيمه", type=['pdf'])
    page_number = st.number_input("اكتب رقم الصفحة التي تريد استخراجها", min_value=1, step=1)
    
    if st.button("تقسيم الصفحة"):
        if uploaded_file:
            reader = PdfReader(uploaded_file)
            writer = PdfWriter()
            writer.add_page(reader.pages[page_number - 1])
            output = io.BytesIO()
            writer.write(output)
            st.success(f"تم استخراج الصفحة رقم {page_number}")
            st.download_button("تحميل الصفحة", output.getvalue(), f"page_{page_number}.pdf", "application/pdf")
