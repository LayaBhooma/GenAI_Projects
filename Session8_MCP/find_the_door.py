import requests

base = "http://127.0.0.1:8000"
# These are all the possible combinations FastMCP uses
paths = ["/", "/sse", "/mcp", "/mcp/sse", "/mcp/messages"]

print(f"Checking server at {base}...\n")

for p in paths:
    url = f"{base}{p}"
    try:
        # We send the 'Accept' header that MCP requires
        r = requests.get(url, headers={"Accept": "text/event-stream"}, timeout=2)
        print(f"PATH: {p:15} | STATUS: {r.status_code}")
        if r.status_code == 200:
            print(f"  >>> FOUND IT! Use this in SSETransport: {url}\n")
        elif "text/event-stream" in r.text:
            print(f"  >>> FOUND IT (but needs POST)! Use: {url}\n")
    except Exception as e:
        print(f"PATH: {p:15} | ERROR: Connection failed")

print("\nIf all are 404, check your server terminal for the 'Serving on...' line.")
