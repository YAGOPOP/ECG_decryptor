import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="docxcompose.properties")

from docxtpl import DocxTemplate
import sys
import os
from datetime import date, datetime





mode_dict = {1: "Домодедово",
             2: "Домодедово (с нагрузкой)",
             3: "Сходненская",
             4: "Третьяковская"
             }

def fufill(value):
    v = str(value)
    if "." in v:
        v1 = v[2:]
        l = len(v1)
        if l < 2:
            v += "0"
        return v.replace(".", ",")
    else:
        return f"0,{value}"

def resource_path(relative_path: str) -> str:
    if hasattr(sys, '_MEIPASS'):
        # noinspection PyProtectedMember
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def getnum(message, minval=0, maxval=1000):
    while True:
        n = input(message)
        if n.isdecimal():
            n = int(n)
            if minval <= n <= maxval:
                return int(n)
        print("Неверный ввод, попробуйте снова.")

def is_valid_date(date_str: str) -> bool:
    try:
        datetime.strptime(date_str, "%d.%m.%Y")
        return True
    except ValueError:
        return False

def getdate(message) -> date:
    while True:
        dt = input(message).replace(",", ".").replace("/", ".")
        if is_valid_date(dt):
            return datetime.strptime(dt, "%d.%m.%Y").date()
        else:
            print("Неверный ввод, попробуйте снова.")

def choose_mode():
    rl = ""
    for k, v in mode_dict.items():
        rl += f"{k} - {v}\n"
    print(rl[0:-1])
    m = getnum("Выберите режим: ", minval=1, maxval=4)
    return m

def get_info(mode):
    name = input("Ф.И.О.: ")
    birthday = getdate("Дата рождения (ДД.ММ.ГГГГ): ")
    pulse = getnum("ЧСС: ")
    alpha = getnum("α: ")
    P = fufill(getnum("P: 0,", maxval=99))
    PQ = fufill(getnum("PQ: 0,", maxval=99))
    QRS = fufill(getnum("QRS: 0,", maxval=99))
    QT = float(f"0.{getnum("QT: 0,", maxval=99)}")
    P23avf = input("P II,III,avf: ")
    T23avf = input("T II,III,avf: ")



    todate = date.today()
    age = int((todate - birthday).days / 365.25)

    QTc = round(QT / (60 / pulse)**0.5, 2)

    if P23avf == "": P23avf = "+"
    if T23avf == "": T23avf = "+"

    context = {
        "date": todate.strftime("%d.%m.%Y"),
        "name": name,
        "age": age,
        "birthday": birthday.strftime("%d.%m.%Y"),
        "pulse": pulse,
        "alpha": alpha,
        "P": P,
        "PQ": PQ,
        "QRS": QRS,
        "QT": fufill(QT),
        "QTc": fufill(QTc),
        "P23avf": P23avf,
        "T23avf": T23avf,
        "company": "ООО «ГОЛД ТЕСТ»",
        "address": "МО г. Домодедово , ул. Курыжова д 19",
        "license": "Лицензия № : ЛО-50-01-008140 от 18.10.2016г.",
        "tel_num": "+7(929)954-89-43",
        "foreseen_consequences": ""
    }
    if mode == 1:
        pass
    elif mode == 2:
        context["foreseen_consequences"] = "После нагрузки (20 приседаний) – синусовая тахикардия, ЧСС уд/мин, в остальном без существенной динамики (адекватная реакция на нагрузку)."
    elif mode == 3:
        context["company"] = "ООО «ЗДРАВ»"
        context["address"] = "г. Москва, ул. Героев Панфиловцев д.1 кор.1, 1эт.,п.III"
        context["license"] = "Лицензия № : ЛО-50-01-008140 от 18.10.2016г."
        context["tel_num"] = "8(499)762-00-17"
    else:
        context["company"] = "ООО «САН»"
        context["address"] = "г. Москва, ул. Пятницкая д. 28"
        context["license"] = "Лицензия № : ЛО-77-01-015456 от 09.01.2018 г"
        context["tel_num"] = "8(495)953-89-48"

    return context, name