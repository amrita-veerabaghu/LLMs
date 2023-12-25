from langchain.schema import (
    HumanMessage
)
from fetch_and_parse import fetch_and_parse
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv

load_dotenv('../../env.sh')


class ChatNewsSummarizer:
    def __init__(self,
                 system_message,
                 chat_model_name,
                 model_temperature):
        self.template = system_message + """
        
                        Here's the article you want to summarize.
                        
                        ==================
                        Title: {article_title}
                        
                        {article_text}
                        ==================
                        
                        Write a summary of the previous article.
                        """
        # load the model
        self.chat = ChatOpenAI(model_name=chat_model_name, temperature=model_temperature)

    def summarize_article(self, article_url):
        title, text = fetch_and_parse(article_url)
        prompt = self.template.format(article_title=title, article_text=text)
        summary = self.chat([HumanMessage(content=prompt)])
        return summary.content


if __name__ == '__main__':
    system_mess = "You are an advanced AI assistant that summarizes online articles into bulleted lists"
    example_article = \
        "https://www.artificialintelligence-news.com/2022/01/25/meta-claims-new-ai-supercomputer-will-set-records/"
    news_summarizer = ChatNewsSummarizer(system_message=system_mess,
                                         chat_model_name="gpt-4",
                                         model_temperature=0)

    print(news_summarizer.summarize_article(example_article))

