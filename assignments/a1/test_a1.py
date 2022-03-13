import nltk
import unittest
import numpy as np

import a1


class TestBasic(unittest.TestCase):
    def test_task1(self):
        self.assertEqual(a1.count_pos('austen-emma.txt', 'NOUN'),
                             32000)
        self.assertEqual(a1.count_pos('austen-sense.txt', 'VERB'),
                             25074)

    # def test_task2(self):
    #     self.assertListEqual(a1.get_top_stem_bigrams('austen-emma.txt', 3),
    #                          [(',', 'and'), ('.', "''"), (';', 'and')])
    #     self.assertListEqual(a1.get_top_stem_bigrams('austen-sense.txt',4),
    #                          [(',', 'and'), ('.', "''"), (';', 'and'), (',', "''")])

    def test_task3(self):
        self.assertListEqual(a1.get_same_stem('austen-emma.txt','respect')[:5],
                             [('Respect', 2), ('respect', 41), ('respectability', 1), ('respectable', 20), ('respectably', 1)])
        self.assertListEqual(a1.get_same_stem('austen-sense.txt','respect')[:5],
                             [('respect', 22), ('respectability', 1), ('respectable', 14), ('respectably', 1), ('respected', 3)])

    def test_task4(self):
        self.assertListEqual(a1.most_frequent_after_pos('austen-emma.txt','VERB'),
                             [('not', 1932)])
        self.assertListEqual(a1.most_frequent_after_pos('austen-sense.txt','NOUN'),
                             [(',', 5310)])

    # def test_task5(self):
    #     self.assertListEqual(a1.get_word_tfidf('Emma is a respectable person'),
    #                          [('emma', 0.8310852062844262), ('person', 0.3245184217533661), ('respectable', 0.4516471784898886)])
    #     self.assertListEqual(a1.get_word_tfidf('Brutus is a honourable person'),
    #                          [('brutus', 0.8405129362379974), ('honourable', 0.4310718596448824), ('person', 0.32819971943754456)])                        

                           

if __name__ == "__main__":
    unittest.main()
