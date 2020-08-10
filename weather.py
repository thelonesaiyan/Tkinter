from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title('Weather App')
root.iconbitmap('icons/weather.ico')
root.geometry("400x50")

try:
    req_api = requests.get(
        'http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=00A4A0EE-EC50-44EF-B3D6-05B3DC050807')
    api = json.loads(req_api.content)

except Exception as e:
    api = "Error....."

lab = Label(root, text=api[0])
lab.pack()


root.mainloop()