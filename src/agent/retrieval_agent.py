from src.utils.vectara_manager import VectaraManager
from typing import List, Tuple
from src.data_model.question import Question
from src.data_model.answer import Answer
from src.utils.secret_manager import SecretManager
import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains import create_qa_with_sources_chain

class RetrievalAgent:
    def __init__(self):
        self.secret_manager = SecretManager()
        self.vectara_manager = VectaraManager()
        self.vectara_client = self.vectara_manager.get_vectara_client()
        self.qa_agent = self.get_qa_agent()

    def get_qa_agent(self):
        '''
        Returns question answering agent
        :return:
        '''

        os.environ['OPENAI_API_KEY'] = self.secret_manager.openai_api_key

        doc_prompt = PromptTemplate(
            template="Content: {page_content}\nSource: {source} \n",
            input_variables=["page_content", "source"],
        )

        llm_src = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")

        qa_chain = create_qa_with_sources_chain(llm_src)
        qa_chain = StuffDocumentsChain(
            llm_chain=qa_chain,
            document_variable_name='context',
            document_prompt=doc_prompt,
        )
        chat = RetrievalQA(
            retriever=self.vectara_client.as_retriever(),
            combine_documents_chain=qa_chain,

        )

        return chat

    def get_full_question(self,
                          input_question,
                          past_conversation: List[Tuple[str,str]]) -> str:
        '''
        Will construct full query
        :param question:
        :param past_conversation:
        :return:
        '''
        query = ""
        for i, (question,answer) in enumerate(past_conversation):
            query += f"User question: {question},"
            query += f"Retrieval agent Answer: {answer},"

        query += f"User question: {input_question}, Retrieval agent Answer: "
        return query

    def chat(self, question: Question) -> Answer:

        query = self.get_full_question(input_question=question.question,
                                       past_conversation=question.context)

        answer = self.qa_agent({"query": query})

        print('---------')
        print(answer)
        print('---------')

        answer_text = answer['result']

        question.context.append((question.question,answer_text))
        return Answer(answer=answer_text,
                      past_conversations=question.context)
