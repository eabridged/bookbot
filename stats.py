def get_word_count(text: str) -> int:
    """Returns the word count of the given text."""
    words = text.split()
    return len(words)

def count_symbols(text:str) -> dict[str, int]:
    symbolDictionary = dict()
    for symbol in text:
        symbol = symbol.lower()
        entry = symbolDictionary.get(symbol)
        symbolDictionary[symbol] = 1 if entry == None else entry+1
    return symbolDictionary

def sort_dictionary(di:dict[str,int]):
    diList = [dict([(key,value)]) for key,value in di.items()]
    diList.sort(key=lambda entry: [i for i in entry.values()][0], reverse=True)
    return diList
