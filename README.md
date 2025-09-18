# Pokemon MCP Server

A simple Model Context Protocol (MCP) server that provides Pokemon data via the [PokeAPI](https://pokeapi.co/).

## Features

This MCP server provides the following tools:

- **get_pokemon_list**: Get a paginated list of Pokemon
- **get_pokemon_details**: Get detailed information about a specific Pokemon by name
- **get_pokemon_by_id**: Get detailed information about a specific Pokemon by ID
- **search_pokemon**: Search for Pokemon by name with partial matching

## Setup

1. **Create and activate virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Server

To run the MCP server:

```bash
python pokemon_server.py
```

The server will start and listen for MCP protocol messages via stdio.

### Available Tools

#### 1. Get Pokemon List

```python
get_pokemon_list(limit=20, offset=0)
```

- `limit`: Number of Pokemon to return (default: 20, max: 100)
- `offset`: Number of Pokemon to skip (default: 0)

#### 2. Get Pokemon Details by Name

```python
get_pokemon_details(name="pikachu")
```

- `name`: The name of the Pokemon (case-insensitive)

#### 3. Get Pokemon Details by ID

```python
get_pokemon_by_id(pokemon_id=25)
```

- `pokemon_id`: The ID of the Pokemon (1 for Bulbasaur, 25 for Pikachu, etc.)

#### 4. Search Pokemon

```python
search_pokemon(query="char", limit=10)
```

- `query`: Partial Pokemon name to search for
- `limit`: Maximum number of results to return

## Example Responses

### Pokemon List

```json
{
  "count": 1302,
  "next": "https://pokeapi.co/api/v2/pokemon/?offset=20&limit=20",
  "previous": null,
  "results": [
    {
      "name": "bulbasaur",
      "url": "https://pokeapi.co/api/v2/pokemon/1/"
    },
    {
      "name": "ivysaur",
      "url": "https://pokeapi.co/api/v2/pokemon/2/"
    }
  ]
}
```

### Pokemon Details

```json
{
  "id": 25,
  "name": "pikachu",
  "height": 4,
  "weight": 60,
  "base_experience": 112,
  "types": [
    {
      "slot": 1,
      "type": {
        "name": "electric",
        "url": "https://pokeapi.co/api/v2/type/13/"
      }
    }
  ],
  "stats": [
    {
      "base_stat": 35,
      "effort": 0,
      "stat": {
        "name": "hp",
        "url": "https://pokeapi.co/api/v2/stat/1/"
      }
    }
  ],
  "abilities": [
    {
      "ability": {
        "name": "static",
        "url": "https://pokeapi.co/api/v2/ability/9/"
      },
      "is_hidden": false,
      "slot": 1
    }
  ]
}
```

## Error Handling

The server includes proper error handling for:

- Network timeouts and connection issues
- Invalid Pokemon names or IDs
- API rate limiting
- Malformed responses

Errors are returned as JSON with an "error" field containing the error message.

## Dependencies

- `mcp`: Model Context Protocol server framework
- `httpx`: Async HTTP client for API requests
- `pydantic`: Data validation and settings management

## License

This project is open source and available under the MIT License.

## MCP Pokemon Connector

```
{
  "mcpServers": {
    "pokemon": {
      "command": "path/to/venv/bin/python",
      "args": [
        "path/to/pokemon-mcp-server/pokemon_server.py"
      ],
      "env": {
        "PYTHONUNBUFFERED": "1"
      },
      "disabled": false
    }
  }
}
```
