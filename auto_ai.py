import requests
import os
from git import Repo

GROQ_API_KEY = "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"
FILE_PATH = "main.py"
MODEL = "llama-3.3-70b-versatile"

def call_groq_api():
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    
    # ĐÂY LÀ PHẦN QUAN TRỌNG NHẤT: PROMPT KHỞI TẠO SIÊU CẤP
    system_prompt = """You are a God-tier Lua Scripter for Roblox Blox Fruit.
TASK: Create a COMPLETELY NEW, high-performance Auto Bounty script named 'MayChemXeoCan V2'.

CORE ARCHITECTURE TO IMPLEMENT:
1. Advanced Combat: 
   - Perfect HumanoidRootPart (HRP) Prediction for moving targets.
   - Ultra-fast Skill Cycle (Z, X, C, V) using VirtualInputManager.
   - Smart Slot Swapping (Keys 1, 2, 3, 4) for Melee, Sword, and Fruit.
2. Movement: 
   - Smooth 'Safe Tween' system to bypass anti-cheat detections.
   - Auto-distance maintainer (keeps 5-10 studs from target).
3. Optimization:
   - Dynamic Delay: Adjusts wait times based on game Ping.
   - 60 FPS Focus: Use task.wait() and avoid heavy loops.
4. Learning Mechanism: 
   - Add a 'Self-Correction' module that checks if a skill hits; if not, adjust prediction.

OUTPUT: Return ONLY the full, clean Lua code. No markdown, no explanations."""

    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": "Create the MayChemXeoCan V2 script from scratch. Make it the most powerful and intelligent Auto Bounty script ever made."}
        ],
        "temperature": 0.3,
        "max_tokens": 8000
    }

    try:
        print("🤖 AI đang tự tay xây dựng 'Máy Chém Xéo Cần V2' từ con số 0...")
        response = requests.post(url, headers=headers, json=data, timeout=300)
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content'].replace("```lua", "").replace("```", "").strip()
    except Exception as e:
        print(f"❌ Error: {e}")
    return None

def main():
    # XÓA CODE CŨ TRƯỚC KHI TẠO MỚI
    print("🧹 Đang dọn dẹp code cũ...")
    new_script = call_groq_api()

    if new_script:
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            f.write(new_script)
        print("✅ ĐÃ TẠO XONG BẢN V2 SIÊU CẤP!")
        
        try:
            repo = Repo(".")
            repo.git.add(A=True)
            repo.index.commit("Initial Build: MayChemXeoCan V2 - God Mode")
            repo.git.push('origin', repo.active_branch.name)
            print("🚀 ĐÃ PUSH SIÊU PHẨM LÊN GITHUB!")
        except:
            print("⚠️ Push lỗi, nhưng code đã nằm trong main.py.")

if __name__ == "__main__":
    main()
    
