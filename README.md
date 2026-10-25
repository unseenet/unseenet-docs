<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/unseenet/unseenet/main/assets/logo-dark.svg">
    <img src="https://raw.githubusercontent.com/unseenet/unseenet/main/assets/logo-light.svg" alt="Unseenet" width="360">
  </picture>
</p>

<h1 align="center">unseenet-docs</h1>

<p align="center"><b>The site unseenet.org.</b><br>
The front page, the guide, getting started and the project - and the docs of every Unseenet repository, gathered in one place.</p>

<p align="center">
  <a href="https://github.com/unseenet/unseenet-docs/actions/workflows/site.yml"><img src="https://github.com/unseenet/unseenet-docs/actions/workflows/site.yml/badge.svg" alt="site"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache--2.0-blue" alt="Apache-2.0"></a>
</p>

> **Pre-alpha.** Nothing is stable yet, and Unseenet has not had a security
> review. Do not rely on it to protect anyone yet.

## What it is

The site [unseenet.org](https://unseenet.org): the front page, what Unseenet
is and why, the guide (how it works, the threat model), getting started, and
the project.

It holds what belongs to the project as a whole, in `pages/`, and gathers,
when it builds, the docs every other repository keeps of what it holds - the
UN-RFCs, the node, the CLI and the developers' reference from unseenet, and
in time the manuals of the terminal and graphical clients, the entrance, the
gateway and the bots. Addresses on unseenet.org stay the same wherever a page
lives.

## How it works

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

## Develop

### Where does a page go?

- **About one repository** (the node, a client, the entrance, a gateway):
  in that repository's `docs/`. Link to pages in other repositories with
  their full address on `https://unseenet.org/...`, so each repository's
  own docs check stays strict.
- **About the project as a whole** (the front page, why, the guide, the
  project, getting help): here, in `pages/`.
- **The protocol**: the UN-RFCs stay in unseenet's `rfc/`, next to the code
  that implements them, and are published under `/spec/`.

## Versions and releases

The site is built from `main` of every source each night, on every push
here and by hand; it has no releases. Pages about what is not released yet
say so.

## Part of Unseenet

| Repository | What it is |
|---|---|
| [unseenet](https://github.com/unseenet/unseenet) | The protocol (UN-RFCs), the core library, the node and the command-line client |
| [unseenet-tui](https://github.com/unseenet/unseenet-tui) | The terminal client |
| [unseenet-gui](https://github.com/unseenet/unseenet-gui) | The graphical client - in a window, booted, or in a browser |
| [unseenet-portable](https://github.com/unseenet/unseenet-portable) | Builds the portable clients, Terminal and Graphical, with Tor inside |
| [unseenet-bootable](https://github.com/unseenet/unseenet-bootable) | Builds the bootable images, Terminal and Graphical |
| [unseenet-docs](https://github.com/unseenet/unseenet-docs) | The site [unseenet.org](https://unseenet.org) |
| [unseenet-entrance](https://github.com/unseenet/unseenet-entrance) | Web entrances: the graphical client in an ordinary browser |
| [unseenet-gateway](https://github.com/unseenet/unseenet-gateway) | Gateways to other networks: Usenet, Nostr, Matrix |
| [unseenet-bots](https://github.com/unseenet/unseenet-bots) | Bots that keep channels filled with current content |
| [unseenet-helpbot](https://github.com/unseenet/unseenet-helpbot) | The bot that answers questions in `unseenet.help` |
| [unseenet-stats](https://github.com/unseenet/unseenet-stats) | Statistics for the network |
| [unseenet-mcp](https://github.com/unseenet/unseenet-mcp) | An MCP server, so a language model can read and post as you (planning) |
| [unseenet-demo](https://github.com/unseenet/unseenet-demo) | Demo people, feeds and sites, made with the command-line client |

## License

[Apache License 2.0](LICENSE). The Unseenet logo: CC BY 4.0.
