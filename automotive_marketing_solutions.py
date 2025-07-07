import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="DigitalDrive by Rut",
    page_icon="logo_ams.png",  # Logo como icono de pestaña
    layout="centered"
)

# Mostrar logo en la cabecera
st.image("logo_ams.png", width=200)

# Título y subtítulo principal
st.title("DigitalDrive by Rut")
st.subheader("Soluciones digitales para el sector de la automoción")
st.markdown("---")

# Menú lateral
menu = st.sidebar.radio("Explora los servicios", ["Inicio", "Paneles y Datos", "Email Marketing", "Automatización de Procesos"])

# Sección: INICIO
if menu == "Inicio":
    col1, col2 = st.columns([1, 2])  # Imagen a la izquierda, texto a la derecha

    with col1:
        st.image("automotive_mkt_solutions.png", width=200)  # Asegúrate del formato correcto

    with col2:
        st.markdown("""
        ### ¡Hola! Soy **Rut**,  
        experta en soluciones digitales enfocadas en el mundo de la automoción 🚗💻

        Ayudo a empresas y autónomos del sector a:
        - Optimizar procesos
        - Analizar datos con claridad
        - Mejorar su comunicación digital con campañas efectivas

        Mi enfoque es práctico, directo y totalmente personalizado.
        """)

# Sección: PANELES Y DATOS
elif menu == "Paneles y Datos":
    st.header("📊 Paneles y Seguimiento de Datos")
    st.markdown("""
    - Creación de paneles personalizados con Excel, Google Sheets o CRMs.
    - Integración con plataformas como **Salesforce** o **HubSpot**.
    - Informes visuales e interactivos adaptados a tus necesidades.
    - Ideal para equipos de ventas, dirección o gestión de flotas.
    """)

# Sección: EMAIL MARKETING
elif menu == "Email Marketing":
    st.header("💌 Email Marketing & Base de Datos")
    st.markdown("""
    - Diseño de campañas impactantes con herramientas como **Mailchimp**, **Brevo** o integraciones personalizadas.
    - Alimentación y segmentación de bases de datos.
    - Calendarios editoriales y automatizaciones.
    - Métricas clave para evaluar resultados: aperturas, clics, conversiones.
    """)

# Sección: AUTOMATIZACIÓN
elif menu == "Automatización de Procesos":
    st.header("⚙️ Automatización de Procesos")
    st.markdown("""
    - Automatización de tareas repetitivas con **Zapier**, **Power Automate** o scripts propios.
    - Aplicaciones personalizadas de escritorio o en la nube.
    - Optimización de flujos complejos en el área comercial, postventa o administración.
    - Ahorro de tiempo, reducción de errores y mayor control.
    """)

# Pie de página
st.markdown("---")
st.markdown("📬 Contacto: rut.marketingautomocion@gmail.com | Instagram: @aun_noexiste_pero_sevienen_cositas | Madrid, España")
