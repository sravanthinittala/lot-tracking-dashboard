# Product Lot Tracking Dashboard

Many manufacturers rely on databases to track shipment lots of different products from their warehouses. This web application aims to provide a consolidated dashboard to track shipment lots from the time they are added to the warehouse database to when they have passed quality control checks and are ready to be shipped.

## Features

- Track **product lots** in warehouses  
- Record **quantity**, **QC status**, and **shipment**  
- Update lot information via **REST API**  
- Simple, responsive **frontend dashboard** with React 

## Tech Stack

- **Backend:** FastAPI, SQLAlchemy, Pydantic  
- **Database:** SQLite (can be replaced with PostgreSQL/MySQL)  
- **Frontend:** React with Vite  
- **Containerization:** Docker & Docker Compose  

## Folder Structure 
```
root/
├── api/
│   └── app/
│       ├── core/           # Database connection, common utils
│       ├── models/         # SQLAlchemy models
│       ├── schemas/        # Pydantic schemas
│       ├── services/       # Business logic
│       ├── routes/         # API endpoints
│       ├── main.py         # FastAPI app
├── data/                   # SQLite database file
├── frontend/               # React frontend (Vite)
└── README.md
```
<!--

## Setup with Docker

1. Build the Docker Images

```
docker-compose build
```

2. Run the services 

```
docker-compose up
```

Backend API: [http://localhost:8000/docs](http://localhost:8000/docs/) (Swagger UI)
Fronted: [http://localhost:5173](http://localhost:5173)

3. Stop the services

```
docker-compose down
```
-->
## Setup

### Backend

1. Install dependencies:
(recommended to create a virtual environment)

```
cd ./api
pip install -r requirements.txt
```

2. Run the server:

Navigate to the `api` dir and run the following

```
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
The API will be launched with docs available at [http://localhost:8000/docs/](http://localhost:8000/docs/)

### Frontend

Run the following to deploy the frontend:

```
cd frontend
npm install
npm run dev
```

The frontend will be available at [http://localhost:5173](http://localhost:5173)