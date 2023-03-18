import unittest
from unittest.mock import patch
from io import StringIO

from model import MenuFunctions


class TestFunction(unittest.TestCase):  # Eric Salkovic
    # unit test class
    def testFileNotFound(self):
        with self.assertRaises(FileNotFoundError):
            with open("testfile.txt"):
                pass
            # test case to check if file 'testfile.txt' does not exist

    # def testFileNotFound2(self):
    #     with self.assertRaises(FileNotFoundError):
    #         with open("32100358.csv"):
    #             pass
    # test case to check if file '32100358.csv' does not exist

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['ref_date_test', 'dguid_test', 'geo_test', 'area_test', 'uom_test', 'uom_id_'
                                          'test', 'scalar_factor_test', 'scalar_id_test', 'vector_test', 'coord_test',
                                          'value_test', 'status_test', 'symbol_test', 'term_test', 'decimals_test'])
    def testAddRecord(self, test_input, expected_output):
        test_input = {'REF_DATE: ref_date_test, DGUID: dguid_test, GEO: geo_test,' 
                      ' Area_production_and_farm_value_of_potatoes: area_test, UOM: uom_test, UOM_ID: uom_id_test,' 
                      ' SCALAR_FACTOR: scalar_factor_test, SCALAR_ID: scalar_id_test, VECTOR: vector_test,' 
                      ' COORDINATE: coord_test, VALUE: value_test, STATUS: status_test, SYMBOL: symbol_test,' 
                      ' TERMINATED: term_test, DECIMALS: decimals_test'}

        expected_output = {'REF_DATE: ref_date_test, DGUID: dguid_test, GEO: geo_test,' 
                           ' Area_production_and_farm_value_of_potatoes: area_test, UOM: uom_test, UOM_ID: uom_id_test,' 
                           ' SCALAR_FACTOR: scalar_factor_test, SCALAR_ID: scalar_id_test, VECTOR: vector_test,' 
                           ' COORDINATE: coord_test, VALUE: value_test, STATUS: status_test, SYMBOL: symbol_test,' 
                           ' TERMINATED: term_test, DECIMALS: decimals_test'}
        test = MenuFunctions()
        test.new_dict_record()
        self.assertEqual(test_input, expected_output)
        pass
