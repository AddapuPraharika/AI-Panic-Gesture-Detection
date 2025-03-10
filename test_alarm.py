import pygame
import time

pygame.mixer.init()
pygame.mixer.music.load("alarm.mp3")  # Ensure alarm.mp3 is in the same folder
pygame.mixer.music.play()

print("🔊 Playing Alarm...")
time.sleep(5)  # Play for 5 seconds
pygame.mixer.music.stop()
print("✅ Alarm Stopped!")
