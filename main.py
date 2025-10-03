from functions import *
from docxtpl import DocxTemplate

if __name__ == "__main__":
    os.makedirs("output", exist_ok=True)
    while True:
        modef = choose_mode()
        if modef != 0:
            result = get_info(modef)
            docname = f"./output/ЭКГ {result["name"]}.docx"
            doc = DocxTemplate(resource_path("template.docx"))
            doc.render(result)
            doc.save(docname)
            print(f"\n{"-" * 30}\nУспешно сохранено в {docname}\n{"-" * 30}\n")
        else:
            break