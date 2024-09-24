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


"""
chords = []

for a in range(0,2):
    for b in range(0,2):
        for c in range(0,2):
            for d in range(0,2):
                for e in range(0,2):
                    for f in range(0,2):
                        for g in range(0,2):
                            for h in range(0,2):
                                for i in range(0,2):
                                    for j in range(0,2):
                                        for k in range(0,2):
                                            chord = [0]
                                            if (a == 1):
                                                chord.append(1)
                                            if (b == 1):
                                                chord.append(2)
                                            if (c == 1):
                                                chord.append(3)
                                            if (d == 1):
                                                chord.append(4)
                                            if (e == 1):
                                                chord.append(5)
                                            if (f == 1):
                                                chord.append(6)
                                            if (g == 1):
                                                chord.append(7)
                                            if (h == 1):
                                                chord.append(8)
                                            if (i == 1):
                                                chord.append(9)
                                            if (j == 1):
                                                chord.append(10)
                                            if (k == 1):
                                                chord.append(11)
                                            if (len(chord) <= 6):
                                                chords.append(chord)
"""
"""
chord_notes = []
for h in range(0,12):
    for i in chords:
        chord_note = []
        for j in i:
            chord_note.append(notes[(j+h)%12])
        chord_note = set(chord_note)
        chord_notes.append(chord_note)
print(chord_notes)
"""
"""
output = []
for j in chord_spaces[0]:
    output.append(notes[j%12])
#print(set(output))
"""
"""
for i in range(0,12):
    output = []
    for j in major:
        output.append(notes[(i+j)%12])
    print(set(output))
"""
"""
chord = [0,4,7]

for j in range(0,12):
    current_chord = chord
    for i in range(0,len(current_chord)):
        current_chord[i] += 1
        current_chord[i] %= 12
    print(current_chord)
guitar_notes = []
guitar_notes = set(guitar_notes)
print(guitar_notes)
tabs = []

chord = chords_names[i]
base_note = notes[j]


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
                        if tab_to_note(tab) == guitar_notes:
                            tabs.append(tab)

my_deck = genanki.Deck(
2059400110,
'Guitar::' + chord + '::' + base_note)

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

for i in range(0,len(tabs)):
    my_note = genanki.Note(
    model=my_model,
    fields=[base_note + ' ' + chord + ' ' + str(i), str(tabs[i])])

    my_deck.add_note(my_note)

genanki.Package(my_deck).write_to_file(base_note + ' ' + chord + '.apkg')
"""