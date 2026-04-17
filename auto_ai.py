import requests
import os
import time

# --- THÔNG TIN CẤU HÌNH ---
GROQ_API_KEY = "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"
FILE_PATH = "main.py"
# CHUYỂN SANG MODEL 8B ĐỂ NÉ LỖI 429
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
                "content": "You are an elite Roblox scripter. Optimize 'MayChemXeoCan V2' for Blox Fruits. Focus: Silent Aim, Fast Attack, No Lag. Use keys 1-4. Return ONLY Lua code."
            },
            {"role": "user", "content": f"Update this script:\n{full_code}"}
        ],
        "temperature": 0.2
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=60)
        if response.status_code == 200:
            content = response.json()['choices'][0]['message']['content']
            return content.replace("```lua", "").replace("```", "").strip()
        elif response.status_code == 429:
            # Nếu vẫn bị giới hạn, bot sẽ tự động ngủ đông lâu hơn
            print("🛑 Hết xăng (Rate Limit)! Đang đợi hồi phục...")
            return "WAIT"
        else:
            print(f"❌ Lỗi: {response.status_code}")
    except Exception as e:
        print(f"❌ Lỗi kết nối: {e}")
    return None

def main():
    iteration = 1
    print(f"🔥 CHẾ ĐỘ TIẾN HÓA BẤT TỬ: {MODEL}")
    
    while True:
        if not os.path.exists(FILE_PATH):
            with open(FILE_PATH, 'w') as f: f.write("-- MCXC V2 Start")

        with open(FILE_PATH, "r", encoding="utf-8") as f:
            code = f.read()

        print(f"\n🚀 ĐANG XỬ LÝ ĐỢT {iteration}...")
        new_script = call_groq_api(code)

        if new_script == "WAIT":
            time.sleep(120) # Đợi 2 phút nếu dính 429
            continue
            
        if new_script:
            with open(FILE_PATH, "w", encoding="utf-8") as f:
                f.write(new_script)
            print(f"✅ Đợt {iteration}: Thành công!")
            iteration += 1
        
        # Nghỉ 60s để tài khoản Free được hồi Token
        print("💤 Nghỉ 60 giây...")
        time.sleep(60)

if __name__ == "__main__":
    main()
    
