filename = 'programming.txt'
text_filename = 'text.txt'

with open(filename, 'w') as write_oject:
    text_module = write_oject.write('import os\n')
    text_module = write_oject.write('print("Ну ты и Ламер")\n')
    print(text_module)

with open(filename, 'r') as read_object:
    for i in read_object:
        print(i.rstrip())
with open(filename, 'a') as write_object:
    write_object.write('def dumbas(self):\n')
    write_object.write('\t print("I hate this code")')
    print(filename)