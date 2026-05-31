import streamlit as st
from pypdf import PdfWriter
import io

st.title("موقع eipdf - أدوات PDF")

# القائمة الجانبية
menu = st.sidebar.selectbox("اختر أداة", ["دمج ملفات PDF"])

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
            
            st.success("تم الدمج بنجاح!")
            st.download_button("تحميل الملف المدمج", output.getvalue(), "merged.pdf", "application/pdf")
        else:
            st.error("يرجى اختيار ملفات أولاً!")
