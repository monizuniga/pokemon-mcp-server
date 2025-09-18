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
    
    async def get_ability(self, ability_id_or_name: str) -> Dict[str, Any]:
        """Get detailed information about a Pokemon ability."""
        url = f"{self.BASE_URL}/ability/{ability_id_or_name.lower()}"
        
        try:
            response = await self.client.get(url)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            return {"error": f"HTTP error: {str(e)}"}
        except Exception as e:
            return {"error": f"Unexpected error: {str(e)}"}
    
    async def get_egg_group(self, egg_group_id_or_name: str) -> Dict[str, Any]:
        """Get data about an egg group."""
        url = f"{self.BASE_URL}/egg-group/{egg_group_id_or_name.lower()}"
        
        try:
            response = await self.client.get(url)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            return {"error": f"HTTP error: {str(e)}"}
        except Exception as e:
            return {"error": f"Unexpected error: {str(e)}"}
    
    async def get_gender(self, gender_id_or_name: str) -> Dict[str, Any]:
        """Get information on a Pokemon gender."""
        url = f"{self.BASE_URL}/gender/{gender_id_or_name.lower()}"
        
        try:
            response = await self.client.get(url)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            return {"error": f"HTTP error: {str(e)}"}
        except Exception as e:
            return {"error": f"Unexpected error: {str(e)}"}
    
    async def get_growth_rate(self, growth_rate_id_or_name: str) -> Dict[str, Any]:
        """Get how experience required per level grows for different species."""
        url = f"{self.BASE_URL}/growth-rate/{growth_rate_id_or_name.lower()}"
        
        try:
            response = await self.client.get(url)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            return {"error": f"HTTP error: {str(e)}"}
        except Exception as e:
            return {"error": f"Unexpected error: {str(e)}"}
    
    async def get_nature(self, nature_id_or_name: str) -> Dict[str, Any]:
        """Get Pokemon nature information including stat boosts/debuffs."""
        url = f"{self.BASE_URL}/nature/{nature_id_or_name.lower()}"
        
        try:
            response = await self.client.get(url)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            return {"error": f"HTTP error: {str(e)}"}
        except Exception as e:
            return {"error": f"Unexpected error: {str(e)}"}
    
    async def get_pokeathlon_stat(self, pokeathlon_stat_id_or_name: str) -> Dict[str, Any]:
        """Get stats used in Pokeathlon competitions."""
        url = f"{self.BASE_URL}/pokeathlon-stat/{pokeathlon_stat_id_or_name.lower()}"
        
        try:
            response = await self.client.get(url)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            return {"error": f"HTTP error: {str(e)}"}
        except Exception as e:
            return {"error": f"Unexpected error: {str(e)}"}
    
    async def get_pokemon_color(self, color_id_or_name: str) -> Dict[str, Any]:
        """Get the color category of a Pokemon species."""
        url = f"{self.BASE_URL}/pokemon-color/{color_id_or_name.lower()}"
        
        try:
            response = await self.client.get(url)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            return {"error": f"HTTP error: {str(e)}"}
        except Exception as e:
            return {"error": f"Unexpected error: {str(e)}"}
    
    async def get_pokemon_form(self, form_id_or_name: str) -> Dict[str, Any]:
        """Get a particular form/variation of a Pokemon."""
        url = f"{self.BASE_URL}/pokemon-form/{form_id_or_name.lower()}"
        
        try:
            response = await self.client.get(url)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            return {"error": f"HTTP error: {str(e)}"}
        except Exception as e:
            return {"error": f"Unexpected error: {str(e)}"}
    
    async def get_pokemon_habitat(self, habitat_id_or_name: str) -> Dict[str, Any]:
        """Get where the Pokemon species tends to live."""
        url = f"{self.BASE_URL}/pokemon-habitat/{habitat_id_or_name.lower()}"
        
        try:
            response = await self.client.get(url)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            return {"error": f"HTTP error: {str(e)}"}
        except Exception as e:
            return {"error": f"Unexpected error: {str(e)}"}
    
    async def get_pokemon_shape(self, shape_id_or_name: str) -> Dict[str, Any]:
        """Get the general shape classification for a Pokemon species."""
        url = f"{self.BASE_URL}/pokemon-shape/{shape_id_or_name.lower()}"
        
        try:
            response = await self.client.get(url)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            return {"error": f"HTTP error: {str(e)}"}
        except Exception as e:
            return {"error": f"Unexpected error: {str(e)}"}
    
    async def get_pokemon_species(self, species_id_or_name: str) -> Dict[str, Any]:
        """Get species-level data including evolution, varieties, flavor texts."""
        url = f"{self.BASE_URL}/pokemon-species/{species_id_or_name.lower()}"
        
        try:
            response = await self.client.get(url)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            return {"error": f"HTTP error: {str(e)}"}
        except Exception as e:
            return {"error": f"Unexpected error: {str(e)}"}
    
    async def get_type(self, type_id_or_name: str) -> Dict[str, Any]:
        """Get data about Pokemon types including effectiveness."""
        url = f"{self.BASE_URL}/type/{type_id_or_name.lower()}"
        
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
async def get_pokemon_list(limit: int = 20, offset: int = 0) -> str:
    """
    Get a list of Pokemon with pagination support.
    
    Args:
        limit: Number of Pokemon to return (default: 20, max: 100)
        offset: Number of Pokemon to skip (default: 0)
    
    Returns:
        JSON string containing the list of Pokemon with their names and URLs
    """
    result = await pokemon_api.get_pokemon_list(limit=limit, offset=offset)
    return json.dumps(result, indent=2)


@mcp.tool()
async def get_pokemon_details(name: str) -> str:
    """
    Get detailed information about a specific Pokemon by name.
    
    Args:
        name: The name of the Pokemon (e.g., 'pikachu', 'charizard')
    
    Returns:
        JSON string containing detailed Pokemon information including stats, abilities, types, etc.
    """
    result = await pokemon_api.get_pokemon_by_name(name)
    return json.dumps(result, indent=2)


@mcp.tool()
async def get_pokemon_by_id(pokemon_id: int) -> str:
    """
    Get detailed information about a specific Pokemon by ID.
    
    Args:
        pokemon_id: The ID of the Pokemon (e.g., 1 for Bulbasaur, 25 for Pikachu)
    
    Returns:
        JSON string containing detailed Pokemon information including stats, abilities, types, etc.
    """
    result = await pokemon_api.get_pokemon_by_id(pokemon_id)
    return json.dumps(result, indent=2)


@mcp.tool()
async def search_pokemon(query: str, limit: int = 10) -> str:
    """
    Search for Pokemon by name (partial matching).
    
    Args:
        query: The search query (partial Pokemon name)
        limit: Maximum number of results to return (default: 10)
    
    Returns:
        JSON string containing matching Pokemon names and their details
    """
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


@mcp.tool()
async def get_ability(ability_id_or_name: str) -> str:
    """
    Get detailed information about a Pokemon ability.
    
    Args:
        ability_id_or_name: The ID or name of the ability (e.g., 'blaze', '1')
    
    Returns:
        JSON string containing ability details including effect, generation, etc.
    """
    result = await pokemon_api.get_ability(ability_id_or_name)
    return json.dumps(result, indent=2)


@mcp.tool()
async def get_egg_group(egg_group_id_or_name: str) -> str:
    """
    Get data about an egg group (which determines breeding compatibility).
    
    Args:
        egg_group_id_or_name: The ID or name of the egg group (e.g., 'monster', '1')
    
    Returns:
        JSON string containing egg group data and compatible Pokemon species
    """
    result = await pokemon_api.get_egg_group(egg_group_id_or_name)
    return json.dumps(result, indent=2)


@mcp.tool()
async def get_gender(gender_id_or_name: str) -> str:
    """
    Get information on a Pokemon gender and which species can have it.
    
    Args:
        gender_id_or_name: The ID or name of the gender (e.g., 'male', '1')
    
    Returns:
        JSON string containing gender information and compatible species
    """
    result = await pokemon_api.get_gender(gender_id_or_name)
    return json.dumps(result, indent=2)


@mcp.tool()
async def get_growth_rate(growth_rate_id_or_name: str) -> str:
    """
    Get how experience required per level grows for different species.
    
    Args:
        growth_rate_id_or_name: The ID or name of the growth rate (e.g., 'medium-slow', '1')
    
    Returns:
        JSON string containing growth rate data and experience requirements
    """
    result = await pokemon_api.get_growth_rate(growth_rate_id_or_name)
    return json.dumps(result, indent=2)


@mcp.tool()
async def get_nature(nature_id_or_name: str) -> str:
    """
    Get Pokemon nature information including stat boosts/debuffs and preferences.
    
    Args:
        nature_id_or_name: The ID or name of the nature (e.g., 'adamant', '1')
    
    Returns:
        JSON string containing nature data including stat modifications and flavor preferences
    """
    result = await pokemon_api.get_nature(nature_id_or_name)
    return json.dumps(result, indent=2)


@mcp.tool()
async def get_pokeathlon_stat(pokeathlon_stat_id_or_name: str) -> str:
    """
    Get stats used in Pokeathlon competitions.
    
    Args:
        pokeathlon_stat_id_or_name: The ID or name of the Pokeathlon stat (e.g., 'speed', '1')
    
    Returns:
        JSON string containing Pokeathlon stat data
    """
    result = await pokemon_api.get_pokeathlon_stat(pokeathlon_stat_id_or_name)
    return json.dumps(result, indent=2)


@mcp.tool()
async def get_pokemon_color(color_id_or_name: str) -> str:
    """
    Get the color category of a Pokemon species (used for Pokedex sorting).
    
    Args:
        color_id_or_name: The ID or name of the color (e.g., 'red', '1')
    
    Returns:
        JSON string containing color data and Pokemon species with this color
    """
    result = await pokemon_api.get_pokemon_color(color_id_or_name)
    return json.dumps(result, indent=2)


@mcp.tool()
async def get_pokemon_form(form_id_or_name: str) -> str:
    """
    Get a particular form/variation of a Pokemon (cosmetic or otherwise).
    
    Args:
        form_id_or_name: The ID or name of the form (e.g., 'pikachu-rock-star', '1')
    
    Returns:
        JSON string containing form data including stats, sprites, and type changes
    """
    result = await pokemon_api.get_pokemon_form(form_id_or_name)
    return json.dumps(result, indent=2)


@mcp.tool()
async def get_pokemon_habitat(habitat_id_or_name: str) -> str:
    """
    Get where the Pokemon species tends to live (habitat).
    
    Args:
        habitat_id_or_name: The ID or name of the habitat (e.g., 'cave', '1')
    
    Returns:
        JSON string containing habitat data and Pokemon species that live there
    """
    result = await pokemon_api.get_pokemon_habitat(habitat_id_or_name)
    return json.dumps(result, indent=2)


@mcp.tool()
async def get_pokemon_shape(shape_id_or_name: str) -> str:
    """
    Get the general shape classification for a Pokemon species.
    
    Args:
        shape_id_or_name: The ID or name of the shape (e.g., 'quadruped', '1')
    
    Returns:
        JSON string containing shape data and Pokemon species with this shape
    """
    result = await pokemon_api.get_pokemon_shape(shape_id_or_name)
    return json.dumps(result, indent=2)


@mcp.tool()
async def get_pokemon_species(species_id_or_name: str) -> str:
    """
    Get species-level data including evolution, varieties, flavor texts, etc.
    
    Args:
        species_id_or_name: The ID or name of the species (e.g., 'pikachu', '25')
    
    Returns:
        JSON string containing species data including evolution chain, varieties, and flavor text
    """
    result = await pokemon_api.get_pokemon_species(species_id_or_name)
    return json.dumps(result, indent=2)


@mcp.tool()
async def get_type(type_id_or_name: str) -> str:
    """
    Get data about Pokemon types including effectiveness against other types.
    
    Args:
        type_id_or_name: The ID or name of the type (e.g., 'fire', '10')
    
    Returns:
        JSON string containing type data including damage relations and Pokemon of this type
    """
    result = await pokemon_api.get_type(type_id_or_name)
    return json.dumps(result, indent=2)


def calculate_type_effectiveness(attacking_type: str, defending_types: List[str], type_data: Dict[str, Any]) -> float:
    """
    Calculate type effectiveness multiplier based on type matchups.
    
    Args:
        attacking_type: The type of the attacking move
        defending_types: List of defending Pokemon's types
        type_data: Type data from PokeAPI containing damage relations
    
    Returns:
        Effectiveness multiplier (0.25, 0.5, 1.0, 2.0, or 4.0)
    """
    if "damage_relations" not in type_data:
        return 1.0
    
    damage_relations = type_data["damage_relations"]
    
    # Get lists of types that are super effective, not very effective, and no effect
    super_effective = [t["name"] for t in damage_relations.get("double_damage_to", [])]
    not_very_effective = [t["name"] for t in damage_relations.get("half_damage_to", [])]
    no_effect = [t["name"] for t in damage_relations.get("no_damage_to", [])]
    
    effectiveness = 1.0
    
    for defending_type in defending_types:
        if defending_type in no_effect:
            effectiveness *= 0.0
        elif defending_type in super_effective:
            effectiveness *= 2.0
        elif defending_type in not_very_effective:
            effectiveness *= 0.5
    
    return effectiveness


def calculate_battle_score(pokemon_data: Dict[str, Any], opponent_types: List[str], type_effectiveness: float) -> Dict[str, Any]:
    """
    Calculate a battle score for a Pokemon based on stats and type effectiveness.
    
    Args:
        pokemon_data: Pokemon data from PokeAPI
        opponent_types: List of opponent Pokemon's types
        type_effectiveness: Type effectiveness multiplier
    
    Returns:
        Dictionary containing battle score and analysis
    """
    if "stats" not in pokemon_data:
        return {"score": 0, "analysis": "No stats available"}
    
    # Extract base stats
    stats = {}
    for stat in pokemon_data["stats"]:
        stat_name = stat["stat"]["name"]
        base_stat = stat["base_stat"]
        stats[stat_name] = base_stat
    
    # Calculate weighted battle score
    # HP, Attack, Defense, Special Attack, Special Defense, Speed
    battle_score = (
        stats.get("hp", 0) * 0.15 +
        stats.get("attack", 0) * 0.20 +
        stats.get("defense", 0) * 0.15 +
        stats.get("special-attack", 0) * 0.20 +
        stats.get("special-defense", 0) * 0.15 +
        stats.get("speed", 0) * 0.15
    )
    
    # Apply type effectiveness multiplier
    battle_score *= type_effectiveness
    
    # Analyze strengths and weaknesses
    analysis = []
    
    # Type effectiveness analysis
    if type_effectiveness >= 2.0:
        analysis.append(f"Super effective against opponent (x{type_effectiveness})")
    elif type_effectiveness <= 0.5:
        analysis.append(f"Not very effective against opponent (x{type_effectiveness})")
    elif type_effectiveness == 0.0:
        analysis.append("No effect against opponent")
    else:
        analysis.append(f"Normal effectiveness against opponent (x{type_effectiveness})")
    
    # Stat analysis
    if stats.get("attack", 0) > stats.get("special-attack", 0):
        analysis.append("Physical attacker")
    elif stats.get("special-attack", 0) > stats.get("attack", 0):
        analysis.append("Special attacker")
    else:
        analysis.append("Balanced attacker")
    
    if stats.get("speed", 0) > 100:
        analysis.append("High speed - likely to attack first")
    elif stats.get("speed", 0) < 50:
        analysis.append("Low speed - likely to attack last")
    
    if stats.get("hp", 0) > 100:
        analysis.append("High HP - good survivability")
    
    if stats.get("defense", 0) > 100 or stats.get("special-defense", 0) > 100:
        analysis.append("High defenses - good tanking ability")
    
    return {
        "score": round(battle_score, 2),
        "stats": stats,
        "analysis": analysis,
        "type_effectiveness": type_effectiveness
    }


@mcp.tool()
async def compare_pokemon_battle(pokemon1_name: str, pokemon2_name: str) -> str:
    """
    Compare two Pokemon in battle and determine which would win and why.
    
    Args:
        pokemon1_name: Name of the first Pokemon (e.g., 'pikachu')
        pokemon2_name: Name of the second Pokemon (e.g., 'charizard')
    
    Returns:
        JSON string containing battle analysis, winner prediction, and detailed reasoning
    """
    # Get Pokemon data
    pokemon1_data = await pokemon_api.get_pokemon_by_name(pokemon1_name)
    pokemon2_data = await pokemon_api.get_pokemon_by_name(pokemon2_name)
    
    if "error" in pokemon1_data:
        return json.dumps({"error": f"Error fetching {pokemon1_name}: {pokemon1_data['error']}"}, indent=2)
    
    if "error" in pokemon2_data:
        return json.dumps({"error": f"Error fetching {pokemon2_name}: {pokemon2_data['error']}"}, indent=2)
    
    # Extract Pokemon types
    pokemon1_types = [t["type"]["name"] for t in pokemon1_data.get("types", [])]
    pokemon2_types = [t["type"]["name"] for t in pokemon2_data.get("types", [])]
    
    # Get type data for effectiveness calculations
    pokemon1_type_data = {}
    pokemon2_type_data = {}
    
    for pokemon_type in pokemon1_types:
        type_data = await pokemon_api.get_type(pokemon_type)
        if "error" not in type_data:
            pokemon1_type_data[pokemon_type] = type_data
    
    for pokemon_type in pokemon2_types:
        type_data = await pokemon_api.get_type(pokemon_type)
        if "error" not in type_data:
            pokemon2_type_data[pokemon_type] = type_data
    
    # Calculate type effectiveness for each Pokemon against the other
    pokemon1_effectiveness = 1.0
    pokemon2_effectiveness = 1.0
    
    # Pokemon1's effectiveness against Pokemon2
    for pokemon1_type in pokemon1_types:
        if pokemon1_type in pokemon1_type_data:
            effectiveness = calculate_type_effectiveness(
                pokemon1_type, pokemon2_types, pokemon1_type_data[pokemon1_type]
            )
            pokemon1_effectiveness *= effectiveness
    
    # Pokemon2's effectiveness against Pokemon1
    for pokemon2_type in pokemon2_types:
        if pokemon2_type in pokemon2_type_data:
            effectiveness = calculate_type_effectiveness(
                pokemon2_type, pokemon1_types, pokemon2_type_data[pokemon2_type]
            )
            pokemon2_effectiveness *= effectiveness
    
    # Calculate battle scores
    pokemon1_score = calculate_battle_score(pokemon1_data, pokemon2_types, pokemon1_effectiveness)
    pokemon2_score = calculate_battle_score(pokemon2_data, pokemon1_types, pokemon2_effectiveness)
    
    # Determine winner
    if pokemon1_score["score"] > pokemon2_score["score"]:
        winner = pokemon1_name.title()
        winner_score = pokemon1_score["score"]
        loser_score = pokemon2_score["score"]
        margin = winner_score - loser_score
    elif pokemon2_score["score"] > pokemon1_score["score"]:
        winner = pokemon2_name.title()
        winner_score = pokemon2_score["score"]
        loser_score = pokemon1_score["score"]
        margin = winner_score - loser_score
    else:
        winner = "Tie"
        winner_score = pokemon1_score["score"]
        loser_score = pokemon2_score["score"]
        margin = 0
    
    # Create detailed battle analysis
    battle_analysis = {
        "pokemon1": {
            "name": pokemon1_name.title(),
            "types": pokemon1_types,
            "score": pokemon1_score["score"],
            "stats": pokemon1_score["stats"],
            "type_effectiveness_against_opponent": pokemon1_effectiveness,
            "analysis": pokemon1_score["analysis"]
        },
        "pokemon2": {
            "name": pokemon2_name.title(),
            "types": pokemon2_types,
            "score": pokemon2_score["score"],
            "stats": pokemon2_score["stats"],
            "type_effectiveness_against_opponent": pokemon2_effectiveness,
            "analysis": pokemon2_score["analysis"]
        },
        "battle_result": {
            "winner": winner,
            "winner_score": winner_score,
            "loser_score": loser_score,
            "score_difference": round(margin, 2),
            "confidence": "High" if margin > 50 else "Medium" if margin > 20 else "Low"
        },
        "battle_summary": {
            "type_advantage": f"{pokemon1_name.title()} has {pokemon1_effectiveness}x effectiveness against {pokemon2_name.title()}, while {pokemon2_name.title()} has {pokemon2_effectiveness}x effectiveness against {pokemon1_name.title()}",
            "key_factors": [
                f"{pokemon1_name.title()}'s battle score: {pokemon1_score['score']}",
                f"{pokemon2_name.title()}'s battle score: {pokemon2_score['score']}",
                f"Type effectiveness plays a {'major' if max(pokemon1_effectiveness, pokemon2_effectiveness) >= 2.0 or min(pokemon1_effectiveness, pokemon2_effectiveness) <= 0.5 else 'moderate'} role in this matchup"
            ]
        }
    }
    
    return json.dumps(battle_analysis, indent=2)


# Cleanup function for graceful shutdown
async def cleanup():
    """Cleanup resources on shutdown."""
    await pokemon_api.close()


if __name__ == "__main__":
    # Run the MCP server
    import sys
    try:
        # FastMCP.run uses AnyIO internally and manages its own event loop.
        # Call it directly to avoid nesting event loops.
        mcp.run(transport="stdio")
    except KeyboardInterrupt:
        print("Server shutting down...")
    finally:
        asyncio.run(cleanup())
