import genanki
import os

song_names = ["Under_The_Bridge", "Come_As_You_Are", "Andy_Warhol", "Telephones", "Blackbird", "Fast_Car"]

for i in range(0,len(song_names)):
    try:
        my_model = genanki.Model(
            1607392319,
            'Indented Flashcard Model',
            fields=[
                {'name': 'Question'},
                {'name': 'Answer'},
            ],
            templates=[
                {
                    'name': 'Card 1',
                    'qfmt': '{{Question}}',
                    'afmt': '{{Question}}<br><div class="indented-answer">{{Answer}}</div>',
                },
            ],
            css="""
            .card {
            font-family: monospace;
            font-size: 20px;
            text-align: left;
            color: black;
            background-color: white;
            }
            .indented-answer {
            text-indent: 20px; /* Indentation of 20px */
            margin-top: 10px;
            }
            """
        )

        my_deck = genanki.Deck(
            2059400110,
            'Guitar::Songs::' + song_names[i]
        )

        output = ""
        f = open("tab_store/" + song_names[i] + ".txt")
        for x in f:
            output += x 
            output += "<br>"

        my_note = genanki.Note(
            model=my_model,
            fields=[song_names[i], output]
        )

        my_deck.add_note(my_note)

        genanki.Package(my_deck).write_to_file('tab_store_anki/' + song_names[i] + '.apkg')

    except:
        with open('tab_store/' + song_names[i] + '.txt', 'w') as fp:
            pass