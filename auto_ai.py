import requests
import os
import time

# --- CONFIG ---
GROQ_API_KEY = "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"
FILE_PATH = "main.py"
# Lựa chọn 2: Mixtral-8x7b chuẩn của Groq (Hết lỗi 404)
MODEL = "mixtral-8x7b-32768"

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
                "content": "You are a professional Roblox Lua developer. Improve 'MayChemXeoCan V2' for Blox Fruits. Focus: Fast Attack, Prediction Silent Aim, Mobile Optimization. Return ONLY raw Lua code."
            },
            {"role": "user", "content": f"Optimize this script now:\n{full_code}"}
        ],
        "temperature": 0.2
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=60)
        if response.status_code == 200:
            content = response.json()['choices'][0]['message']['content']
            return content.replace("```lua", "").replace("```", "").strip()
        elif response.status_code == 429:
            print("🛑 Rate Limit! Đang đợi hồi Token...")
            return "WAIT"
        else:
            print(f"❌ Lỗi API: {response.status_code}")
    except Exception as e:
        print(f"❌ Connection Error: {e}")
    return None

def main():
    iteration = 1
    print(f"🔥 KHỞI CHẠY MIXTRAL-8x7b (Vượt rào 404)")
    
    while True:
        if not os.path.exists(FILE_PATH):
            with open(FILE_PATH, 'w') as f: f.write("-- Initializing...")

        with open(FILE_PATH, "r", encoding="utf-8") as f:
            current_code = f.read()

        print(f"\n🚀 ĐANG XỬ LÝ ĐỢT {iteration}...")
        new_script = call_groq_api(current_code)

        if new_script == "WAIT":
            time.sleep(120)
            continue

        if new_script:
            with open(FILE_PATH, "w", encoding="utf-8") as f:
                f.write(new_script)
            print(f"✅ Đợt {iteration}: Thành công! Đã lưu vào {FILE_PATH}")
            iteration += 1
        
        print("💤 Nghỉ 60s để tài khoản hồi sức...")
        time.sleep(60)

if __name__ == "__main__":
    main()
        
