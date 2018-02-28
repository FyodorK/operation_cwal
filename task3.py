import os
from datetime import datetime

PATH_TO_LOG = os.path.join(os.environ.get('UserProfile'), 'Documents', 'task', 'task_1_2.log')

info = {}
error = {}

format_tmpl = '[%Y-%m-%d %H:%M:%S.%f] INFO {} processing of >Request {}<'
started = None
finished = None

if os.path.isfile(PATH_TO_LOG):
    with open(PATH_TO_LOG, 'r') as fd:
        content = fd.readlines()
else:
    raise FileNotFoundError

requests = {int(line.strip().split()[-1].strip('<')) for line in content}

for lin in content:
    for _ in requests:
        lin = lin.strip()
        req = '>Request {}<'.format(_)
        if ' Started ' in lin and req in lin:
            frmt = format_tmpl.format('Started', _)
            started = datetime.strptime(lin, frmt)
            info[_] = started
        if ' Finished ' in lin and req in lin:
            frmt = format_tmpl.format('Finished', _)
            finished = datetime.strptime(lin, frmt)
            info[_] = finished - info.get(_)
        if ' ERROR ' in lin and req in lin:
            error[_] = ' '.join(__import__('re').findall(r'ERROR (.+) for', lin))

#output
print('\nParsing results: ')
for k,v in info.items():
    if ' ' in str(v):
        v = '-1'
    print('Request {}: {}'.format(k, v))
print('\nErrors:')
for k, v in error.items():
    print('Request {}: {}'.format(k, v))