# MicroCloud Commerce

## Overview
MicroCloud Commerce is a **microservices-based architecture** designed for cloud-native applications. It features **user management and order processing services**, connected to **PostgreSQL databases**, and managed through **Docker and Docker Compose**. This project is built with scalability, modularity, and cloud deployment in mind, making it an ideal foundation for e-commerce, ERP, or any business logic that requires separate but interconnected services.

### Why Microservices?
Traditional monolithic applications bundle all services together, leading to scalability, maintenance, and deployment issues. This project follows the microservices architecture, where each service is independent, loosely coupled, and can be scaled independently.

### Key Benefits:
✅ Modularity: Separate services for User Management and Order Processing.

✅ Independent Scaling: Each microservice can scale based on demand.

✅ Fault Isolation: Issues in one service do not crash the entire system.

✅ Technology Agnostic: Different microservices can use different technologies in the future.

✅ Cloud-Ready Deployment: Designed for easy deployment on AWS, GCP, or Azure.


## Features & Technologies used:
- **Microservices Architecture**: Independent services for users and orders.
- **API Gateway**: for centralized routing of API requests to respective microservices.
- **REST API**: for communication between services.
- **Database Integration**: PostgreSQL support for persistent storage.
- **Dockerized Deployment**: used for containerized deployment of services for scalability.
- **Scalability & Modularity**: Easily extend services without affecting the system.
- **Security**: Authentication and authorization can be added.

## Project Goals
### Core Objectives
Develop a modular application with a microservices approach.
Enable seamless communication between the services via RESTful APIs.
Implement a PostgreSQL database for persistent data storage.
Containerize services with Docker for easy deployment.
Use API Gateway to centralize requests and responses.
Provide scalability and future cloud deployment readiness.

### Potential Use Cases
E-Commerce Platform: Users place orders, and the order system handles processing.
Enterprise Resource Planning (ERP): Separate services for handling employees, sales, and inventory.
Event Management System: Users register for events, and orders represent ticket purchases.

## System Architecture
### Microservices Breakdown

| Service Name | Description | Port |
| -------- | -------- | -------- |
| API Gateway    | Central entry point for handling requests  | 5000  |
| User Service |	Manages user-related operations |	5001
| Order Service |	Handles order processing |	5002
| User Database |	PostgreSQL instance for storing users |	5432
| Order Database |	PostgreSQL instance for storing orders |	5433

## Architecture Diagram
(Add an architectural diagram here to show the relationships between services)

## Project Structure
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
│── docs/
│   ├── screenshots/
```

## Services
### 1️⃣ **User Service**
- Handles user-related operations.
- Connects to **PostgreSQL** for data storage.
- Runs on **port 5001**.

(Screenshot: Add a screenshot of the User Service API response)

### 2️⃣ **Order Service**
- Manages order-related operations.
- Uses **PostgreSQL** for order tracking.
- Runs on **port 5002**.

(Screenshot: Add a screenshot of the Order Service API response)

### 3️⃣ **API Gateway**
- Routes requests to the correct microservices.
- Exposes API endpoints at **port 5000**.

(Screenshot: Add a screenshot of the API Gateway response)

## Setup & Deployment
### **1️⃣ Clone Repository**
```bash
git clone https://github.com/Pascalpedro/MicroCloud_Commerce.git
cd MicroCloud_Commerce
```

### **2️⃣ Build & Run Services**
```bash
docker-compose up --build
```

(Screenshot: Add a screenshot of Docker Compose running successfully)

### **3️⃣ Test APIs**
#### Get Users
```bash
curl http://localhost:5000/users
```
(Screenshot: Add a screenshot of a successful API response for users)

#### Get Orders
```bash
curl http://localhost:5000/orders
```
(Screenshot: Add a screenshot of a successful API response for orders)

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
(Screenshot: Add a screenshot of database table creation and data insertion)

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
(Screenshot: Add a screenshot of order database setup) 

## Contribution Guidelines
We welcome contributions! Please follow these steps:
1. Fork the repository.
2. Create a new feature branch.
3. Commit changes with meaningful messages.
4. Submit a pull request.

## License
This project is open-source and available under the **MIT License**.

## Contributors
- **Pascal Attama** – [GitHub](https://github.com/Pascalpedro)
- Contributions are welcome! Feel free to submit PRs.

