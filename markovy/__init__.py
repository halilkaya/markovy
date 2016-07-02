from collections import defaultdict
from functools import wraps
import random


class MarkovChain(object):
    """
    Parody generation with Markov Chain.
    """

    # Default values:
    COUNT = 1
    MIN = 5
    MAX = 10

    def __init__(self, dataset):
        """
        Defines dataset and calls method to parse it.
        """

        if hasattr(dataset, 'read'):
            f = dataset.read()
            self.words = [w for w in f.replace('\n', ' ').split(' ')]
        elif isinstance(dataset, str):
            self.words = [w for w in dataset.replace('\n', ' ').split(' ')]
        elif isinstance(dataset, list):
            self.words = dataset
        else:
            raise TypeError('Dataset must be string (as filename) or ' +
                            'list (word list)')

        self.ENDING_PUNCTUTATIONS = ['.', '?', '!', '...', '..', '?!']

        self._parse()


    def _parse(self):
        """
        Parses dataset into words.
        """

        self.chain = defaultdict(list)

        for i, word in enumerate(self.words):
            try:
                if word not in self.chain:
                    self.chain[word] = [self.words[i+1]]
                else:
                    self.chain[word].append(self.words[i+1])
            except IndexError:
                continue


    def _is_end_of(self, text):
        """
        Checks if text ends with dot or not.
        """

        return text and len(text) > 0 and text[-1] in self.ENDING_PUNCTUTATIONS


    def HandleIntTypes(func):
        """
        Decorator to handle int types for the parameters.
        """

        @wraps(func)
        def decorated_function(*args, **kwargs):
            for arg in kwargs.keys():
                k = arg
                v = kwargs[k]

                if not isinstance(v, int):
                    raise TypeError('%s must be integer.' % k)

                if v < 0:
                    raise ValueError('%s must be greater than zero.' % k)

            return func(*args, **kwargs)

        return decorated_function


    @HandleIntTypes
    def make_word(self, count=COUNT):
        """
        Generates irrelevant word from the dataset.
        """

        return [random.choice(self.words) for _ in range(count)]


    @HandleIntTypes
    def make_sentence(self, count=COUNT):
        """
        Generates random sentences from the dataset.
        """

        output = []

        for _ in range(count):
            word = self.make_word(1)[0]
            sentence = ''.join([word[0].upper(), word[1:]])

            if self._is_end_of(sentence):
                output.append(sentence)
            else:
                while not self._is_end_of(sentence):
                    word = random.choice(self.chain[word])
                    sentence += ''.join([' ', word])

                output.append(sentence)

        return output


    @HandleIntTypes
    def make_paragraph(self, count=COUNT, minimum=MIN, maximum=MAX):
        """
        Generates random paragraphs from the dataset.
        """

        output = []

        for _ in range(count):
            paragraph = ''

            for __ in range(random.randint(minimum, maximum)):
                paragraph += ''.join([self.make_sentence(1)[0], ' '])

            output.append(paragraph[0:len(paragraph)-1])

        return output


    @HandleIntTypes
    def make_text(self, count=COUNT, minimum=MIN, maximum=MAX):
        """
        Generates random texts from the dataset.
        """

        output = []

        for _ in range(count):
            text = ''

            for __ in range(random.randint(minimum, maximum)):
                text += ''.join([self.make_paragraph(1, minimum, maximum)[0], \
                                 '\n\n'])

            output.append(text[0:len(text)-2])

        return output
