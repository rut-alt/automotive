import streamlit as st

# Configuración inicial
st.set_page_config(page_title="DigitalDrive by Rut", page_icon="logo_ams.png", layout="centered")

# Mostrar el logo en la parte superior
st.image("logo_ams.png", width=200)  # Ajusta el ancho si lo ves muy grande o pequeño

# Títulos principales
st.title("DigitalDrive by Rut")
st.subheader("Soluciones digitales para el sector de la automoción")

st.markdown("---")

# Menú lateral
menu = st.sidebar.radio("Explora los servicios", ["Inicio", "Paneles y Datos", "Email Marketing", "Automatización de Procesos"])

# Contenido según la opción elegida
if menu == "Inicio":
    st.markdown("""
    Soy Rut, experta en soluciones digitales enfocadas en el mundo de la automoción.
    
    Ayudo a empresas y autónomos del sector a optimizar sus procesos, analizar sus datos y mejorar su comunicación digital 🚀.
    """)

elif menu == "Paneles y Datos":
    st.header("📊 Paneles y Seguimiento de Datos")
    st.markdown("""
    - Creación de paneles personalizados con Excel, Google Sheets o CRMs.
    - Integración con plataformas como **Salesforce** o **HubSpot**.
    - Informes visuales e interactivos adaptados a tus necesidades.
    - Ideal para equipos de ventas, dirección o gestión de flotas.
    """)

elif menu == "Email Marketing":
    st.header("💌 Email Marketing & Base de Datos")
    st.markdown("""
    - Diseño de campañas impactantes con herramientas como **Mailchimp**, **Brevo** o integraciones personalizadas.
    - Alimentación y segmentación de bases de datos.
    - Calendarios editoriales y automatizaciones.
    - Métricas clave para evaluar resultados: aperturas, clics, conversiones.
    """)

elif menu == "Automatización de Procesos":
    st.header("⚙️ Automatización de Procesos")
    st.markdown("""
    - Automatización de tareas repetitivas con **Zapier**, **Power Automate** o scripts propios.
    - Aplicaciones personalizadas de escritorio o en la nube.
    - Optimización de flujos complejos en el área comercial, postventa, o administración.
    - Ahorro de tiempo, reducción de errores y mayor control.
    """)

# Pie de página
st.markdown("---")
st.markdown("📬 Contacto: rut@tudominio.com | Instagram: @rut_digitaldrive | Madrid, España")
