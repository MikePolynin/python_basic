import re


def registration_marks() -> None:
    marks = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

    civil_pattern = r'\b[А,В,Е,К,М,Н,О,Р,С,Т,У,Х]\d{3}[А,В,Е,К,М,Н,О,Р,С,Т,У,Х]{2}\d{2,3}\b'
    taxi_pattern = r'\b[А,В,Е,К,М,Н,О,Р,С,Т,У,Х]{2}\d{5,6}\b'

    civil_cars = re.findall(civil_pattern, marks)
    taxi_cars = re.findall(taxi_pattern, marks)

    print('Список номеров частных автомобилей: {}'.format(civil_cars))
    print('Список номеров такси: {}'.format(taxi_cars))


registration_marks()
