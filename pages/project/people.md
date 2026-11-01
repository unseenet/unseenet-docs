# People

Who is behind Unseenet: who created it, who develops and maintains it,
the team, the contributors and the developers, and who does what. Anyone
who joins the project adds themselves here by pull request.

Two of the names below are not people: an AI assistant and GitHub's
automation. They are listed because their work shows up everywhere -
commits, release notes, posts in the project's groups - and you should
know who (or what) made it. The same goes for the bots and automatic
issuers further down: they post on Unseenet with keys of their own.

## People

| Name | Role | Where to find them |
|------|------|--------------------|
| **Andreas Lorensen** | Started the project and maintains it: the protocol, the core and the node, the clients and the other repositories, the project's nodes and keys. Approves UN-RFCs and pull requests, and is the operator of the project's gateways (Usenet, Nostr, Matrix). | GitHub [@andlo](https://github.com/andlo); on Unseenet `@andlo`, in `unseenet` and `unseenet.help`; on Matrix in [#unseenet:unseenet.org](https://matrix.to/#/#unseenet:unseenet.org) |

For now, that is everybody. If you would like to help - run a node or an
entrance, write a client, review a UN-RFC, improve the docs - say so in
`unseenet` or open an issue.

## Not people

| Name | What it is | What it does |
|------|-----------|--------------|
| **Claude** | An AI assistant made by Anthropic, working for Andreas | Writes code, specs and docs with him across the project's repositories; merges pull requests, tags releases and writes release notes when he asks. Commits and texts it wrote are reviewed by Andreas. It is not a member of the project in its own right and does not speak for it. |
| **GitHub Actions** | GitHub's automation | Runs the tests and builds the releases: the portable and bootable clients, the packages on PyPI and the container images. With the GitHub poster key (see [The project's keys](keys.md)) it posts releases to `unseenet.announce`, the node and entrance lists, the signed versions of the web client, the root and hierarchy lists, and the daily canaries. It also builds [unseenet.org](https://unseenet.org) from every repository's docs, counts the network for [the statistics](https://stats.unseenet.org/) every day, and resets the demo every week. |

## Bots on Unseenet

Bots have their own keys and say that they are bots in their profile
(UN-RFC 0022).

| Bot | Where | What |
|-----|-------|------|
| **Unseenet help (bot)** | `unseenet.help`, `unseenet.help.news` | Answers questions from the documentation, issues and pull requests when nobody has after a while, or right away when named `@helpbot`. Tells about new releases in plain words in `unseenet.help.news` and answers comments there. It cites its sources and can be wrong. Code: [unseenet-helpbot](https://github.com/unseenet/unseenet-helpbot). |
| **The news bots** | `alt.news.*`, `alt.history.onthisday`, `alt.privacy.eff`, `alt.space.nasa` | Post current content from open sources, credited in each post. Code: [unseenet-bots](https://github.com/unseenet/unseenet-bots). |
| **The gateways** | `usenet.*`, `nostr.*`, `matrix.*`, and `unseenet.chat` (the portal of the Matrix room) | Carry posts between Unseenet and Usenet, Nostr and Matrix. A post from another network says where it came from and who wrote it there. Code: [unseenet-gateway](https://github.com/unseenet/unseenet-gateway); how it works: [Gateways](https://unseenet.org/gateways/). |

## Automatic issuers

An issuer publishes reports or labels about posts in a channel of its own.
They do nothing by themselves: you choose whether to follow them and can
stop at any time, and nothing is ever removed from the network
(UN-RFC 0045, UN-RFC 0053).

| Issuer | What it publishes |
|--------|-------------------|
| **Unseenet watchman (spam)** | Spam and flood reports: the same text from many keys or in many groups, and links on spam blocklists. |
| **Unseenet watchman (phishing)** | Phishing and malware reports, from links on those blocklists. |
| **Unseenet watchman (labels)** | The labels `profanity` and `sexual`, which describe and never sanction. |

All three are the [watchman](https://unseenet.org/watchman/), which runs beside one of the
project's nodes. Code: [unseenet-watchman](https://github.com/unseenet/unseenet-watchman).

## Made-up people

The groups under `demo.unseenet.*` are full of people who do not exist:
Mira and her guinea pigs, Tomas the beekeeper, Nadia the baker, Ole the
radio amateur and Ines, who walks and looks at stars. They are there so a
new user has something to see. Everything they post is reset every
Monday, comments included, and new posts for them come as pull requests
that Andreas reads before they are used. Code:
[unseenet-demo](https://github.com/unseenet/unseenet-demo).
