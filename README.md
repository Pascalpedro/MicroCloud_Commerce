#MicroCloud Commerce

## Overview

MicroCloud Commerce is a **microservices-based architecture** designed for cloud-native applications. It features **user management and order processing services**, connected to **PostgreSQL databases**, and managed through **Docker and Docker Compose**.

## Features

- **Microservices Architecture**: Independent services for users and orders.
- **API Gateway**: Centralized routing of API requests.
- **Database Integration**: PostgreSQL support for persistent storage.
- **Dockerized Deployment**: Containerized services for scalability.

## Architecture

```
MicroCloud Commerce
│── docker-compose.yml
│── user-service/
│   ├── Dockerfile
│   ├── app.py
│   ├── db.py
│   ├── requirements.txt
│── order-service/
│   ├── Dockerfile
│   ├── app.py
│   ├── db.py
│   ├── requirements.txt
│── api-gateway/
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
```

## Services

### 1️⃣ **User Service**

- Handles user-related operations.
- Connects to **PostgreSQL** for data storage.
- Runs on **port 5001**.

### 2️⃣ **Order Service**

- Manages order-related operations.
- Uses **PostgreSQL** for order tracking.
- Runs on **port 5002**.

### 3️⃣ **API Gateway**

- Routes requests to the correct microservices.
- Exposes API endpoints at **port 5000**.

## Setup & Deployment

### **1️⃣ Clone Repository**

```bash
git clone https://github.com/pascalpedro/MicroCloud-Commerce.git
cd MicroCloud-Commerce
```

### **2️⃣ Build & Run Services**

```bash
docker-compose up --build
```

### **3️⃣ Test APIs**

#### Get Users

```bash
curl http://localhost:5000/users
```

#### Get Orders

```bash
curl http://localhost:5000/orders
```

## Database Setup

### Connect to User Database

```bash
docker exec -it $(docker ps -qf "name=user-db") psql -U postgres -d usersdb
```

Run SQL commands:

```sql
CREATE TABLE users (id SERIAL PRIMARY KEY, name VARCHAR(100));
INSERT INTO users (name) VALUES ('Pedro'), ('Pascal');
SELECT * FROM users;
```

### Connect to Order Database

```bash
docker exec -it $(docker ps -qf "name=order-db") psql -U postgres -d ordersdb
```

Run SQL commands:

```sql
CREATE TABLE orders (id SERIAL PRIMARY KEY, item VARCHAR(100));
INSERT INTO orders (item) VALUES ('Order1'), ('Order2');
SELECT * FROM orders;
```

## Roadmap

✅ **Add Database Support**\
🚀 **Integrate Authentication (JWT)**\
🌍 **Deploy on AWS using Kubernetes (EKS)**

## License

This project is open-source and available under the **MIT License**.

## Contributors

- **Your Name** – [GitHub](https://github.com/Pascalpedro)
- Contributions are welcome! Feel free to submit PRs.

