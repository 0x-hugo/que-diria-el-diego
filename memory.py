import json


class HistorySaver:
    def __init__(self, file_name):
        self.file_name = file_name

    def _build_json(self, user_input, output):
        return {
            "user": user_input,
            "gpt": output
        }

    def save_history(self, user_input, gpt_output):
        with open(self.file_name, "a") as file:
            json_output = json.dumps(
                self._build_json(user_input, gpt_output),
                indent=4)
            file.write(json_output)
            file.write("\n")
