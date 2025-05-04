# URL Shortener

A simple URL shortener built with **FastAPI** and **MongoDB**. This project provides a RESTful API to create and retrieve shortened URLs, allowing users to map long URLs to shorter ones for easier sharing.

## Prerequisites

Before running this application, ensure you have the following installed:

* Docker and Docker Compose (for containerized environment)

If you want to run locally:

* Python 3.13 (for local development)
* MongoDB (for local or Docker environment)

## Environment Variables

This project relies on environment variables that you can configure in a `.env` file. You can also just go with the defaults.

### Environment Variables:

* `MONGO_URI`: URI for connecting to MongoDB (e.g., `mongodb://localhost:27017/` for local or `mongodb://mongodb:27017/` for Docker).
* `MONGO_USERNAME`: MongoDB username (default: `admin`).
* `MONGO_PASSWORD`: MongoDB password (default: `secret`).
* `MONGO_DATABASE`: The database name (default: `url_shortener`).
* `MONGO_COLLECTION`: The collection name (default: `urls`).
* `API_HOST`: Host for the FastAPI application (default: `127.0.0.1` locally and `0.0.0.0` when in Docker).
* `API_PORT`: Internal port of the FastAPI application (default: `8000`).
* `API_PORT_MAP`: External port mapping for accessing the API when using docker (default: `1234`).
* `RELOAD_ON_CHANGE`: Whether to enable auto-reloading when code changes (default: `true` locally and `false` when in Docker).

## Setup

You can run this project either in **Docker** (recommended) or **locally**.

### Docker Setup (Recommended)

1. Clone the repository:

   ```bash
   git clone https://github.com/danilo-alm/url-shortener.git
   cd url-shortener
   ```

2. Build and run the application with Docker Compose:

   ```bash
   docker-compose up --build
   ```

3. The application will be available at `http://localhost:1234` (or the port specified in your `.env`).

### Local Setup (Without Docker)

1. Install and start MongoDB

I won't go into that. [Read the MongoDB Docs](https://www.mongodb.com/docs/manual/installation/)

2. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/url-shortener.git
   cd url-shortener
   ```

3. Install `uv`
   ```bash
   python -m pip install uv
   ```

4. Install dependencies and run
   ```bash
   uv run -- python -m app.run
   ```

5. The application will be available at `http://localhost:8000` (or the port specified in your `.env`).

## API Endpoints

### POST /shorten

Shorten a long URL.

#### Request Body:

```json
{
  "long_url": "https://www.example.com"
}
```

#### Response:

```json
{
  "short_url": "http://localhost:8000/abc123"
}
```

### GET /{short\_url}

Retrieve the original long URL from a shortened URL. The user will be automatically redirected to the original URL.

#### Request:

```bash
GET http://localhost:8000/abc123
```

#### Response:

The request will result in an HTTP redirect (status code 308) to the original long URL, e.g.,:
   ```html
   HTTP/1.1 308 Permanent Redirect
   Location: https://www.example.com
   ```