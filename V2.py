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

limit = guitar_notes

fretted_notes = []

for i in range(0,6):
    base_note = guitar_notes[i]
    for j in range(0,21):
        tab = ["X","X","X","X","X","X"]
        tab[i] = j
        fretted_notes.append([tab, base_note])
        base_note = next_note(base_note)


print(fretted_notes)

# notes

cards = []
starting_note = ["E", 2]
ending_note = ["E", 4]

while start_note != ending_note:
    for x in fretted_notes:
        if fretted_notes[1] == starting_note:
            cards.append(x)
    starting_note = next_note(starting_note)

for x in cards:
    print(x)
    print(" ")



# chords - smart reverse note method 

# scales