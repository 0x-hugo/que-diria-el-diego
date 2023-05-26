import openai
from config import OPENAI_API_KEY
from memory import HistorySaver


class Gpt3Turbo:
    def __init__(
        self,
        temperature=.3,
        max_tokens=100,
        memory=HistorySaver("history.txt")
    ):
        self._model = "gpt-3.5-turbo"
        openai.api_key = OPENAI_API_KEY
        self._memory = memory
        self._temperature = temperature
        self._max_tokens = max_tokens

    def set_personality(self, personality):
        self._personality = personality

    def chat(self, user_input):
        messages = [
            {"role": "system", "content": f"{self._personality}"},
            {"role": "user", "content": f"{user_input}"}
        ]
        response = openai.ChatCompletion.create(
            model=self._model,
            messages=messages,
            temperature=self._temperature,
        )
        gpt_output = response.choices[0].message["content"]
        self._debug(user_input, gpt_output)
        self._memory.save_history(user_input, gpt_output)
        return gpt_output

    def _debug(self, user_input, gpt_output):
        print("\nUser:", user_input)
        print("\nGPT3:", gpt_output)
