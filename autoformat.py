# -*- coding: utf-8 -*-

import json
import os
import chardet
import shutil

import jsbeautifier
import pangu
from yapf.yapflib.yapf_api import FormatCode
import sqlparse


def format_template(func):
    def _format_template(self, filepath):
        with open(filepath, 'rb') as fp:
            content = fp.read()
            encoding = chardet.detect(content)['encoding']
        with open(filepath, 'r', encoding=encoding, errors='ignore') as fp:
            text = fp.read()
        text = func(self, text)
        with open(filepath, 'w', encoding=encoding, errors='ignore') as fp:
            fp.write(text)

    return _format_template


class AutoFormat:
    def filter_filepaths(self):
        # 筛选出符合 include 属性，并且不再 exclude 属性描述中的文件
        # include 和 exclude 属性均不支持通配符
        with open('autoformat.json', 'r', encoding='utf-8') as fp:
            content = json.load(fp)
        include_dirs = (os.path.abspath(x) for x in content['include']['dirs']
                        if os.path.exists(x))
        include_suffixes = content['include']['suffixes']
        exclude_dirs = {
            os.path.abspath(x)
            for x in content['exclude']['dirs'] if os.path.exists(x)
        }
        exclude_files = content['exclude']['files']
        all_filepaths = (os.path.join(y[0], z) for x in include_dirs
                         for y in os.walk(x) for z in y[2])
        excluded_filepaths = (x for x in all_filepaths if not any(
            x.startswith(y) for y in exclude_dirs))
        return (x for x in excluded_filepaths
                if os.path.splitext(x)[-1] in include_suffixes
                and os.path.basename(x) not in exclude_files)

    def backup(self, filepath, filepath_bak):
        shutil.copyfile(filepath, filepath_bak)

    @format_template
    def format_css(self, text):
        return jsbeautifier.beautify(pangu.spacing_text(text))

    @format_template
    def format_html(self, text):
        return jsbeautifier.beautify(pangu.spacing_text(text))

    @format_template
    def format_js(self, text):
        return jsbeautifier.beautify(pangu.spacing_text(text))

    @format_template
    def format_json(self, text):
        return jsbeautifier.beautify(pangu.spacing_text(text))

    @format_template
    def format_md(self, text):
        return pangu.spacing_text(text)

    @format_template
    def format_python(self, text):
        return FormatCode(pangu.spacing_text(text))[0]

    @format_template
    def format_sql(self, text):
        return sqlparse.format(pangu.spacing_text(text))

    def format_file(self, filepath):
        suffix = os.path.splitext(filepath)[-1]
        with open('autoformat.json', 'r', encoding='utf-8') as fp:
            rules = json.load(fp)['rules']
        self.backup(filepath, filepath + '.bak')
        getattr(self, rules[suffix])(filepath)

    def do_format(self):
        for fp in self.filter_filepaths():
            print(fp)
            #self.format_file(fp)


if __name__ == '__main__':
    AutoFormat().do_format()
