from fastmcp import Client
from fastmcp.client import PythonStdioTransport
import asyncio

async def main():
    transport = PythonStdioTransport("mcp_server_fastmcp.py")

    async with Client(transport) as client:
        tools = await client.list_tools()
        print("Tools:", [t.name for t in tools])

if __name__ == "__main__":
    asyncio.run(main())