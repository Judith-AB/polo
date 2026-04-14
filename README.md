# FastAPI Real-Time Chat Backend

A high-performance, asynchronous chat system built with **FastAPI**, **Redis Pub/Sub**, and **Supabase**. This architecture is designed for horizontal scalability, allowing WebSockets to communicate across multiple server instances.

## System Architecture

The backend uses a **Distributed Pub/Sub** pattern to synchronize messages:
1. **FastAPI**: Manages WebSocket lifecycles and JWT verification.
2. **Redis**: Acts as the message broker between different server nodes.
3. **Supabase (Postgres)**: Provides persistent storage for chat history and user metadata.



---

##  Features

* **Real-time Messaging**: Low-latency communication via WebSockets.
* **Scalable Pub/Sub**: Redis ensures users on different server instances can chat seamlessly.
* **Persistent Storage**: Automatic message logging to Supabase PostgreSQL.
* **JWT Authentication**: Secure handshake using OAuth2 password flow and JWT.
* **Type Safety**: Full Pydantic model integration for request/response validation.

---

## Tech Stack

* **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
* **Database**: [Supabase](https://supabase.com/) (PostgreSQL)
* **Message Broker**: [Redis](https://redis.io/)
* **Auth**: `python-jose` (JWT), `passlib` (Bcrypt)

---

##  Getting Started

### 1. Environment Setup
Create a `.env` file in your root directory:

```env
# Supabase Transaction Pooler (AWS South 1)
DATABASE_URL="postgresql://postgres.tgkmygugwiwxkddnvpvk:<mypassword>@[aws-1-ap-south-1.pooler.supabase.com:6543/postgres](https://aws-1-ap-south-1.pooler.supabase.com:6543/postgres)"

# Redis Cloud Endpoint (AWS Southeast 1)
REDIS_URL="redis://:<key>@redis-17163.c252.ap-southeast-1-1.ec2.cloud.redislabs.com:17163"

### 2. Installation
Make sure you are in the `backend/` directory and your virtual environment is activated:

```bash
# Upgrade pip to the latest version
python -m pip install --upgrade pip

# Install all project dependencies
pip install -r requirements.txt


### 3. Run Development Server
Ensure your virtual environment is activated and you are in the `backend/` directory:

```bash
uvicorn app.main:app --reload