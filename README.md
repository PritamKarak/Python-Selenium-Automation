# Final Project and Assignment Submission - Wipro Python Automation

This repository contains the complete coursework, practical assignments, lab exercises, and final project completed as part of the **Wipro Python Automation Training Program**. It demonstrates the progression from Python programming fundamentals to web UI automation, BDD-based testing, Robot Framework, and REST API automation.

---

## 📂 Repository Structure

The repository is divided into two primary sections: progressive learning **Assignments** and the **Final Project**.

### 1. Assignments

The `Assignments/` directory contains the practical assignments and lab exercises completed throughout the Wipro Python Automation training program. These assignments cover Python programming, Selenium WebDriver, BDD, Page Object Model, and Robot Framework concepts.

- **`Module 1/`**: Python programming assignments and Jupyter Notebooks covering fundamental programming concepts, problem-solving, data structures, functions, exception handling, and object-oriented programming.

- **`Module 2/`**: Web UI automation assignments using Python and Selenium WebDriver. Includes browser automation, web element handling, form interactions, validations, and data-driven testing.

- **`Module 3/`** (`Module3_BDD_Lab`): Behavior-Driven Development (BDD) implementation using the Behave framework. Includes Gherkin feature files, step definitions, environment configuration, and Page Object Model (POM) implementation.

- **`Module 4/`** (`Module4_Robot_Framework`): Keyword-driven test automation using the Robot Framework. Includes Robot Framework test cases, custom Python keywords, data-driven testing, and automated execution and reporting.

These assignments demonstrate the progression from **Python programming fundamentals to structured web automation and test automation frameworks**.

---

### 2. Final Project - : Python API Automation Framework with Requests + Behave BDD

The `Project/` directory contains the final **REST API Automation Framework** developed using Python, Requests, Behave BDD, and Allure Reporting.

The framework is designed to automate positive and negative API scenarios while providing reusable API clients, centralized configuration, response validation, logging, API execution evidence, and detailed Allure reporting.

#### 🛠️ Technologies Used

- **Python** - Core programming language
- **Requests** - REST API communication
- **Behave** - Behavior-Driven Development (BDD)
- **Allure** - Test reporting and execution results
- **JSON** - API data and schema handling
- **Pillow** - API execution evidence generation
- **Git/GitHub** - Version control

#### 📁 Core Framework Components

- **`config/`**: Contains configuration files used for managing API settings and environment-related configurations.

- **`features/`**: Contains Gherkin feature files and BDD test scenarios for authentication, user management, and negative API testing.

- **`framework/`**: Contains reusable framework components such as the API client and configuration reader.

- **`schemas/`**: Contains JSON schemas used for API validation.

- **`test_data/`**: Contains test data required by the API test scenarios.

- **`utils/`**: Contains reusable utility functions used by the automation framework.

- **`scripts/`**: Contains supporting scripts used for project execution and automation.

- **`behave.ini`**: Contains configuration settings for the Behave test runner.

- **`requirements.txt`**: Contains the Python dependencies required to install and execute the framework.

---

## 🧪 API Test Scenarios

The final project includes automated API scenarios covering authentication, user management, and negative testing.

### Authentication

- Verify login with a dynamically registered user
- Verify login with invalid credentials
- Verify login without an email parameter
- Verify login using an unsupported HTTP method
- Update a registered user's account
- Get a registered user's account details

### User Management

- Create a new user
- Delete a user
- Get all users successfully
- Get a user by valid ID
- Get a user that does not exist
- Update a user using PUT
- Partially update a user using PATCH

### Negative Scenarios

- Unsupported POST method for products list
- Search product without required parameter
- Unsupported PUT method for brands list

