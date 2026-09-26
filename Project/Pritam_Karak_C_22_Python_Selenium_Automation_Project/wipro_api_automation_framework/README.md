# Enterprise User Management API Automation Framework

##  Features

- BDD-based API automation using Behave
- Reusable API client implementation
- Positive and negative API test scenarios
- HTTP status code validation
- Request and response validation
- JSON schema support
- Centralized configuration management
- Environment variable support
- Logging of test execution
- API request/response evidence
- Allure test reporting
- API execution screenshots/evidence
- Modular and maintainable project structure

---

##  Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming language |
| Behave | BDD test framework |
| Requests | HTTP API communication |
| Allure | Test reporting |
| Pytest/Python utilities | Supporting test utilities |
| Pillow | API evidence screenshot generation |
| JSON | Request, response and test data handling |
| Git/GitHub | Version control |

## APIs

### JSONPlaceholder
Base URL: https://jsonplaceholder.typicode.com

Used for user retrieval and CRUD-style API response validation.

### Automation Exercise
Base URL: https://automationexercise.com

Used for authentication and user-account lifecycle testing.

> JSONPlaceholder is a fake API. Its POST/PUT/PATCH/DELETE operations simulate server changes rather than persisting them. The framework therefore validates the response contract instead of claiming persistent state changes.

## Architecture

Feature files -> Behave step definitions -> reusable API client -> REST API -> validators/logging -> Allure report.

## Project Structure

```text
config/          Configuration
features/        BDD feature files and step definitions
framework/       Reusable API framework components
schemas/         JSON response schemas
test_data/       External sample data
utils/           Data generation and reporting helpers
scripts/         Test execution/cleanup helpers
logs/            Runtime logs
allure-results/  Generated Allure data
```

## Setup

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
cp .env.example .env
```

## Allure CLI

The Python package `allure-behave` creates Allure result files. The Allure command-line tool is also required to generate/open the HTML report.

Check:

```bash
allure --version
```

If Java is required by your Allure installation, install a supported Java runtime as documented by Allure.

## Run all tests

```bash
python -m behave
```

or:

```bash
python scripts/run_tests.py
```

## Run by tag

```bash
python scripts/run_tests.py smoke
python scripts/run_tests.py users
python scripts/run_tests.py authentication
python scripts/run_tests.py negative
python scripts/run_tests.py regression
```

## Generate Allure report

```bash
allure serve allure-results
```

Or generate a static report:

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

## Important API note

Automation Exercise documents:
- valid login -> 200
- invalid login -> 404
- missing login parameter -> 400
- unsupported DELETE on verifyLogin -> 405
- create account -> 201
- delete account -> 200
- update account -> 200
- get user by email -> 200

The test suite uses these documented contracts.

## Test Coverage

| ID | Area | Scenario |
|---|---|---|
| TC001 | Users | Get all users |
| TC002 | Users | Get valid user IDs |
| TC003 | Users | Invalid user |
| TC004 | Users | Create user |
| TC005 | Users | PUT update |
| TC006 | Users | PATCH update |
| TC007 | Users | DELETE |
| TC008 | Auth | Valid dynamic login |
| TC009 | Auth | Invalid login |
| TC010 | Auth | Missing email |
| TC011 | Auth | Unsupported method |
| TC012 | Auth | Update account |
| TC013 | Auth | User detail |
| TC014 | Negative | Unsupported POST |
| TC015 | Negative | Missing search parameter |
| TC016 | Negative | Unsupported PUT |

## Design Principles

1. Separation of concerns
2. Reusable API client
3. Centralized configuration
4. Explicit response validation
5. BDD-readable scenarios
6. Independent test data generation
7. Request/response logging
8. Allure evidence and environment metadata
9. No credentials committed to Git
10. Clear distinction between functional API testing and performance testing

## Future Enhancements

- GitHub Actions CI
- Multiple environment files
- API contract versioning
- More schema coverage
- Parallel execution
- Central test-data service
- CI artifact publishing


---

## 📁 Project Structure

```text
wipro_api_automation_framework/
│
├── config/
│   └── Configuration files
│
├── features/
│   ├── authentication/
│   ├── negative/
│   ├── users/
│   ├── environment.py
│   └── Step definitions
│
├── framework/
│   ├── api_client.py
│   ├── config_reader.py
│   └── Other framework components
│
├── schemas/
│   └── API response/request schemas
│
├── test_data/
│   └── Test data used by API scenarios
│
├── utils/
│   └── Utility functions
│
├── scripts/
│   └── Supporting execution scripts
│
├── screenshots/
│   └── Generated API execution evidence
│
├── logs/
│   └── Generated execution logs
│
├── allure-results/
│   └── Generated Allure test results
│
├── allure-report/
│   └── Generated HTML Allure report
│
├── .env
├── .env.example
├── .gitignore
├── behave.ini
├── requirements.txt
└── README.md