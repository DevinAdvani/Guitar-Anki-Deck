import genanki

tunings = "EADGBE"#"DADGAD"
notes = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
start = -1
max_fret = 2#12
chord_shapes = [[0,4,7]]#,[0,4,7,11],[0,4,7,9]]
chord_names = ["Major", "Major 7", "6", "6/9", "Major 9", "Major 11", "Minor", "Minor 7", "Minor 6", "Minor 6/9", "Minor 9", "Minor 11", "Minor Major 7", "Minor Major 9", "7", "9", "11", "Diminished", "Diminished 7", "Half-Diminished", "Augmented", "Augmented 7", "7-5", "7+5", "7-9", "7+9", "7#11", "5", "Add 9", "Add 2", "Add 11", "Add 4", "Suspended 4", "Suspended 2"]

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

def reduce_tabs(input_tab):
    minimum = min(input_tab)
    for i in range(0,6):
        input_tab[i] -= minimum 
    return input_tab

the_list = produce_all_chord_tabs(chord_shapes, chord_names)

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

for i in range(0,len(the_list[0])):
    my_deck = genanki.Deck(
    2059400110,
    'Guitar Chords::' + tunings + '::' + the_list[0][i])
    for j in range(0,len(the_list[1][i])):
        my_note = genanki.Note(
        model=my_model,
        fields=[str(the_list[0][i] + " " + str(reduce_tabs(the_list[1][i][j]))), str(the_list[1][i][j])])
        my_deck.add_note(my_note)
    genanki.Package(my_deck).write_to_file(tunings + " " + the_list[0][i] + '.apkg')
