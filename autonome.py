

# 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



import openai

# openai.api_key = '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'

openai.api_key = 'sk-BJbo37QpvgqMxHKzCZGPmLUfWIfWA0wos4aD8St5LqT3BlbkFJSgU7tjJv3NelsTxuI4KRJQpPNnPQ6_-TDaUZcIyjIA'

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Ou un autre modèle comme gpt-4
    messages=[
        {"role": "user", "content": "Quelle est la capitale de la France ?"}
    ]
)

print(response.choices[0].message.content.strip())

#
# import openai
# import asyncio
#
#
# async def get_response(prompt):
#     response = await openai.ChatCompletion.acreate(
#         model="gpt-4o-mini",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     print(response['choices'][0]['message']['content'])
#
# async def main():
#     prompts = ["Quelle est la capitale de la France ?"] * 20  # 20 fois la même question
#     tasks = [get_response(prompt) for prompt in prompts]
#     await asyncio.gather(*tasks)
#
# # Exécutez le programme
# asyncio.run(main())
