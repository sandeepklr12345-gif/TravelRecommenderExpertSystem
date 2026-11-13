# Travel Recommender Expert System

A rule-based travel destination recommender. The user selects a budget, preferred climate, and place type; a FastAPI endpoint returns a destination for a supported combination.

## Features

- Budget choices: low, medium, and high.
- Climate choices: cold, moderate, and hot.
- Place types: beach, mountain, historical, and wildlife.
- Eight predefined recommendations, with a no-match response for other combinations.
- A simple browser interface backed by a FastAPI service.

## Tech stack

- Python with FastAPI
- HTML, CSS, and JavaScript

## Project structure

```text
backend/
  main.py       # FastAPI application and recommendation rules
frontend/
  index.html    # Browser interface
dataset.csv     # Example recommendation data
```

The CSV documents the example combinations. The current API logic is defined directly in `backend/main.py` and does not load the CSV at runtime.

## Run locally

1. Install Python and open a terminal in the project folder.
2. Install the backend packages:

   ```bash
   python -m pip install fastapi uvicorn
   ```

3. Start the API from the `backend` folder:

   ```bash
   cd backend
   python -m uvicorn main:app --reload
   ```

4. Open `frontend/index.html` in a browser. Keep the API running while using the page.

The API documentation is available at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## API

Send a `POST` request to `http://127.0.0.1:8000/recommend` with JSON such as:

```json
{
  "budget": "low",
  "climate": "hot",
  "place_type": "beach"
}
```

Example response:

```json
{
  "destination": "Goa, India"
}
```

The supported budget values are `low`, `medium`, and `high`; climate values are `cold`, `moderate`, and `hot`; place types are `beach`, `mountain`, `historical`, and `wildlife`. Combinations without a predefined rule return a “No match found” message.
