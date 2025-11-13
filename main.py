from requests import Session
import base64

# the bearer token is always required and well, its expire after some time
# Thats an example of the decoded jtw: {"alg":"HS256","typ":"JWT"}{"iat":1763004248386,"exp":1763005148,"bundleId":"com.chatbot.ai.aichat.openaibot.chat","os":"Android","versionApp":"35.0.2"}
# Im kidding, u have to use the modded version to get the premium auth token, get it here: https://t.me/c/2365551068/334 (private channel, make a request to join)
# u should know how to get the token via httptoolkit intercept, and memu, easyy


class GPTReverse:
    def __init__(self):
        self.models = ["gemini-2.0-flash", "gemini-2.0", "gpt-4o", "gpt-4o-mini"]
        self.max_tokens = 1250
        self.session = Session()
        self.token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3NjMwMDQyNDgzODYsImV4cCI6MTc2MzAwNTE0OCwiYnVuZGxlSWQiOiJjb20uY2hhdGJvdC5haS5haWNoYXQub3BlbmFpYm90LmNoYXQiLCJvcyI6IkFuZHJvaWQiLCJ2ZXJzaW9uQXBwIjoiMzUuMC4yIn0.yJf_VOu_9MjcuYvXtzufLp8mUFVLQyVoxfnJf0bG-c4"
        self.base_api = "https://chatapi.begamob.com/api/"
        self.headers = {
            "Authorization": "Bearer " + self.token,
            "Accept": "application/json",
            "Host": "chatapi.begamob.com",
            "user-header": "bundleId:com.chatbot.ai.aichat.openaibot.chat/versionApp:35.0.2/OS:Android/osVersion:28/userId:bc73a627e28df4b4a281ade5cb895a94/deviceId:null",
            "User-Agent": "okhttp/4.12.0",
        }

    def chat_custom(self, prompt: str | dict, model: str) -> str:
        "Chat with a custom model (main function)"
        try:
            if model not in self.models:
                return "Model not found"
            response = self.session.post(
                self.base_api + "v2/chatCustom",
                headers=self.headers,
                json={
                    "max_tokens": 1250,
                    "messages": [
                        {
                            "content": [
                                {
                                    "text": prompt,
                                    "type": "text",
                                }
                            ],
                            "role": "user",
                        }
                    ],
                    "model": model,
                },
            ).json()
            if "type" in response:
                for choice in response["choices"]:
                    return choice["message"]["content"]
            else:
                return response
        except Exception as e:
            return e


if __name__ == "__main__":
    gpt = GPTReverse()
    print(gpt.chat_custom("make me a jwt reverse tool", "gemini-2.0-flash"))
