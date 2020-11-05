import unittest
from unittest.mock import patch 
from components import Cell

class TestComponents(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @patch('builtins.print')
    def test_print(self, mock_print):
        celda = Cell()
        celda.set_state('ON')

        celda.print_state()
        mock_print.assert_called_with('ON')

        celda.set_state('OFF')
        celda.print_state()
        mock_print.assert_called_with('OFF')
    

if __name__ == '__main__':
    unittest.main()

