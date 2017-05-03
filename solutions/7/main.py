import base64

# Paste the base64 with all the code in entrada.txt
# Execute this command
# Copy and paste everything inside salida.txt in Chrome's console
# For the next level, only paste the 's2(XXXXXX)' lines

f2 = open("entrada.txt", "r")
result = f2.readline().strip()

x = base64.b64decode(result)
s = "tablero=" + x[x.find("[["):x.find("]]")+2]
exec(s)
t = "palabras=" + x[x.find("[", x.find("]]")+2):x.find("]", x.find("]]")+2)+1]
exec(t)

tab = [''.join(x) for x in tablero]
tab = '\n'.join(tab)

f = open("salida.txt", "w")

f.write('''
    const mn=t=>{
    let n,e,o,s=0;
    c=t+"-saltbae";
    if(!c.length)
        return s;
    for(n=0,o=c.length;n<o;n++)
        e=c.charCodeAt(n),s=(s<<5)-s+e,s|=0;
    return Math.abs(s)
},
s2=((t)=>{
    //console.log(t + "-");
    //console.log(`${t}-${mn(t)}`);
    w.send(btoa(`${t}-${mn(t)}`));
});
''')

puzzle = tab
clues = palabras
   
puzzle = puzzle.replace(' ','')          
length = puzzle.index('\n')+1
letters = [(letter, divmod(index, length))
            for  index, letter in enumerate (puzzle)]

lines = {}
offsets = {'down':0, 'right down':-1, 'left down':1}
for direction, offset in offsets.items():
    lines[direction] = []
    for i in range(length):
        for j in range(i, len(letters), length + offset):
            lines[direction].append(letters[j])
        lines[direction].append('\n')
lines['left']  = letters
lines['right'] = [i for i in reversed(letters)]
lines['up'] = [i for i in reversed(lines['down'])]
lines['right up'] = [i for i in reversed(lines['right down'])]
lines['left up'] = [i for i in reversed(lines['left down'])]

for direction, tup in lines.items():
    string = ''.join([i[0] for i in tup])
    for word in clues:
        if word in string:
            location = tup[string.index(word)][1]
            resa = location[0]
            resb = location[1]
            l = len(word)-1

            if direction == "left":
                resc = resa
                resd = resb+l
            if direction == "right":
                resc = resa
                resd = resb-l
            if direction == "up":
                resc = resa-l
                resd = resb
            if direction == "down":
                resc = resa+l
                resd = resb
            if direction == "left down":
                resc = resa+l
                resd = resb+l
            if direction == "left up":
                resc = resa-l
                resd = resb-l
            if direction == "right down":
                resc = resa+l
                resd = resb-l
            if direction == "right up":
                resc = resa-l
                resd = resb+l

            f.write("s2(\"" + str(resb)+"-"+str(resa)+"-"+str(resd)+"-"+str(resc) + "\")\n")
f.close()