import unittest


def test_choosetracks(self):
    self.assertEqual(Music.choosetracks(20), 'error')
    self.assertEqual(Music.choosetracks(10), 'error')
    self.assertEqual(Music.choosetracks(0), 'error')
    self.assertEqual(Music.choosetracks(1), 'error')

def test_bassboost(self):
    self.assertEqual(Music.bassboost(20), 'error')
    self.assertEqual(Music.bassboost(10), 'error')
    self.assertEqual(Music.bassboost(0), 'error')
    self.assertEqual(Music.bassboost(1), 'error')

def test_speedup(self):
    self.assertEqual(Music.speedup(20), 'error')
    self.assertEqual(Music.speedup(10), 'error')
    self.assertEqual(Music.speedup(0), 'error')
    self.assertEqual(Music.speedup(1), 'error')

def test_mergetracks(self):
    self.assertEqual(Music.mergetracks(20), 'error')
    self.assertEqual(Music.mergetracks(10), 'error')
    self.assertEqual(Music.mergetracks(0), 'error')
    self.assertEqual(Music.mergetracks(1), 'error')

def test_outputname(self):
    self.assertEqual(Music.speedup(20), 'error')
    self.assertEqual(Music.speedup(10), 'error')
    self.assertEqual(Music.speedup(0), 'error')
    self.assertEqual(Music.speedup(1), 'error')

def test_exporttrack(self):
    self.assertEqual(Music.exporttrack(20), 'error')
    self.assertEqual(Music.exporttrack(10), 'error')
    self.assertEqual(Music.exporttrack(0), 'error')
    self.assertEqual(Music.exporttrack(1), 'error')

def test_choosingoption(self):
    self.assertEqual(Music.choosingoption(20), 'error')
    self.assertEqual(Music.choosingoption(10), 'error')
    self.assertEqual(Music.choosingoption(0), 'error')
    self.assertEqual(Music.choosingoption(1), 'error')

if __name__ == 'main':
    unittest.main()
