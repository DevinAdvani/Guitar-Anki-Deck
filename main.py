import genanki

tunings = "EADGBE"#"DADGAD"
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
guitar_notes = set(["C","E","G"])

def chord_to_chromatic_notes(input_chord_list):
    output = []
    for i in range(0, 12):
        chord = []
        for k in input_chord_list:
            chord.append(notes[(k+i)%12])
        output.append(set(chord))
    return output

def produce_tabs(input_start, input_max_fret, input_notes):
    tabs = []
    for a in range(start, max_fret+1):
        for b in range(start, max_fret+1):
            for c in range(start, max_fret+1):
                for d in range(start, max_fret+1):
                    for e in range(start, max_fret+1):
                        for f in range(start, max_fret+1):
                            count = 0
                            tab = [a,b,c,d,e,f]
                            for i in range(0,6):
                                if (tab[i] == -1):
                                    tab[i] = "X"
                                    count += 1
                            if tab_to_note(tab) == input_notes:
                                if count <= 1:
                                    tabs.append(tab)
    return tabs

def produce_chord_tabs(input_chord_list):
    chord_list = chord_to_chromatic_notes(input_chord_list)
    for i in range(0,12):
        print(notes[i])
        print(produce_tabs(start, max_fret, chord_list[i]))


#print(produce_tabs(start, max_fret, guitar_notes))

produce_chord_tabs([0, 4, 7])
