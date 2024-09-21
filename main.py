tunings = "EADGBE"
notes = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]

def shift(input_note, semi_tones):
    position = notes.index(input_note)
    position += semi_tones
    position %= 12
    return notes[position]

def tab_to_note(input_tab):
    output = ""
    for i in range(0,6):
        output += shift(tunings[i], int(input_tab[2 * i]))
        output += " "
    return output

max_fret = 3

for a in range(0, max_fret+1):
    for b in range(0, max_fret+1):
        for c in range(0, max_fret+1):
            for d in range(0, max_fret+1):
                for e in range(0, max_fret+1):
                    for f in range(0, max_fret+1):
                        print(str(a) + " " + str(b) + " " +  str(c) + " " +  str(d) + " " +  str(e) + " " +  str(f))
                        print(tab_to_note(str(a) + " " + str(b) + " " +  str(c) + " " +  str(d) + " " +  str(e) + " " +  str(f)))
