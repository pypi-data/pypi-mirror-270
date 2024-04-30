from argparse import ArgumentParser, Namespace
import binascii
import hashlib
from pathlib import Path
import subprocess
from typing import Optional

from gadzooks import Subcommand, error


def xor_bytes(hashes: list[bytes]) -> bytes:
    """Computes the XOR of a collection of byte strings of the same length."""
    assert len(hashes) > 0
    arr = [0 for _ in hashes[0]]
    for h in hashes:
        for (i, b) in enumerate(arr):
            arr[i] = b ^ h[i]
    return binascii.hexlify(bytes(arr))


class BuildDocs(Subcommand):
    """build project documentation"""

    @classmethod
    def configure_parser(cls, parser: ArgumentParser) -> None:
        parser.add_argument('--src-docs', nargs='*', help='path(s) to input docs (will use checksum to decide whether to rebuild)')
        parser.add_argument('--checksum-file', type=Path, default='.doc-checksum', help='checksum file')

    @classmethod
    def main(cls, args: Namespace, extra_args: Optional[list[str]] = None) -> None:
        if not extra_args:
            error('must provide: -- <BUILD_DOCS_COMMAND>')
        assert isinstance(extra_args, list)
        paths: list[Path] = []
        for path in args.src_docs:
            path = Path(path)
            if path.is_dir():
                paths.extend([p for p in path.rglob('*') if p.is_file()])
            else:
                paths.append(path)
        if paths:
            print(f'computing checksum of {len(paths)} file(s)')
            cmd = ['sha1sum'] + list(map(str, paths))
            lines = subprocess.check_output(cmd, text=True).splitlines()
            hashes = []
            for line in lines:
                [content_hash, name] = line.split()
                name_hash = hashlib.sha1(name.encode()).hexdigest()
            hashes += list(map(binascii.unhexlify, [name_hash, content_hash]))
            checksum = xor_bytes(hashes).decode()
        else:
            checksum = None
        rebuild = True
        if args.checksum_file.exists():
            with open(args.checksum_file) as f:
                prev_checksum = f.read().strip()
            if checksum == prev_checksum:
                print(f'checksum matches {args.checksum_file} -- source docs are unchanged')
                rebuild = False
            else:
                print('source docs have changed... rebuilding')
        else:
            print('no checksum file found... rebuilding')
        if rebuild:
            print(' '.join(extra_args))
            subprocess.run(extra_args)
            if checksum:
                with open(args.checksum_file, 'w') as f:
                    print(checksum, file=f)
