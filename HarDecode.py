"""Reads a har file with encoded base 64 text field from the filesystem, converts to har file with decoded text field.
"""
import argparse
import json
import base64
from urlparse import urlparse



def main(harfile_path):
    """Reads a har file with encoded base 64 text field from the filesystem, converts to har file with decoded text field.
    """
    harfile = open(harfile_path)
    harfile_json = json.loads(harfile.read())
    with open(harfile_path[:-3] + 'decoded.har', 'w') as f:
        for entry in harfile_json['log']['entries']:
            entry['response']['content']['text'] = base64.decodestring(entry['response']['content']['text'])
            del entry['response']['content']['encoding']
        jstr = json.dumps(harfile_json, indent=4)
        f.write(jstr)

if __name__ == '__main__':
    argparser = argparse.ArgumentParser(
        prog='HarDecode',
        description='Parse .har files into .har files with decode text field.')
    argparser.add_argument('harfile', type=str, nargs=1,
                        help='path to harfile to be processed.')
    args = argparser.parse_args()

    main(args.harfile[0])
