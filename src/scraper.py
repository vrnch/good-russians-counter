import re
from typing import List
import mechanicalsoup
from collections import namedtuple
from dataclasses import dataclass

from datetime import date
from data_sources import MINFIN_URL


browser = mechanicalsoup.Browser()
CasualtiesData = namedtuple(
    'CasualtiesData', ['last_date', 'today_date', 'number_of_dead_orcs', 'info'])


def update():
    page = browser.get(MINFIN_URL)
    html = page.soup

    data = html.find('li', attrs={'class': 'gold'})

    last_date = data.span.get_text()
    info = data.div.div.ul
    casualties = info.find_all('li')

    number_of_dead_orcs: str = [i.get_text()
                                       for i in casualties if "Особовий склад" in i.get_text()].pop()

    number_of_dead_orcs: List[int] = re.findall(
        '[0-9]+', number_of_dead_orcs)

    today_date = date.today().strftime('%d.%m.%Y')

    return CasualtiesData(last_date, today_date, number_of_dead_orcs, info)





