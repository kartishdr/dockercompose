# Multi-Container Docker App (Python + MySQL)

This project demonstrates a simple multi-container application using **Docker Compose**:
- **Web App**: Python Flask app running on port `8080`
- **Database**: MySQL container with initial data
- **Scaling**: Web app can be scaled to handle more traffic


```bash
🔹 1. Build & Start Containers

From the root of your repo (multi-container-app/):

docker-compose build --no-cache
docker-compose up



What happens:

Docker builds the web app image from webapp/Dockerfile.

Pulls the MySQL image.

Starts both containers, sets up a private Docker network, and runs your app.

✅ Expected output:

MySQL logs show DB creation + execution of init.sql.

Flask logs show it’s running on 0.0.0.0:8080.

🔹 2. Test Web Application

Open a browser or use curl:

curl http://localhost:8080


Expected response:

Hello from Python App! DB time: 2025-09-26 07:20:00


👉 This confirms:

Flask app is running.

It can connect to the MySQL container.

DB query works (returns current DB time).

🔹 3. Verify Database Init Script

Connect to MySQL container:

docker exec -it multi-container-app-db-1 mysql -uroot -prootpassword myappdb


Run:

SELECT * FROM users;


Expected result:

+----+---------+
| id | name    |
+----+---------+
|  1 | Alice   |
|  2 | Bob     |
|  3 | Charlie |
+----+---------+


👉 Confirms init.sql executed successfully.

🔹 4. Stop Containers
docker-compose down


This stops and removes containers, but keeps the data in the volume (db_data).

If you want a clean start (remove DB data too):

docker-compose down -v

🔹 5. Scale the Web App

Docker Compose makes scaling super easy 🚀

Run:

docker-compose up --scale web=3 -d


What happens:

Creates 3 replicas of your Flask web app.

All containers are still accessible via localhost:8080 (Compose automatically load balances requests across replicas).

Check running containers:

docker ps


You’ll see multiple containers like:

multi-container-app_web_1
multi-container-app_web_2
multi-container-app_web_3
multi-container-app_db_1

🔹 6. Test Load Balancing

Since multiple replicas are running, hitting the app repeatedly should route to different containers.

Try:

for i in {1..5}; do curl http://localhost:8080; echo; done


If you add some unique log (like container hostname in app.py), you’ll see requests served by different containers.
