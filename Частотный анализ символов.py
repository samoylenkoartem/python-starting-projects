def char_frequency(text):
    text = text.lower().replace(' ', '')
    dict = {}
    for id in text:
        dict[id] = dict.get(id, 0) + 1
    arr = [(k,v) for k,v in dict.items()]
    arr = sorted(arr,key = lambda x: (-x[1], x[0]))
    return arr
print(char_frequency("Hello world!"))

