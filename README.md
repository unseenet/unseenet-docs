# unseenet-docs

The site [unseenet.org](https://unseenet.org): the front page, what Unseenet
is and why, the guide (how it works, the threat model), getting started, and
the project.

It holds what belongs to the project as a whole, in `pages/`, and gathers,
when it builds, the docs every other repository keeps of what it holds - the
UN-RFCs, the node, the CLI and the developers' reference from unseenet, and
in time the manuals of the terminal and graphical clients, the entrance, the
gateway and the bots. Addresses on unseenet.org stay the same wherever a page
lives.

> **Being set up** ([unseenet#547](https://github.com/unseenet/unseenet/issues/547)).
> The site is still published from unseenet/unseenet; this repository builds
> the same site, page for page, and takes over when the domain is moved.

## How it is built

| | |
|---|---|
| [`sources.yml`](sources.yml) | which repositories the pages come from, and where they go on the site |
| [`pages/`](pages/) | this repository's own pages, images, styles and scripts |
| [`tools/gather.py`](tools/gather.py) | checks the sources out and puts everything in `build/docs/` |
| [`mkdocs.yml`](mkdocs.yml) | the site: theme, navigation, plugins |
| [`tools/docs_hooks.py`](tools/docs_hooks.py) | the newest versions on the front page, the About text from the core, the guide's drawings, where to edit each page |
| [`site-extra/`](site-extra/) | files copied as they are (`.well-known`) |
| [`.github/workflows/site.yml`](.github/workflows/site.yml) | builds on push, each night, by hand and when another repository asks; publishes when the variable `PAGES_LIVE` is `true` |

```bash
pip install -r requirements.txt
./build.sh serve                                   # with the sources' main
./build.sh --local unseenet=../unseenet serve      # with your own checkout
```

## Where does a page go?

- **About one repository** (the node, a client, the entrance, a gateway):
  in that repository's `docs/`. Link to pages in other repositories with
  their full address on `https://unseenet.org/...`, so each repository's
  own docs check stays strict.
- **About the project as a whole** (the front page, why, the guide, the
  project, getting help): here, in `pages/`.
- **The protocol**: the UN-RFCs stay in unseenet's `rfc/`, next to the code
  that implements them, and are published under `/spec/`.

## Part of Unseenet

Unseenet is made in several repositories, each released on its own:

| Repository | What it is |
|---|---|
| [unseenet](https://github.com/unseenet/unseenet) | The protocol (UN-RFCs), the core library, the node and the command-line client |
| [unseenet-tui](https://github.com/unseenet/unseenet-tui) | The terminal client (moving here from unseenet, unseenet#548) |
| [unseenet-gui](https://github.com/unseenet/unseenet-gui) | The graphical client - in a window, booted, or in a browser |
| [unseenet-portable](https://github.com/unseenet/unseenet-portable) | Builds the portable clients, Terminal and Graphical, with Tor inside (unseenet#549) |
| [unseenet-bootable](https://github.com/unseenet/unseenet-bootable) | Builds the bootable images, Terminal and Graphical, and later a node image (unseenet#550) |
| [unseenet-docs](https://github.com/unseenet/unseenet-docs) | The site [unseenet.org](https://unseenet.org), gathering the docs of every repository (unseenet#547) |
| [unseenet-entrance](https://github.com/unseenet/unseenet-entrance) | Web entrances: the graphical client in an ordinary browser |
| [unseenet-gateway](https://github.com/unseenet/unseenet-gateway) | Gateways to other networks: Usenet, Nostr, Matrix |
| [unseenet-bots](https://github.com/unseenet/unseenet-bots) | Bots that keep channels filled with current content |
| [unseenet-helpbot](https://github.com/unseenet/unseenet-helpbot) | The bot that answers questions in `unseenet.help` |
| [unseenet-stats](https://github.com/unseenet/unseenet-stats) | Statistics for the network |
| [unseenet-mcp](https://github.com/unseenet/unseenet-mcp) | An MCP server, so a language model can read and post as you (planning) |
| [unseenet-demo](https://github.com/unseenet/unseenet-demo) | Demo people, feeds and sites, made with the command-line client |

## License

[Apache License 2.0](LICENSE), as in unseenet; the specification and the logo are [CC BY 4.0](https://github.com/unseenet/unseenet/blob/main/rfc/LICENSE.md).
