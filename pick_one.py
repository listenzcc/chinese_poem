# coding: utf-8

import json
import os
import random

root_dir = os.path.join('C:\\Users\\liste', 'Documents', 'chinese-poetry')

ci_dir = os.path.join(root_dir, 'ci')

ci_files = [e for e in os.listdir(ci_dir) if e.startswith('ci.song')]

ci_path = os.path.join(ci_dir, random.choice(ci_files))

with open(ci_path, 'r', encoding='utf-8') as f:
    lst = json.load(f)


class Ci:
    def __init__(self, content):
        self.ci = content
        self._repair()

    def _repair(self):
        self.ci['rhythmic'] = self.ci['rhythmic'].replace('\u30fb', '-')

    def _print(self):
        print('%s  %s' % (self.ci['rhythmic'], self.ci['author']))
        print('')
        for e in self.ci['paragraphs']:
            print(e)


this_ci = Ci(random.choice(lst))
this_ci._print()
