from gtts import gTTS
import os
import pygame


# Read a message from the user
message = input("Enter a message in Vietnamese: ")

# Convert the message to speech
tts = gTTS(message, lang='vi')

# Save the audio file
tts.save("message.mp3")

# Play the audio file
# os.system("start message.mp3")


# Initialize pygame
pygame.init()

# Load the audio file
audio_file = "message.mp3"
pygame.mixer.music.load(audio_file)

# Play the audio file
pygame.mixer.music.play()

# Wait for the audio to finish
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
