import requests
import os
from git import Repo

# --- CONFIGURATION ---
GROQ_API_KEY = "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"
FILE_PATH = "main.py"
MODEL = "llama-3.3-70b-versatile"

def call_groq_api():
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    
    # SỬ DỤNG SIÊU PROMPT TỪ KINH NGHIỆM PHÁT TRIỂN CỦA BRO
    system_prompt = """You are a senior Roblox Lua developer with deep expertise in mobile-optimized exploit scripting for Delta X executor. 
    Your task is to build a Blox Fruits PvP Macro from scratch based on the provided specifications.
    
    ## CORE SPECIFICATIONS:
    1. Executor: Delta X (Mobile). Use gethui(), task.spawn, task.wait.
    2. Architecture: Modular (Config, UI, CombatEngine, SilentAim, Visuals, LagFixer, FakeLag, Utils).
    3. Combat: Tool detection types 1-4, ExecuteCombo logic with switch-case, Stun/Busy state checks.
    4. SilentAim: __namecall hook, target nearest enemy, override Vector3/CFrame arguments.
    5. Visuals: BillboardGui ESP, Beam Tracer, FOV Changer.
    6. LagFixer: Particle reduction, effect disabling, smooth plastic materials.
    7. FakeLag: SetNetworkOwner(nil) at 10Hz.
    8. UI: MaruUI style, draggable, mobile-friendly sliders and toggles.
    
    OUTPUT: Return ONLY the full, production-ready Lua code. No markdown, no chat."""

    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": "Follow the 'MayChemXeoCan V2' full technical specifications and generate the complete script now."}
        ],
        "temperature": 0.2, # Độ chính xác tuyệt đối theo specs
        "max_tokens": 8192
    }

    try:
        print("🛠️ AI đang đúc kết kinh nghiệm và xây dựng V2 theo Spec chuẩn...")
        response = requests.post(url, headers=headers, json=data, timeout=300)
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content'].replace("```lua", "").replace("```", "").strip()
        else:
            print(f"❌ API Error: {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")
    return None

def main():
    # Xóa trắng file cũ để AI tự do sáng tạo bản V2
    if os.path.exists(FILE_PATH):
        open(FILE_PATH, 'w').close()

    new_script = call_groq_api()

    if new_script:
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            f.write(new_script)
        print("✅ SIÊU PHẨM V2 ĐÃ HOÀN THÀNH DỰA TRÊN SPEC!")
        
        try:
            repo = Repo(".")
            repo.git.add(A=True)
            repo.index.commit("Production: MayChemXeoCan V2 Build from Technical Specs")
            repo.git.push('origin', repo.active_branch.name)
            print("🚀 ĐÃ PUSH BẢN V2 LÊN GITHUB!")
        except Exception as e:
            print(f"⚠️ Push Error: {e}")

if __name__ == "__main__":
    main()
    
