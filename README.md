# Multi-Container Docker App

This project demonstrates a simple multi-container setup using **Docker Compose**:
- **Web App**: Flask (Python) running on port 8080
- **Database**: MySQL with initialization script

## Run the project

---

#  How to Test
1. Clone repo:
   ```bash
   git clone 
   cd dockercompose 

Build & run:
docker-compose up --build -d
Creating network "dockercompose_default" with the default driver
Building web
Sending build context to Docker daemon  5.632kB
Step 1/6 : FROM python:3.10-slim
 ---> f5270789d44e
Step 2/6 : WORKDIR /app
 ---> Using cache
 ---> 9cef5458db29
Step 3/6 : COPY requirements.txt .
 ---> Using cache
 ---> 8d46d3efbce9
Step 4/6 : RUN pip install --no-cache-dir --progress-bar=off -r requirements.txt
 ---> Using cache
 ---> 116915fd7a63
Step 5/6 : COPY . .
 ---> Using cache
 ---> ce95053b96c5
Step 6/6 : CMD ["python", "app.py"]
 ---> Using cache
 ---> c5dca10a3a92
Successfully built c5dca10a3a92
Successfully tagged dockercompose_web:latest
Creating dockercompose_db_1 ... done
Creating dockercompose_web_1 ... done
Creating dockercompose_web_2 ... done
Creating dockercompose_nginx_1 ... done

✅ At this point:

Nginx should start correctly

Host port 5000 → Nginx → Flask containers

You can open http://localhost:5000



for testing 

 docker-compose up -d --scale web=4
Starting dockercompose_db_1 ... done
Creating dockercompose_web_3 ... done
Creating dockercompose_web_4 ... done
dockercompose_nginx_1 is up-to-date

docker-compose ps
        Name                       Command               State                   Ports                
------------------------------------------------------------------------------------------------------
dockercompose_db_1      docker-entrypoint.sh mysqld      Exit 1                                       
dockercompose_nginx_1   /docker-entrypoint.sh ngin ...   Up       0.0.0.0:5000->80/tcp,:::5000->80/tcp
dockercompose_web_1     python app.py                    Up       8080/tcp                            
dockercompose_web_2     python app.py                    Up       8080/tcp                            
dockercompose_web_3     python app.py                    Up       8080/tcp                            
dockercompose_web_4     python app.py                    Up       8080/tcp   

