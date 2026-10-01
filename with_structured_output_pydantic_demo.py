from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel,Field
from typing import Optional,Literal


load_dotenv()


class Review(BaseModel):
    summay:str=Field(description='a short summary of the review in less than 10 words')
    sentimet:Literal['pos','neg','neu']=Field(description="a sentiment of the review")
    key_themes:Optional[list[str]] = Field(default=None,description='write down all the important key themes discussed in the review')
    pros : Optional[list[str]] = Field(default=None,description="write down all the pros present in the review")
    cons:Optional[list[str]] = Field(default=None,description="write down all the cons present in the review")


model=ChatOpenAI(model='gpt-4o')
model=model.with_structured_output(Review)

result=model.invoke("""Usb 2.0 port? Man thats a scam
The 3.2 was what set samsung apart from far better value "flagship killer" chinese phones...""")

print(result)
print(result.sentimet)