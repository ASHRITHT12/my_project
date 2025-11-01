import unittest
from main import to_upper
class TestMain(unittest.TestCase):
	def test_upper(self):
		self.assertEqual(to_upper("devops"),"DEVOPS")
if __name__=="__main__":
	unittest.main()