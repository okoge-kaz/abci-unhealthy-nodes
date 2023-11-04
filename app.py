import argparse
import os


def read_hostfiles(paths: list[str]) -> list[str]:
    healthy_hosts: list[str] = []
    for path in paths:
        with open(path, 'r') as f:
            for line in f:
                line: str = line.replace("slots=8", "")
                line = line.strip()
                # print(f"DEBUG: {line}")
                if line.startswith("a"):
                    healthy_hosts.append(line)
                else:
                    print(f"ERROR: {line}")
    return healthy_hosts


def arg_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Read hostfile and return healthy hosts')
    parser.add_argument('--hostfile-dir', type=str, default="hostfiles/", help='hostfile to read')
    parser.add_argument("--all-hosts-file", type=str, default="all_hosts.txt", help="all hosts file")
    return parser.parse_args()

def main() -> None:
    args = arg_parser()

    # hostfiles
    hostfiles: list[str] = os.listdir(args.hostfile_dir)
    hostfiles = [os.path.join(args.hostfile_dir, path) for path in hostfiles]

    # all nodes
    all_nodes: list[str] = []
    with open(args.all_hosts_file, 'r') as f:
        for line in f:
            line: str = line.strip()
            all_nodes.append(line)

    healthy_hosts: list[str] = read_hostfiles(hostfiles)
    for host in all_nodes:
        if host not in healthy_hosts:
            print(f"unhealthy node: {host}")

if __name__ == '__main__':
    main()
