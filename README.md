# Polo 

A real-time messaging backend built with FastAPI, WebSockets, PostgreSQL, and Redis.

Live Demo: https://polo-ffo6.onrender.com/docs

## Tech Stack

- **FastAPI** — Python web framework for building APIs
- **WebSockets** — Real-time bidirectional communication
- **PostgreSQL** — Relational database for persistent storage (hosted on Supabase)
- **Redis Pub/Sub** — Message broker for horizontal scaling
- **JWT** — Stateless authentication
- **Docker** — Containerization
- **GitHub Actions** — CI/CD pipeline
- **Render** — Cloud deployment

## Features

- User registration and login with JWT authentication
- Password hashing with bcrypt
- Real-time messaging using WebSockets
- Multi-room chat support
- JWT protected WebSocket connections
- Persistent chat history stored in PostgreSQL
- Message states — sent, delivered, read
- Horizontal scaling with Redis Pub/Sub
- Containerized with Docker
- CI/CD pipeline with GitHub Actions

## Architecture

Client → FastAPI Server → Redis Pub/Sub → All Server Instances
↓
PostgreSQL (Supabase)

**Message Flow:**
1. Client connects to `/ws/{room_id}` with JWT token
2. Server verifies token and accepts WebSocket connection
3. Client sends message
4. Server saves message to PostgreSQL
5. Server publishes message to Redis channel
6. All subscribed server instances receive from Redis
7. Each instance forwards message to their connected clients

## API Endpoints

| Method |      Endpoint         |          Description        | Auth Required |
|--------|-----------------------|-----------------------------|---------------|
| GET    | `/`                   | Health check                |        No     |
| POST   | `/register`           | Register a new user         |        No     |
| POST   | `/login`              | Login and get JWT token     |        No     |
| WS     | `/ws/{room_id}`       | WebSocket chat connection   |      Yes (JWT)|
| GET    | `/messages/{room_id}` | Get chat history for a room |        No     |


## Running Locally

1. Clone the repository
```bash
git clone https://github.com/Judith-AB/polo.git
cd polo/backend
```
2. Create a `.env` file with your credentials
DATABASE_URL=your_supabase_connection_string
REDIS_URL=your_redis_connection_string

3. Run with Docker
```bash
docker-compose up --build
```

4. Visit `http://127.0.0.1:8000/docs`