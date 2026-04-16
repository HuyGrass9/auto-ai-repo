import requests
import os
import time
from git import Repo

# --- CẤU HÌNH ---
GROQ_API_KEY = "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"
FILE_PATH = "main.py"
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
                "content": "You are a senior Python developer. Improve the code for a game macro. Return ONLY raw code. No markdown."
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
            clean_code = content.replace("```python", "").replace("```", "").strip()
            return clean_code
    except Exception as e:
        print(f"❌ Lỗi AI: {e}")
    return None

def git_process():
    try:
        repo = Repo(".")
        # 1. Add và Commit
        repo.git.add(A=True)
        if repo.is_dirty():
            repo.index.commit("AI Evolution: Auto-update code")
            print("📝 Đã commit sự thay đổi.")
        else:
            print("ℹ️ Không có gì thay đổi để commit.")
            return

        # 2. Xử lý Push (Tự động nhận diện branch main hoặc master)
        print("🚀 Đang đẩy code lên GitHub...")
        try:
            # Ép push lên main
            repo.git.push('-u', 'origin', 'main')
            print("🔥 ĐÃ PUSH THÀNH CÔNG LÊN NHÁNH MAIN!")
        except:
            # Nếu không có main thì thử master
            repo.git.push('-u', 'origin', 'master')
            print("🔥 ĐÃ PUSH THÀNH CÔNG LÊN NHÁNH MASTER!")

    except Exception as e:
        print(f"⚠️ Lỗi Git: {e}")

def main():
    if not os.path.exists(FILE_PATH):
        # Tạo file main.py trống nếu chưa có để AI nâng cấp
        with open(FILE_PATH, "w") as f: f.write("# Start coding here")

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        old_code = f.read()

    print(f"🤖 Đang nhờ AI nâng cấp file {FILE_PATH}...")
    new_code = call_groq_api(old_code)

    if new_code and len(new_code) > 10:
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            f.write(new_code)
        print("✅ Đã ghi code mới.")
        git_process()
    else:
        print("💀 AI không trả về code hợp lệ.")

if __name__ == "__main__":
    main()

