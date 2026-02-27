from fastmcp import FastMCP

mcp = FastMCP("CalmServer")

@mcp.tool()
def get_guidance(trigger: str, modality: str) -> str:
    # Minimal logic to prevent any internal crashes
    return f"Guidance for {trigger} ({modality}): Take three deep breaths and focus on the present."

if __name__ == "__main__":
    # We use 'sse' and '0.0.0.0' to ensure Windows allows the connection
    print("Starting server on http://127.0.0.1")
    mcp.run(transport="sse", host="127.0.0.1", port=8000)
