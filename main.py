import os
import json
import shutil
from subprocess import run
from time import sleep

home = os.path.expanduser('~')
configFileSrc = home+'/.config/prio/config.json'


def renice(nice, pid):
    run(f"renice {nice} -p {pid}", shell=True, stdout=False)


def ionice(ionice, pid):
    n = None
    c = None

    if 'n' in ionice:
        n = ionice["n"]

    if 'c' in ionice:
        c = ionice["c"]

    if n == int and c is None:
        run(f"ionice -n {n} -p {pid}", shell=True, stdout=False)
    elif c == int and n is None:
        run(f"ionice -c {c} -p {pid}", shell=True, stdout=False)
    elif c == int and n == int:
        run(
            f"ionice -c {c} -n {n} -p {pid}", shell=True, stdout=False)


# Get pid of process
def get_pid(name):
    def output_pidof(name):
        result = run(f"pidof {name}", shell=True, capture_output=True)
        if result.stdout:
            return result.stdout.decode("utf-8")
        else:
            return None

    original = output_pidof(name)
    if original:
        return original

    capitalize = output_pidof(name.capitalize())
    if capitalize:
        return capitalize

    lower = output_pidof(name.lower())
    if lower:
        return lower


def main_loop(config):
    for process in config["processes"]:
        if "name" in process:
            pid = get_pid(process["name"])

            if pid:
                # Renice process
                if "nice" in process:
                    renice(process["nice"], pid)

                # Ionice process
                if "ionice" in process:
                    ionice(process["ionice"], pid)

    # Recursive func with delay
    sleep(config["update_freq"])
    main_loop(config)


if os.path.exists(configFileSrc):
    fileSrc = configFileSrc
else:
    fileSrc = "/opt/prio/data/config.json"

with open(fileSrc, "r") as file:
    config = json.loads(file.read())

    # Defaults
    if "update_freq" not in config:
        config["update_freq"] = 30

    # Run loop
    if "processes" in config:
        main_loop(config)
    else:
        raise("Processes array in JSON config file is required, find and configure it: "+configFileSrc)
        exit(1)
