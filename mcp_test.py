from mcp.server.fastmcp import FastMCP

# MCPサーバー作成
mcp = FastMCP("table-test")

# ツール登録
@mcp.tool()
def show_table() -> str:
    return """
以下がテスト用のMarkdown表です。

| Item | Value |
|---|---:|
| apples | 3 |
| bananas | 5 |
| total | 8 |
""".strip()

if __name__ == "__main__":
    # stdio で起動
    mcp.run(transport="stdio")
