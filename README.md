python3.11 -m venv antenv

echo ">>> Activating virtual environment..."
source ./antenv/bin/activate

python3.11 -m pip install -r requirements.txt

1. Create Azure OpenAI resource
2. Extract the key info and set the environment variables
3. Create the azureaimodels.py file 