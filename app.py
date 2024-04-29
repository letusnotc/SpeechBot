import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import cv2
import numpy as np

class Frost:
    def _init_(self):
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)

    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def start(self):
        hour = datetime.datetime.now().hour
        if 5< hour < 12:
            self.speak("Good morning")
        elif 12 <= hour < 17:
            self.speak("Good afternoon")
        else:
            self.speak("Good evening")
        self.speak("I am Sarojjj. How can I help you?")

    def take_command(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language='en-in')
            print("User said:", query)
        except Exception as e:
            print("Can you please say that again......")
            self.speak("Can you please say that again......")
            return 'None'
        return query.lower()

    def run_frost(self):
        self.start()
        while True:
            query = self.take_command()
            if 'wikipedia' in query:
                self.speak("Searching Wikipedia.....")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2, auto_suggest=False)
                self.speak("According to Wikipedia")
                print(results)
                self.speak(results)
            elif 'open youtube' in query:
                self.speak("Opening YouTube")
                webbrowser.open("https://www.youtube.com")
            elif 'open google' in query:
                self.speak("Opening Google")
                webbrowser.open("https://www.google.com")
            elif 'the time' in query:
                str_time = datetime.datetime.now().strftime("%H:%M:%S")
                self.speak("The time is")
                self.speak(str_time)
                print(str_time)
            elif 'how are you' in query:
                self.speak("I am fine. Thank you for asking.")
            elif 'tell me something about yourself' in query:
                self.speak("My name is Saroj. I am a virtual assistant made to help you in your day-to-day works.")
            elif 'play music' in query:
                music_dir = 'C:\\Users\\harsh\\Music\\New folder'  # Change this to your music directory
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))
                break
            elif 'turn off' in query:
                self.speak("Goodbye folks")
                break
            elif 'colour recognition' in query:
            
                cap = cv2.VideoCapture(0)
                cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
                cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

                colors = {
                    "RED": ([0, 50, 50], [10, 255, 255]),  # Hue range: 0-10 and 170-180
                    "ORANGE": ([10, 100, 100], [20, 255, 255]),  # Hue range: 10-20
                    "YELLOW": ([20, 100, 100], [30, 255, 255]),  # Hue range: 20-30
                    "GREEN": ([30, 100, 100], [60, 255, 255]),  # Hue range: 30-60
                    "CYAN": ([90, 100, 100], [110, 255, 255]),  # Hue range: 90-110
                    "BLUE": ([110, 100, 100], [130, 255, 255]),  # Hue range: 110-130
                    "VIOLET": ([130, 100, 100], [155, 255, 255]),  # Hue range: 130-155
                    "MAGENTA": ([155, 100, 100], [175, 255, 255]),  # Hue range: 155-175
                    "PINK": ([175, 100, 100], [185, 255, 255]),  # Hue range: 175-185
                    "WHITE": ([0, 0, 240], [255, 15, 255]),  # Hue range: all
                    "BLACK": ([0, 0, 0], [180, 255, 60]),  # Hue range: all
                    "GRAY": ([0, 0, 105], [180, 30, 190]),
                    "BROWN": ([10, 60, 60], [20, 180, 180]),
                    "MAROON": ([0, 100, 100], [10, 255, 255]),
                    "GOLD": ([20, 120, 120], [30, 255, 255]),
                    "SILVER": ([0, 0, 180], [180, 25, 255]),
                    "PURPLE": ([130, 100, 100], [160, 255, 255]),
                    "INDIGO": ([100, 100, 100], [130, 255, 255]),
                    "TEAL": ([80, 100, 100], [90, 255, 255]),
                    "LIME": ([60, 100, 100], [80, 255, 255]),
                    "OLIVE": ([30, 100, 100], [50, 255, 255]),
                    "TURQUOISE": ([70, 100, 100], [80, 255, 255]),
                    "AQUA": ([85, 100, 100], [100, 255, 255]),
                    "CORAL": ([0, 100, 100], [10, 255, 255]),
                    "SALMON": ([0, 100, 100], [10, 255, 255]),
                    "TAN": ([10, 100, 100], [20, 200, 200]),
                    "BEIGE": ([20, 100, 100], [30, 200, 200]),
                }

                # Define the size of the region around the center pixel
                region_size = 10

                while True:
                    _, frame = cap.read()
                    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                    height, width, _ = frame.shape

                    cx = int(width / 2)
                    cy = int(height / 2)

                    # Define the region of interest around the center pixel
                    roi = hsv_frame[cy - region_size:cy + region_size, cx - region_size:cx + region_size]

                    # Calculate the average color within the ROI
                    avg_hue = np.mean(roi[:, :, 0])
                    avg_saturation = np.mean(roi[:, :, 1])
                    avg_value = np.mean(roi[:, :, 2])

                    color = "Undefined"
                    for col, (lower, upper) in colors.items():
                        lower_bound = np.array(lower)
                        upper_bound = np.array(upper)
                        if lower_bound[0] <= avg_hue <= upper_bound[0] and \
                           lower_bound[1] <= avg_saturation <= upper_bound[1] and \
                           lower_bound[2] <= avg_value <= upper_bound[2]:
                            color = col
                            break

                    cv2.rectangle(frame, (cx - region_size, cy - region_size), (cx + region_size, cy + region_size), (255, 255, 255), 2)
                    cv2.putText(frame, color, (cx - 100, cy - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                    cv2.imshow("Frame", frame)
                    key = cv2.waitKey(1)
                    if key == 27:
                        break

                cap.release()
                cv2.destroyAllWindows()
            else:
                self.speak("Sorry!!! Out of my current abilities")




z=input("")
if __name__ == "__main__":
    frost = Frost()
    frost.run_frost()