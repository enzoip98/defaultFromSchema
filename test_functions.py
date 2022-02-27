import unittest
import functions

class getDefaultColumnsTestCase(unittest.TestCase):

    def test_get_columns_from_schema(self):
        result = functions.getColumnsFromSchema("C:/Users/Enzo/Desktop/defaultFromSchema/regulatoryinformation.output.schema")
        self.assertEqual(result,['gf_cutoff_date', 'gf_local_contract_number_id', 'g_management_breakdown_type', 'g_contract_id', 'gf_information_origin_id', 'g_lcr_liquidity_category_type', 'g_local_currency_id', 'gf_unencumbered_lc_amount', 'gf_encumbered_lc_amount', 'gf_rk_ead_ptl_lc_amount', 'gf_rwa_crr_ptl_lc_amount', 'gf_rk_crr_ptl_lc_amount', 'gf_rk_crr_12m_lc_amount', 'gf_rk_crr_annl_lc_amount', 'gf_rk_ead_ptl_oc_amount', 'gf_rwa_crr_ptl_oc_amount', 'gf_rk_crr_ptl_oc_amount', 'g_sppi_type', 'g_business_model_type', 'g_poci_type', 'gf_source_encumbrance_type', 'g_entific_id', 'gf_audit_date'])

    def test_get_default_columns(self):
        result = functions.getDefaultColumns(["gf_local_contract_number_id"],["gf_local_contract_number_id","gf_cutoff_date"])
        self.assertEqual(result, ["gf_cutoff_date"])

    def test_get_values_for_null_columns(self):
        result = functions.getValuesForNullColumns(["gf_local_contract_number_id"],1)
        self.assertEqual(result,{"gf_local_contract_number_id":[""]})

    def test_merge_columns(self):
        result = functions.mergeColumns({"gf_local_contract_number_id":""},{"gf_cutoff_date":""})
        self.assertEqual(result,{"gf_local_contract_number_id":"","gf_cutoff_date":""})

if __name__ == '_main_':
    unittest.main()
