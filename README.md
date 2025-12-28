# MCP Todo Application

> An AI-powered todo manager using the Model Context Protocol (MCP) pattern with FastAPI, MongoDB, HTMX, and OpenRouter LLM.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)
![MongoDB](https://img.shields.io/badge/MongoDB-6.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🎯 Overview

This application demonstrates the MCP (Model Context Protocol) pattern where an LLM acts as a reasoning engine that selects tools, while FastAPI endpoints execute those tools against MongoDB. The LLM **never** directly accesses the database.

### Architecture

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐     ┌──────────┐
│   Browser   │────▶│  LLM Router  │────▶│  OpenRouter │    │          │
│   (HTMX)    │     │  /llm/chat   │◀────│     LLM     │     │  MongoDB │
└─────────────┘     └──────────────┘     └─────────────┘     └──────────┘
       │                   │                                       ▲
       │                   ▼ Tool Selection                        │
       │            ┌──────────────┐                               │
       └───────────▶│   Endpoints  │───────────────────────────────┘
                    │   /todos/*   │
                    └──────────────┘
```

### Key Features

- 🧠 **Natural Language Interface** - Ask the AI to manage your todos
- 📋 **Full CRUD Operations** - Create, read, update, delete todos
- ⚡ **HTMX Frontend** - Dynamic updates without page reloads
- 🔧 **MCP Pattern** - Clean separation between reasoning and execution
- 🎨 **Modern UI** - Glassmorphism design with smooth animations

## 📁 Project Structure

```
src/
├── main.py                 # FastAPI app entry point
├── config.py               # Environment configuration
├── database.py             # MongoDB connection management
├── schemas.py              # Pydantic models
├── mcp
│   ├──mcp.py               # MCP tools defined
├── routers/
│   ├── endpoints.py        # Todo CRUD routes
│   ├── llm.py              # MCP/LLM router
│   └── helpers/
│       ├── endpoint_helper.py  # Database operations
│       └── llm_helper.py       # OpenRouter client & MCP tools
├── templates/
│   ├── index.html          # Main page
│   └── partials/           # HTMX partial templates
└── static/
    └── css/
        └── styles.css      # Custom styles
```

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- MongoDB 6.0+ (running locally or MongoDB Atlas)
- OpenRouter API key ([Get one here](https://openrouter.ai/keys))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/nudgeai.git
   cd nudgeai
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your values
   ```

5. **Start MongoDB** (if running locally)
   ```bash
   mongod
   ```

6. **Run the application**
   ```bash
   uvicorn src.main:app --reload
   ```

7. **Open in browser**
   ```
   http://localhost:8000
   ```

## ⚙️ Configuration

Create a `.env` file based on `.env.example`:

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `MONGODB_URI` | MongoDB connection string | ✅ | - |
| `MONGODB_DB_NAME` | Database name | ✅ | - |
| `OPENROUTER_API_KEY` | OpenRouter API key | ✅ | - |
| `OPENROUTER_MODEL` | LLM model identifier | ❌ | `xiaomi/mimo-v2-flash:free` |
| `APP_NAME` | Application display name | ❌ | `MCP Todo` |

## 📚 API Documentation

Once running, access the interactive API docs:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/` | Main application page |
| `GET` | `/health` | Health check |
| `GET` | `/todos/` | List all todos |
| `POST` | `/todos/` | Create a todo |
| `GET` | `/todos/{id}` | Get a single todo |
| `PUT` | `/todos/{id}` | Update a todo |
| `DELETE` | `/todos/{id}` | Delete a todo |
| `POST` | `/todos/{id}/toggle` | Toggle completion |
| `POST` | `/llm/chat` | Natural language interface |

## 🧠 MCP Tools

The LLM has access to these tools for todo management:

| Tool | Description | Parameters |
|------|-------------|------------|
| `create_todo` | Create a new todo | `title*`, `description`, `due_date` |
| `list_todos` | Get all todos | `completed` (optional filter) |
| `update_todo` | Update existing todo | `todo_id*`, `title`, `description`, `due_date`, `completed` |
| `delete_todo` | Delete a todo | `todo_id*` |
| `toggle_complete` | Toggle todo status | `todo_id*` |

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - Modern Python web framework
- [HTMX](https://htmx.org/) - High power tools for HTML
- [OpenRouter](https://openrouter.ai/) - LLM API gateway
- [Motor](https://motor.readthedocs.io/) - Async MongoDB driver
