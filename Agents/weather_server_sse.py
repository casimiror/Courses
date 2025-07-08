from mcp.server.fastmcp import FastMCP

mcp = FastMCP("WeatherServer")

@mcp.tool()
def get_weather(city: str) -> dict:
    """Gets the current weather for a specific city.

    Args:
        city (str): The name of the city to get the weather for.

    Returns:
        dict: A dictionary containing the weather information.
    """

    # Simulated weather data
    weather_data = {
        "city": city,
        "temperature": 22,
        "description": "Sunny",
    }

    return weather_data


# Transport stdio tells the server to:
# - Use standard input/output for communication.
# - Listen for requests on stdin and send function call responses to stdout.


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
