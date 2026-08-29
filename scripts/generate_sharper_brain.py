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
        # Use active gemini-3.6-flash model identifier
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
        )

        # Create target output directory if it does not exist
        os.makedirs("build", exist_ok=True)
        binary_path = os.path.join("build", "memory_update.bin")

        # Save output response payload to binary file
        with open(binary_path, "wb") as f:
            if response.text:
                f.write(response.text.encode("utf-8"))
            else:
                f.write(b"")

        print(f"[SUCCESS] Memory binary generated successfully at: {binary_path}")
            
    except Exception as e:
        print(f"[FATAL] Failed to generate memory binary: {e}")
        sys.exit(1)

if __name__ == "__main__":
    compile_memory_binary()
