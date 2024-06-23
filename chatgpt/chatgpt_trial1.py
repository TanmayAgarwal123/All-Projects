import openai
import tkinter as tk
from tkinter import simpledialog

# Set up tkinter window
ROOT = tk.Tk()
ROOT.withdraw()

# Set OpenAI API key
openai.api_key = "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"

# Set the model and prompt(question)
model_engine = "text-davinci-003"
prompt = simpledialog.askstring(title="Chat-GPT version T.0", prompt="Hi!! What would you like to ask me or talk about ?")

# Generate response
response = openai.Completion.create(
    model=model_engine,
    prompt=prompt,
    max_tokens=150,
    temperature=0.5,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

# Print the response
print(response.choices[0].text)
