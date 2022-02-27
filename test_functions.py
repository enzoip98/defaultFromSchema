import unittest
import Local.functions_local as functions_local

class getDefaultColumnsTestCase(unittest.TestCase):
    def test_get_default_columns(self):
        result = functions_local.getDefaultColumns(["gf_local_contract_number_id"],["gf_local_contract_number_id","gf_cutoff_date"])
        self.assertEqual(result, ["gf_cutoff_date"])

    def test_getValuesForColumns(self):
        result = functions_local.getValuesForColumns(["gf_local_contract_number_id","gf_cutoff_date"])
        self.assertEqual(result,{"gf_local_contract_number_id":["PE001"],"gf_cutoff_date":["2022/02/26"]})

if __name__ == '_main_':
    unittest.main()
