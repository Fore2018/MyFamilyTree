# -*- coding: utf-8 -*-

import json
import os
import shutil


class PatchesInstaller:
    def __init__(self):
        with open('patches.json', 'r', encoding='utf-8') as fp:
            content = json.load(fp)
        self.args = content['args']
        self.files = content['files']
        self.dirs = content['dirs']

    def install(self):
        for patch in self.files:
            print(patch['description'])
            if 'backup' in patch and not os.path.exists(patch['backup']):
                if not os.path.exists(os.path.dirname(patch['backup'])):
                    os.makedirs(os.path.dirname(patch['backup']))
                shutil.copyfile(patch['to'], patch['backup'])
            shutil.copyfile(patch['from'], patch['to'])
            if 'append' in patch:
                args = [self.args[x] for x in patch['append']['args']
                        ] if 'args' in patch['append'] else []
                content = patch['append']['content'].format(*args)
                with open(patch['to'], 'a') as fp:
                    fp.write(content)
        for patch in self.dirs:
            print(patch['description'])
            if 'backup' in patch and not os.path.exists(patch['backup']):
                shutil.copytree(patch['to'], patch['backup'], False)
            if os.path.exists(patch['to']):
                shutil.rmtree(patch['to'])
            shutil.copytree(patch['from'], patch['to'], False)


if __name__ == '__main__':
    pi = PatchesInstaller()
    pi.install()
