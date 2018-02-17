import os
import sys
import requests
import re
import json
from bs4 import BeautifulSoup
import subprocess


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

    def task3(self):
        """
        Parse log for time of requests
        :return: None
        """

if __name__ == '__main__':
    Tasks().task1('http://mail.ru')