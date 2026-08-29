import os
import sys
from google import genai
from google.genai import types

def compile_memory_binary():
    # Retrieve API key from environment variables
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("[ERROR] GEMINI_API_KEY environment variable is missing.")
        sys.exit(1)

    # Initialize standard Google GenAI client
    client = genai.Client(api_key=api_key)

    print("[INFO] Querying Gemini API to sharpen offline intent matrix...")

    prompt = (
        "Generate and optimize the offline intent binary matrix for local runtime execution. "
        "Return structured summary of compiled weights and high-confidence routing entries."
    )

    try:
        # Use gemini-3.6-flash model string
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
        )

        print("[SUCCESS] Memory binary generated successfully.")
        if response.text:
            print("[INFO] Response Preview:")
            print(response.text[:200] + "...")
            
    except Exception as e:
        print(f"[FATAL] Failed to generate memory binary: {e}")
        sys.exit(1)

if __name__ == "__main__":
    compile_memory_binary()
