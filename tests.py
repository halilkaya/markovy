from unittest import TestCase, main
import random
from markovy import MarkovChain


class MarkovyTest(TestCase):

    def test_word(self):
        random.seed(0)
        mc = MarkovChain('./test_dataset.txt')
        output35 = ['puzzles']
        output27 = ['With']
        output = [output35, output27]
        self.assertIn(mc.make('word'), output)

    def test_multiple_words(self):
        random.seed(0)
        mc = MarkovChain('./test_dataset.txt')
        output35 = ['puzzles', 'know', 'and',
                    'man\'s', 'action.-', 'moment']
        output27 = ['With', 'of', 'scorns',
                    'To', 'patient', 'would']
        output = [output35, output27]
        self.assertIn(mc.make('word', count=6), output)

    def test_sentence(self):
        random.seed(1)
        mc = MarkovChain('./test_dataset.txt')
        output35 = ['Devoutly to say we know not of?']
        output27 = ['To grunt and by opposing end The undiscover\'d ' \
                    'country, from whose bourn No more; and sweat under ' \
                    'a weary life, But that we have shuffled off this ' \
                    'mortal coil, Must give us pause.']
        output = [output35, output27]
        self.assertIn(mc.make(), output)

    def test_multiple_sentences(self):
        random.seed(5)
        mc = MarkovChain('./test_dataset.txt')
        output35 = ['The native hue of action.- Soft you now!',
                    'Dream: ay, there\'s the name of office, and the rub!']
        output27 = ['Dread of thought, And enterprises of outrageous ' \
                    'fortune Or to others that sleep to say we end them.',
                    'There\'s the will, And enterprises of something after ' \
                    'death- The heartache, and moment With a weary life, ' \
                    'But that we have Than fly to sleep- No more; and the ' \
                    'spurns That patient merit of thought, And makes ' \
                    'calamity of outrageous fortune Or to dream: ay, ' \
                    'there\'s the spurns That flesh is heir to.']
        output = [output35, output27]
        self.assertIn(mc.make('sentence', count=2), output)

    def test_one_word_sentence(self):
        random.seed(15)
        mc = MarkovChain('./test_dataset.txt')
        output35 = ['Pause.']
        output27 = ['Word.']
        output = [output35, output27]
        self.assertIn(mc.make(), output)

    def test_paragraph(self):
        random.seed(5)
        mc = MarkovChain('./test_dataset.txt')
        output35 = ['Dread of action.- Soft you now! Dream: ay, ' \
                    'there\'s the name of office, and the rub!']
        output27 = ['Thus conscience does make cowards of office, ' \
                    'and the pale cast of so long life. Not to take ' \
                    'arms against a bare bodkin?']
        output = [output35, output27]
        self.assertIn(mc.make('paragraph', min=1, max=2), output)

    def test_text(self):
        random.seed(0)
        mc = MarkovChain('./test_dataset.txt')
        output35 = ['And the spurns That makes us rather bear the spurns ' \
                    'That makes calamity of us rather bear those ills we ' \
                    'have Than fly to sleep. Quietus make cowards of ' \
                    'action.- Soft you now!\n\n' \
                    'Bear the dread of action.- Soft you now!']
        output27 = ['Scorns of th\' unworthy takes, When we have Than fly ' \
                    'to sleep. The rub!\n\nAnd. Cast of time, Th\' ' \
                    'oppressor\'s wrong, the mind to be wish\'d.']
        output = [output35, output27]
        self.assertIn(mc.make('text', min=1, max=2), output)

    def test_manual_dataset(self):
        random.seed(0)
        mc = MarkovChain(['For', 'in', 'that', 'sleep', 'of',
                          'death', 'what', 'dreams', 'may', 'come'])
        output35 = ['what']
        output27 = ['may']
        output = [output35, output27]
        self.assertIn(mc.make('word'), output)

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
