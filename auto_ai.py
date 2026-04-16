import requests
import os
import time
from git import Repo

# --- CONFIGURATION ---
GROQ_API_KEY = "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"
FILE_PATH = "main.py"
MODEL = "llama-3.3-70b-versatile"

def call_groq_api():
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    
    # Sử dụng Siêu Prompt từ kinh nghiệm của bro
    system_prompt = """You are a senior Roblox Lua developer. 
    Build/Refine MayChemXeoCan V2 based on the technical specs.
    Focus on making the SilentAim and CombatEngine more aggressive and precise.
    OUTPUT: Return ONLY raw Lua code."""

    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": "Analyze the current trends in Roblox DeltaX Blox Fruit PvP and update the script to be even more powerful. Optimize the prediction math."}
        ],
        "temperature": 0.3,
        "max_tokens": 8000
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=300)
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content'].replace("```lua", "").replace("```", "").strip()
    except Exception as e:
        print(f"❌ Error: {e}")
    return None

def main():
    iteration = 1
    while True: # VÒNG LẶP VÔ HẠN
        print(f"\n🚀 BẮT ĐẦU ĐỢT TIẾN HÓA THỨ {iteration}...")
        
        new_script = call_groq_api()

        if new_script and len(new_script) > 1000:
            with open(FILE_PATH, "w", encoding="utf-8") as f:
                f.write(new_script)
            print(f"✅ Đợt {iteration}: Đã cập nhật xong code mới.")
            
            try:
                repo = Repo(".")
                repo.git.add(A=True)
                repo.index.commit(f"Evolution Cycle {iteration}: Auto-Refinement")
                repo.git.push('origin', repo.active_branch.name)
                print(f"🔥 Đã Push đợt {iteration} lên GitHub thành công!")
            except Exception as e:
                print(f"⚠️ Git Error: {e}")
        
        print(f"💤 Nghỉ 5 phút để tránh nghẽn API, sau đó sẽ tiếp tục...")
        time.sleep(300) # Nghỉ 5 phút giữa các đợt update
        iteration += 1

if __name__ == "__main__":
    main()
