import os

from pydub import AudioSegment


def choosetracks(a, b):
    sound1 = AudioSegment.from_mp3(a + ".mp3")
    sound2 = AudioSegment.from_mp3(b + ".mp3")
    return [sound1, sound2]


def bassboost(a, b):
    a = a + 10
    b = b + 10
    return [a, b]


def speedup(a, b):
    a = a._spawn(a.raw_data, overrides={"frame_rate": int(a.frame_rate * 1.2)})
    b = b._spawn(b.raw_data, overrides={"frame_rate": int(b.frame_rate * 1.2)})
    return [a, b]


def mergetracks(a, b):
    return a + b


def outputname():
    print("Введите имя готового мэшапа")
    return input()


def exporttrack(a, name):
    a.export(name + ".mp3", format="mp3")


def choosingoption(a, mas):
    if a == 1:
        mas = bassboost(mas[0], mas[1])
    if a == 2:
        mas = speedup(mas[0], mas[1])
    if a == 3:
        mas = [mas[0][20 * 1000:150 * 1000], mas[1][20 * 1000:150 * 1000]]
    return mas

print("1.Гимн украины\n")
print("2.Моргештерн\n")
print("3.Шнип шнап шнапи\n")
print("4.Лсп\n")
print("Выберите первый файл для создания мэшапа")
a = input()
print("Выберите второй файл для создания мэшапа")
b = input()
mas = choosetracks(a, b)
while (True):
    print("Выберите то, что следует сделать с треками:" + '\n')
    print("1.Бассбуст" + '\n')
    print("2.Ускорить треки" + '\n')
    print("3.Обрезать треки" + '\n')
    print("4.Перейти к сохранению" + '\n')
    c = input()
    if (c == 4):
        break
    mas = choosingoption(c, mas)
outputfile = mergetracks(mas[0], mas[1])
name = outputname()
exporttrack(outputfile, name)
#
# if __name__ == 'main':
#     main()

# sound1 = AudioSegment.from_mp3("1.mp3")
# sound1 = sound1[20 * 1000:150 * 1000]
# sound1 = sound1 + 10
# sound1 = sound1._spawn(sound1.raw_data, overrides={
#     "frame_rate": int(sound1.frame_rate * 1.5)
# })
# sound2 = AudioSegment.from_mp3("2.mp3")
# sound2 = sound2[60 * 1000:]
# sound2 = sound2 + 10
# sound2 = sound2._spawn(sound2.raw_data, overrides={
#     "frame_rate": int(sound2.frame_rate * 1.3)
# })
# sound3 = sound2 + sound1
# sound3.export("3.mp3", format="mp3")