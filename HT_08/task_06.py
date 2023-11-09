'''6. Напишіть функцію,яка прймає рядок з декількох слів і повертає
довжину найкоротшого слова. Реалізуйте обчислення за допомогою генератора.
'''


def shortest_word_length(sentence):
    word_lengths = (len(word) for word in sentence.split())
    return min(word_lengths, default=0)


text = ('She is kind-hearted and always willing to help those in need , ')
print(shortest_word_length(text))