from unittest import TestCase, main
import random
from markovy import MarkovChain


class MarkovyTest(TestCase):

    def test_word(self):
        random.seed(0)
        mc = MarkovChain('./test_dataset.txt')
        output = ['puzzles']
        self.assertEqual(mc.make('word'), output)

    def test_multiple_words(self):
        random.seed(0)
        mc = MarkovChain('./test_dataset.txt')
        output = ['puzzles', 'know', 'and',
                  'man\'s', 'action.-', 'moment']
        self.assertEqual(mc.make('word', count=6), output)

    def test_sentence(self):
        random.seed(1)
        mc = MarkovChain('./test_dataset.txt')
        output = ['Devoutly to say we know not of?']
        self.assertEqual(mc.make(), output)

    def test_multiple_sentences(self):
        random.seed(5)
        mc = MarkovChain('./test_dataset.txt')
        output = ['The native hue of action.- Soft you now!',
                  'Dream: ay, there\'s the name of office, and the rub!']
        self.assertEqual(mc.make('sentence', count=2), output)

    def test_one_word_sentence(self):
        random.seed(8)
        mc = MarkovChain('./test_dataset.txt')
        output = ['Life.']
        self.assertEqual(mc.make(), output)

    def test_paragraph(self):
        random.seed(5)
        mc = MarkovChain('./test_dataset.txt')
        output = ['Dread of action.- Soft you now! Dream: ay, ' \
                  'there\'s the name of office, and the rub!']
        self.assertEqual(mc.make('paragraph', min=1, max=2), output)

    def test_text(self):
        random.seed(0)
        mc = MarkovChain('./test_dataset.txt')
        output = ['And the spurns That makes us rather bear the spurns ' \
                  'That makes calamity of us rather bear those ills we ' \
                  'have Than fly to sleep. Quietus make cowards of ' \
                  'action.- Soft you now!\n\n' \
                  'Bear the dread of action.- Soft you now!']
        self.assertEqual(mc.make('text', min=1, max=2), output)

    def test_manual_dataset(self):
        random.seed(0)
        mc = MarkovChain(['For', 'in', 'that', 'sleep', 'of',
                          'death', 'what', 'dreams', 'may', 'come'])
        output = ['what']
        self.assertEqual(mc.make('word'), output)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            mc = MarkovChain(True)

    def test_handling_int_type(self):
        mc = MarkovChain('./test_dataset.txt')
        with self.assertRaises(TypeError):
            print(mc.make('sentence', count='1', min='2', max='3'))

    def test_handling_int_value(self):
        mc = MarkovChain('./test_dataset.txt')
        with self.assertRaises(ValueError):
            print(mc.make('sentence', count=-1, min=-2, max=-3))

    def test_handling_make_type(self):
        mc = MarkovChain('./test_dataset.txt')
        with self.assertRaises(TypeError):
            print(mc.make(5))


if __name__ == '__main__':
    main()
