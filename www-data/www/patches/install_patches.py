# -*- coding: utf-8 -*-

import json
import shutil


class PatchesInstaller:
    def __init__(self):
        with open('patches.json', 'r', encoding='utf-8') as fp:
            self.patches = json.load(fp)['patches']

    def install(self):
        for patch in self.patches:
            print(patch['description'])
            shutil.copyfile(patch['to'], patch['backup'])
            shutil.copyfile(patch['from'], patch['to'])


if __name__ == '__main__':
    pi = PatchesInstaller()
    pi.install()
