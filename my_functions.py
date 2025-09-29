import sys
import os
from datetime import date


mode_dict = {1: "Домодедово",
             2: "Домодедово (с нагрузкой)",
             3: "Сходненская",
             4: "Третьяковская"
             }


def resource_path(relative_path: str) -> str:
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def fufill(value:float):
    v = str(value)
    v1 = v[2:]
    l = len(v1)
    if l < 2:
        v += "0"
    return v.replace(".", ",")

def get_mode():
    print("1 - Домодедово\n2 - Домодедово (с нагрузкой)\n3 - Сходненская\n4 - Третьяковская")
    return int(input("Выберите режим: "))

def collect_data():
    # Collecting data
    name = input("Ф.И.О.: ")
    bdr = input("Дата рождения (ДД.ММ.ГГГГ): ").replace(",", ".")
    pulse = int(input("ЧСС: "))
    alpha = input("α: ")
    P = input("P: 0,")
    PQ = input("PQ: 0,")
    QRS = input("QRS: 0,")
    QT = float("0." + input("QT: 0,"))
    PG = input("P II,III,avf: ")
    TG = input("T II,III,avf: ")


    # Processing data
    todate = date.today()
    bd = list(map(int, bdr.split(".")))
    birthday = date(bd[2], bd[1], bd[0])
    age = int((todate - birthday).days / 365.25)

    QTc = round(QT / (60 / pulse)**0.5, 2)

    if TG == "":
        TG = "+"
    if PG == "":
        PG = "+"

    replacements = {
        "DATE": f"{str(todate.day).zfill(2)}.{str(todate.month).zfill(2)}.{todate.year}",
        "NAME": f"Ф.И.О.: {name}",
        "AGE": f"Возраст: {bdr} / {age} лет",
        "PULSE": f"ЧСС {pulse} уд/мин",
        "ALPHA": f"α= {alpha}°",
        "PP": f"P - 0,{P} с",
        "PQ": f"PQ - 0,{PQ} с",
        "QRS": f"QRS - 0,{QRS} с",
        "QT": f"QT - {fufill(QT)} с",
        "QTs": f"QTc - {fufill(QTc)} с",
        "PG": f"{PG}",
        "TG": f"{TG}",
        "n": name
    }

    return replacements