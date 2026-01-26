from mcp.server.fastmcp import FastMCP
import httpx
mcp =FastMCP("weather")

@mcp.tool()
async def get_weather(city :str)->str:
  """Fetch  weather condtion of the given city"""
  print(city)
  clean_city = city.split(",")[0].strip()
  clean_city = clean_city.replace(" city", "")

  url = f"https://wttr.in/{clean_city}?format=%C+%t"

  async with httpx.AsyncClient() as client:
        response = await client.get(url)
  return  (f"Weather in {clean_city.lower()} is {response.text}")

if __name__=="__main__":
  mcp.run(transport="streamable-http")
