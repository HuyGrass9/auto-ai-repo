import requests
import os
import time

# --- THÔNG TIN CẤU HÌNH ---
GROQ_API_KEY = "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"
FILE_PATH = "main.py"
# Model Llama-3.3-70b cực kỳ thông minh về logic lập trình
MODEL = "llama-3.3-70b-versatile"

def call_groq_api(full_code):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Chỉ thị tập trung vào "Máy Chém Xéo Cần V2"
    system_message = (
        "You are a professional Roblox script developer. "
        "Your task is to improve a Blox Fruits bounty hunter script called 'MayChemXeoCan V2'. "
        "Focus on: Advanced Silent Aim (vector prediction), frame-perfect skill combos, "
        "and optimizing for Delta X executor on mobile. "
        "Use numeric keys 1, 2, 3, 4 for tool selection. "
        "Return ONLY the pure Lua code, no explanations."
    )

    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_message},
            {"role": "user", "content": f"Here is the current code. Make it stronger and more optimized:\n{full_code}"}
        ],
        "temperature": 0.1 # Để code ra chuẩn xác, ít bị biến tấu linh tinh
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=60)
        if response.status_code == 200:
            result = response.json()
            content = result['choices'][0]['message']['content']
            # Tự động lọc bỏ các ký hiệu thừa
            return content.replace("```lua", "").replace("```", "").strip()
        else:
            print(f"❌ Lỗi API: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Lỗi kết nối: {e}")
    return None

def main():
    iteration = 1
    print("🔥 HỆ THỐNG GROQ ĐÃ SẴN SÀNG!")
    
    while True:
        print(f"\n🚀 [GROQ - {MODEL}] TIẾN HÓA ĐỢT {iteration}...")
        
        # Đảm bảo file main.py tồn tại để đọc
        if not os.path.exists(FILE_PATH) or os.stat(FILE_PATH).st_size == 0:
            with open(FILE_PATH, 'w') as f:
                f.write("-- MayChemXeoCan V2 Initializing...")

        with open(FILE_PATH, "r", encoding="utf-8") as f:
            current_code = f.read()

        new_script = call_groq_api(current_code)

        if new_script and len(new_script) > 100:
            with open(FILE_PATH, "w", encoding="utf-8") as f:
                f.write(new_script)
            print(f"✅ Đợt {iteration}: Đã tối ưu và lưu vào {FILE_PATH}")
        else:
            print(f"⚠️ Đợt {iteration}: Không nhận được code mới hợp lệ.")

        # Groq cho phép chạy rất nhanh, nhưng nên nghỉ 30s để tránh bị giới hạn (Rate Limit)
        print("💤 Nghỉ 30 giây để tránh nóng máy...")
        time.sleep(30)
        iteration += 1

if __name__ == "__main__":
    main()
                      
