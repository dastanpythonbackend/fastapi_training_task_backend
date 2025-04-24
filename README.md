# fastapi_training_task_backend

A test assignment project built with FastAPI. The service provides basic URL shortening functionality and demonstrates handling of asynchronous requests.

## Features

- `POST /` — Accepts a long URL and returns a shortened version (HTTP 201).
- `GET /{shorten_id}` — Redirects to the original URL (HTTP 307).
- Example of an async request to an external API.

## Requirements

- Python 3.13+
- Install dependencies:

```bash
pip install -r requirements.txt

## Running the Server

**To start the server with Uvicorn:**

```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8080

## Example Requests

### Shorten a URL

**Request:**

```http
POST /
Content-Type: application/json

{
  "url": "https://example.com"
}

**Response:**

```json
{
  "shorten_url": "http://127.0.0.1:8080/{shorten_id}"
}

**Note: {shorten_id} will be a random string generated for each URL.**

## Redirect to Original

**Request:**

```http
GET /{shorten_id}

**Response:**

- Status: 307 Temporary Redirect

- Header: Location: https://example.com

## Running Tests

### This project uses pytest.

**To run the tests:**

```bash
pytest
