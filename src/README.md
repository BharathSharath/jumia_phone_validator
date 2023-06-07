# jumia_phone_validator

This is a microservice for validating phone numbers using the Jumia Phone Validator.

## Installation

1. Create a virtual environment: `python -m venv venv`
2. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/Mac: `source venv/bin/activate`
3. Install the dependencies: `pip install -r requirements.txt`

## Usage

Start the application: `python app.py`

The application will be running on http://localhost:5000.

To validate a phone number, send a POST request to http://localhost:5000/validate with a JSON payload:

```json
{
  "phone_number": "+123456789"
}
