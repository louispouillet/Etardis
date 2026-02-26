# 🚆 TARDIS Project  
*Predicting the Unpredictable*

TARDIS is a machine learning project designed to predict train delays.  
The project includes:
- 📊 Exploratory Data Analysis (EDA)
- 🤖 Model training and export
- 🌐 Interactive dashboard using Streamlit

---

# 📦 Installation Guide

Follow these steps to correctly install and run the project.

---

## 1️⃣ Create a Python Virtual Environment

### Unix / macOS
```bash
python3 -m venv .venv
```

### Windows
```bash
py -m venv .venv
```

---

## 2️⃣ Activate the Virtual Environment

### Unix / macOS
```bash
source .venv/bin/activate
```

### Windows
```bash
.venv\Scripts\activate
```

After activation, you should see `(.venv)` in your terminal.

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📊 Data Preparation

## 4️⃣ Generate the Cleaned Dataset

Open the Jupyter Notebook:

```bash
jupyter notebook
```

Then open:

```
tardis_eda.ipynb
```

Click **"Run All"** (or *Kernel → Restart & Run All*).

This will generate:

```
cleaned_dataset.csv
```

This dataset will be used to train the model.

---

# 🤖 Model Training

## 5️⃣ Train and Export the Model

Open:

```
tardis_model.ipynb
```

Click **"Run All"**.

This will:
- Train the machine learning model
- Export the trained model file
- Make it ready for the dashboard

---

# 🌐 Launch the Dashboard

## 6️⃣ Run the Streamlit App

In your terminal:

```bash
streamlit run tardis_dashboard.py
```

A browser page will automatically open.

Fill in the form and click **Predict** to get the estimated train delay.

If you don’t have some information, you can leave the default values — they are already set for convenience.

---

# 🛠 Project Structure

```
├── tardis_eda.ipynb        # Data exploration & cleaning
├── tardis_model.ipynb      # Model training & export
├── tardis_dashboard.py     # Streamlit prediction interface
├── requirements.txt        # Project dependencies
└── cleaned_dataset.csv     # Generated cleaned dataset
```

---

# ⚙️ Requirements

- Python 3.9+
- pip
- Jupyter Notebook
- Streamlit

---

# 🚀 Summary Workflow

1. Create and activate virtual environment  
2. Install dependencies  
3. Run `tardis_eda.ipynb`  
4. Run `tardis_model.ipynb`  
5. Launch `streamlit run tardis_dashboard.py`  

---

# 📌 Notes

- Make sure your virtual environment is activated before running any command.
- Always regenerate the dataset before retraining the model.
- If Streamlit does not open automatically, copy the local URL shown in the terminal and paste it into your browser.

---

✨ Enjoy predicting the unpredictable!