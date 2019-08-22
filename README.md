# deltree

deltree is a python command that finds auto-generated directories under a root tree (and optionally, deletes them).

If you have a dev laptop with a full disk and lots of old build folders lying around, this is useful (or if you're about to do a backup).

## Things it can find / delete

* .direnv directories
* node\_modules
* files references by a .deltree file (i.e. a bespoke build or dist location)

## Things we may support in the future

* `git clean`-ing a git tree. This is tricky because some hoarders out there keep important trash in the root dirs of corp repos
* python virtualenvs

## Help wanted

Want to add the local package tree of the language of your choice? Submit a PR. Please link to official docs making a case for what you're proposing.

## Feature roadmap

* hook into backup tools
