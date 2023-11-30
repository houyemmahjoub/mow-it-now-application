from unittest import TestCase
from entities.lawn_entity import Lawn
from entities.mower_entity import Mower


class TestMower(TestCase):
    def test_move_mower(self):
        lawn = Lawn(5,5)
        mower1 = Mower(1, 2, "N", lawn)
        mower1.move("GAGAGAGAA")
        self.assertEqual(str(mower1), str(Mower(1, 3, "N", lawn)))

        mower2 = Mower(3, 3, "E", lawn)
        mower2.move("AADAADADDA")
        self.assertEqual(str(mower2), str(Mower(5, 1, "E", lawn)))



