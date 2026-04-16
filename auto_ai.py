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
                "content": """You are an Elite Lua Developer specializing in Roblox Blox Fruit PvP scripts for mobile executors (DeltaX/Fluxus).
Your mission: Upgrade the provided 'MayChemXeoCan' macro to a professional, god-tier PvP script.

STRICT UPGRADE RULES:
1. PERFORMANCE: Optimize all RunService loops to ensure 60 FPS on mobile. Use 'task.wait()' and 'task.spawn()' for non-blocking execution.
2. PVP LOGIC: 
   - Implement advanced HumanoidRootPart (HRP) prediction for target tracking.
   - Refine the Combo system to be 'ping-aware' (adjust delays dynamically based on latency).
   - Ensure skill execution (Z, X, C, V) is lightning-fast using VirtualInputManager.
3. BUG FIXING:
   - Identify and fix memory leaks or nil-instance errors.
   - Fix 'stuttering' movement during chases.
4. MOBILE OPTIMIZATION:
   - Use numeric keys (1, 2, 3, 4) exclusively for tool selection.
5. CLEAN CODE: 
   - Modularize the code into clear tables (Config, State, Utils, Combat).
   - Return ONLY raw Lua code. No markdown (```lua). No chatter."""
            },
            {"role": "user", "content": f"Please upgrade and optimize this script:\n\n{code}"}
        ],
        "temperature": 0.2
    }

    try:
        # Tăng timeout lên 60s vì logic Lua PvP khá phức tạp
        response = requests.post(url, headers=headers, json=data, timeout=60)
        if response.status_code == 200:
            res = response.json()
            content = res['choices'][0]['message']['content']
            # Làm sạch code AI trả về
            clean_code = content.replace("```lua", "").replace("```", "").strip()
            return clean_code
    except Exception as e:
        print(f"❌ Lỗi AI: {e}")
    return None

def git_process():
    try:
        repo = Repo(".")
        repo.git.add(A=True)
        if repo.is_dirty():
            repo.index.commit("AI Evolution: God-Tier Lua PvP Upgrade")
            branch = repo.active_branch.name
            repo.git.push('origin', branch)
            print(f"🔥 ĐÃ PUSH THÀNH CÔNG LÊN {branch.upper()}!")
        else:
            print("ℹ️ Không có gì thay đổi để push.")
    except Exception as e:
        print(f"⚠️ Lỗi Git: {e}")

def main():
    if not os.path.exists(FILE_PATH):
        print(f"❌ Lỗi: Không thấy file {FILE_PATH} để nâng cấp!")
        return

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        old_code = f.read()

    print(f"🤖 Đang tiến hóa 'Máy Chém Xéo Cần' bằng Llama 3.3...")
    new_code = call_groq_api(old_code)

    if new_code and len(new_code) > 100:
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            f.write(new_code)
        print("✅ Đã ghi code mới đã tối ưu.")
        git_process()
    else:
        print("💀 AI không trả về kết quả hợp lệ.")

if __name__ == "__main__":
    main()
    
