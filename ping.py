from platform import system
from subprocess import run, PIPE
import re

def ping(host):
    if system() == 'Windows':
        command = ['ping', '-n', '1', '-w', '1000', host]

    elif system() == 'Darwin':
        command = ['ping', '-c', '1', '-t', '1', host]

    else:
        command = ['ping', '-c', '1', '-w', '1', host]

    result = run(command, stdout=PIPE)

    if result.returncode != 0:
        return False

    # On Windows, Destination host unreachable returns True,
    # so, need to check fail messages in output

    fail_messages = [
        'unreachable',
    ]

    for fail_message in iter(fail_messages):
        if re.search(fail_message, result.stdout.decode('utf-8'), re.I):
            return False

    return True

print(ping('192.168.1.1'))
