from src.rest.controller import Controller
from src.data_model.question import Question
from src.data_model.answer import Answer

class CliClient:
    def __init__(self):
        self.controller = Controller()

    def chat(self):
        context = []
        while True:
            prompt = input('Enter your question: ')
            q = Question(question=prompt,
                         context=context
                         )
            answer: Answer = self.controller.chat(q)
            context = answer.past_conversations
            print(f"Answer: {answer.answer} Retrieved from: {answer.source}")

if __name__ == '__main__':
    cli_client = CliClient()
    cli_client.chat()