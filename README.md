# FastAPI Intern Assessment - Task Management API

## Overview

This is a Task Management API built with FastAPI, SQLModel, and SQLite. It demonstrates RESTful API design, data validation, database operations, and clean code practices.

## Features
- Create, Read, Update, Delete tasks
- Filter by status and priority
- Pagination and validation
- Bulk operations (create, update, delete)
- Auto-generated Swagger docs
- Dockerized for easy deployment
- Database migrations with Alembic

## Tech Stack
- **FastAPI** (web framework)
- **SQLModel** (ORM, built on SQLAlchemy)
- **Pydantic** (data validation)
- **SQLite** (database)
- **Alembic** (migrations)
- **Docker** (containerization)

## Project Structure
```
├── app/
│   ├── main.py         # FastAPI app entrypoint
│   ├── routes.py       # API endpoints
│   ├── models.py       # SQLModel models
│   ├── schemas.py      # Pydantic schemas
│   ├── database.py     # DB connection/session
│   └── utils.py        # Validation utilities
├── alembic/            # DB migrations
├── alembic.ini         # Alembic config
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker config
├── docker-compose.yml  # Docker Compose config
├── .env                # Environment variables
├── task.db             # SQLite database
└── README.md           # Project documentation
```

## Setup Instructions

### 1. Clone the repository
```bash
git clone <repo>
cd task_management_api
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the root directory:
```
DATABASE_URL=sqlite:///./task.db
```

### 5. Run database migrations (optional, for Alembic)
```bash
alembic upgrade head
```

### 6. Start the application
```bash
python -m app.main
```

### 7. (Optional) Run with Docker
```bash
docker-compose up --build
```

## API Documentation
- Interactive docs: [http://localhost:8000/docs](http://localhost:8000/docs)
- Alternative docs: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Example API Calls
```bash
# Create a task
curl -X POST "http://localhost:8000/tasks" \
     -H "Content-Type: application/json" \
     -d '{"title": "Sample Task", "priority": "high"}'

# List tasks
curl "http://localhost:8000/tasks?skip=0&limit=10"

# Get a task by ID
curl "http://localhost:8000/tasks/1"

# Update a task
curl -X PUT "http://localhost:8000/tasks/1" \
     -H "Content-Type: application/json" \
     -d '{"status": "completed"}'

# Delete a task
curl -X DELETE "http://localhost:8000/tasks/1"
```

## API Endpoints
- `GET /` - API info
- `GET /health` - Health check
- `POST /tasks` - Create task
- `GET /tasks` - List tasks (with pagination)
- `GET /tasks/{task_id}` - Get task by ID
- `PUT /tasks/{task_id}` - Update task
- `DELETE /tasks/{task_id}` - Delete task
- `GET /tasks/status/{status}` - Filter by status
- `GET /tasks/priority/{priority}` - Filter by priority
- `POST /tasks/bulk` - Bulk create
- `PUT /tasks/bulk/update` - Bulk update
- `DELETE /tasks/bulk/delete` - Bulk delete

## Validation Rules
- **Title**: Cannot be empty/whitespace, trimmed
- **Due date**: Must be in the future (if provided)
- **HTTP status codes**: 201 (created), 200 (success), 404 (not found), 422 (validation error), 400 (client error)

## Testing
- Install dependencies and run the app as above
- Access [http://localhost:8000/docs](http://localhost:8000/docs) for interactive testing
- Use `curl` or Postman for manual API testing

## Design Decisions
- Uses environment variables for DB config
- Alembic for migrations
- Docker for reproducibility
- Clean separation of models, schemas, routes, and DB logic

## Resources
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [SQLModel Docs](https://sqlmodel.tiangolo.com/)
- [Pydantic Docs](https://docs.pydantic.dev/latest/)

---

For questions, see the resources above or contact the project maintainer.

```bash
git clone <repo>
cd task_management_api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m app.main
