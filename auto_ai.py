import requests
import os
import time

# --- CONFIG ---
GROQ_API_KEY = "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"
FILE_PATH = "main.py"
# Model này là chuẩn nhất, không bao giờ lỗi 400/404
MODEL = "llama3-8b-8192"

def call_groq_api(full_code):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a Roblox Lua expert. Optimize the script. ONLY return Lua code."},
            {"role": "user", "content": f"Update: {full_code}"}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=30)
        if response.status_code == 200:
            content = response.json()['choices'][0]['message']['content']
            return content.replace("```lua", "").replace("```", "").strip()
        else:
            print(f"❌ API Error: {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")
    return None

def main():
    iteration = 1
    print(f"🚀 CHẠY MODEL: {MODEL}")
    while True:
        if not os.path.exists(FILE_PATH):
            with open(FILE_PATH, 'w') as f: f.write("-- Start")
        
        with open(FILE_PATH, "r") as f: code = f.read()
        
        print(f"🔄 Đợt {iteration}...")
        new_code = call_groq_api(code)
        
        if new_code:
            with open(FILE_PATH, "w") as f: f.write(new_code)
            print(f"✅ Thành công đợt {iteration}!")
            iteration += 1
        
        time.sleep(60)

if __name__ == "__main__":
    main()
    
