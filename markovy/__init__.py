from collections import defaultdict
import random


class MarkovChain(object):
    """
    Python module for Markov Chain algorithm.
    """

    # Default values:
    COUNT = 1
    MIN = 5
    MAX = 10

    def __init__(self, dataset):
        """
        Defines dataset and calls method to parse it.
        """

        if isinstance(dataset, str):
            f = open(dataset).read()
            self.words = [w for w in f.replace('\n', ' ').split(' ')]
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


    def _make_word(self, count=COUNT):
        """
        Generates irrelevant word from the dataset.
        """

        output = []

        for _ in range(count):
            output.append(random.choice(self.words))

        return output


    def _is_end_of(self, text):
        """
        Checks if text ends with dot or not.
        """

        if text and len(text) > 0 and text[-1] in self.ENDING_PUNCTUTATIONS:
            return True

        return False


    def _make_sentence(self, count=COUNT):
        """
        Generates random sentences from the dataset.
        """

        output = []

        for _ in range(count):
            word = self._make_word()[0]
            sentence = ''.join([word[0].upper(), word[1:]])

            if self._is_end_of(sentence):
                output.append(sentence)
            else:
                while not self._is_end_of(sentence):
                    word = random.choice(self.chain[word])
                    sentence += ''.join([' ', word])

                output.append(sentence)

        return output


    def _make_paragraph(self, count=COUNT, min=MIN, max=MAX):
        """
        Generates random paragraphs from the dataset.
        """

        output = []

        for _ in range(count):
            paragraph = ''

            for __ in range(random.randint(min, max)):
                paragraph += ''.join([self._make_sentence()[0], ' '])

            output.append(paragraph[0:len(paragraph)-1])

        return output


    def _make_text(self, count=COUNT, min=MIN, max=MAX):
        """
        Generates random texts from the dataset.
        """

        output = []

        for _ in range(count):
            text = ''

            for __ in range(random.randint(min, max)):
                text += ''.join([self._make_paragraph(min=min, max=max)[0], \
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


    def make(self, what='sentence', count=COUNT, min=MIN, max=MAX):
        """
        Generates random outputs based on the parsed data.
        """

        for var in [{'count': count}, {'min': min}, {'max': max}]:
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
            return self._make_paragraph(count, min, max)

        if what == 'text':
            return self._make_text(count, min, max)
