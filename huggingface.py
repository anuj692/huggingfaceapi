from huggingface_hub import InferenceClient

# Apna Token yahan daalein
client = InferenceClient(token="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")

print("🤖 Mera AI start ho gaya! (Type 'exit' to stop)")

while True:
    # 1. User se sawal pucho
    user_input = input("\n👤 Aapka Sawal: ")
    
    if user_input.lower() == 'exit':
        print("Bye Bye! ")
        break

    print("Thinking... 🤔")

    try:
        # 2. AI ko bhejo (Model: Qwen)
        response = client.chat.completions.create(
            model="Qwen/Qwen2.5-72B-Instruct", 
            messages=[
                {"role": "user", "content": user_input}
            ], 
            max_tokens=500
        )
        
        # 3. Jawab dikhao
        print(f"🤖 AI: {response.choices[0].message.content}")

    except Exception as e:
        print(f"❌ Error: {e}")