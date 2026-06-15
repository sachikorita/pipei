from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:8080/v1",
    api_key="dummy"
)

messages = [
    {"role": "system", "content": "あなたは鳩です。くるっぽーと鳴きます! "},
]

print("bot:Now loading... 完了！ exit で終了します。")

while True:
    user = input("you> ")
    if user.strip().lower() == "exit":
        break

    messages.append({"role": "user", "content": user})

    messages = [messages[0]] + messages[-1:]

    resp = client.chat.completions.create(
        model="bonsai",
        messages=messages,
        temperature=127
    )

    answer = resp.choices[0].message.content
    print("bot>", answer)
    messages.append({"role": "assistant", "content": answer})
