# Flask Backend App

This is a Flask-based backend application for managing various states including manual page state, settings page state, and irrigation timer state.

## Setup

1. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

2. Run the application:
    ```
    python app.py
    ```

## Endpoints

- POST `/manual_page/set_state` - Save manual page state
- POST `/settings_page/set_state` - Save settings page state
- POST `/irrigation_timer/set_state` - Save irrigation timer state

- GET `/manual_page/get_state` - Get manual page state
- GET `/settings_page/get_state` - Get settings page state
- GET `/irrigation_timer/get_state` - Get irrigation timer state
