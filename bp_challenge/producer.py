import json
import subprocess


def generate_data():
    p = subprocess.Popen(
        'generator-linux-amd64',
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=False,
        close_fds=True,
        errors='ignore')

    for l in p.stdout:
        try:
            yield json.loads(l)
        except json.JSONDecodeError:
            continue

    p.stdout.close()
