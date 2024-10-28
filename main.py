import genanki
import os

tunings = "EADGBE"#"DADGAD"
notes = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
start_fret = -1
max_fret = 1
chord_shapes = [[0,4,7], [0,4,7,11], [0,4,7,9], [0,4,7,9,14], [0,4,7,9,14], [0,4,7,9,14,17], [0,3,7],[0,3,7,10], [0,3,7,9],[0,3,7,9,14],[0,3,7,10,14], [0,3,7,10,14,17], [0,3,7,11], [0,3,7,11,14], [0,4,7,10], [0,4,7,10,14], [0,4,7,10,14,17], [0,3,6], [0,3,6,9], [0,3,6,10],[0,4,8],[0,4,8,10], [0,4,6,10], [0,4,8,10], [0,4,7,10,13], [0,4,7,10,15], [0,4,7,10,18], [0,7],[0,4,7,14], [0,2,4,7],[0,4,7,17],[0,4,5,7], [0,5,7], [0,2,7]]
overall_chord_names = ["Major", "Major 7", "6", "69", "Major 9", "Major 11", "Minor", "Minor 7", "Minor 6", "Minor 69", "Minor 9", "Minor 11", "Minor Major 7", "Minor Major 9", "7", "9", "11", "Diminished", "Diminished 7", "Half-Diminished", "Augmented", "Augmented 7", "7-5", "7+5", "7-9", "7+9", "7#11", "5", "Add 9", "Add 2", "Add 11", "Add 4", "Suspended 4", "Suspended 2"]
chord_notes = [] # fix slashes
chord_names = []

for i in overall_chord_names:
    try:
        os.rmdir(tunings + "/" + i)
    except:
        pass

try:
    os.rmdir(tunings)
except:
    pass

os.mkdir(tunings)

for i in overall_chord_names:
    try:
        os.mkdir(tunings + "/" + i)
    except:
        pass

def pitch_up_a_tab(input_tab):
    output_tab = []
    for i in range(0,6):
        try:
            output_tab.append(input_tab[i]+1)
        except:
            output_tab.append("X")
    return output_tab

#print(pitch_up_a_tab([1,"X",3,4,5,"X"]))

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

def produce_open_chord_tabs():
    tabs = []
    for a in range(-1,max_fret+1):
        for b in range(-1,max_fret+1):
            for c in range(-1,max_fret+1):
                for d in range(-1,max_fret+1):
                    for e in range(-1,max_fret+1):
                        for f in range(-1,max_fret+1):
                            tab = [a,b,c,d,e,f]
                            if 0 in tab:
                                for i in range(0,6):
                                    if (tab[i] == -1):
                                        tab[i] = "X"
                                tabs.append(tab)
    return tabs

for i in range(0,len(chord_shapes)):
    tmp_notes = chord_to_chromatic_notes(chord_shapes[i])
    for j in range(0,12):
        chord_names.append(notes[j] + " " + overall_chord_names[i])
        chord_notes.append(tmp_notes[j])

open_chords = produce_open_chord_tabs()

chords = []

for i in range(0,len(open_chords)):
    try:
        chords.append([chord_names[chord_notes.index(tab_to_note(open_chords[i]))], open_chords[i]])
    except:
        pass


"""
def make_deck():
    output_tabs = produce_tabs(start_fret, max_fret)

    my_model = genanki.Model(
    1607392319,
    'Simple Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
        {
        'name': 'Card 1',
        'qfmt': '{{Question}}',
        'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
        },
    ])

    my_deck = genanki.Deck(
    2059400110,
    'Guitar Chords::' + tunings + " until " + str(max_fret))

    for i in range(0,len(output_tabs)):
        try:
            other_side = chord_names[chord_notes.index(tab_to_note(output_tabs[i]))]
            my_note = genanki.Note(
            model=my_model,
            fields=[tunings + " " + str(output_tabs[i]), other_side])
            my_deck.add_note(my_note)
        except:
            pass

        
    genanki.Package(my_deck).write_to_file(tunings + " until " + str(max_fret) + '.apkg')

"""