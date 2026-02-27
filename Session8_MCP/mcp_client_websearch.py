import asyncio
from fastmcp import Client
from fastmcp.client import PythonStdioTransport

async def main():
    transport = PythonStdioTransport("mcp_server_websearch.py")

    async with Client(transport) as client:
        # 1) Discover tools
        tools = await client.list_tools()
        print("Tools discovered:", [t.name for t in tools])

        # 2) Call the tool
        query = "super bowl 2026"
        result = await client.call_tool("search_web", {"query": query, "max_results": 5})

        # 3) Print results
        data = result.structured_content or result.data
        print("\nSearch Results:\n", data)

if __name__ == "__main__":
    asyncio.run(main())
