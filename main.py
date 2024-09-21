tunings = "EADGBE"
notes = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]

def shift(input_note, semi_tones):
    position = notes.index(input_note)
    position += semi_tones
    position %= 12
    return notes[position]

def tab_to_note(input_tab):
    output = []
    for i in range(0,6):
        if (input_tab[i] != 'X'):
            output.append(shift(tunings[i], input_tab[i]))
    return set(output)

start = -1
max_fret = 5
"""
for a in range(start, max_fret+1):
    for b in range(start, max_fret+1):
        for c in range(start, max_fret+1):
            for d in range(start, max_fret+1):
                for e in range(start, max_fret+1):
                    for f in range(start, max_fret+1):
                        tab = [a,b,c,d,e,f]
                        for i in range(0,6):
                            if (tab[i] == -1):
                                tab[i] = "X"
                        if tab_to_note(tab) == {"C", "F"}:
                            print(tab)
"""

chord = [0,4,7]

for i in range(0,12):
    output = []
    for j in chord:
        output.append(notes[(i+j)%12])
    print(set(output))