import unittest
from audio_brainstorm.modules.music_theory import (
    get_bpm_from_genre
)


class TestMusicTheory(unittest.TestCase):

    def test_get_bpm_from_genre_valid_genre(self):
        bpm = get_bpm_from_genre("Electronic", "House")
        self.assertTrue(110 <= bpm <= 140,
                        "BPM not within expected range for House music")

    def test_get_bpm_from_genre_invalid_genre(self):
        bpm = get_bpm_from_genre("Electronic", "InvalidGenre")
        self.assertIsNone(bpm, "Should return None for an invalid genre")
