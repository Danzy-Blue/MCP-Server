# MCP-Server
A simple MCP Server built with FastMCP, exposing tools for addition, current time, text summarization, and JSON parsing over Streamable HTTP.


# MCP Server

A simple **Model Context Protocol (MCP) Server** built with `FastMCP`.  
This server exposes a few basic tools that can be used by an MCP client:

- Add two numbers
- Get the current date and time
- Summarize text by truncating to a word limit
- Parse a raw JSON string into an object

The server is configured to run over **Streamable HTTP**.

---

## Features

This MCP Server provides the following tools:

### `add(a: int, b: int) -> int`
Returns the sum of two integers.

### `get_current_time() -> str`
Returns the current local date and time in the format:

`YYYY-MM-DD HH:MM:SS`

### `summarize_text(text: str, max_words: int = 50) -> str`
Creates a basic summary by truncating the input text to a maximum number of words.

### `parse_json(raw: str) -> dict`
Parses a JSON string and returns the corresponding object.

---

## Project Structure

```bash
myserver.py
