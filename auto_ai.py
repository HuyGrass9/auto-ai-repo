import requests
import os
import time
from git import Repo

# --- CONFIGURATION ---
# Mã GitHub PAT bro vừa cung cấp
GITHUB_TOKEN = "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"
FILE_PATH = "main.py"
# Sử dụng DeepSeek-V3 - "Quái vật" lập trình hiện nay
MODEL = "deepseek-v3" 
URL = "https://models.inference.ai.azure.com/chat/completions"

def call_github_model(full_code):
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Content-Type": "application/json"
    }
    
    # Sử dụng toàn bộ "tinh hoa" PvP mà bro đã đúc kết
    system_instruction = """You are a senior Roblox Lua developer. 
    Refine 'MayChemXeoCan V2' based on the technical specs: 
    Modular architecture, Mobile Delta X optimization, __namecall SilentAim, and 1-4 numeric tool switching.
    Make the CombatEngine extremely aggressive and predictive.
    Return ONLY raw Lua code without markdown."""

    data = {
        "messages": [
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": f"Analyze and upgrade this Blox Fruits script to God-tier:\n{full_code}"}
        ],
        "model": MODEL,
        "temperature": 0.2
    }

    try:
        response = requests.post(URL, headers=headers, json=data, timeout=150)
        if response.status_code == 200:
            content = response.json()['choices'][0]['message']['content']
            # Làm sạch code trả về
            return content.replace("```lua", "").replace("```", "").strip()
        else:
            print(f"❌ GitHub API Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Lỗi kết nối: {e}")
    return None

def main():
    iteration = 1
    while True:
        print(f"\n🚀 [GITHUB MODELS - {MODEL.upper()}] TIẾN HÓA ĐỢT {iteration}...")
        
        # Đảm bảo file tồn tại
        if not os.path.exists(FILE_PATH):
            with open(FILE_PATH, 'w') as f: f.write("-- Initializing MayChemXeoCan V2")
            
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            full_code = f.read()

        new_script = call_github_model(full_code)

        if new_script and len(new_script) > 500:
            with open(FILE_PATH, "w", encoding="utf-8") as f:
                f.write(new_script)
            print(f"✅ Đợt {iteration}: {MODEL} đã tối ưu xong!")
            
            try:
                repo = Repo(".")
                # Cấu hình user để push không bị lỗi
                repo.git.config("user.email", "bot@ai.com")
                repo.git.config("user.name", "AI Evolution Bot")
                
                repo.git.add(A=True)
                repo.index.commit(f"DeepSeek-V3 Evolution {iteration}")
                
                # Sử dụng token để push trực tiếp
                origin = repo.remote(name='origin')
                origin.push()
                print("🔥 Đã đẩy code 'Thần Khí' lên GitHub thành công!")
            except Exception as e:
                print(f"⚠️ Git push error: {e}")
        
        # GitHub Models có giới hạn rate limit, nên nghỉ 2 phút là đẹp
        print(f"💤 Nghỉ 120s để hồi năng lượng...")
        time.sleep(120)
        iteration += 1

if __name__ == "__main__":
    main()
    
