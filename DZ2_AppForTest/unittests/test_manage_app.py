import unittest
import os

from sample_data.test_2_testdata import requirements_data, test_cases_data, test_run_data, test_result_data
from manage.manage_app import ManageApp

DEBUG = False


class TestCreateUser(unittest.TestCase):
    def setUp(self):
        self.id1 = 'user1'
        self.admin = 'admin'
        self.manager = ManageApp()

    def tearDown(self):
        self.manager.manage_users('logout', debug=DEBUG)

    def test_01_wipe_db(self):
        # wip db before
        output = self.manager.manage_users('login', self.admin, self.admin, debug=DEBUG)
        self.assertEqual(output.get('response'), 200, 'Administrator login failed')
        output = self.manager.manage_db('droptable', debug=DEBUG)
        self.assertEqual(output.get('response'), 200, 'Can not wipe db')

    def test_02_add_user(self):
        # add new user
        output = self.manager.manage_users('login', self.admin, self.admin, debug=DEBUG)
        self.assertEqual(output.get('response'), 200, 'Administrator login failed')
        output = self.manager.manage_users('useradd', self.id1, self.id1, debug=DEBUG)
        self.assertEqual(output.get('response'), 201, 'Adding user failed')
        self.manager.manage_users('logout', debug=DEBUG)
        output = self.manager.manage_users('login', self.id1, self.id1, debug=DEBUG)
        self.assertEqual(output.get('response'), 200, 'Login user {} failed'.format(self.id1))


class TestTeamReport(unittest.TestCase):
    def setUp(self):
        self.id2 = 'user2'
        self.admin = 'admin'
        self.test_id = 1

        self.manager = ManageApp()
        self.root_folder = self.manager.auxiliary.get_self_location()
        self.pdfconverter = self.manager.auxiliary.pdftotext
        self.md5sum = self.manager.auxiliary.get_md5_sum

        path_to_sample_pdf = os.path.join(self.root_folder, 'sample_data', 'test_2_sample.pdf')
        path_to_sample_txt = os.path.join(self.root_folder, 'sample_data', 'test_2_sample.txt')

        self.pdfconverter(path_to_sample_pdf, path_to_sample_txt)

        self.md5_sample = self.md5sum(path_to_sample_txt)

    def tearDown(self):
        self.manager.manage_users('logout', debug=DEBUG)

    def test_01_wipe_db(self):
        # wip db before
        output = self.manager.manage_users('login', self.admin, self.admin, debug=DEBUG)
        self.assertEqual(output.get('response'), 200, 'Administrator login failed')
        output = self.manager.manage_db('droptable', debug=DEBUG)
        self.assertEqual(output.get('response'), 200, 'Can not wipe db')

    def test_02_add_user(self):
        output = self.manager.manage_users('login', self.admin, self.admin, debug=DEBUG)
        self.assertEqual(output.get('response'), 200, 'Administrator login is failed')
        output = self.manager.manage_users('useradd', self.id2, self.id2, debug=DEBUG)
        self.assertEqual(output.get('response'), 201, 'Adding user \'{}\' is failed'.format(self.id2))

    def test_03_get_pdf_report(self):
        output = self.manager.manage_users('login', self.id2, self.id2, debug=DEBUG)
        self.assertEqual(output.get('response'), 200, 'Login of user \'{}\' is failed'.format(self.id2))
        # add test data
        output = self.manager.manage_test_artifacts('addreq', data=requirements_data, debug=DEBUG)
        for i, v in enumerate(output):
            self.assertEqual(v.get('response'), 201, 'Failed to add {} requirement to db'.format(i))

        output = self.manager.manage_test_artifacts('addts', data=test_cases_data, debug=DEBUG)
        for i, v in enumerate(output):
            self.assertEqual(v.get('response'), 201, 'Failed to add {} test case to db'.format(i))

        output = self.manager.manage_test_artifacts('addtr', data=test_run_data, debug=DEBUG)
        self.assertEqual(output.get('response'), 201, 'Failed to add test run to db')

        output = self.manager.manage_results('addresult', self.test_id, data=test_result_data, debug=DEBUG)
        for i, v in enumerate(output):
            self.assertEqual(v.get('response'), 201, 'Failed to add {} test result to db'.format(i))

        path_to_result_pdf = os.path.join(self.root_folder, 'sample_data', 'test_result.pdf')

        output = self.manager.manage_results('pdf', self.test_id, pdf_drop_path=path_to_result_pdf, debug=DEBUG)
        self.assertEqual(output.get('response'), 200, 'PDF download failed')

        path_to_result_txt = os.path.join(self.root_folder, 'sample_data', 'test_result.txt')
        self.pdfconverter(path_to_result_pdf, path_to_result_txt)

        md5sum = self.md5sum(path_to_result_txt)
        self.assertEqual(md5sum, self.md5_sample, 'Wrong file is created')


if __name__ == '__main__':
    unittest.main()
