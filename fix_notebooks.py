import glob
import json


def fix_widgets_in_notebook(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if "metadata" in data and "widgets" in data["metadata"]:
        del data["metadata"]["widgets"]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)

if __name__ == "__main__":
    nb_files = list(glob.glob("*.ipynb"))
    for path in nb_files:
        fix_widgets_in_notebook(path)
    print("All notebooks in this folder fixed.")
