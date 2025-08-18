# 🚗 Vehículos Usados - Visualización Interactiva con Streamlit

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit" />
  <img src="https://img.shields.io/badge/Status-En%20Desarrollo-yellow?style=for-the-badge" />
</div>

---

## 📌 Descripción del Proyecto

🎯 El objetivo de esta aplicación es visualizar datos de anuncios de **vehículos usados** a través de gráficos interactivos creados con `plotly-express` y presentados mediante `Streamlit`.

<pre><code><b>¡Con solo un clic puedes explorar el odómetro, el precio y mucho más!</b></code></pre>

---

## 🧰 Tecnologías utilizadas

| Herramienta     | Uso principal                         |
|------------------|----------------------------------------|
| 🐍 Python        | Lenguaje principal del proyecto        |
| 📊 pandas        | Manejo de datos tabulares              |
| 📈 plotly-express | Visualización de datos interactiva     |
| 🌐 Streamlit     | Desarrollo de la interfaz web          |

---

## 🚀 ¿Qué puedes hacer en esta app?

✅ Visualizar **histogramas** del odómetro  
✅ Explorar un **gráfico de dispersión** entre odómetro y precio  
✅ Interactuar fácilmente con **casillas de verificación**  
✅ Ejecutar la aplicación local o desplegarla online

---

## 📷 Vista previa de la app

> 💡 Interfaz simple e intuitiva para visualizar los datos con un clic

<img src="https://user-images.githubusercontent.com/placeholder/demo-screenshot.png" width="600"/>

---

## 🛠️ Cómo ejecutar el proyecto localmente

1. 🔽 Clona el repositorio:
   ```bash
   git clone https://github.com/TU_USUARIO/NOMBRE_DEL_REPO.git
   cd NOMBRE_DEL_REPO
🧪 Crea un entorno virtual:

bash
Copiar
Editar
python -m venv vehicles_env
source vehicles_env/bin/activate  # En Windows: vehicles_env\Scripts\activate
📦 Instala las dependencias:

bash
Copiar
Editar
pip install -r requirements.txt
▶️ Ejecuta la aplicación:

bash
Copiar
Editar
streamlit run app.py
🌍 Despliegue en línea
🟢 La aplicación está desplegada en Render.com
🔗 Enlace de la app: https://<TU_APP>.onrender.com/

📁 Estructura del Proyecto
bash
Copiar
Editar
.
├── app.py                  # Código principal de la app Streamlit
├── vehicles_us.csv         # Dataset utilizado
├── requirements.txt        # Librerías requeridas
├── README.md               # Este archivo
└── notebooks/
    └── EDA.ipynb           # Exploración de datos con Jupyter

