#!/usr/bin/env python3
class MyString:
    def __init__(self, value=""):
        self._value = ""
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
            raise TypeError("The value must be a string.")
        self._value = new_value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        punctuation = ['.', '!', '?']
        sentence_count = 0
        for char in self.value:
            if char in punctuation:
                sentence_count += 1
        return sentence_count

# Example usage:
my_string = MyString(123)  # Providing an integer to demonstrate the error message
