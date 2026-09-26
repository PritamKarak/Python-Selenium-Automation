from datetime import datetime
import uuid


def unique_email(prefix="wipro.api"):
    stamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
    return f"{prefix}.{stamp}.{uuid.uuid4().hex[:6]}@example.com"


def user_registration_payload(email=None, password="Test@12345"):
    return {
        "name": "Wipro API Automation",
        "email": email or unique_email(),
        "password": password,
        "title": "Mr",
        "birth_date": "15",
        "birth_month": "5",
        "birth_year": "1999",
        "firstname": "Automation",
        "lastname": "Tester",
        "company": "Wipro Capstone",
        "address1": "100 Test Street",
        "address2": "Automation Block",
        "country": "India",
        "zipcode": "700001",
        "state": "West Bengal",
        "city": "Kolkata",
        "mobile_number": "9000000000",
    }
