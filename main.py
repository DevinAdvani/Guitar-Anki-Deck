import genanki

tunings = "EADGBE"
notes = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
start_fret = -1
max_fret = 2#12
chord_shapes = [[0,4,7], [0,4,7,9]]
overall_chord_names = ["Major", "Major 7", "6", "6/9", "Major 9", "Major 11", "Minor", "Minor 7", "Minor 6", "Minor 6/9", "Minor 9", "Minor 11", "Minor Major 7", "Minor Major 9", "7", "9", "11", "Diminished", "Diminished 7", "Half-Diminished", "Augmented", "Augmented 7", "7-5", "7+5", "7-9", "7+9", "7#11", "5", "Add 9", "Add 2", "Add 11", "Add 4", "Suspended 4", "Suspended 2"]
chord_notes = []
chord_names = []

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

def produce_tabs(input_start, input_max_fret):
    tabs = []
    for a in range(input_start, input_max_fret+1):
        for b in range(input_start, input_max_fret+1):
            for c in range(input_start, input_max_fret+1):
                for d in range(input_start, input_max_fret+1):
                    for e in range(input_start, input_max_fret+1):
                        for f in range(input_start, input_max_fret+1):
                            tab = [a,b,c,d,e,f]
                            for i in range(0,6):
                                if (tab[i] == -1):
                                    tab[i] = "X"
                            tabs.append(tab)
    tabs.remove(["X","X","X","X","X","X"])
    return tabs

for i in range(0,len(chord_shapes)):
    tmp_notes = chord_to_chromatic_notes(chord_shapes[i])
    for j in range(0,12):
        chord_names.append(notes[j] + " " + overall_chord_names[i])
        chord_notes.append(tmp_notes[j])


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
        except:
            other_side =  str(tab_to_note(output_tabs[i]))
        my_note = genanki.Note(
        model=my_model,
        fields=[tunings + " " + str(output_tabs[i]), other_side])
        my_deck.add_note(my_note)
        
    genanki.Package(my_deck).write_to_file(tunings + " until " + str(max_fret) + '.apkg')

make_deck()