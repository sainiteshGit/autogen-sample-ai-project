import asyncio
from teams import get_healthcare_team

async def main(query: str):
    """
    Handles a healthcare emergency scenario asynchronously by delegating the task to the healthcare MAS team,
    retrieving the latest response, and processing the result. If the response ends with "TERMINATE",
    the suffix is removed and the result is stripped of leading/trailing whitespace.
    
    Args:
        query (str): The healthcare scenario query to be processed.
        
    Returns:
        str: The processed response from the healthcare MAS team.
    """
    healthcare_team = get_healthcare_team()
    response = await healthcare_team.run(task=query)
    result = response.messages[-1].content

    if result.endswith("TERMINATE"):
        result = result.removesuffix("TERMINATE").strip()

    return result

if __name__ == "__main__":
    query = "Patients with heart conditions."
    response = asyncio.run(main(query))
    print(response)