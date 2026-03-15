from mcp.server.fastmcp import FastMCP
import datetime, json
# print("Server starting...")
mcp = FastMCP("my-server")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Adds two numbers"""
    return a + b

@mcp.tool()
def get_current_time() -> str:
    """Returns the current date and time"""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@mcp.tool()
def summarize_text(text: str, max_words: int = 50) -> str:
    """Truncates text to a word limit as a basic summary"""
    words = text.split()
    if len(words) <= max_words:
        return text
    return " ".join(words[:max_words]) + "..."

@mcp.tool()
def parse_json(raw: str) -> dict:
    """Parses a JSON string and returns the object"""
    return json.loads(raw)

if __name__ == "__main__":
    # on STDIO transport:
    # mcp.run() 
    # on Streamable HTTP transport:
    mcp.run(transport="streamable-http")