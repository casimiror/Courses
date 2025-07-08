from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MathServer")

@mcp.tool()
def add(a:int, b:int) ->int:
    """Adds two integers.

    Args:
        a (int): The first integer to add.
        b (int): The second integer to add.

    Returns:
        int: The sum of the two integers.
    """

    return a + b

@mcp.tool()
def subtract(a:int, b:int) ->int:
    """Subtracts two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The result of subtracting b from a.
    """

    return a - b

@mcp.tool()
def multiply(a:int, b:int) ->int:
    """Multiplies two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The product of the two integers.
    """

    return a * b

# Transport stdio tells the server to:
# - Use standard input/output for communication.
# - Listen for requests on stdin and send function call responses to stdout.


if __name__ == "__main__":
    mcp.run(transport="stdio")
