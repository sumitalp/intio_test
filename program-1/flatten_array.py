class FlattenArray(object):
	result_arr = []

	def __init__(self, *args, **kwargs):
		self.result_arr = []

	@classmethod
	def set_result_arr(cls, res_arr=[]):
		cls.result_arr = res_arr

	def make_flat(self,array):
		if array is not None:
			for arr in array:
				if isinstance(arr, (list,)):
					ret = self.make_flat(arr)
				else:
					self.result_arr.append(arr)

		return self.result_arr

		
if __name__=='__main__':
	"""
	To test, run: python3 flatten_array.py 
	"""

	array1 = [[1,2,[3]],4]
	array2 = [1,[2,3,[4,5],[6]],7,8,9,10]

	# Testcase 1
	flt_arr = FlattenArray()
	print(flt_arr.make_flat(array1))

	# Testcase 2
	flt_arr.set_result_arr() # Make result_arr empty
	print(flt_arr.make_flat(array2))


