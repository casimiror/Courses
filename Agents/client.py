from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
import asyncio

load_dotenv()

async def main():
    # Create a client to connect to the MCP server
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["-m", "math_server_stdio"],
                "transport": "stdio",
            },
            "weather": {
                "url": "http://localhost:8000/mcp",
                "transport": "streamable_http",
            },
            
        }
    )
    import os
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
    # Create a React agent using the client
    
    tools = await client.get_tools()
    model = ChatOpenAI(model="gpt-4o")
    agent = create_react_agent(
        model=model,
        tools=tools,
    )

    
    # Run the agent with an initial message
    response = await agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What's (3+5) x 12?",
                }
            ]
        }
    )
    print("Result:", response["messages"][-1].content)

asyncio.run(main())

