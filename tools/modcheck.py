#!/usr/bin/env python3
"""Validate a research-stage RDR2 PS4 mod manifest (stdlib only)."""
import json
import pathlib
import sys


def validate(data):
    if not isinstance(data, dict):
        raise ValueError('manifest must be an object')
    for key in ('id', 'name', 'type', 'targets', 'files'):
        if key not in data:
            raise ValueError(f'missing {key}')
    if data['type'] not in ('resource', 'runtime'):
        raise ValueError('unsupported mod type')
    if not isinstance(data['targets'], list) or not data['targets']:
        raise ValueError('targets must be nonempty')
    if not isinstance(data['files'], list):
        raise ValueError('files must be a list')
    for target in data['targets']:
        if target.get('cusa') != 'CUSA08519' or target.get('update') != '1.29':
            raise ValueError('unsupported target: research profile only supports CUSA08519 1.29')
    for entry in data['files']:
        path = pathlib.PurePosixPath(entry)
        if path.is_absolute() or '..' in path.parts:
            raise ValueError('unsafe file path')
    return True


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('usage: python3 tools/modcheck.py path/to/mod.json')
    try:
        validate(json.loads(pathlib.Path(sys.argv[1]).read_text(encoding='utf-8')))
    except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
        sys.exit(f'INVALID: {exc}')
    print('VALID')
