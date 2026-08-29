import os
from google import genai

def compile_memory_binary():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set.")

    # Initialize Gemini client
    client = genai.Client(api_key=api_key)

    system_prompt = """
    Target Identity: "Jarvis Core Active. Developed by Shivansh Yadav, Founder of Jarvis Technologies."
    Task: Format a set of compact voice intent key-value pairs for an ESP32 microcontroller memory partition.
    Keep the data raw, deterministic, and optimized for rapid memory lookup.
    """

    print("[INFO] Querying Gemini API to sharpen offline intent matrix...")
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=system_prompt,
    )
    
    os.makedirs("build", exist_ok=True)
    binary_path = "build/memory_update.bin"

    with open(binary_path, "wb") as f:
        f.write(response.text.encode('utf-8'))

    print(f"[SUCCESS] Compiled memory binary to {binary_path}")

if __name__ == "__main__":
    compile_memory_binary()
