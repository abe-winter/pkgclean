#!/usr/bin/env python3
"entry-point for deltree"

import os, argparse

PACKAGE_DIRS = {
  'direnv': '.direnv',
  'node': '.node_modules',
}

class Walker:
  "thing to manage plugins and walk the tree"
  def __init__(self):
    self.found = [] # abs paths found
    self.detect = [] # folders to detect
    self.ignore = [] # don't recurse into these (abs or relative to .)

  def register_plugins(self, args):
    "setup plugins by importing from plugins dir"
    if args.all:
      self.detect.extend(PACKAGE_DIRS.values())
    else:
      for k, v in PACKAGE_DIRS.items():
        if getattr(args, k):
          self.detect.append(v)
    self.detect.extend(args.extra or [])
    self.ignore.extend(args.ignore or [])
    return self

def make_parser():
  parser = argparse.ArgumentParser(description="find (or delete) disposable package directories to save space")
  parser.add_argument('--delete', action='store_true', help="delete the found stuff instead of just listing it")
  parser.add_argument('--invert', action='store_true', help="instead of listing detected paths, list all paths *not* picked up. not compatible with delete mode")
  parser.add_argument('--ignore', action='append', help="don't delete this path *and* don't recurse into it")
  parser.add_argument('--extra', action='append', help="add an extra folder name to the detector")
  # plugins only below here pls
  parser.add_argument('--all', action='store_true', help='find everything we know how')
  for k in sorted(PACKAGE_DIRS):
    parser.add_argument('--' + k, action='store_true', help="include %s" % PACKAGE_DIRS[k])
  return parser

def main():
  args = make_parser().parse_args()
  if args.invert:
    raise NotImplementedError("invert mode doesn't work yet")
  walker = Walker().register_plugins(args)
  raise NotImplementedError('todo walk')

if __name__ == '__main__': main()
