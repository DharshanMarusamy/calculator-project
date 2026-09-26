# 🧮 Flask Calculator – Jenkins CI/CD

My first project exploring **automated deployment using Jenkins**! 🚀

This is a simple web-based calculator built with Python and Flask. I developed this project to learn how to automate application testing and build processes using Jenkins, while managing source code with Git and GitHub.

## 📌 Project Overview

The Flask Calculator performs basic arithmetic operations through a simple web interface. This project demonstrates how Jenkins can automate dependency installation, testing, and build artifact archiving.

It marks my first hands-on experience with Jenkins CI/CD and deploying a Python web application.

## ✨ Features

- Basic calculator operations
- Simple web interface using HTML and CSS
- Flask backend developed with Python
- Automated testing using Pytest
- Jenkins job integrated with GitHub
- Automated dependency installation and testing
- Build artifact archiving in Jenkins
- Gunicorn application server

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Flask | Web framework |
| HTML & CSS | Frontend |
| Pytest | Automated testing |
| Jenkins | CI/CD automation |
| Git & GitHub | Version control |
| Gunicorn | Application server |

## ⚙️ CI/CD Workflow

The Jenkins job automates the following steps:

1. **Source Code Checkout:** Jenkins retrieves the application code from GitHub.
2. **Environment Setup:** Creates a Python virtual environment.
3. **Dependency Installation:** Installs packages from `requirements.txt`.
4. **Automated Testing:** Runs test cases using Pytest.
5. **Artifact Archiving:** Archives application files after a successful build.

### Jenkins Workflow

```text
GitHub Repository
       |
       v
Jenkins
       |
       v
Create Virtual Environment
       |
       v
Install Dependencies
       |
       v
Run Pytest
       |
       v
Archive Build Artifacts
```

## 🧪 Test Results

The Jenkins build successfully executed the automated tests.

```text
test_app.py::test_home_page PASSED
test_app.py::test_calculator_addition PASSED

2 passed
Finished: SUCCESS
```

## 🚀 Run the Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/DharshanMarusamy/calculator-project.git
cd calculator-project
```

### 2. Create a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
python3 -m pip install -r requirements.txt
```

### 4. Run Automated Tests

```bash
python3 -m pytest -v
```

### 5. Start the Application

```bash
python3 app.py
```

Open your browser and visit:

http://127.0.0.1:5000

## 🎯 What I Learned

Through this project, I gained practical experience with:

- Integrating Jenkins with GitHub
- Automating Python dependency installation
- Running automated tests through Jenkins
- Archiving build artifacts
- Understanding Continuous Integration (CI) and Continuous Delivery (CD)
- Running a Flask application using Gunicorn
- Troubleshooting Jenkins, Python environments, and deployment issues

## 🔮 Future Improvements

- Configure a reliable, persistent deployment process
- Automate deployment after successful tests
- Add more calculator operations and test cases
- Implement Jenkins Pipeline as Code using a `Jenkinsfile`
- Deploy the application to a cloud platform

## 👨‍💻 Author

**Dharshan Marusamy**

- GitHub: [DharshanMarusamy](https://github.com/DharshanMarusamy)

---

⭐ This is my first project exploring automated deployment with Jenkins and an important milestone in my Cloud and DevOps learning journey.
