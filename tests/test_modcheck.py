import unittest
from tools.modcheck import validate


class ManifestTests(unittest.TestCase):
    def setUp(self):
        self.base = {'id': 'sample', 'name': 'Sample', 'type': 'resource', 'targets': [{'cusa': 'CUSA08519', 'update': '1.29'}], 'files': []}

    def test_valid(self):
        self.assertTrue(validate(self.base))

    def test_reject_traversal(self):
        self.base['files'] = ['../secret']
        with self.assertRaises(ValueError):
            validate(self.base)

    def test_reject_wrong_version(self):
        self.base['targets'][0]['update'] = '1.32'
        with self.assertRaises(ValueError):
            validate(self.base)


if __name__ == '__main__':
    unittest.main()
