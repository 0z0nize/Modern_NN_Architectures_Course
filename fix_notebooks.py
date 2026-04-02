import json


def fix_widgets_keep_outputs(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # Проверяем все ячейки
    for cell in notebook['cells']:
        if 'metadata' in cell and 'widgets' in cell['metadata']:
            if 'state' not in cell['metadata']['widgets']:
                cell['metadata']['widgets']['state'] = {}
                print(f"✓ Добавлен state в ячейку {cell.get('execution_count', '?')}")
    
    # Сохраняем с сохранением всех выводов
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=2, ensure_ascii=False)
    
    print(f"Готово! Выводы сохранены: {notebook_path}")

# Запуск
fix_widgets_keep_outputs('Shkarovskiy_1.ipynb')