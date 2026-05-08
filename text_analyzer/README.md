# Анализатор текста

Функция `analyze_text(text)` возвращает подробную статистику по переданному тексту.

## 📦 Возможности

- ✅ Количество слов
- ✅ Количество уникальных слов
- ✅ Самое длинное слово
- ✅ Количество символов (без учёта пробелов)
- ✅ Слова в обратном порядке

##  Как запустить

```python
from text_analyzer import analyze_text
result = analyze_text("hello world hello python")
print(result)
```
### Пример ввода 
```
{
  "word_count": 4,
  "unique_words": 3,
  "longest_word": "python",
  "char_count": 17,
  "reversed_text": "python hello world hello"
}
``` 
