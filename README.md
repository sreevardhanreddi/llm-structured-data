# Structuring Data with LLMs

## Stack

- FAST API
- Docker (for dev and prod)

## Development

```

docker-compose -f docker-compose.dev.yml up --build

```

## Production

```

docker-compose -f docker-compose.prod.yml up --build -d

```

## Required Environment Variables

```
# filename .env

API_KEY=app_api_key
MISTRAL_API_KEY=mistral_api_key


```
