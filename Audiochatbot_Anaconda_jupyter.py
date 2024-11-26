#!/usr/bin/env python
# coding: utf-8

# # Audio chatbot

# In[ ]:


pip install SpeechRecognition pyttsx3


# In[ ]:


pip install pyaudio


# In[1]:


import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Sample chatbot data (input and response pairs)
chatbot_data = {
    "hello": "Hi there! How can I assist you today?",
    "what is your name": "I am your friendly chatbot. You can call me ChatBot!",
    "tell me a joke": "Why don’t skeletons fight each other? They don’t have the guts!",
    "how are you": "I'm just a program, but I'm functioning as expected. How about you?",
    "bye": "Goodbye! Have a great day!",
    "Who Is Ammar": "My Master"
}


# In[2]:


# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech input
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source)
            user_input = recognizer.recognize_google(audio)
            return user_input.lower()  # Convert to lowercase for consistency
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Could you repeat?")
            return None
        except sr.RequestError:
            speak("Sorry, there seems to be an issue with the speech recognition service.")
            return None


# In[3]:


# Main chatbot loop
def chatbot():
    speak("Hello! I am your chatbot. Say something to start.")
    while True:
        user_input = recognize_speech()
        if user_input:
            print(f"You: {user_input}")
            
            # Get chatbot response
            response = chatbot_data.get(user_input, "I'm sorry, I don't understand that.")
            
            # Respond to user
            print(f"Bot: {response}")
            speak(response)
            
            # Exit condition
            if user_input == "bye":
                break

if __name__ == "__main__":
    chatbot()


# In[ ]:




