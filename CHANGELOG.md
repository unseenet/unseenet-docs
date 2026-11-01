# Changelog

All notable changes to unseenet-docs are listed here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions follow the
[Unseenet conventions](https://github.com/unseenet/.github/blob/main/CONVENTIONS.md#versions).

## [Unreleased]

- **Following the core's changes for 0.6.9 and 0.7.0**: the test group is
  `test.unseenet`, the demo `demo.unseenet.*`, and the guide in the network
  `docs.unseenet.clients` (unseenet#821) - in *Getting help*, the front page, *People*,
  *Keys* and *Building*; *Keys* lists `unseenet.nodes.announce` and the guide's group,
  and what `create_groups.py` removes. *Running a node* and *Why* tell that a node
  chooses its hierarchies and always carries the network's own groups, and that a node
  announces itself (UN-RFC 0055).
- **Show your name elsewhere** (#8): the Unseenet mark at 16, 24 and 32 px, light and
  dark, and snippets for a website, a mail signature and Markdown, after UN-RFC 0019
  section 8.5.
- `tools/guide_site.py` (#7): the guide as a folder of UN-RFC 0031 pages, which the
  core's `publish-guide` workflow publishes as the site `docs.unseenet.clients`.

- **The user guide** (#6): *Getting started → How do I …*, ten task pages -
  first start, your key and ripening, groups, writing, following and feeds,
  private posts and contacts, names, nodes, backup and other devices - each
  with a *Graphical* and a *Terminal* tab and screenshots of both. The tab you
  choose is kept on every page (`content.tabs.link`).

- *Getting help* lists the groups a new client starts with - including
  `unseenet.help.news` and the demo - and what each is for.

- The guide speaks of Unseenet 0.6 as it is: "from 0.5.0" marks are gone,
  "your state in the network" is described as built (with what stays in the
  vault), attestations are marked as planned, and the comparison in *Why it
  matters* shows feeds and sites as available now.
- UN-RFC 0055 (what a node carries), 0056 (a group's own emoji) and 0057
  (a people directory) in the specification menu.
