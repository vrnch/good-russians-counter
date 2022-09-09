def message_number_of_dead_orcs(casualties_data):
    return (f'На сьогодні ({casualties_data.last_date})' if casualties_data.today_date == casualties_data.last_date else f'На {casualties_data.last_date}') + \
        f' вбито +{casualties_data.number_of_dead_orcs[1]} русні.\nВсього за весь час винищено близько {casualties_data.number_of_dead_orcs[0]} орків.'


def message_rest_of_the_casualties(casualties_data):
    casualties = [casualty.get_text() for casualty in casualties_data.info]
    casualties.pop()
    return "Решта винищенних боєприпасів складає:\n" + "\n".join(casualties)
