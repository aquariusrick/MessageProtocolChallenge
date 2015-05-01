import unittest

from message_protocol import check_message


class TestMessageProtocolChallenge(unittest.TestCase):
    def test_check_message(self):
        self.assertEqual(check_message('Qa'), "INVALID")
        self.assertEqual(check_message('Zj'), "VALID")
        self.assertEqual(check_message('MZca'), "VALID")
        self.assertEqual(check_message('Khfa'), "INVALID")
    
        self.assertEqual(check_message('Maa'), "VALID")
        self.assertEqual(check_message('MaZa'), "VALID")
        self.assertEqual(check_message('MZaZa'), "VALID")
        self.assertEqual(check_message('MZaMaa'), "VALID")
        self.assertEqual(check_message('MMaaMaa'), "VALID")
        self.assertEqual(check_message('MMaMaa'), "INVALID")
        self.assertEqual(check_message('ZMaa'), "VALID")
        self.assertEqual(check_message('Zu'), "INVALID")
        self.assertEqual(check_message('u'), "INVALID")
        self.assertEqual(check_message('ZZa'), "VALID")

        self.assertEqual(check_message('3aaa'), "VALID")
        self.assertEqual(check_message('2aaa'), "INVALID")
        self.assertEqual(check_message('2ZaMbb'), "VALID")
        self.assertEqual(check_message('K2aaa'), "VALID")
