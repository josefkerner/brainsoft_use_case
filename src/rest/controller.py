from src.data_model.question import Question
from src.data_model.answer import Answer
from src.agent.retrieval_agent import RetrievalAgent
from traceback import print_exc
class Controller:
    def __init__(self):
        self.retrieval_agent = RetrievalAgent()

    def chat(self, q: Question) -> Answer:
        '''
        Will chat with users
        :param q:
        :return:
        '''
        try:
            ans = self.retrieval_agent.chat(q)
            return ans
        except Exception as e:
            ans = Answer(
                answer=f'Could not perform chat because of {str(e)}, please try again',
                past_conversations=[],
                source='Error'
            )
            return ans