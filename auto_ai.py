import requests
import os
import time
from git import Repo

# --- CẤU HÌNH ---
GROQ_API_KEY = "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"
FILE_PATH = "main.py"
# Llama-3.3-70b-versatile là model sửa code cực tốt và miễn phí trên Groq
MODEL = "llama-3.3-70b-versatile" 

def call_groq_api(code):
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
                "content": "You are a senior Python developer. Improve, optimize, and fix the provided code. Return ONLY the raw code. NO markdown, NO explanation, NO backticks."
            },
            {"role": "user", "content": code}
        ],
        "temperature": 0.2
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=30)
        if response.status_code == 200:
            res = response.json()
            content = res['choices'][0]['message']['content']
            # Lọc bỏ dấu ``` nếu AI cố tình thêm vào
            clean_code = content.replace("```python", "").replace("```", "").strip()
            return clean_code
        else:
            print(f"❌ Lỗi API Groq ({response.status_code}): {response.text}")
    except Exception as e:
        print(f"❌ Lỗi kết nối: {e}")
    return None

def main():
    if not os.path.exists(FILE_PATH):
        print(f"❌ Không tìm thấy file {FILE_PATH}!")
        return

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        old_code = f.read()

    print(f"🚀 Đang dùng Groq AI (Llama 3.3) nâng cấp code...")
    new_code = call_groq_api(old_code)

    if new_code and len(new_code) > 10:
        # Ghi code mới
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            f.write(new_code)
        print("✅ Đã cập nhật code mới.")

        # Push GitHub
        try:
            repo = Repo(".")
            repo.git.add(A=True)
            repo.index.commit("AI auto-evolution via Groq")
            origin = repo.remote(name='origin')
            origin.push()
            print("🔥 ĐÃ PUSH LÊN GITHUB THÀNH CÔNG!")
        except Exception as e:
            print(f"⚠️ Push thất bại: {e}. Hãy đảm bảo bạn đã login git trên Termux.")
    else:
        print("💀 AI không trả về code hợp lệ. Thử lại sau!")

if __name__ == "__main__":
    main()

