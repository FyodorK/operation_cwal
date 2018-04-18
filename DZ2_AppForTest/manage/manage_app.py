import requests
from urllib3 import disable_warnings
from manage.auxiliary import Auxiliary


class ManageApp:
    """
    Class for managing test web application.
    If url of web application didn't provided, it uses 'https://localhost:5000' url as default
    """
    def __init__(self, target=None):

        self.session = requests.Session()
        self.session.verify = False
        disable_warnings()

        self.auxiliary = Auxiliary()

        self.tails = {'login': '/login',
                      'logout': '/logout',
                      'useradd': '/admin/user',
                      'who':  '/admin/users',
                      'droptable': '/admin/recreatedb',
                      'addreq': '/req',
                      'showreqs': '/reqs',
                      'addts': '/testcase',
                      'showts': '/testcases',
                      'addtr': '/testrun',
                      'showtr': '/testruns',
                      'addresult': '/testrun/{id}/result',
                      'showresult': '/testrun/{id}/results',
                      'pdf': '/testrun/{id}/pdf'}

        if target:
            self._url = target
            print('Using url: {}\n'.format(self._url))
        else:
            self._url = "https://localhost:5000"
            print('Using default: url {}\n'.format(self._url))

        if not self.web_server_is_started():
            raise Exception('No server binds to target url {}'.format(self._url))

    def __del__(self):
        self.session.close()

    def web_server_is_started(self):
        s = None
        try:
            s = self.session.get(self._url).status_code
        except requests.RequestException:
            pass
        return True if s else False

    def manage_db(self, ops, debug=False):
        """
        Manage db:
        droptable - wipe db

        :param ops: operation as string
        :param debug: printout debug messages
        :return: dict of {'response': int, 'output': str}
        """
        target_url = self._url + self.tails.get(ops)
        if debug:
            print("Operation: {}  Target url: {}".format(ops, target_url))

        result = {'response': None, 'output': None}

        if 'droptable' in ops:
            if debug:
                print ("\n\t DB is wiped out\n")
            res_ = self.session.post(target_url)
        else:
            raise NotImplemented

        result['response'] = res_.status_code
        result['output'] = res_.content.decode()

        return result

    def manage_users(self, ops, id_=None, pswd_=None, debug=False):
        """
        Perform authentication and manage users:
        login - log in to db
        logout - log out of db
        useradd - add new user no db
        who - show available users

        :param ops: operation as string
        :param id_: user id as string
        :param pswd_: user password as string
        :param debug: print debug messages
        :return: dict of {'response': int, 'output': str}
        """
        json_template = {'login': ('login', 'password'),
                         'useradd': ('new_login', 'new_password')}

        target_url = self._url + self.tails.get(ops)
        if debug:
            print("Operation: {}  Target url: {}".format(ops, target_url))
        auth_pair = (id_, pswd_)
        result = {'response': None, 'output': None}

        if 'who' is not ops and 'logout' is not ops:
            json = dict(zip(json_template.get(ops), auth_pair))
            res_ = self.session.post(target_url, json=json)
        else:
            if 'who' is ops:
                res_ = self.session.get(target_url)
            else:
                res_ = self.session.post(target_url)

        result['response'] = res_.status_code
        result['output'] = res_.content.decode()
        return result

    def manage_test_artifacts(self, operation, data, debug=False):
        """
        Manage test artifacts:

        'addreq' - adding requirements
        'showreqs' - show all requirements in db
        'addts' - add a testcase
        'showts' - show all test cases in db
        'addtr' - add a testrun
        'showtr' - show all testruns in db

        :param operation: operation as string
        :param data: data as list of jsons or single json
        :param debug: print debug messages
        :return: dict of {'response': int, 'output': str} or list of dicts
        """
        target_url = self._url + self.tails.get(operation)
        if debug:
            print("Operation: {}  Target url: {}".format(operation, target_url))

        results = []
        result = {'response': None, 'output': None}

        if operation.startswith('show'):
            res_ = self.session.get(target_url)
            result['response'] = res_.status_code
            result['output'] = res_.content.decode()

        elif operation.startswith('add'):
            if self.auxiliary.is_list(data):
                """ Data is passed as list of dicts"""
                for chunk in data:
                    res_ = self.session.post(target_url, json=chunk)
                    result['response'] = res_.status_code
                    result['output'] = res_.content.decode()
                    results.append(result)
                return results
            elif self.auxiliary.is_dict(data):
                """ Data is passed as single dict"""
                res_ = self.session.post(target_url, json=data)
                result['response'] = res_.status_code
                result['output'] = res_.content.decode()

            else:
                raise NotImplemented
        else:
            raise NotImplemented
        return result

    def manage_results(self, ops, test_run_id, data=None, pdf_drop_path=None, debug=False):
        """
        Manage test results:
        'addresult' - add test run result to db by test run id
        'showresult' - show available results for test run id
        'pdf' - forge test run results as pdf doc and put it to
        :param ops: operation as string
        :param test_run_id: id of testrun as int
        :param data: data container json or list of jsons
        :param pdf_drop_path:  path to pdf as string
        :param debug: print debug messages
        :return: dict of {'response': int, 'output': str} or list of dicts or binary file
        """

        target_url = self._url + self.tails.get(ops).format(id=test_run_id)
        if debug:
            print("Operation: {}  Target url: {}".format(ops, target_url))

        results = []
        result = {'response': None, 'output': None}

        if 'show' in ops:
            res_ = self.session.get(target_url)
            result['response'] = res_.status_code
            result['output'] = res_.content.decode()

        elif 'pdf' in ops:
            res_ = self.session.get(target_url)

            with open(pdf_drop_path, 'wb') as fo:
                fo.write(res_.content)

            result['response'] = res_.status_code
            result['output'] = res_.content

        elif 'add' in ops:
            if self.auxiliary.is_list(data):
                """ Data is passed as list of dicts"""
                for chunk in data:
                    res_ = self.session.post(target_url, json=chunk)
                    result['response'] = res_.status_code
                    result['output'] = res_.content.decode()
                    results.append(result)
                return results
            elif self.auxiliary.is_dict(data):
                """ Data is passed as single dict"""
                res_ = self.session.post(target_url, json=data)
                result['response'] = res_.status_code
                result['output'] = res_.content.decode()

            else:
                raise NotImplemented

        else:
            raise NotImplemented
        return result
