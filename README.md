#  Quantium Software Engineering Job Simulation

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Dash](https://img.shields.io/badge/Dash-2.18.2-008DE4?style=for-the-badge&logo=plotly&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.2.3-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-5.24.1-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-8.3.5-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

<br/>

> **Quantium × Forage** — A complete data engineering and visualisation project built for Soul Foods to analyse the impact of a Pink Morsel price increase on sales.

<br/>

![App Preview](quantium-soul-foods/quantium-soul-foods/preview.png)

</div>

---

## 📌 Project Overview

Soul Foods wanted to answer one key business question:

> *"Were sales higher before or after the Pink Morsel price increase on 15th January 2021?"*

This project processes raw transaction data and visualises it through an interactive Dash web application — making the answer immediately obvious.

---

## 🗂️ Project Structure

```
quantium-soul-foods/
├── data/
│   ├── daily_sales_data_0.csv
│   ├── daily_sales_data_1.csv
│   ├── daily_sales_data_2.csv
│   └── processed_data.csv
├── tests/
│   └── test_app.py
├── app.py
├── process_data.py
├── run_tests.sh
├── requirements.txt
└── preview.png
```

---

## ⚙️ Tasks Completed

| Task | Description |
|------|-------------|
| ✅ Task 1 | Set up local dev environment with Python virtual environment |
| ✅ Task 2 | Data processing — merged CSVs, filtered Pink Morsel, computed sales |
| ✅ Task 3 | Built Dash app with line chart visualisation |
| ✅ Task 4 | Added region radio filter + CSS styling |
| ✅ Task 5 | Wrote 3 Pytest tests for header, chart and region picker |
| ✅ Bonus  | CI bash script to automate test execution |

---

## 🚀 Getting Started

**1. Clone the repo**
```bash
git clone https://github.com/aniketlabs77/Quantium-Software-Engineering-Job-Simulation-.git
cd Quantium-Software-Engineering-Job-Simulation-
```

**2. Create and activate virtual environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
pip install "dash[testing]"
```

**4. Process the data**
```bash
python process_data.py
```

**5. Run the app**
```bash
python app.py
```

Open your browser at **http://localhost:8050**

---

## 🧪 Running Tests

```bash
pytest tests/
```

Or use the CI bash script:
```bash
bash run_tests.sh
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Pandas | Data processing |
| Dash | Web app framework |
| Plotly | Interactive charts |
| Pytest | Automated testing |
| Bash | CI scripting |
| Git | Version control |

---

## 📊 Key Insight

The line chart clearly shows that **sales were higher before the price increase** on January 15, 2021. After the price increase from **$2.99 → $3.99**, daily Pink Morsel sales dropped noticeably — giving Soul Foods a clear, data-backed answer.

---

<div align="center">

**Completed as part of the Quantium Software Engineering Virtual Experience on Forage**

</div>
