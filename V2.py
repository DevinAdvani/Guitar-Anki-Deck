import genanki

keyboard_notes = []
octave_notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
start_note = ["A", 0]
end_note = ["C#", 8]

def next_note(current_note):
    if current_note[0] == "B":
        return ["C", current_note[1]+1]
    else:
        return [octave_notes[(octave_notes.index(current_note[0])+1)%12], current_note[1]]
    
while start_note != end_note:
    keyboard_notes.append(start_note)
    start_note = next_note(start_note)
    
guitar_notes = [["E",2],["A",2],["D",3],["G",3],["B",3],["E",4]]

guitar_strings = []

for i in range(0,6):
    note = guitar_notes[i]
    string = [note]
    for j in range(0,20):
        note = next_note(note)
        string.append(note)
    guitar_strings.append(string)

# notes - Assumption that there are no breaks in notes (i.e. there isn't a string that is 20 semitones higher) and that the last string is the highest string and the first is the lowest

guitar_range = [guitar_notes[0]]

while True:
    guitar_range.append(next_note(guitar_range[-1]))
    if guitar_range[-1] == guitar_strings[5][-1]:
        break

note_flashcards = []

for x in guitar_range:
    tab = []
    for i in range(0,6):
        try:
            tab.append(guitar_strings[i].index(x))
        except:
            tab.append("X")
    note_flashcards.append([x,tab])

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
  'EADGBE')

for x in note_flashcards:
    my_note = genanki.Note(
    model=my_model,
    fields=[str(x[0]), str(x[1])])

    my_deck.add_note(my_note)

genanki.Package(my_deck).write_to_file('EADGBE.apkg')

# chords - smart reverse note method 

chord_names = ["Major"]
chord_tabs = [[0,4,7]]

chord_notes = []
for x in octave_notes:
    notes = []
    for y in chord_tabs:
        for z in y:
            notes.append(octave_notes[z])
    chord_notes.append(notes)
#print(chord_notes)

# scales