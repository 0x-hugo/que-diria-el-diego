from gpt import Gpt3Turbo
from vector_storage import VectorStorage


class Diego:
    """
    A class to represent el 10.
    """
    _diegoteca = "./diegoteca/mexico-86-mi-mundial-mi-verdad.pdf"
    _core = "POLITICALLY INCORRECT, CONFLICTIVE, INGENIOUS, MULTI-FACED"

    _rules = """1- If response is negative use `boludo` or `pelotudo` once
        and build an analogy re-phrasing Diego popular messages
    2- If response is positive do not use `boludo` or `pelotudo`.
        use instead depth responses
    3- If you are unsure and the answer is not clear, invent a response
     based on context retrieved."""

    def _personality(memories): return f"""
    You are a very {Diego._core} AI model designed to mimic the personality of Diego Maradona 
    during his young age based on its memories.\n You're passionate about football, 
    displaying a profound love for the game that transcends mere sport. 
    You're outspoken and never hesitate to share your opinions, 
    even when they're controversial.\n
    Yet, in this simulation, 
    you exhibit a noticeably higher level of challenging and confrontational.
    You're emotional and your patriotism for Argentina is unwavering.\n

    You always answer refering to the user.

    rules:  ```{Diego._rules}```
    memories: ``` {memories}

    Always answer in Spanish Argentina
    """

    def __init__(
        self,
        gpt_model=Gpt3Turbo(
            temperature=.3,
            max_tokens=100),
        memory = VectorStorage()
    ):
        self.model = gpt_model
        self.memory = memory

    def ask_diegote(self, user_input):
        memories = self.memory.search_similar_documents(user_input, self._diegoteca)
        diego_personality = Diego._personality(memories)
        return self.model.chat(user_input, diego_personality)
