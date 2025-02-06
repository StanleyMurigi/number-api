# Number Classification API

This project is a simple API that classifies numbers based on mathematical properties and retrieves fun facts using the Numbers API. The API is implemented using FastAPI.

## Features
- Checks if a number is **Armstrong**, **Prime**, or **Perfect**.
- Determines if a number is **Odd** or **Even**.
- Calculates the **sum of digits** of the number.
- Fetches a **fun fact** about the number from the Numbers API.
- Returns data in **JSON format**.

## Technology Stack
- **FastAPI** (for building the API)
- **Uvicorn** (for running the server)
- **Requests** (for fetching data from the Numbers API)

## Installation & Setup

### Prerequisites
Ensure you have Python 3.8+ installed.

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/StanleyMurigi/number-api.git
   cd number-classification-api
   ```
2. Install dependencies:
   ```bash
   pip install fastapi uvicorn requests
   ```
3. Run the API:
   ```bash
   uvicorn main:app --reload
   ```
   Replace `main` with the filename containing the FastAPI application.

## Usage
Send a GET request to:
```
http://127.0.0.1:8000/api/classify-number?number=371
```

### Example Response
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

## Deployment
You can deploy this API using **Vercel, Railway, or Render**.

## License
This project is open-source under the MIT License.

## Author
Stanley Murigi 
