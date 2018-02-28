import sys
import requests
import subprocess
import json
from bs4 import BeautifulSoup
from os import path
from re import findall
from datetime import datetime


def cosmetic(func_name):
    def wrapper(*arg, **kwarg):
        print('Started {}'.format(func_name.__name__))
        a = func_name(*arg, **kwarg)
        print('Finished {}'.format(func_name.__name__))
        return a
    return wrapper


class Tasks:
    """
    Class for automation python training via auriga colleagues
    """
    @staticmethod
    def execute(cmd):
        """
        Simple wrapper for subpoccess
        :param cmd: command line to execute as string
        :return: ret as dictionary
        """

        ret = {'command': cmd, 'output': [], 'ret_code': None}

        try:
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        except subprocess.SubprocessError as ex:
            return ex

        while process.poll() is None:
            raw_output = process.stdout.readline()
            output = raw_output.decode('utf-8', errors='ignore').replace('\n', '').replace('\r', '')
            if output:
                ret["output"].append(output)

        for line in process.stdout.readlines():
            output = line.decode('utf-8', errors='ignore').replace('\n', '').replace('\r', '')
            if output:
                ret["output"].append(output)

        ret['ret_code'] = process.returncode
        return ret

    @staticmethod
    def get_file_log_content(path_to_log):
        content = None
        if path.isfile(path_to_log):
            with open(path_to_log, 'r') as fd:
                content = fd.readlines()
        return content


    @staticmethod
    @cosmetic
    def task1(url):
        """
        Collect links from a internet page to json format
        :return: None
        """
        r = requests.get(url)
        soup = BeautifulSoup(r.content.decode(), "html.parser")
        d = dict()
        for a in soup.findAll("a", href=True):
            d[a.text.strip().replace('\n', '')] = '{}{}'.format(url, a.get('href')) \
                if 'http' not in a.get('href') else a.get('href')
        ret = [{'text':text, 'link': link} for text, link in d.items()]
        with open('result.json', 'w') as fp:
            json.dump(ret, fp, indent=4)

    @cosmetic
    def task2(self):
        """
        Get formated output of command 'netstat -a -o' in case windows
        or command 'lsof -p <pid>' in case linux
        :return: None
        """
        head = 'PID  {}'
        output_tmplt = '{:5}{:5}'

        if sys.platform.startswith('win'):
            raw = self.execute('netstat -a -o').get('output')[2:]
            uniq_pids = {int(item.split()[-1]) for item in raw}
            connections_per_pid = {pid:0 for pid in uniq_pids}

            for line in raw:
                for pid in uniq_pids:
                    if str(pid) in line:
                        connections_per_pid[pid] = connections_per_pid.get(pid) + 1
            print(head.format('\t Connections'))
            for pid, conns in sorted(connections_per_pid.items(), key=lambda x: x[0]):
                print(output_tmplt.format(pid, conns))
        else:
            cmd_tmplt = 'lsof -p {pid}'
            # get uniq pids from live processes
            raw = self.execute('ps -ef').get('output')[1:]
            uniq_pids = {int(item.split()[1]) for item in raw}

            print(head.format('\tOpened files'))
            for pid in sorted(uniq_pids):
                files_count = len(self.execute(cmd_tmplt.format(pid=pid)).get('output')[1:])
                print(output_tmplt.format(pid, files_count))

    @cosmetic
    def task3(self, path_to_log):
        """
        Parse a log file for requests, them time, and errors
        :return: None
        """

        info = {}
        errors = {}

        format_tmpl = '[%Y-%m-%d %H:%M:%S.%f] INFO {state} processing of >Request {num}<'
        output_tmlt = 'Request {number}: {content}'

        log_content = self.get_file_log_content(path_to_log)

        if not log_content:
            raise FileNotFoundError('Error on loading log file, can\'t proceed further' )

        # get all requests numbers from log as set
        requests_set = {int(line.strip().split()[-1].strip('<')) for line in log_content}

        # fill info and error dicts with content:
        #  info - request <number>:  <execution time> if it has 'Finished' status or <start time> else
        #  errors - request <number>:  <error type>
        for lin in log_content:
            for _ in requests_set:
                lin = lin.strip()
                req = '>Request {}<'.format(_)
                if ' Started ' in lin and req in lin:
                    frmt = format_tmpl.format(state='Started', num=_)
                    started = datetime.strptime(lin, frmt)
                    info[_] = started
                if ' Finished ' in lin and req in lin:
                    frmt = format_tmpl.format(state='Finished', num=_)
                    finished = datetime.strptime(lin, frmt)
                    info[_] = finished - info.get(_)
                if ' ERROR ' in lin and req in lin:
                    errors[_] = ' '.join(findall(r'ERROR (.+) for', lin))

        # output result
        print('\nParsing results: ')
        for k, v in info.items():
            # Change request value to -1  if it is not finished ergo has only starttime
            if ' ' in str(v):
                v = '-1'
            print(output_tmlt.format(number=k, content=v))
        print('\nErrors:')
        for k, v in errors.items():
            print(output_tmlt.format(number=k, content=v))

if __name__ == '__main__':
    url = 'http://mail.ru'
    log = path.join(path.dirname(__file__), 'example.log')

    tasks = Tasks()
    tasks.task1(url)
    tasks.task2()
    tasks.task3(log)
