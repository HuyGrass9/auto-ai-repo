import requests
import os
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
                "content": "You are an Elite Lua Developer. Upgrade this Blox Fruit script. Focus on optimization. Return ONLY the code."
            },
            {"role": "user", "content": f"Upgrade this script, keeping it efficient for mobile:\n\n{code}"}
        ],
        "temperature": 0.2,
        "max_tokens": 8192 # Tăng tối đa lượng code trả về
    }

    try:
        # Tăng timeout lên 90 giây vì file của bạn rất dài
        response = requests.post(url, headers=headers, json=data, timeout=90)
        
        if response.status_code != 200:
            print(f"❌ Lỗi API (Status {response.status_code}): {response.text}")
            return None
            
        res = response.json()
        content = res['choices'][0]['message']['content']
        
        # Nếu AI trả về code kèm giải thích, ta chỉ lấy phần code
        clean_code = content.replace("```lua", "").replace("```", "").strip()
        return clean_code
        
    except Exception as e:
        print(f"❌ Lỗi kết nối: {e}")
    return None

def git_process():
    try:
        repo = Repo(".")
        repo.git.add(A=True)
        if repo.is_dirty():
            repo.index.commit("AI Evolution: Optimized Large Script")
            repo.git.push('origin', repo.active_branch.name)
            print("🔥 ĐÃ PUSH THÀNH CÔNG!")
        else:
            print("ℹ️ Không có thay đổi.")
    except Exception as e:
        print(f"⚠️ Lỗi Git: {e}")

def main():
    if not os.path.exists(FILE_PATH):
        print("❌ Không tìm thấy file main.py")
        return

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        old_code = f.read()

    print(f"🤖 Đang xử lý file {len(old_code)} ký tự. Vui lòng đợi...")
    new_code = call_groq_api(old_code)

    if new_code and len(new_code) > 100:
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            f.write(new_code)
        print("✅ Đã cập nhật bản nâng cấp!")
        git_process()
    else:
        print("💀 AI không trả về code hợp lệ (có thể do file quá dài).")

if __name__ == "__main__":
    main()
    
