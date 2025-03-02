# **Random Word Generator app**
implementing test automation on a random word generator app, including vowels check of EXACTLY 100 generated words list

## **Table of Contents**
1. [Introduction](#introduction)  
2. [Project Overview](#project-overview)  
3. [Features](#features)  
4. [Installation](#installation)    
5. [Development](#development)  
  
---

## **1. Introduction**
This project is a **Flask-based Random Word Generator** that fetches words from an external API, processes them to add random special characters, and displays them in a user-friendly web interface. It also includes **comprehensive automated tests** to validate functionality, including vowel checking.

---

## **2. Project Overview**
The Random Word Generator app:
- Provides a **Flask server** that interacts with an external API to fetch random words.
- **Generates words or phrases** and randomly inserts special characters.
- Allows users to click a button and dynamically fetch words.
- Includes **API testing and UI automation** with **pytest** and **Playwright**.

### **Tech Stack**
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS
- **Testing:** Pytest, Playwright
- **Automation:** Mock API calls, browser interaction, functional validation

---

## **3. Features**
✅ **Random Word Generation** – Fetches words from an external API.  
✅ **Random Special Characters** – Inserts special characters dynamically.  
✅ **Automatic Flask Server Check and execution** – Ensures the Flask server is running before executing tests.  
✅ **UI Button Interaction** – Allows users to generate words via a button click.  
✅ **Automated Testing** – Includes **functional, API, and 100 words that contains vowels**.  
✅ **Mocked API Calls** – Uses **unittest.mock** to simulate API responses.  
✅ **CI/CD Ready** – Can be integrated into continuous deployment workflows.  

---

## **4. Installation**
### **Prerequisites**
- Python 3.8+
- pip (Python package manager)
- Playwright for UI testing
- A virtual environment (recommended)

### **Setup Instructions**
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/random-word-generator.git
   cd random-word-generator 
   ```

2. **Create and activate a virtual environment** 
python -m venv venv

source venv/bin/activate

3. **Install the project dependencies**
pip install -r requirements.txt


4. ### **Run All Tests**
To execute all test cases one by one, use the following command:
```bash
pytest tests/

```
## Project Structure

```bash
random-word-generator/
│── random_word_app.py     # Main Flask app
│── templates/
│   └── index.html         # Web interface
│── requirements.txt       # Dependencies
│── README.md              # Documentation
│── tests/
│   ├── conftest.py        # Pytest fixtures & test setup for ui client, api and for automated server startup
│   ├── test_app_vowels.py # Tests for vowels and 100 words generation
```

## **5. Development**
**Key Components**:

``` random_word_app.py ```: Flask server that fetches and modifies words. 

```tests/conftest.py```: Centralized pytest fixtures and automated app server execution and tierdown for the test.

```tests/test_app_vowels.py```: Automated API test,and vowel verification of 100 generated words and with length above 3.

```templates/index.html```: UI with a button to generate words dynamically from an external API.



