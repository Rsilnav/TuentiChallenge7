def transform(caracteres):
    try:
        return '{0:1x}'.format(int(caracteres))
    except:
        return "N/A"

import io
file = io.open("submitInput.txt",'r',encoding='utf-16-le')
for i, line in enumerate(file.readlines()[1:]):
    print "Case #" + str(i+1) + ": " + transform(line.strip())
