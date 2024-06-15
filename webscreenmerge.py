# HTML Template mit den Daten der Tag/Value Liste befüllen

screen = open("/home/pi/webscreentemplate.html", "r").read()

with open("/home/pi/data/webscreendata.txt", "r") as f:
    lines = f.readlines()

line_number = 0
for line in lines:
    tag, value = line.strip().split(":", 1)
    if line_number == 0:
        screen = screen.replace("%HEADER%", value)
    else:
        screen = screen.replace(f"%BEZ{line_number}%", tag)
        screen = screen.replace(f"%VAL{line_number}%", value)
    line_number += 1

print(screen)

