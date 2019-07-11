from Led import Led

myLed = Led(0)

myLed.set_color((255, 0, 255), 1)
myLed.set_color((0, 255, 255), 2)

for i in range(21):
    myLed.update(.1)
    print(myLed.average_colors_with_opacity())