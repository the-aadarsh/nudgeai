#🚀 NudgeAI
An MCP-powered AI Task & Reminder Agent

NudgeAI is an AI-driven task and reminder system that acts like a personal sidekick — creating tasks, tracking progress, and nudging you at the right time using intelligent tool-calling via Model Context Protocol (MCP).

Instead of manually managing to-do lists, you simply talk to NudgeAI. (Text or Voice)

“If I haven’t finished Python by 8 PM, remind me.”

🧩 Uses a Custom MCP to let the LLM decide which action to take

🛠️ Clean separation between reasoning (LLM) and execution (tools)

💬 Natural language → real actions

This project is designed to be beginner-friendly, yet showcases real AI agent architecture.

✨ Key Features

💬 Chat with an AI agent to manage tasks

✅ Create, list, and complete tasks
⏱️ Time-based reminders

🧠 MCP-based tool calling (LLM does not handle logic)

🖥️ Simple UI built with Jinja templates

🏗️ Tech Stack
Backend: FastAPI
AI / Agents: Custom MCP Server
LLM Integration: OpenAI-compatible client
Database: SQLite (easily swappable)
Frontend: Jinja2 Templates + HTML/CSS + HTMX

🧩 Architecture Overview
User
↓
LLM (Reasoning)
↓ decides tool
MCP Server
↓ executes
Tool (Task / Reminder / Notify)
↓
Database / Action

🔑 The LLM never directly modifies data — it only chooses tools.

🛠️ MCP Tools Implemented
(still under-development)

🧪 Example Prompts

1. “Create a task to study calculus by 7 PM”
2. “What tasks do I have today?”
3. “If I haven’t finished DSA by 9, remind me”
4. “Mark my Python task as done”

🤝 Contributing

Contributions are welcome!

Feel free to open issues or submit pull requests.


Built with ❤️ by Adarsh
