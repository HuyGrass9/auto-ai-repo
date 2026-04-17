import requests
import os
import time
from git import Repo

# --- CONFIGURATION ---
# API Key bro vừa gửi
GEMINI_API_KEY = "AQ.Ab8RN6IZOku1junDZrso5GS-ByiW_w-1Up7lapurlc4V9UEe1w"
FILE_PATH = "main.py"
# Sử dụng bản Flash 1.5 để tốc độ nhanh nhất và miễn phí
MODEL_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

def call_gemini_api(full_code):
    headers = {"Content-Type": "application/json"}
    
    # Sử dụng Siêu Prompt từ kinh nghiệm của bro
    system_instruction = """You are a senior Roblox Lua developer. 
    Build/Refine 'MayChemXeoCan V2' based on the technical specs.
    Focus on: Perfect SilentAim, Mobile Optimization for Delta X, and Frame-perfect combos.
    You must return ONLY the raw Lua code. No markdown, no chat."""

    data = {
        "contents": [{
            "parts": [{
                "text": f"{system_instruction}\n\nHere is the current code, analyze and evolve it to God-tier level:\n\n{full_code}"
            }]
        }],
        "generationConfig": {
            "temperature": 0.2,
            "maxOutputTokens": 8192,
        }
    }

    try:
        response = requests.post(MODEL_URL, headers=headers, json=data, timeout=300)
        if response.status_code == 200:
            result = response.json()
            # Lấy nội dung code từ cấu trúc JSON của Gemini
            content = result['candidates'][0]['content']['parts'][0]['text']
            return content.replace("```lua", "").replace("```", "").strip()
        else:
            print(f"❌ Gemini Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Exception: {e}")
    return None

def main():
    iteration = 1
    while True:
        print(f"\n🚀 [GEMINI MODE] BẮT ĐẦU ĐỢT TIẾN HÓA THỨ {iteration}...")
        
        if not os.path.exists(FILE_PATH):
            full_code = "-- Initial Script"
        else:
            with open(FILE_PATH, "r", encoding="utf-8") as f:
                full_code = f.read()

        new_script = call_gemini_api(full_code)

        if new_script and len(new_script) > 1000:
            with open(FILE_PATH, "w", encoding="utf-8") as f:
                f.write(new_script)
            print(f"✅ Đợt {iteration}: Gemini đã tối ưu xong toàn bộ file.")
            
            try:
                repo = Repo(".")
                repo.git.add(A=True)
                repo.index.commit(f"Gemini Evolution {iteration}: Massive Optimization")
                repo.git.push('origin', repo.active_branch.name)
                print(f"🔥 Đã Push đợt {iteration} lên GitHub thành công!")
            except Exception as e:
                print(f"⚠️ Git Error: {e}")
        
        # Gemini bản Free cho phép khoảng 15 lần/phút, mình nghỉ 1 phút cho an toàn và sâu sắc
        print(f"💤 Nghỉ 60 giây để Gemini 'hồi mana'...")
        time.sleep(60)
        iteration += 1

if __name__ == "__main__":
    main()
    
