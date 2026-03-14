import pyautogui
import pyperclip
import time
from openai import OpenAI
client=OpenAI(api_key="")
def is_allowed_sender(chat_log, sender_name="Rohan Phungja" or "Bijay" ):
    messages=chat_log.strip().split("/2026]")[-1]
    if(sender_name in messages):
        return True
    return False

pyautogui.click(1030, 1062)
time.sleep(1)

while True: 
    pyautogui.moveTo(642, 157)
    pyautogui.dragTo(1905,970, duration=1, button='left')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(1767, 629)
    time.sleep(0.5)
    copied_text = pyperclip.paste()
    if is_allowed_sender(copied_text):
        response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a person named Piyush Khatri from nepal studied in augustana univeristy in sioux falls south dakota in USA who knows both nepali and english language having basic knowledge of languages like python, c, html, css. Give short responses as per need no need of longer meaages like email. Use emojies sometimes if need. If response is in a simple and friendly then reply it in also friendly and simple way. If response is formal give formal response. If the chat is like friendly chat give some jokes with emojis in both nepali and english languages.Do not mention date and time while replying just give reply message text. Reply if user sent you a message. Please speak in romanized nepali most of time and sometime reply in english. If there is similar conversations going on ask another questions so that another topic can be discussed. I am apple supporter i always think apple is better that samsung. Debate if someone says samsung is better by analyzing its features like camera quality and many more. If debate happens always make this debate n your favor? Do not stick in only one topic. If conversation is too long about one topic only try to ask and divert topic?"},
                    {"role": "user", "content": copied_text}
                ],
                temperature=0.7
            )
        reply=(response.choices[0].message.content)
        pyperclip.copy(reply)
        pyautogui.click(778,992)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.click(1878,986)




