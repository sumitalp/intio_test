import unittest
from flatten_array import FlattenArray


class TestFlattenArray(unittest.TestCase):

    def test_method_exists(self):
        all_methods = dir(FlattenArray)
        assert 'set_result_arr' in all_methods
        assert 'make_flat' in all_methods

    def test_set_result_arr(self):
        flt_arr = FlattenArray()
        arr1 = []
        flt_arr.set_result_arr(res_arr=arr1)
        self.assertEqual(arr1, flt_arr.result_arr)

        arr2=[None]
        flt_arr.set_result_arr(res_arr=arr2)
        self.assertEqual(arr2, FlattenArray.result_arr)

    def test_make_flat(self):
        tcase1 = []
        flt_arr = FlattenArray()
        self.assertEqual([], flt_arr.make_flat(tcase1))

        tcase2 = [1,2,3]
        flt_arr = FlattenArray()
        self.assertEqual([1,2,3], flt_arr.make_flat(tcase2))

        tcase3 = [[1],[2],[3,4]]
        flt_arr = FlattenArray()
        self.assertEqual([1,2,3,4], flt_arr.make_flat(tcase3))

if __name__=='__main__':
    unittest.main()