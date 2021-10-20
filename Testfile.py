import unittest

import Music


def test_choosetracks(self):
    self.assertEqual(Music.choosetracks(20, 2), 'error')
    self.assertEqual(Music.choosetracks(10, 22), 'error')
    self.assertEqual(Music.choosetracks(2, 12), 'error')
    self.assertEqual(Music.choosetracks(1, 2), [])

def test_bassboost(self):
    self.assertEqual(Music.bassboost(20), 'error')
    self.assertEqual(Music.bassboost(10), 'error')
    self.assertEqual(Music.bassboost(0), 'error')
    self.assertEqual(Music.bassboost('AudioSegment.from_mp3(a + ".mp3")', 'AudioSegment.from_mp3(a + ".mp3")'), [])

def test_speedup(self):
    self.assertEqual(Music.speedup(20), 'error')
    self.assertEqual(Music.speedup(10), 'error')
    self.assertEqual(Music.speedup(0), 'error')
    self.assertEqual(Music.speedup('a._spawn(a.raw_data, overrides={"frame_rate": int(a.frame_rate * 1.2)})', 'b._spawn(b.raw_data, overrides={"frame_rate": int(b.frame_rate * 1.2)})'), [])

def test_mergetracks(self):
    self.assertEqual(Music.mergetracks(20), 'error')
    self.assertEqual(Music.mergetracks(10), 'error')
    self.assertEqual(Music.mergetracks(0), 'error')
    self.assertEqual(Music.mergetracks('AudioSegment.from_mp3(a + ".mp3")', 'AudioSegment.from_mp3(b + ".mp3")'), [])


def test_exporttrack(self):
    self.assertEqual(Music.exporttrack(20), 'error')
    self.assertEqual(Music.exporttrack(10), 'error')
    self.assertEqual(Music.exporttrack(0), 'error')
    self.assertEqual(Music.exporttrack('a.export(name + ".mp3", format="mp3")'), [])

def test_choosingoption(self):
    self.assertEqual(Music.choosingoption(20), 'error')
    self.assertEqual(Music.choosingoption(1), [])
    self.assertEqual(Music.choosingoption(2), [])
    self.assertEqual(Music.choosingoption(3), [])

if __name__ == 'main':
    unittest.main()
