Sure! Here's a brief 10-20 line description for installing and running the application using Docker Compose:

---

### Quick Start Guide for Installation

1. **Clone the Repository**: 
   First, clone the project repository using Git:
   ```bash
   git clone https://github.com/NagendraT12/fyle-interview-intern-backend.git
   cd fyle-interview-intern-backend
   ```

2. **Install Docker**: 
   If Docker isn't installed, download and install Docker from the [official site](https://www.docker.com/), and ensure Docker Desktop is running.

3. **Start Docker**: 
   Ensure Docker is up and running by checking Docker Desktop or using the `docker --version` command in the terminal.

4. **Run the Application**: 
   Use Docker Compose to build and start the application:
   ```bash
   docker-compose up
   ```

5. **Run Test Cases**: 
   To execute the test suite, use the following command. If tests fail on the first try, rerun them:
   ```bash
   docker-compose run test
   ```

6. **Stop the Application**: 
   To stop the running application, execute:
   ```bash
   docker-compose down
   ```

---

# Fyle Backend Challenge

## Who is this for?

This challenge is meant for candidates who wish to intern at Fyle and work with our engineering team. You should be able to commit to at least 6 months of dedicated time for internship.

## Why work at Fyle?

Fyle is a fast-growing Expense Management SaaS product. We are ~40 strong engineering team at the moment. 

We are an extremely transparent organization. Check out our [careers page](https://careers.fylehq.com) that will give you a glimpse of what it is like to work at Fyle. Also, check out our Glassdoor reviews [here](https://www.glassdoor.co.in/Reviews/Fyle-Reviews-E1723235.htm). You can read stories from our teammates [here](https://stories.fylehq.com).


## Challenge outline

**You are allowed to use any online/AI tool such as ChatGPT, Gemini, etc. to complete the challenge. However, we expect you to fully understand the code and logic involved.**

This challenge involves writing a backend service for a classroom. The challenge is described in detail [here](./Application.md)


## What happens next?

You will hear back within 48 hours from us via email. 


## Installation

1. Fork this repository to your github account
2. Clone the forked repository and proceed with steps mentioned below

### Install requirements

```
virtualenv env --python=python3.8
source env/bin/activate
pip install -r requirements.txt
```
### Reset DB

```
export FLASK_APP=core/server.py
rm core/store.sqlite3
flask db upgrade -d core/migrations/
```
### Start Server

```
bash run.sh
```
### Run Tests

```

Here's how to modify the installation steps for Windows:

---

### **Installation (Windows)**

1. **Fork the Repository**:
   Fork this repository to your GitHub account.

2. **Clone the Forked Repository**:
   Clone the forked repository to your local machine using Git:
   ```bash
   git clone https://github.com/<your-username>/fyle-interview-intern-backend.git
   cd fyle-interview-intern-backend
   ```

3. **Install Virtual Environment**:
   Install the required virtual environment using Python 3.8 (Make sure Python 3.8 is installed).
   In the terminal, run:
   ```bash
   virtualenv env --python=python3.8
   ```

4. **Activate Virtual Environment** (Windows):
   To activate the virtual environment on Windows, run:
   ```bash
   .\env\Scripts\activate
   ```

5. **Install Requirements**:
   Install the required Python packages by running:
   ```bash
   pip install -r requirements.txt
   ```

6. **Reset the Database**:

   a. Set the `FLASK_APP` environment variable for Windows:
   ```powershell
   $env:FLASK_APP = "core/server.py"
   ```

   b. Remove the old SQLite database (if it exists):
   ```powershell
   Remove-Item core\store.sqlite3
   ```

   c. Apply the migrations to update the database:
   ```bash
   flask db upgrade -d core/migrations/
   ```

7. **Start the Server**:
   To start the server, execute:
   ```powershell
   .\run.sh
   ```

   If `.sh` files aren't supported, you can manually run the contents of `run.sh` inside the terminal.

8. **Run Tests**:
   Run the test cases to ensure everything works:
   ```bash
   pytest -vvv -s tests/
   ```

9. **Generate Test Coverage Report**:
   For a test coverage report, run:
   ```bash
   pytest --cov
   ```

   To view the HTML coverage report, open:
   ```bash
   open htmlcov/index.html
   ```

---


pytest -vvv -s tests/

# for test coverage report
# pytest --cov
# open htmlcov/index.html
```
