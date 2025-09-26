# Multi-Container Docker App (Python + MySQL)

This project demonstrates a simple multi-container application using **Docker Compose**:
- **Web App**: Python Flask app running on port `8080`
- **Database**: MySQL container with initial data
- **Scaling**: Web app can be scaled to handle more traffic


```bash
docker-compose up --build
docker-compose up --scale web=3 -d


This runs 3 replicas of the web app.
