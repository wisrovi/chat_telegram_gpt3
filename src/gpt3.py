import openai # pip install openai

from config import API_KEY_GPT3, CONTEXT

#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = API_KEY_GPT3
completion = openai.Completion()

start_sequence = "\n\nSAM:"
restart_sequence = "\n\nPersona:"
session_prompt = CONTEXT

def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
      engine="davinci",
      prompt=prompt_text,
      temperature=0.8,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0.3,
      stop=["\n"],
    )
    story = response['choices'][0]['text']
    return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'

if __name__ == '__main__':
    incoming_msg = "como te llamas?"
    chat_log = None

    answer = ask(incoming_msg, chat_log)
    print(answer)