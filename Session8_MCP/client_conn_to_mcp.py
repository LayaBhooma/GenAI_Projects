import asyncio
import sys
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    # 1. Define the server parameters
    # This tells the client to run 'python mcp_server_fastmcp.py'
    server_params = StdioServerParameters(
        command=sys.executable, # Uses the python.exe from your .venv
        args=["mcp_server_fastmcp.py"], 
        env=None
    )

    # 2. Establish the transport connection
    async with stdio_client(server_params) as (read, write):
        # 3. Create the session
        async with ClientSession(read, write) as session:
            # 4. Initialize the connection
            await session.initialize()
            print("--- Connection Successful ---")

            # List available tools to verify it's working
            tools = await session.list_tools()
            print(f"Server Tools: {tools}")

if __name__ == "__main__":
    asyncio.run(main())
