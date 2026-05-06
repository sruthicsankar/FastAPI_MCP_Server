from mcp.server.fastmcp import FastMCP
import requests

# Create MCP server
mcp = FastMCP("IPLookupServer")

@mcp.tool()
def get_ip_info(ip_address: str) -> dict:
    """
    Get IP address details from FastAPI
    """

    url = f"http://127.0.0.1:8000/ip/{ip_address}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return {"error": "IP not found"}

if __name__ == "__main__":
    mcp.run()
    