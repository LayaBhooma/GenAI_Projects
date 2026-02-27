import asyncio
from fastmcp import Client
from fastmcp.client import SSETransport

async def main():
    # This URL matches the server exactly
    url = "http://127.0.0.1:8000/sse"
    
    print(f"Connecting to {url}...")
    try:
        # Using the SSETransport that we verified earlier
        async with Client(SSETransport(url)) as session:
            print("Connected!")
            
            # Requesting the tool
            result = await session.call_tool("get_guidance", {
                "trigger": "anxiety",
                "modality": "DBT"
            })
            
            # Print the result
            print("\nServer Response:")
            for block in result.content:
                print(block.text)
                
    except Exception as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    asyncio.run(main())
