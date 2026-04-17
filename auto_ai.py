import requests
import os
import time
from git import Repo

# --- CONFIGURATION ---
# Lấy token từ môi trường máy (không ghi đè mã vào đây)
GITHUB_TOKEN = os.getenv("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")
FILE_PATH = "main.py"
MODEL = "deepseek-v3" 
URL = "https://models.inference.ai.azure.com/chat/completions"

def call_github_model(full_code):
    if not GITHUB_TOKEN:
        print("❌ Lỗi: Chưa nạp mã MY_GITHUB_TOKEN vào hệ thống!")
        return None

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Content-Type": "application/json"
    }
    
    system_instruction = """You are a senior Roblox Lua developer. 
    Refine 'MayChemXeoCan V2' with:
    - Modular architecture
    - Mobile Delta X optimization
    - __namecall SilentAim
    - Pure 1-4 numeric hotkey logic (no inventory scan)
    Make it aggressive and predictive. Return ONLY raw Lua code."""

    data = {
        "messages": [
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": f"Upgrade this code:\n{full_code}"}
        ],
        "model": MODEL,
        "temperature": 0.2
    }

    try:
        response = requests.post(URL, headers=headers, json=data, timeout=150)
        if response.status_code == 200:
            content = response.json()['choices'][0]['message']['content']
            return content.replace("```lua", "").replace("```", "").strip()
        else:
            print(f"❌ GitHub API Error: {response.status_code}")
    except Exception as e:
        print(f"❌ Exception: {e}")
    return None

def main():
    iteration = 1
    if not GITHUB_TOKEN:
        print("❌ BRO CHƯA NHẬP MÃ! Hãy chạy lệnh: export MY_GITHUB_TOKEN=ghp_... && python auto_ai.py")
        return

    while True:
        print(f"\n🚀 [DEEPSEEK-V3] TIẾN HÓA ĐỢT {iteration}...")
        
        if not os.path.exists(FILE_PATH):
            with open(FILE_PATH, 'w') as f: f.write("-- MayChemXeoCan V2 Initial")
            
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            full_code = f.read()

        new_script = call_github_model(full_code)

        if new_script and len(new_script) > 500:
            with open(FILE_PATH, "w", encoding="utf-8") as f:
                f.write(new_script)
            print(f"✅ Đợt {iteration}: Xong!")
            
            try:
                repo = Repo(".")
                repo.git.add(A=True)
                repo.index.commit(f"Evolution {iteration}")
                repo.git.push('origin', 'main')
                print("🔥 Đã đẩy code lên GitHub!")
            except Exception as e:
                print(f"⚠️ Git error: {e}")
        
        print("💤 Nghỉ 120s...")
        time.sleep(120)
        iteration += 1

if __name__ == "__main__":
    main()
    
