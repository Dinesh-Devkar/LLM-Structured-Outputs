from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Optional,Literal,Annotated

load_dotenv()

class Review(TypedDict):
    summary:Annotated[str,"a short summary of the review in 3 words"]
    sentiment:Annotated[Literal['pos','neg'],"write down sentiment of the review"]
    pros:Annotated[Optional[list[str]],"write down all the pros mention in review. Note :  mention the pros only if explicitely present in review"]
    cons: Annotated[Optional[list[str]],'write down all the cons mention in review.  Note :  mention the cons only if explicitely present in review']
    reviewer: Annotated[Optional[str],"write the name of the person who write the review"]


model= ChatOpenAI(model='gpt-4o')

model=model.with_structured_output(Review)

result=model.invoke(""""Usb 2.0 port? Man thats a scam
The 3.2 was what set""")

print(result)