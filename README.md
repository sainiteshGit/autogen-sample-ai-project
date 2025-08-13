# autogen-ai-project

A sample AI project demonstrating agent-based architecture, domain-specific prompts, and integration with Azure AI models.

## Features

- Modular API for agent orchestration
- Domain-specific prompt management
- Azure AI model integration
- Database utilities
- Service and team management

## Project Structure

```
autogen-sample-ai-project/
├── .env
├── .gitignore
├── README.md
├── requirements.txt
└── api/
	├── agent_domain_prompts.py
	├── agents.py
	├── api.py
	├── azureaimodels.py
	├── db.py
	├── main.py
	├── services.py
	├── teams.py
	└── __pycache__/
```

## Setup

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure environment variables in `.env` as needed.

## Usage

Run the main API entry point:
```bash
python api/main.py
```

## Modules

- `agent_domain_prompts.py`: Handles domain-specific prompts for agents.
- `agents.py`: Defines agent logic and orchestration.
- `api.py`: API endpoints and routing.
- `azureaimodels.py`: Azure AI model integration utilities.
- `db.py`: Database connection and operations.
- `services.py`: Service layer for business logic.
- `teams.py`: Team management utilities.

## Contributing

Feel free to open issues or submit pull requests for improvements.


### Additonal Info

```
python3.11 -m venv antenv

echo ">>> Activating virtual environment..."
source ./antenv/bin/activate

python3.11 -m pip install -r requirements.txt

```