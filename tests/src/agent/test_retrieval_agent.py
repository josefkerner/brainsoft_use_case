from src.agent.retrieval_agent import RetrievalAgent
from src.data_model.question import Question
def test_chat():
    agent = RetrievalAgent()
    context = []
    questions = [
        "What does constant LEARNING_RATE mean in TunesAPIDescriptions class?",
        "what other constants does this class have?"
    ]
    for question in questions:
        response = agent.chat(Question(question=question, context=context))
        context = response.past_conversations
        print('answer',response.answer)
        assert response.answer is not None
        assert 'I don\'t know' not in response.answer
