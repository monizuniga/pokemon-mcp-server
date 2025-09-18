"""Pokemon MCP Server - A simple MCP server that provides Pokemon data via the PokeAPI."""

import asyncio
import json
from typing import Any, Dict, List, Optional

import httpx
from mcp.server.fastmcp import FastMCP

# Initialize the MCP server
mcp = FastMCP(name="Pokemon MCP Server")


class PokemonAPI:
    """Client for interacting with the PokeAPI."""
    
    BASE_URL = "https://pokeapi.co/api/v2"
    
    def __init__(self):
        self.client = httpx.AsyncClient(timeout=30.0)
    
    async def close(self):
        """Close the HTTP client."""
        await self.client.aclose()
    
    async def get_pokemon_list(self, limit: int = 20, offset: int = 0) -> Dict[str, Any]:
        """Get a list of Pokemon with pagination."""
        url = f"{self.BASE_URL}/pokemon"
        params = {"limit": limit, "offset": offset}
        
        try:
            response = await self.client.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            return {"error": f"HTTP error: {str(e)}"}
        except Exception as e:
            return {"error": f"Unexpected error: {str(e)}"}
    
    async def get_pokemon_by_name(self, name: str) -> Dict[str, Any]:
        """Get detailed information about a specific Pokemon by name."""
        url = f"{self.BASE_URL}/pokemon/{name.lower()}"
        
        try:
            response = await self.client.get(url)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            return {"error": f"HTTP error: {str(e)}"}
        except Exception as e:
            return {"error": f"Unexpected error: {str(e)}"}
    
    async def get_pokemon_by_id(self, pokemon_id: int) -> Dict[str, Any]:
        """Get detailed information about a specific Pokemon by ID."""
        url = f"{self.BASE_URL}/pokemon/{pokemon_id}"
        
        try:
            response = await self.client.get(url)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            return {"error": f"HTTP error: {str(e)}"}
        except Exception as e:
            return {"error": f"Unexpected error: {str(e)}"}


# Global Pokemon API instance
pokemon_api = PokemonAPI()


@mcp.tool()
def get_pokemon_list(limit: int = 20, offset: int = 0) -> str:
    """
    Get a list of Pokemon with pagination support.
    
    Args:
        limit: Number of Pokemon to return (default: 20, max: 100)
        offset: Number of Pokemon to skip (default: 0)
    
    Returns:
        JSON string containing the list of Pokemon with their names and URLs
    """
    async def _get_pokemon_list():
        result = await pokemon_api.get_pokemon_list(limit=limit, offset=offset)
        return json.dumps(result, indent=2)
    
    return asyncio.run(_get_pokemon_list())


@mcp.tool()
def get_pokemon_details(name: str) -> str:
    """
    Get detailed information about a specific Pokemon by name.
    
    Args:
        name: The name of the Pokemon (e.g., 'pikachu', 'charizard')
    
    Returns:
        JSON string containing detailed Pokemon information including stats, abilities, types, etc.
    """
    async def _get_pokemon_details():
        result = await pokemon_api.get_pokemon_by_name(name)
        return json.dumps(result, indent=2)
    
    return asyncio.run(_get_pokemon_details())


@mcp.tool()
def get_pokemon_by_id(pokemon_id: int) -> str:
    """
    Get detailed information about a specific Pokemon by ID.
    
    Args:
        pokemon_id: The ID of the Pokemon (e.g., 1 for Bulbasaur, 25 for Pikachu)
    
    Returns:
        JSON string containing detailed Pokemon information including stats, abilities, types, etc.
    """
    async def _get_pokemon_by_id():
        result = await pokemon_api.get_pokemon_by_id(pokemon_id)
        return json.dumps(result, indent=2)
    
    return asyncio.run(_get_pokemon_by_id())


@mcp.tool()
def search_pokemon(query: str, limit: int = 10) -> str:
    """
    Search for Pokemon by name (partial matching).
    
    Args:
        query: The search query (partial Pokemon name)
        limit: Maximum number of results to return (default: 10)
    
    Returns:
        JSON string containing matching Pokemon names and their details
    """
    async def _search_pokemon():
        # First get a list of Pokemon
        pokemon_list = await pokemon_api.get_pokemon_list(limit=1000, offset=0)
        
        if "error" in pokemon_list:
            return json.dumps(pokemon_list, indent=2)
        
        # Filter Pokemon that match the query
        query_lower = query.lower()
        matching_pokemon = [
            pokemon for pokemon in pokemon_list.get("results", [])
            if query_lower in pokemon["name"].lower()
        ][:limit]
        
        result = {
            "query": query,
            "matches": len(matching_pokemon),
            "results": matching_pokemon
        }
        
        return json.dumps(result, indent=2)
    
    return asyncio.run(_search_pokemon())


# Cleanup function for graceful shutdown
async def cleanup():
    """Cleanup resources on shutdown."""
    await pokemon_api.close()


if __name__ == "__main__":
    # Run the MCP server using stdio
    try:
        asyncio.run(mcp.run_stdio_async())
    except KeyboardInterrupt:
        print("Server shutting down...")
    finally:
        asyncio.run(cleanup())
