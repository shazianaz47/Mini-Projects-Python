import time
import random
from colorama import Fore, init, Style


init(autoreset=True)  # Initialize colorama

print(Fore.GREEN + "🎉✨ Eid Mubarak Mad Libs Game ✨🎉\n")
print(Fore.YELLOW + "🔹 Aapko kuch random words dene hain, aur hum ek mazedaar Eid story banayenge!\n")

# User Inputs
adjective = input(Fore.CYAN + "Ek adjective likho (e.g.roshan, happy, bright): ")
noun = input(Fore.CYAN + "Ek noun likho (e.g., sawaiyan, eidi): ")
verb = input(Fore.CYAN + "Ek verb likho (e.g., mingle each other, mubarakbad de rahay hain): ")
place = input(Fore.CYAN + "Ek jagah ka naam likho (e.g.relative'shome, market): ")
person = input(Fore.CYAN + "Ek person ka naam likho (e.g., Ahmed, Ammi, Dada): ")

# Multiple Random Stories
stories = [
    f"\nThe day of Eid was very {adjective}. Early in the morning, {person} woke me up, and we went to {place}.\n"
f"There, everyone was enjoying {noun} happily and {verb}. Sweets and the lights of Eid were everywhere! 🕌✨\n",

f"\nA grand celebration of Eid at {place}! Everyone wore new clothes, and {person} gave {noun} to everyone.\n"
f"Then we started {verb} and greeted everyone with 'Eid Mubarak'! 🎊"

]

# Select a random story
selected_story = random.choice(stories)

print(Fore.MAGENTA + "\n⏳ Creating your Eid story...\n")
time.sleep(3)  # ⏳ 2 sec delay for fun
print(Fore.LIGHTGREEN_EX + selected_story)
print(Fore.YELLOW + "🎉 Eid Mubarak! 🎉")
