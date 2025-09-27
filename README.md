# Multi-Container Docker App

This project demonstrates a simple multi-container setup using **Docker Compose**:
- **Web App**: Flask (Python) running on port 8080
- **Database**: MySQL with initialization script

## Run the project

```bash
docker-compose up --build
Access the app:
 http://localhost:8080

Scaling the Web App
bash
Copy code
docker-compose up --build --scale web=3
This will start 3 replicas of the web app behind Docker's internal load balancer.

yaml
Copy code

---

#  How to Test
1. Clone repo:
   ```bash
   git clone https://github.com/<your-username>/multi-container-app.git
   cd multi-container-app
Build & run:

bash
Copy code
docker-compose up --build
Visit in browser:
 http://localhost:8080
You should see:

json
Copy code
{"message": "Hello from MySQL + Flask + Docker!"}
Scale web app:

bash
Copy code
docker-compose up --build --scale web=3.
