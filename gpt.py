import openai
from config import OPENAI_API_KEY
from history_saver import HistorySaver


class Gpt3Turbo:
    def __init__(
        self,
        temperature=.3,
        max_tokens=100,
        history_saver=HistorySaver("history.txt")
    ):
        self._model = "gpt-3.5-turbo"
        openai.api_key = OPENAI_API_KEY
        self._history_saver = history_saver
        self._temperature = temperature
        self._max_tokens = max_tokens

    def chat(self, user_input, context):
        messages = [
            {"role": "system", "content": f"{context}"},
            {"role": "user", "content": f"{user_input}"}
        ]
        response = openai.ChatCompletion.create(
            model=self._model,
            messages=messages,
            temperature=self._temperature,
        )
        print(f'reponse: [{response}]')
        gpt_output = response.choices[0].message["content"]
        self._log_and_save(user_input, gpt_output)
        return gpt_output

    def _debug(self, user_input, gpt_output):
        print("\nUser:", user_input)
        print("\nGPT3:", gpt_output)

    def _log_and_save(self, user_input, gpt_output):
        self._history_saver.save_history(user_input, gpt_output)
        self._debug(user_input, gpt_output)