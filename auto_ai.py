import requests
import os
import time

# --- CONFIG ---
GROQ_API_KEY = "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"
FILE_PATH = "main.py"
# Dùng bản 8b để không bị giới hạn Token (vẫn rất thông minh với Lua)
MODEL = "llama-3-1-8b-instant" 

def call_groq_api(full_code):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": MODEL,
        "messages": [
            {
                "role": "system", 
                "content": "You are a professional Roblox Lua developer. Improve 'MayChemXeoCan V2' for Blox Fruits. Focus: Silent Aim, No-Lag Mobile, Fast Attack. Return ONLY raw Lua code."
            },
            {"role": "user", "content": f"Optimize this script:\n{full_code}"}
        ],
        "temperature": 0.3
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=60)
        if response.status_code == 200:
            content = response.json()['choices'][0]['message']['content']
            return content.replace("```lua", "").replace("```", "").strip()
        elif response.status_code == 429:
            print("🛑 Đang bị Rate Limit! Bot sẽ tự đợi 60s rồi thử lại...")
            time.sleep(60)
            return None
        else:
            print(f"❌ Lỗi: {response.status_code}")
    except Exception as e:
        print(f"❌ Connection Error: {e}")
    return None

def main():
    iteration = 1
    print(f"🔥 ĐANG CHẠY CHẾ ĐỘ TIẾN HÓA BẤT TỬ (Model: {MODEL})")
    
    while True:
        print(f"\n🚀 ĐỢT {iteration} ĐANG XỬ LÝ...")
        
        if not os.path.exists(FILE_PATH):
            with open(FILE_PATH, 'w') as f: f.write("-- Initializing...")

        with open(FILE_PATH, "r", encoding="utf-8") as f:
            current_code = f.read()

        new_script = call_groq_api(current_code)

        if new_script:
            with open(FILE_PATH, "w", encoding="utf-8") as f:
                f.write(new_script)
            print(f"✅ Đợt {iteration}: Xong! Đã lưu vào {FILE_PATH}")
            iteration += 1
        
        # Nghỉ 60s để tài khoản Free không bị quá tải
        print("💤 Nghỉ 60s để hồi Token...")
        time.sleep(60)

if __name__ == "__main__":
    main()
    
