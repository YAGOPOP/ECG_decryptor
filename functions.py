import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="docxcompose.properties")

import sys
import os
from datetime import date, datetime


mode_dict = {0: "Выйти",
             1: "Домодедово",
             2: "Домодедово (с нагрузкой)",
             3: "Сходненская",
             4: "Третьяковская"
             }

def is_valid_date(date_str: str) -> bool:
    try:
        datetime.strptime(date_str, "%d.%m.%Y")
        return True
    except ValueError:
        return False

def getfloat(response, maxlen=2):
    if response.isdecimal() and len(response) <= maxlen:
        return float(f"0.{response}")
    else:
        return False

def getstr(response:str, awaitedset:set={"+", "-"}):
    if set(response) <= awaitedset:
        print(response)
        return response
    else:
        return False

def getint(response, minval=0, maxval=float("inf")):
    if response.isdecimal() and minval <= int(response) <= maxval:
        return int(response)
    else:
        return False

def is_valid_date(date_str: str) -> bool:
    try:
        datetime.strptime(date_str, "%d.%m.%Y")
        return True
    except ValueError:
        return False

def getdate(response):
    dt = response.replace(",", ".").replace("/", ".")
    if is_valid_date(dt):
        return datetime.strptime(dt, "%d.%m.%Y").date()
    else:
        return False

def safe_input(message, meth, **kwargs):
    while True:
        response = input(message)
        res = meth(response, **kwargs)
        if type(res) != bool:
            return res
        else:
            print("Неверный ввод, попробуйте снова.")

def resource_path(relative_path:str) -> str:
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def choose_mode():
    rl = ""
    for k, v in mode_dict.items():
        rl += f"{k} - {v}\n"
    rl += "Выберите режим: "
    m = safe_input(rl, getint, maxval=4)
    return m

def precise(value:float, rounding:int=2) -> str:
    return f"{value:.{rounding}f}".replace(".", ",")

def get_info(mode):
    name = input("Ф.И.О.: ")
    birthday = safe_input("Дата рождения (ДД.ММ.ГГГГ): ", getdate)
    pulse = safe_input("ЧСС: ", getint)
    alpha = safe_input("α: ", getint)
    P = safe_input("P: 0,", getfloat)
    PQ = safe_input("PQ: 0,", getfloat)
    QRS = safe_input("QRS: 0,", getfloat)
    QT = safe_input("QT: 0,", getfloat)
    P23avf = safe_input("P II,III,avf: ", getstr) or "+"
    T23avf = safe_input("T II,III,avf: ", getstr) or "+"

    todate = date.today()
    age = int((todate - birthday).days / 365.25)

    QTc = QT / (60 / pulse)**0.5

    context = {
        "date": todate.strftime("%d.%m.%Y"),
        "name": name,
        "age": age,
        "birthday": birthday.strftime("%d.%m.%Y"),
        "pulse": pulse,
        "alpha": alpha,
        "P": precise(P),
        "PQ": precise(PQ),
        "QRS": precise(QRS),
        "QT": precise(QT),
        "QTc": precise(QTc),
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

    return context