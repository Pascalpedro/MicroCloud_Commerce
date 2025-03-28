# MicroCloud Commerce

## Overview
MicroCloud Commerce is a **microservices-based architecture** designed for cloud-native applications. It features **user management and order processing services**, connected to **PostgreSQL databases**, and managed through **Docker and Docker Compose**.

## Features
- **Microservices Architecture**: Independent services for users and orders.
- **API Gateway**: Centralized routing of API requests.
- **Database Integration**: PostgreSQL support for persistent storage.
- **Dockerized Deployment**: Containerized services for scalability.
- **Scalability & Modularity**: Easily extend services without affecting the system.
- **Security**: Authentication and authorization can be added.

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

## Roadmap
✅ **Add Database Support**  
🚀 **Integrate Authentication (JWT)**  
🌍 **Deploy on AWS using Kubernetes (EKS)**  
📈 **Add Monitoring and Logging**  
🔐 **Enhance Security Measures**  

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

