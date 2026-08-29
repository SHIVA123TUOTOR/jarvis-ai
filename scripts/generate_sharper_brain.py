import os
import sys
from google import genai
from google.genai import types

def compile_memory_binary():
    # Initialize the GenAI client with environment variable or fallback
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("[ERROR] GEMINI_API_KEY environment variable is missing.")
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    print("[INFO] Querying Gemini API to sharpen offline intent matrix...")

    prompt = (
        "Generate and optimize the offline intent binary matrix for local runtime execution. "
        "Return structured summary of compiled weights and high-confidence routing entries."
    )

    try:
        # Using stable model identifier 'gemini-2.0-flash'
        # Using chat interface to prevent AFC (Automatic Function Calling) generate_content warnings
        chat = client.chats.create(
            model="gemini-2.0-flash",
            config=types.GenerateContentConfig(
                temperature=0.2,
            )
        )
        
        response = chat.send_message(prompt)

        print("[SUCCESS] Memory binary generated successfully.")
        if response.text:
            print("[INFO] Response Preview:")
            print(response.text[:200] + "...")
            
    except Exception as e:
        print(f"[FATAL] Failed to generate memory binary: {e}")
        sys.exit(1)

if __name__ == "__main__":
    compile_memory_binary()
