import openai
import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.withdraw()

openai.api_key = "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"
# Set the model and prompt(question)
model_engine = "text-davinci-003"
prompt = simpledialog.askstring(title="Chat-GPT version T.0", prompt="Hi!! What would you like to ask me or talk about ?")

max_tokens = 1024
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=max_tokens,
    temperature=0.5,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
print(completion.choices[0].text)