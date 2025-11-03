# 🇮🇳 India Census 2011 Interactive Dashboard

An interactive web application built with **Streamlit** that visualizes district-level census data across India (2011). Users can explore, compare, and analyze census parameters for all Indian states or focus on a specific state using an interactive **Mapbox** visualization powered by **Plotly**.

👉 **Live Demo:** [Click here to explore the app](https://nihu791-india-census-2011-app-no0qlu.streamlit.app/)

## 🚀 Features

* Select any **state** or view data for **all states** at once.
* Compare two parameters simultaneously:

  * **Bubble size** represents one parameter.
  * **Color gradient** represents another parameter.
* Interactive **map-based visualization** of census data.
* Hover over districts to view detailed information.

## 🗂️ Dataset

The dashboard uses data from the **India Census 2011**, including district-level details such as population, literacy rate, area, and other socio-economic indicators.
Custom latitude and longitude centroids are used to map districts accurately on India’s map.

## 🧠 How It Works

1. Select any state from the sidebar.
2. Choose two parameters to visualize.
3. Click **Plot Map** to generate an interactive map visualization.

## 📦 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/india-census-dashboard.git
cd india-census-dashboard
pip install -r requirements.txt
```

## ▶️ Run the App

```bash
streamlit run app.py
```

## 🧰 Requirements

The project uses the following libraries:

```
streamlit
pandas
numpy
plotly
```

## 🧾 Project Overview

This dashboard was created to make census data more accessible and insightful for analysis. It helps users visualize key demographics and socio-economic indicators across Indian districts in an interactive, map-driven format.

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

**Live App:** [https://nihu791-india-census-2011-app-no0qlu.streamlit.app/](https://nihu791-india-census-2011-app-no0qlu.streamlit.app/)

**Built with:** Streamlit, Plotly, Pandas, and NumPy
