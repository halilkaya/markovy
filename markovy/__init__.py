from collections import defaultdict
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


    def _make_word(self, count):
        """
        Generates irrelevant word from the dataset.
        """

        return [random.choice(self.words) for _ in range(count)]


    def _is_end_of(self, text):
        """
        Checks if text ends with dot or not.
        """

        return text and len(text) > 0 and text[-1] in self.ENDING_PUNCTUTATIONS


    def _make_sentence(self, count):
        """
        Generates random sentences from the dataset.
        """

        output = []

        for _ in range(count):
            word = self._make_word(1)[0]
            sentence = ''.join([word[0].upper(), word[1:]])

            if self._is_end_of(sentence):
                output.append(sentence)
            else:
                while not self._is_end_of(sentence):
                    word = random.choice(self.chain[word])
                    sentence += ''.join([' ', word])

                output.append(sentence)

        return output


    def _make_paragraph(self, count, minimum, maximum):
        """
        Generates random paragraphs from the dataset.
        """

        output = []

        for _ in range(count):
            paragraph = ''

            for __ in range(random.randint(minimum, maximum)):
                paragraph += ''.join([self._make_sentence(1)[0], ' '])

            output.append(paragraph[0:len(paragraph)-1])

        return output


    def _make_text(self, count, minimum, maximum):
        """
        Generates random texts from the dataset.
        """

        output = []

        for _ in range(count):
            text = ''

            for __ in range(random.randint(minimum, maximum)):
                text += ''.join([self._make_paragraph(1, minimum, maximum)[0], \
                                 '\n\n'])

            output.append(text[0:len(text)-2])

        return output


    def _handle_int_type(self, value, variable):
        """
        Handler for value is integer and greater than zero.
        """

        if not isinstance(value, int):
            raise TypeError('%s must be integer.' % variable)

        if value < 0:
            raise ValueError('%s must be greater than zero.' % variable)


    def make(self, what='sentence', count=COUNT, minimum=MIN, maximum=MAX):
        """
        Generates random outputs based on the parsed data.
        """

        variables = [
            {'count': count},
            {'minimum': minimum},
            {'maximum': maximum}
        ]

        for var in variables:
            key = list(var.keys())[0]
            self._handle_int_type(var[key], key)

        if not isinstance(what, str):
            raise TypeError('what must be string: word, sentence ' +
                            '(default), paragraph or text')

        if what == 'word':
            return self._make_word(count)

        if what == 'sentence':
            return self._make_sentence(count)

        if what == 'paragraph':
            return self._make_paragraph(count, minimum, maximum)

        if what == 'text':
            return self._make_text(count, minimum, maximum)
