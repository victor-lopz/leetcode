from collections import defaultdict

def groupBy(array: list, func = lambda x:x):
    groupped = defaultdict(list)
    for element in array:
        output = func(element)
        groupped[output].append(element)
    return groupped

def groupCount(array: list, func = lambda x:x):
    groupped = defaultdict(int)
    for element in array:
        output = func(element)
        groupped[output] += 1
    return groupped

def groupByTestCase():
    array = ["a", "a", "b", "A", "A", "B"]
    
    def grouppingFunc(s: str) -> bool:
        return s.islower()
    
    groups = groupBy(array, grouppingFunc)
    print(f"{groups = }")

def groupCountTestCase():
    array = [1, 7, 1, 5, 7, 7, 3, -665465]
    
    def grouppingFunc(number: int) -> int:
        return number
    
    counts = groupCount(array, grouppingFunc)
    print(f"{counts = }")

if __name__ == "__main__":
    groupByTestCase()
    groupCountTestCase()