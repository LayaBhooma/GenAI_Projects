from fastmcp import FastMCP
#from duckduckgo_search import DDGS
from ddgs import DDGS

mcp = FastMCP("beginner-websearch")

@mcp.tool()
def search_web(query: str, max_results: int = 5) -> dict:
    """
    Search the internet using DuckDuckGo and return top results.

    Args:
        query: search query
        max_results: number of results to return
    """
    results = []
    try: 
        with DDGS(timeout=30) as ddgs:
            search_gen = ddgs.text(query, max_results=max_results, backend="lite")
            for r in search_gen:
                results.append({
                    "title": r.get("title"),
                    "url": r.get("href"),
                    "snippet": r.get("body"),
                })
    except Exception as e:
        return {"query": query, "count": len(results), "results": results, "error": str(e)}
        
    return {"query": query, "count": len(results), "results": results}
if __name__ == "__main__":
    mcp.run()
    # Run as HTTP server
    # mcp.run_http(host="127.0.0.1", port=3333)
