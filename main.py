import sqlite3
import flask
import json

app = flask.Flask(__name__)

def get_by_index(index):
    with sqlite3.connect("animal.db") as connection:
        connection.row_factory = sqlite3.Row
        result = connection.execute(f"""SELECT 
                                        new_animals.id, 
                                        age_upon_outcome,
                                        new_animals.name,
                                        date_of_birth,
                                        animal_type.name as 'type',
                                        animal_breed.name as 'breed',
                                        animal_color1.name as 'color1',
                                        animal_color2.name as 'color2',
                                        outcome_subtype.name as 'outcome_subtype'                                                                                                          
                                        FROM new_animals
                                        LEFT JOIN animal_type
                                            ON animal_type.id = new_animals.type_id
                                        LEFT JOIN animal_breed
                                            ON animal_breed.id = new_animals.breed_id
                                        LEFT JOIN animal_color as animal_color1
                                            ON animal_color1.id = new_animals.color1_id
                                        LEFT JOIN animal_color as animal_color2
                                           ON animal_color2.id = new_animals.color2_id   
                                        LEFT JOIN outcome_subtype
                                            ON outcome_subtype.id = new_animals.outcome_subtype_id
                                        WHERE new_animals.id = {index}""").fetchone()

        return dict(result)

@app.route('/<itemid>')
def response(itemid):
    return app.response_class(response=
                              json.dumps(get_by_index(itemid), ensure_ascii=False),
                                         status=200,
                                         mimetype='application/json'
                              )




if __name__ == '__main__':
    app.run()
