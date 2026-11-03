# JSON-конвертер

Небольшое приложение на Flet: принимает обычный текст или JSON и сохраняет
результат в `output.json` в каталоге `complete-program`.

## Запуск из PowerShell

```powershell
python -m venv .venv
.\.venv\bin\python.exe -m pip install -r requirements.txt
.\.venv\bin\python.exe main.py
```

Запускайте команды из каталога `complete-program`. Если используется стандартный
CPython для Windows, замените `.\.venv\bin\python.exe` на
`.\.venv\Scripts\python.exe`.

Корректный JSON во входном поле сохраняется как соответствующее JSON-значение;
другой текст записывается как JSON-строка.
