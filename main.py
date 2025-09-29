from fileinput import filename

from docx import Document
from my_functions import *

os.makedirs("output", exist_ok=True)

while True:
    mode = get_mode()
    doc = Document(resource_path(os.path.join("templates", f"{mode}.docx")))

    repl = collect_data()
    for p in doc.paragraphs:
        for key, val in repl.items():
            if key in p.text:
                inline = p.runs
                for r in inline:
                    if r.text == key:
                        r.text = r.text.replace(r.text, val)

    fnm = f"./output/ЭКГ {mode_dict[mode]} {repl["n"]}.docx"
    doc.save(fnm)

    print(f"Успешно сохранено в {fnm}\n{"-"*20}\n")
