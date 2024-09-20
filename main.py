tunings = "EADGBE"
notes = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]

def shift(input_note, semi_tones):
    position = notes.index(input_note)
    position += semi_tones
    return notes[position]

def tab_to_note(input_tab):
    for i in range(0,len(input_tab)):
        pass

print(tab_to_note("000001"))