from functions import *

if __name__ == "__main__":
    os.makedirs("output", exist_ok=True)
    while True:
        modef = choose_mode()
        result = get_info(modef)
        docname = f"./output/ЭКГ {mode_dict[modef]} {result[0]["name"]}.docx"

        doc = DocxTemplate("template.docx")
        doc.render(result[0])
        doc.save(docname)

        print(f"Успешно сохранено в {docname}\n{"-" * 20}\n")
