import requests
import os
from git import Repo

# --- CONFIGURATION ---
GROQ_API_KEY = "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"
FILE_PATH = "main.py"
MODEL = "llama-3.3-70b-versatile"

def call_groq_api(code_snippet):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    # High-level technical system prompt
    system_prompt = """You are a Senior Lua Developer specialized in Roblox Blox Fruit mobile optimization (DeltaX).
TASK: Refactor and optimize the provided script snippet.
OBJECTIVES:
1. Performance: Use task.wait() and task.spawn() to prevent frame drops on mobile.
2. Combat: Enhance HumanoidRootPart tracking and prediction logic.
3. Latency: Make combos 'ping-aware' by implementing dynamic delays.
4. Logic: Simplify complex loops and ensure memory efficiency (avoid leaks).
5. Mobile: Ensure compatibility with VirtualInputManager for touch-emulated key presses (1,2,3,4).

OUTPUT: Return ONLY the optimized Lua code. No markdown, no comments, no chatter."""

    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Optimize this core section of my Blox Fruit script:\n\n{code_snippet}"}
        ],
        "temperature": 0.1, # Low temperature for high precision
        "max_tokens": 4096
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=60)
        if response.status_code == 200:
            content = response.json()['choices'][0]['message']['content']
            # Remove markdown formatting if present
            return content.replace("```lua", "").replace("```", "").strip()
        else:
            print(f"DEBUG: API Error {response.status_code} - {response.text}")
    except Exception as e:
        print(f"DEBUG: Connection failed: {e}")
    return None

def main():
    if not os.path.exists(FILE_PATH):
        print(f"ERROR: {FILE_PATH} not found.")
        return

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        all_lines = f.readlines()

    # STRATEGY: Focus on the first 400 lines (Core Logic & Combat)
    # Most Blox Fruit scripts define their logic/math at the top.
    core_logic = "".join(all_lines[:400])
    footer_logic = "".join(all_lines[400:])

    print(f"PROCESS: AI is evolving the core logic (400 lines)...")
    optimized_code = call_groq_api(core_logic)

    if optimized_code:
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            f.write(optimized_code + "\n" + footer_logic)
        print("SUCCESS: Core logic updated and optimized.")
        
        # Git Operations
        try:
            repo = Repo(".")
            repo.git.add(A=True)
            repo.index.commit("Automation: Technical Refactor for Mobile Performance")
            origin = repo.remote(name='origin')
            origin.push()
            print("GITHUB: Push completed successfully.")
        except Exception as e:
            print(f"GIT_ERROR: {e}")
    else:
        print("FAILURE: AI could not process the request.")

if __name__ == "__main__":
    main()
        
