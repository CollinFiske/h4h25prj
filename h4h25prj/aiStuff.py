from groq import Groq
import os

client = Groq(
    api_key = ""
)

def getAIStuff(address, price):
    
    chat_completion = client.chat.completions.create(
        messages=[
                {
                "role" : "system", # user or system
                "content" : "You are trying to figure out if an inputted rental property is a good deal. Given the address and the monthly rental price and that is in Los Angeles in California, give it a score out of 10 where 1 is a bad deal, 7 is a good deal and 10 is an amazing deal."
            },
            {
                "role" : "user", # user or system
                "content" : f"Here's the address: {address} and the monhtly rent: {price}."
            }
        ],
        model="llama3-8b-8192" #from groq website
    )

    output = chat_completion.choices[0].message.content
    return output
