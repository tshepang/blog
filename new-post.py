"""
$ python blog-post.py 'Fight Club (1999)' movies --tags 2000-movies masterpiece
$ cat "~/projects/blog/posts/movies/Fight Club (1999).rst"
Fight Club (1999)
================

:date: 2012-04-09
:tags: masterpiece 2000-movies


$ python startpost.py 'I love Python' computing
$ cat "~/projects/blog/posts/computing/I love Python.rst"
I love Python
=============

:date: 2012-04-09

"""

import argparse
import datetime
import os
import subprocess
import shlex


def title_markup(f, text):
    f.write(text)
    f.write('=' * (len(text) - 1))
    f.write('\n\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('title')
    parser.add_argument('category',
                         choices='movies computing misc arts'.split())
    parser.add_argument('-t', '--tags', nargs='+')
    args = parser.parse_args()

    today = datetime.date.today()

    if args.title == 'links':
        filename = '{} {}.rst'.format(args.title, today)
    else:
        filename = '{}.rst'.format(args.title)
    filename = os.path.join('~/projects/blog/content', args.category, filename)
    filename = os.path.expanduser(filename)

    if os.path.exists(filename):
        print('file with the same name exists: "{}"'.format(filename))

    else:
        with open(filename, 'w') as f:
            if args.title == 'links':
                title_markup(f, '{} {}\n'.format(args.title, today))
                if not args.tags:
                    args.tags = list()
                args.tags.append('links')
            else:
                title_markup(f, '{}\n'.format(args.title))
            f.write(':date: {}\n'.format(today))
            if args.tags:
                f.write(':tags: {}\n'.format(', '.join(args.tags)))
            f.write('\n\n\n')

    command = 'editor "{}"'.format(filename)
    command = shlex.split(command)
    subprocess.call(command)


if __name__ == "__main__":
    main()
