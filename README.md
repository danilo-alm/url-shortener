# URL Shortener

A simple URL shortener built with FastAPI, MongoDB and Redis.

![alt text](docs/_media/preview.png)

## Prerequisites

Before running this application, ensure you have the following installed:

* Docker and Docker Compose (for containerized environment)

If you want to run locally:

* Python 3.13
* MongoDB

## Environment Variables

This project relies on environment variables that you can configure in a `.env` file. You can also just go with the defaults.

### 🔗 MongoDB Configuration

* `MONGO_URI`: URI para conexão com o MongoDB
  (ex: `mongodb://localhost:27017/` para uso local ou `mongodb://mongodb:27017/` no Docker).
* `MONGO_USERNAME`: Nome de usuário do MongoDB (padrão: `admin`).
* `MONGO_PASSWORD`: Senha do MongoDB (padrão: `secret`).
* `MONGO_DATABASE`: Nome do banco de dados (padrão: `url_shortener`).
* `MONGO_COLLECTION`: Nome da coleção (padrão: `urls`).

---

### 🚀 FastAPI Application

* `API_HOST`: Host da aplicação FastAPI
  (padrão: `127.0.0.1` localmente, `0.0.0.0` no Docker).
* `API_PORT`: Porta interna da aplicação FastAPI (padrão: `8000`).
* `API_PORT_MAP`: Mapeamento externo de porta para acesso via Docker (padrão: `1234`).
* `RELOAD_ON_CHANGE`: Ativa recarregamento automático ao mudar o código
  (padrão: `true` localmente, `false` no Docker).

---

### 🧠 Redis Cache

* `REDIS_HOST`: Host do Redis (padrão: `127.0.0.1`).
* `REDIS_PORT`: Porta do Redis (padrão: `6379`).
* `REDIS_DB`: Banco de dados Redis (padrão: `0`).
* `REDIS_EXPIRATION_SECONDS`: Tempo de expiração das entradas no cache (padrão: `7200` segundos ou 2 horas).


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

3. The frontend will be available at `http://localhost:1234` (or the port specified in your `.env`).

### Local Setup (Without Docker)

1. Install and start MongoDB

[Read the MongoDB Docs](https://www.mongodb.com/docs/manual/installation/)

2. Install and start redis

[Read the Redis Docs](https://redis.io/docs/latest/operate/oss_and_stack/install/archive/install-redis/)

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

5. The frontend will be available at `http://localhost:8000` (or the port specified in your `.env`).