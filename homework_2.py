import runner_and_tournament
import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}


    def setUp(self):
        self.runner1 = runner_and_tournament.Runner('Усэйн', 4)
        self.runner2 = runner_and_tournament.Runner('Андрей', 5)
        self.runner3 = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for value in cls.all_results.values():
            print(value)

    def test_tour1(self):
        tour = runner_and_tournament.Tournament(9, self.runner1, self.runner3)
        self.all_results['test1'] = tour.start()
        temp = list(self.all_results.values())
        self.assertTrue(temp[-1],'Ник')

    def test_tour2(self):
        tour = runner_and_tournament.Tournament(9, self.runner2, self.runner3)
        self.all_results['test2'] = tour.start()
        temp = list(self.all_results.values())
        self.assertTrue(temp[-1],'Ник')

    def test_tour3(self):
        tour = runner_and_tournament.Tournament(9, self.runner1, self.runner2, self.runner3)
        self.all_results['test3'] = tour.start()
        temp = list(self.all_results.values())
        self.assertTrue(temp[-1],'Ник')

    def test_tour4(self):
        tour = runner_and_tournament.Tournament(9, self.runner1, self.runner2, self.runner3)
        self.all_results['test4'] = tour.start()
        temp = list(self.all_results.values())
        self.assertTrue(temp[0],'Андрей')

if __name__ == '__main__':
    unittest.main()