# Profile /me API

A FastAPI-based REST API that provides profile information along with a random cat fact. The API fetches cat facts from an external service and includes fallback facts if the external API is unavailable.

## Features

- **Profile Endpoint**: Retrieve user profile information including email, name, and tech stack
- **Cat Facts Integration**: Fetches random cat facts from the Cat Facts API
- **Fallback Mechanism**: Uses local cat facts if the external API fails
- **Configurable Settings**: Environment-based configuration using Pydantic settings
- **CORS Support**: Configured for cross-origin requests
- **Error Handling**: Proper HTTP status codes and error responses

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/codenamemomi/HNG_stage_0
   cd HNG_stage_0
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory with your configuration:
   ```env
   EMAIL=your.email@example.com
   FULL_NAME=Your Full Name
   STACK=Python/FastAPI
   ```

## Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `EMAIL` | User's email address | - | Yes |
| `FULL_NAME` | User's full name | - | Yes |
| `STACK` | Tech stack description | `Python/FastAPI` | No |
| `CATFACT_URL` | Cat Facts API URL | `https://catfact.ninja/fact` | No |
| `CATFACT_TIMEOUT_SECONDS` | Timeout for cat fact API requests | `2.0` | No |
| `FAIL_ON_CATFACT_ERROR` | Whether to fail if cat fact API is unavailable | `False` | No |

## Running the Application

Start the development server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

Visit `http://localhost:8000/docs` for interactive API documentation.

## API Endpoints

### GET /
Returns a welcome message.

**Response:**
```json
{
  "message": "Welcome to the Profile API. Visit /me for info."
}
```

### GET /me
Retrieves profile information with a random cat fact.

**Success Response (200):**
```json
{
  "status": "success",
  "user": {
    "email": "your.email@example.com",
    "name": "Your Full Name",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2024-01-15T10:30:45.123456Z",
  "fact": "Cats have five toes on their front paws, but only four on their back paws."
}
```

**Error Response (502) - When FAIL_ON_CATFACT_ERROR=true and API fails:**
```json
{
  "status": "error",
  "message": "Failed to fetch cat fact from external API"
}
```

## Technologies Used

- **FastAPI**: Modern, fast web framework for building APIs
- **httpx**: Asynchronous HTTP client for API requests
- **Pydantic**: Data validation and settings management
- **Uvicorn**: ASGI server for running FastAPI applications
- **Python-dotenv**: Environment variable management

## Project Structure

```
.
├── main.py                 # FastAPI application entry point
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore rules
├── README.md              # This file
├── api/
│   ├── route/
│   │   └── me.py          # API route definitions
│   └── service/
│       └── me.py          # Business logic for profile service
└── core/
    └── settings.py        # Application settings and configuration
```

## Development

The application uses logging for monitoring API requests and errors. Logs are output to the console with timestamps and log levels.

For production deployment, consider:
- Setting `FAIL_ON_CATFACT_ERROR=true` for stricter error handling
- Configuring proper CORS origins instead of allowing all (`*`)
- Adding authentication/authorization if needed
- Using a production ASGI server like Gunicorn with Uvicorn workers
