#!/usr/bin/env python3
# encoding: utf-8

__author__ = "ChenyangGao <https://chenyanggao.github.io>"
__doc__ = "torrent to magnet"

from argparse import ArgumentParser

parser = ArgumentParser(description=__doc__)
parser.add_argument("paths", nargs="*", metavar="path", help="paths to torrent files, use stdin as default")
parser.add_argument("-f", "--full", action="store_true", help="more detailed query string")
parser.add_argument("-v", "--version", action="store_true", help="print the current version")
args = parser.parse_args()
if args.version:
    from torrent_tool import __version__
    print(".".join(map(str, __version__)))
    raise SystemExit(0)

from collections import deque
from os import scandir
from os.path import isdir
from sys import stdout

from torrent_tool import torrent_to_magnet

full = args.full
paths = args.paths
if not paths:
    from sys import stdin
    paths = (line.removesuffix("\n") for line in stdin)

dq: deque[str] = deque(paths)
get = dq.popleft
write = stdout.buffer.raw.write # type: ignore

try:
    while dq:
        path = get()
        try:
            if isdir(path):
                dq.extend(p.path for p in scandir(path))
            elif path.endswith(".torrent"):
                try:
                    data = open(path, "rb").read()
                    write(torrent_to_magnet(data, full=full).encode("utf-8"))
                    write(b"\n")
                except (ValueError, LookupError):
                    pass
        except OSError:
            pass
except BrokenPipeError:
    from sys import stderr
    stderr.close()
except KeyboardInterrupt:
    pass

