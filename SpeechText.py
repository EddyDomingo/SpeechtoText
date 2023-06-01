import speech_recognition as sr
import os
import openai

# Set up your OpenAI API key
openai.api_key = 'API-KEY'

# # Create a recognizer object
r = sr.Recognizer()

# # Load the audio file
audio_file = sr.AudioFile('Prompt.wav')

# # Open the audio file and convert speech to text
with audio_file as source:
     audio = r.record(source)

# # Use Google Cloud Speech API for speech recognition
text = r.recognize_google(audio)

# # Print the transcribed text
#print(text)

# # Make a request to ChatGPT
response = openai.Completion.create(
  engine='text-davinci-003',
  prompt=text,
  max_tokens=500,
  n=2,
  stop=None,
  temperature=0.7
)

# # Get the generated text from the response
generated_text = response.choices[0].text.strip()
generated_text1 = response.choices[1].text.strip()

# # Print the generated text
print(generated_text)
print('-------------')
print(generated_text1)










