import requests
import os
from git import Repo

# --- CONFIGURATION ---
GROQ_API_KEY = "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"
FILE_PATH = "main.py"
MODEL = "llama-3.3-70b-versatile"

def call_groq_api(full_code):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    
    system_prompt = """You are a Master Lua Developer. 
    Your task is to REWRITE and OPTIMIZE the ENTIRE script provided.
    - Improve every single function for maximum mobile performance (DeltaX).
    - Ensure the logic for combos, tracking, and UI is flawless.
    - Implement professional coding patterns and ping-aware delays.
    - Output ONLY the full, complete Lua code. No chat, no markdown."""

    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Refactor this entire script for God-tier performance:\n\n{full_code}"}
        ],
        "temperature": 0.2,
        "max_tokens": 32768 
    }

    try:
        # TĂNG TIMEOUT LÊN 10 PHÚT (600 GIÂY)
        print("⏳ AI đang suy nghĩ cực sâu... Có thể mất vài phút, bro đừng tắt máy nhé...")
        response = requests.post(url, headers=headers, json=data, timeout=600)
        
        if response.status_code == 200:
            content = response.json()['choices'][0]['message']['content']
            return content.replace("```lua", "").replace("```", "").strip()
        else:
            print(f"❌ API Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Lỗi: Có thể do file quá dài hoặc kết nối bị ngắt. Chi tiết: {e}")
    return None

def main():
    if not os.path.exists(FILE_PATH): return

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        full_code = f.read()

    print(f"🤖 Đang tiến hóa TOÀN BỘ code ({len(full_code)} ký tự)...")
    optimized_code = call_groq_api(full_code)

    if optimized_code and len(optimized_code) > 500:
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            f.write(optimized_code)
        print("✅ TIẾN HÓA XONG! Đang đẩy lên GitHub...")
        
        try:
            repo = Repo(".")
            repo.git.add(A=True)
            repo.index.commit("AI Master: 10-minute deep optimization")
            repo.git.push('origin', repo.active_branch.name)
            print("🚀 ĐÃ PUSH LÊN GITHUB!")
        except Exception as e:
            print(f"⚠️ Git Error: {e}")
    else:
        print("💀 AI không thể hoàn thành bản nâng cấp (File quá lớn hoặc cạn Token).")

if __name__ == "__main__":
    main()
            
