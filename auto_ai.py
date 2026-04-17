import requests
import os
import time
from git import Repo

# --- CONFIGURATION ---
# Dán cái mã AQ... bro vừa copy vào đây
GEMINI_TOKEN = "AQ.Ab8RN6L2qWqgrdU6O6199p34M..." 
FILE_PATH = "main.py"
# URL bản này không kèm Key ở đuôi
URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"

def call_gemini_api(full_code):
    # Gửi Token qua Header Authorization
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GEMINI_TOKEN}"
    }
    
    system_instruction = """You are a senior Roblox Lua developer. 
    Build/Refine 'MayChemXeoCan V2' based on the technical specs.
    Focus on: Perfect SilentAim, Mobile Optimization for Delta X, and Frame-perfect combos.
    You must return ONLY the raw Lua code."""

    data = {
        "contents": [{
            "parts": [{
                "text": f"{system_instruction}\n\nCode:\n{full_code}"
            }]
        }],
        "generationConfig": {
            "temperature": 0.2,
            "maxOutputTokens": 8192,
        }
    }

    try:
        response = requests.post(URL, headers=headers, json=data, timeout=120)
        if response.status_code == 200:
            result = response.json()
            content = result['candidates'][0]['content']['parts'][0]['text']
            return content.replace("```lua", "").replace("```", "").strip()
        else:
            # Nếu vẫn lỗi 401, thử phương án dự phòng (dán thẳng vào URL như cũ)
            fallback_url = f"{URL}?key={GEMINI_TOKEN}"
            res2 = requests.post(fallback_url, json=data, timeout=120)
            if res2.status_code == 200:
                content = res2.json()['candidates'][0]['content']['parts'][0]['text']
                return content.replace("```lua", "").replace("```", "").strip()
            print(f"❌ Lỗi: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Lỗi kết nối: {e}")
    return None

def main():
    iteration = 1
    while True:
        print(f"\n🚀 [GEMINI V2] ĐANG TIẾN HÓA ĐỢT {iteration}...")
        
        if not os.path.exists(FILE_PATH):
            open(FILE_PATH, 'w').close()
            
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            full_code = f.read()

        new_script = call_gemini_api(full_code)

        if new_script and len(new_script) > 500:
            with open(FILE_PATH, "w", encoding="utf-8") as f:
                f.write(new_script)
            print(f"✅ Thành công đợt {iteration}!")
            
            try:
                repo = Repo(".")
                repo.git.add(A=True)
                repo.index.commit(f"Gemini Evolution {iteration}")
                repo.git.push('origin', repo.active_branch.name)
                print("🚀 Đã đẩy lên GitHub!")
            except:
                print("⚠️ Git update...")
        
        print("💤 Đợi 1 phút...")
        time.sleep(60)
        iteration += 1

if __name__ == "__main__":
    main()
    
