from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def generate_pet_name():
    llm = OpenAI(temperature=0.7)
    name = llm.invoke("I have a dog and I want a cool name for it. Can you suggest me 5 cool names and explain the meaning of those name.")
    return name
if __name__ == "__main__":
    print(generate_pet_name())
