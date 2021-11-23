import openai # pip install openai
from config import API_KEY_GPT3 as config
from train import CONTEXT as train

openai.api_key = config.API_KEY_GPT3

start_sequence = "\nSAM:"
restart_sequence = "\nHuman:"

def ask(question, chat_log=None):
  prompt_text = f"{chat_log}{restart_sequence}: {question}{start_sequence}:"
  response = openai.Completion.create(
    engine="davinci",
    prompt=prompt_text,
    temperature=0.8,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.3,
    stop=["\n"]
  )
  story = response['choices'][0]['text']
  return str(story)

def append_interaction_to_chat_log(question, answer, chat_log):
  if chat_log is None:
    chat_log = train.CONTEXT
  return f"{chat_log}{restart_sequence} {question}{start_sequence}{answer}:"

def getAnswer(question, chat_log):
  answer = ask(question, chat_log)
  new_log = append_interaction_to_chat_log(question, answer, chat_log)
  return answer, new_log


if __name__=="__main__":
  texto_usuario = "hola, como estas, quiero conocerte, como te llamas?"
  chat_log = train.CONTEXT
  answer, _ = getAnswer(texto_usuario, chat_log)
  print(answer)









































