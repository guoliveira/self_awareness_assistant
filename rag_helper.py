INSTRUCTIONS = """
You are a helpful assistant that answers questions regarding self-awareness based on the provided context.

Use the context to find relevant information and provide accurate
answers. 
With the answer, provide one link to the YouTube video where the answer can be found.
If the answer is not found in the context,
respond with "I don't know."
"""

PROMPT_TEMPLATE = """
QUESTION: {question}

CONTEXT:
{context}
""".strip()

class RAGBase:
    """Base helper for performing Retrieval-Augmented Generation (RAG).

    Wraps a vector index and an LLM client to search course content,
    assemble a contextual prompt, and call the LLM to generate an answer.

    Args:
        index: A vector index instance implementing a `search(query, ...)`
            method that returns a list of documents (dict-like) with keys
            `section`, `question`, and `answer`.
        llm_client: An LLM client with a `responses.create(...)` API used to
            call the model. The `llm` method expects `llm_client.responses.create`
            to return an object with an `output_text` attribute.
        instructions: Optional developer instructions passed to the LLM.
        prompt_template: Template string used to build the LLM prompt.
        course: Filter value applied to searches to scope results.
        model: Model name passed to the LLM client.
    """

    def __init__(
        self,
        index,
        llm_client,
        instructions=INSTRUCTIONS,
        prompt_template=PROMPT_TEMPLATE,
        model="gpt-5.4-mini"
    ):
        self.index = index
        self.llm_client = llm_client
        self.instructions = instructions
        self.prompt_template = prompt_template
        self.model = model

    def search(self, query, num_results=5):
        #boost_dict = {"question": 3.0, "section": 0.5}
        #filter_dict = {"course": self.course}

        return self.index.search(
            query,
            num_results=num_results,
            #boost_dict=boost_dict,
            #filter_dict=filter_dict
        )
    
    def build_context(self, search_results):
        lines = []

        for doc in search_results:
            lines.append('Q: ' + doc['question'])
            lines.append('A: ' + doc['answer'])
            lines.append('Suggested Video: https://www.youtube.com/watch?v=' + doc['video_id'])
            lines.append(' ')

        return '\n'.join(lines).strip()
    
    def build_prompt(self, question, search_results):

        context = self.build_context(search_results)
        prompt = self.prompt_template.format(
            question=question,
            context=context
        )
        return prompt.strip()
    
    def llm(self, prompt):
        """Call the LLM client with developer instructions and a user prompt.

        Args:
            prompt (str): The prompt text to send as the user message.

        Returns:
            str: The model's textual response.
        """
        input_messages = [
            {"role": "developer", "content": self.instructions},
            {"role": "user", "content": prompt}
        ]

        response = self.llm_client.responses.create(
            model=self.model,
            input=input_messages
        )

        return response.output_text

    def rag(self, query):
        """Full RAG flow: search, prompt build, and LLM call.

        Args:
            query (str): User question.

        Returns:
            str: Answer returned by the LLM.
        """
        search_results = self.search(query)
        prompt = self.build_prompt(query, search_results)
        answer = self.llm(prompt)
        return answer
    