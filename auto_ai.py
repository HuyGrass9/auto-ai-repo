import requests
import os
import time

# --- THÔNG TIN CẤU HÌNH ---
GROQ_API_KEY = "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"
FILE_PATH = "main.py"
# Lựa chọn 2: Mixtral-8x7b - Cân bằng cực tốt giữa thông minh và hạn mức Token
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
                "content": "You are an expert Roblox Lua developer. Focus on optimizing 'MayChemXeoCan V2'. Improve Silent Aim, prediction logic, and mobile performance for Delta X. Use hotkeys 1, 2, 3, 4. Return ONLY raw Lua code."
            },
            {"role": "user", "content": f"Full script evolution:\n{full_code}"}
        ],
        "temperature": 0.2
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=60)
        if response.status_code == 200:
            content = response.json()['choices'][0]['message']['content']
            # Làm sạch code trả về
            return content.replace("```lua", "").replace("```", "").strip()
        elif response.status_code == 429:
            print("🛑 Hết quota tạm thời! Nghỉ 120s để hồi sức...")
            return "WAIT"
        elif response.status_code == 404:
            print(f"❌ Model {MODEL} không tìm thấy. Thử lại với llama3-8b-8192...")
            return "RETRY_LOW"
        else:
            print(f"❌ Lỗi API: {response.status_code}")
    except Exception as e:
        print(f"❌ Lỗi kết nối: {e}")
    return None

def main():
    iteration = 1
    print(f"🔥 KHỞI CHẠY TIẾN HÓA VỚI: {MODEL}")
    
    while True:
        if not os.path.exists(FILE_PATH):
            with open(FILE_PATH, 'w') as f: f.write("-- MayChemXeoCan V2 Start")

        with open(FILE_PATH, "r", encoding="utf-8") as f:
            code = f.read()

        print(f"\n🚀 ĐANG XỬ LÝ ĐỢT {iteration}...")
        new_script = call_groq_api(code)

        if new_script == "WAIT":
            time.sleep(120)
            continue
        
        if new_script == "RETRY_LOW":
            # Tự động hạ cấp model nếu bị lỗi 404 để bot không dừng lại
            global MODEL
            MODEL = "llama3-8b-8192"
            continue
            
        if new_script:
            with open(FILE_PATH, "w", encoding="utf-8") as f:
                f.write(new_script)
            print(f"✅ Đợt {iteration}: Thành công! (Lưu vào {FILE_PATH})")
            iteration += 1
        
        # Nghỉ 60s để tài khoản Free bền bỉ hơn
        print("💤 Nghỉ 60 giây tiếp nhiên liệu...")
        time.sleep(60)

if __name__ == "__main__":
    main()
    
