from playsound import playsound
import time
import keyboard
from random import randrange
import os
import re

# Load sound
base_path = os.getcwd()
tones_path = base_path + "/Tones/"
scales_path = base_path + "/MajorScales/"

tones = [tones_path + "01G.mp3",
         tones_path + "02Gis.mp3",
         tones_path + "03A.mp3",
         tones_path + "04B.mp3",
         tones_path + "05H.mp3",
         tones_path + "06c.mp3",
         tones_path + "07cis.mp3",
         tones_path + "08d.mp3",
         tones_path + "09dis.mp3",
         tones_path + "10e.mp3",
         tones_path + "11f.mp3",
         tones_path + "12fis.mp3",
         tones_path + "13g.mp3",
         tones_path + "14gis.mp3",
         tones_path + "15a.mp3",
         tones_path + "16b.mp3",
         tones_path + "17h.mp3",
         tones_path + "18c1.mp3",
         tones_path + "19cis1.mp3",
         tones_path + "20d1.mp3",
         tones_path + "21dis1.mp3",
         tones_path + "22e1.mp3",
         tones_path + "23f1.mp3",
         tones_path + "24fis1.mp3",
         tones_path + "25g1.mp3"]


scales = [scales_path + "Scale01G.mp3",
          scales_path + "Scale02Gis.mp3",
          scales_path + "Scale03A.mp3",
          scales_path + "Scale04B.mp3",
          scales_path + "Scale05H.mp3",
          scales_path + "Scale06C.mp3",
          scales_path + "Scale07Cis.mp3",
          scales_path + "Scale08D.mp3",
          scales_path + "Scale09Dis.mp3",
          scales_path + "Scale10E.mp3",
          scales_path + "Scale11F.mp3",
          scales_path + "Scale12Fis.mp3"]

scale_default = [0, 2, 4, 5, 7, 9, 11, 12]
scale_names = ['G', 'Gis', 'A', 'B', 'H', 'C', 'Cis', 'D', 'Dis', 'E', 'F', 'Fis']
tones_number = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th']


def get_random_scale():
    offset = randrange(len(scales))
    time.sleep(0.2)
    return offset, [offset + index for index in scale_default]


def play_random_tones(current_scale, number_of_tones):
    played_tones = []
    played_tones_exact = []
    for i in range(number_of_tones):
        index = randrange(len(current_scale))
        played_tones.append(index)
        played_tones_exact.append(tones[current_scale[index]])
        playsound(tones[current_scale[index]])
    return played_tones, played_tones_exact


def play_tones(current_scale, played_tones):
    for tone in played_tones:
        playsound(tones[current_scale[tone]])


def play_scale(offset):
    playsound(scales[offset])


def change_number_of_tones(number_of_tones, by):
    number_of_tones += by
    if number_of_tones <= 0:
        number_of_tones = 0
    time.sleep(0.2)
    return number_of_tones


def show_answer(played_tones, played_tones_exact):
    print("\nThat was: ", end="")
    for i in played_tones[0:-1]:
        print(tones_number[i], end=", ")
    print(tones_number[played_tones[-1]], end="")

    print(" (", end="")
    for i in played_tones_exact[0:-1]:
        print(re.sub(".*[0-9]{2}(.*)\.mp3", "\\1", i), end=", ")
    print(re.sub(".*[0-9]{2}(.*)\.mp3", "\\1", played_tones_exact[-1]), end="")
    print(")")
    time.sleep(0.2)


def show_status(offset, number_of_tones):
    print("\nCurrent key:", scale_names[offset])
    print("Number of tones:", number_of_tones)


def show_commands():
    print("Commands:")
    print("  N: play random tones")
    print("  M: show answer")
    print("  B: repeat tones")
    print("  Q: quit")
    print("  1-8: play tone from scale")
    print("  S: play scale")
    print("  Y: increase number of tones played by 1")
    print("  X: decrease number of tones played by 1")
    print("  C: change the scale")


def app():
    number_of_tones = 1
    played_tones = []
    offset, current_scale = get_random_scale()
    show_commands()
    show_status(offset, number_of_tones)

    while True:
        try:
            if keyboard.is_pressed('q'):
                break

            elif keyboard.is_pressed('n'):  # Next
                played_tones, played_tones_exact = play_random_tones(current_scale, number_of_tones)

            elif keyboard.is_pressed('m'):
                show_answer(played_tones, played_tones_exact)

            elif keyboard.is_pressed('b'):  # Repeat
                play_tones(current_scale, played_tones)

            elif keyboard.is_pressed('s'):
                play_scale(offset)

            elif keyboard.is_pressed('y'):
                number_of_tones = change_number_of_tones(number_of_tones, by=1)
                show_status(offset, number_of_tones)

            elif keyboard.is_pressed('x'):
                number_of_tones = change_number_of_tones(number_of_tones, by=-1)
                show_status(offset, number_of_tones)

            elif keyboard.is_pressed('c'):
                offset, current_scale = get_random_scale()
                show_status(offset, number_of_tones)

            elif keyboard.is_pressed('1'):
                playsound(tones[current_scale[0]])
            elif keyboard.is_pressed('2'):
                playsound(tones[current_scale[1]])
            elif keyboard.is_pressed('3'):
                playsound(tones[current_scale[2]])
            elif keyboard.is_pressed('4'):
                playsound(tones[current_scale[3]])
            elif keyboard.is_pressed('5'):
                playsound(tones[current_scale[4]])
            elif keyboard.is_pressed('6'):
                playsound(tones[current_scale[5]])
            elif keyboard.is_pressed('7'):
                playsound(tones[current_scale[6]])
            elif keyboard.is_pressed('8'):
                playsound(tones[current_scale[7]])
        except:
            print("inside except")
            continue

if __name__ == "__main__":
    app()