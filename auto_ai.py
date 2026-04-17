import requests
import os
import time
import re

# --- CẤU HÌNH HỆ THỐNG ---
GROQ_API_KEY = "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"
FILE_PATH = "main.py"
MODEL = "llama-3.1-8b-instant"

# --- SIÊU PROMPT ---
SUPER_PROMPT = """
Role: Senior Roblox Lua Developer (Delta X Expert).
Task: Build/Optimize 'MayChemXeoCan V2' PvP Macro.
REQUIRED MODULES: 1. Services, 2. Config, 3. State, 4. Cache, 5. Utils, 6. CombatEngine, 7. SilentAim, 8. Visuals, 9. LagFixer, 10. FakeLag, 11. MaruUI.
STRICT RULES: Use task.spawn, Mobile Touch, Output FULL script, NO placeholders, NO markdown.
"""

def clean_lua_code(text):
    text = re.sub(r"^```[A-Za-z]*\n", "", text, flags=re.MULTILINE)
    text = re.sub(r"```$", "", text, flags=re.MULTILINE)
    return text.strip()

def call_groq_api(full_code):
    # CHÚ Ý: URL phải sạch, không có dấu ngoặc vuông/tròn của markdown
    url = "https://api.groq.com/openai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SUPER_PROMPT},
            {"role": "user", "content": f"Update and complete the full script. Current code:\n{full_code}"}
        ],
        "temperature": 0.1
    }
    
    try:
        response = requests.post(url, headers=headers, json=data, timeout=90)
        if response.status_code == 200:
            return clean_lua_code(response.json()['choices'][0]['message']['content'])
        else:
            print(f"❌ API Error {response.status_code}: {response.text}")
    except Exception as e:
        print(f"❌ Connection Error: {e}")
    return None

def main():
    print(f"🚀 KHỞI CHẠY BUILDER V4 (FIXED URL)")
    it = 1
    while True:
        if not os.path.exists(FILE_PATH):
            with open(FILE_PATH, 'w') as f: f.write("-- Initializing...")

        with open(FILE_PATH, "r", encoding="utf-8") as f:
            code = f.read()

        print(f"\n🔄 Đợt {it}: Đang xử lý {len(code)} ký tự...")
        new_code = call_groq_api(code)
        
        if new_code and len(new_code) > 100:
            with open(FILE_PATH, "w", encoding="utf-8") as f:
                f.write(new_code)
            print(f"✅ Đã đúc code mới thành công!")

            # --- GIT PUSH ---
            os.system("git add .")
            os.system(f'git commit -m "Evolution {it}: Fixed connection issue"')
            os.system("git stash")
            os.system("git pull origin main --rebase")
            os.system("git stash pop")
            os.system("git add .")
            os.system("git commit --allow-empty -m 'Resolved merge'")
            os.system("git push origin main")
            it += 1
        
        print("💤 Nghỉ 60s tiếp nhiên liệu...")
        time.sleep(60)

if __name__ == "__main__":
    main()

