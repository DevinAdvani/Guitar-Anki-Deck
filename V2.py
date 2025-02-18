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

# chords - smart reverse note method 

# scales