from requests import Session
from re import search


class ChatBotII:
    def __init__(self):
        self.api_url = "https://firebasevertexai.googleapis.com/v1beta/projects/chatbot-ii/models/gemini-2.5-flash:streamGenerateContent?alt=sse"
        self.session = Session()
        self.headers = {
            "Accept": "application/json",
            "Accept-Charset": "UTF-8",
            "Accept-Encoding": "gzip",
            "Authorization": "Firebase eyJhbGciOiJSUzI1NiIsImtpZCI6IjM4MDI5MzRmZTBlZWM0NmE1ZWQwMDA2ZDE0YTFiYWIwMWUzNDUwODMiLCJ0eXAiOiJKV1QifQ.eyJwcm92aWRlcl9pZCI6ImFub255bW91cyIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9jaGF0Ym90LWlpIiwiYXVkIjoiY2hhdGJvdC1paSIsImF1dGhfdGltZSI6MTc2MzQyMzc5MSwidXNlcl9pZCI6InM5QWhlbEg0aXFjMmpSOGgyRjkyNU9xUWdDNzMiLCJzdWIiOiJzOUFoZWxINGlxYzJqUjhoMkY5MjVPcVFnQzczIiwiaWF0IjoxNzYzNDIzNzkxLCJleHAiOjE3NjM0MjczOTEsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnt9LCJzaWduX2luX3Byb3ZpZGVyIjoiYW5vbnltb3VzIn19.clXC-f-i0a5f56-yrtQXno8VZgHMUB5i8Dlo-_NzKxpIt3sTRncC19iSSQy_Jyv14MM4b13RLW5j-_vliRySxCEF210Oq-0GqDtmqGbWhtF_1mybyv8Tb7gXskzJ99GAXyBIsSf-aiO54Sy8Nf0VS82N5m8T_9wgHPb9qZGPLenrN078EHDe9X9nwOtm6N0TZ4225u3yiOShQBnMV-3QOnXgr-UJqGQnxCHfrtu-EQdu62qqmELjMg5F74RUqx2Y3LPKhuTNrU1qfamLQVp77nI2Npe2YhRkt3mLyzfasy-W5ZJz1QVPL6jcFYFnuM5ZvAfEImu0Rr1lkeF2_RoQ7Q",
            "Connection": "Keep-Alive",
            "Content-Type": "application/json",
            "Host": "firebasevertexai.googleapis.com",
            "User-Agent": "ktor-client",
            "X-Firebase-AppCheck": "eyJlcnJvciI6IlVOS05PV05fRVJST1IifQ==",
            "X-Firebase-AppId": "1:580590751392:android:447c986e256a0794e083c5",
            "X-Firebase-AppVersion": "11",
            "x-goog-api-client": "gl-kotlin/2.1.21-ai fire/17.2.0",
            "x-goog-api-key": "AIzaSyCJ1AcbdrK2BzjCEo9LEkoQ5p8PMBfLrnY",
        }

    def create_chat(self, prompt: str | dict) -> str:
        response = self.session.post(
            self.api_url,
            stream=True,
            json={
                "model": "projects/chatbot-ii/models/gemini-2.5-flash",
                "contents": [
                    {
                        "role": "user",
                        "parts": [{"text": prompt, "thought": False}],
                    }
                ],
            },
            headers=self.headers,
        )
        for c in response.iter_lines():
            if c:
                data = c.decode("utf-8")
                if data.startswith("data:"):
                    match = search(r'"text":\s*"([^"]+)"', data)
                    if match:
                        text = match.group(1)
                        print(text)


if __name__ == "__main__":
    prompt = input("[?]Prompt >>> ")
    ChatBotII().create_chat(prompt)
