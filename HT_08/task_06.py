'''6. Напишіть функцію,яка прймає рядок з декількох слів і повертає
довжину найкоротшого слова. Реалізуйте обчислення за допомогою генератора.
'''
import string

def shortest_word_length(sentence):
    word_lengths = (len(word.strip(string.punctuation)) for word in sentence.split())
    return min(word_lengths, default=0)


text = ('She is kind-hearted and always willing to help those in need , ')
print(shortest_word_length(text))