import genanki

tunings = "EADGBE"#"DADGAD"
notes = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
start = -1
max_fret = 5
chord_shapes = [[0,4,7],[0,3,7]]
chord_names = ["Major", "Minor"]

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
                                if count <= 0:
                                    tabs.append(tab)
    return tabs

def produce_chord_tabs(input_chord_list, chord_name):
    chord_list = chord_to_chromatic_notes(input_chord_list)
    output = [[],[]]
    for i in range(0,12):
        output[0].append(notes[i] + " " + chord_name)
        output[1].append(produce_tabs(start, max_fret, chord_list[i]))
    return output

def produce_all_chord_tabs(chord_shape_list, chord_names_list):
    output = [[],[]]
    for i in range(0,len(chord_shape_list)):
        chord_output = produce_chord_tabs(chord_shape_list[i], chord_names_list[i])
        for j in range(0,len(chord_output[0])):
            output[0].append(chord_output[0][j])
            output[1].append(chord_output[1][j])
    return output


print(produce_all_chord_tabs(chord_shapes, chord_names))
