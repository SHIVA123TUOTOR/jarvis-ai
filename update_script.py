import os
from google import genai

# Read the API key injected by GitHub Actions
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY secret is missing.")

client = genai.Client(api_key=api_key)

# Query Gemini
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Generate a quick daily update summary."
)

# Output result to file
with open("daily_output.txt", "w", encoding="utf-8") as f:
    f.write(response.text)

print("Update completed successfully.")
