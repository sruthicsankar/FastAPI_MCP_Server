# FastAPI_MCP_Server
Agentic AI project demonstrating MCP tool calling with FastAPI backend, JSON datastore, and Claude Desktop integration.

This project showcases how an LLM like Claude can dynamically invoke external tools through MCP to fetch structured IP address information from a FastAPI service.

---

# Architecture

```text
Claude Desktop
       ↓
MCP Server (Python)
       ↓
FastAPI Backend
       ↓
JSON Datastore
```

---

# Features

- MCP tool integration
- FastAPI backend APIs
- JSON-based datastore
- Claude Desktop integration
- Dynamic IP intelligence retrieval
- AI tool orchestration workflow

---

# Tech Stack

- Python
- FastAPI
- MCP (Model Context Protocol)
- Uvicorn
- Requests
- JSON
- Claude Desktop

---

# Project Structure

```text
ip_mcp_project/
│
├── data/
│   └── ip_data.json
│
├── api_server.py
├── mcp_server.py
├── requirements.txt
└── README.md
```

---

# Installation

## 1. Clone Repository

## 2. Create Virtual Environment

```bash
python3 -m venv .venv
```

Activate:

```bash
source .venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install fastapi uvicorn requests mcp
```
---

# FastAPI Backend

## Run FastAPI Server

```bash
uvicorn api_server:app --reload
```

Server runs at:

```text
http://127.0.0.1:8000
```

---

# Available API Endpoints

## Home Endpoint

```text
GET /
```

Response:

```json
{
  "message": "FastAPI Running"
}
```

---

## Get IP Details

```text
GET /ip/{ip_address}
```

Example:

```text
http://127.0.0.1:8000/ip/192.168.1.1
```

Response:

```json
{
  "ip": "192.168.1.1",
  "country": "India",
  "city": "Bangalore",
  "provider": "Airtel"
}
```

---

# MCP Server

## Run MCP Server

```bash
python mcp_server.py
```

The MCP server exposes AI tools that can be used by Claude Desktop.

---

# MCP Tool

## get_ip_info

### Input

```python
get_ip_info(ip_address: str)
```

### Example

```python
get_ip_info("192.168.1.1")
```

### Response

```json
{
  "ip": "192.168.1.1",
  "country": "India",
  "city": "Bangalore",
  "provider": "Airtel"
}
```

---

# Claude Desktop Integration

## Claude MCP Config Path (Mac)

```text
~/Library/Application Support/Claude/claude_desktop_config.json
```

## Configuration

```json
{
  "mcpServers": {
    "ip-server": {
      "command": "/FULL_PATH/.venv/bin/python",
      "args": [
        "/FULL_PATH/mcp_server.py"
      ]
    }
  }
}
```

Restart Claude Desktop after saving the config.

---

# Example Claude Prompt

```text
Use get_ip_info for 192.168.1.1
```

---

# Workflow

```text
User Query
    ↓
Claude Desktop
    ↓
MCP Tool Call
    ↓
FastAPI Request
    ↓
JSON Data Retrieval
    ↓
Structured Response
```

---

# Outcomes

This project demonstrates:

- MCP server development
- AI tool orchestration
- FastAPI integration
- LLM tool calling
- Backend service communication
- JSON datastore usage
- Claude Desktop MCP integration

---

# Future Improvements

- PostgreSQL integration
- MongoDB support
- Authentication & Authorization
- Async FastAPI endpoints
- Vector database integration
- RAG pipelines
- Multi-agent workflows
- Logging & monitoring
- Docker deployment
- Kubernetes support

---

# Use Cases

- IP intelligence systems
- AI-powered backend tools
- Agentic AI workflows
- Enterprise AI integrations
- Security analysis systems
- Internal AI tool platforms

---

# Author

## Sruthi CS
 AI Engineer | Agentic AI Enthusiast

 
