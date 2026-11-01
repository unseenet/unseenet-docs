# How robust is it?

[The threat model](threats.md) is about you: what Unseenet protects you
against, and what it does not. This chapter is about the network: what
keeps working when parts of it are taken down, lie or are stolen, and -
just as plainly - where it is fragile today. It is written for people who
want to judge the design before they rely on it or help run it.

!!! warning "Pre-alpha, and not reviewed"
    Neither the protocol nor the code has had an independent security
    review. What follows is what the design intends and what the code does
    as far as the project knows. Reports are welcome:
    [Security](https://github.com/unseenet/unseenet/security/policy).

## How it is built

A short map of the parts, and what each one is trusted with:

| Part | What it does | Trusted with |
|---|---|---|
| **Your key** | Signs everything you post; opens what is sealed to you | Everything about your identity. It never leaves your vault |
| **A client** | Checks every signature itself, encrypts and decrypts, keeps your vault | Your keys - it is your own program on your own machine |
| **A node** | Stores posts, passes them to other nodes, serves readers | Nothing secret: it cannot forge, change or read sealed posts |
| **A group's owner** | Decides who may post, who is banned, the group's settings, in signed manifests | Its own group only |
| **A council** | A set of keys that keeps one shared thing - from 0.7.0 the names - by public rules | Only what it keeps, and only when a majority signs the same change |
| **The project key** | Signs the project's lists and the releases | Today: the lists of nodes, hierarchies, entrances and gateways, and the releases (see below) |
| **Entrances and gateways** | Doors at the edge: a browser in, or posts to and from Usenet, Matrix and Nostr | What passes through them in the clear - never keys or sealed posts |

The rule underneath all of it: **a server is never trusted to tell the
truth**. Every post, manifest, ban, withdrawal, certificate and list is
signed, and the client checks it itself. A server can only decide what to
pass on.

## What is robust

**Taking nodes down.** Nodes are onion services: they have no public
address, so they cannot be found by address or blocked one by one. Every
node keeps what it carries, and a post reaches many nodes by many paths.
A node that disappears loses nothing others have. From version 0.7.0 nodes
also announce themselves and find peers by themselves, so a new node joins
the network without anybody's agreement, and the network heals around
nodes that go.

**Nodes that lie.** A node cannot forge a post, change one, or invent a
ban, because it has none of the keys. What it can do is **withhold**: not
pass a post on, or not show it to you. That is the one power a node has,
and the answer is many paths - posts flow between many nodes, a client
can use several, and a group can be read from another node that carries
it. Nodes that announce themselves must prove they hold the key they
announced, so one node cannot pose as another.

**A seized node.** It holds the public groups it carries and the
encrypted rest. It has no user's keys and no closed group's secrets, and
it never learned where its readers are.

**A stolen node key.** The thief can pose as that node towards its peers
until they stop trusting the key. It cannot read or forge anything; the
node key only says "this is node X".

**A stolen group-owner key.** The thief controls that one group, as its
owner could - and nothing else. Other groups, other keys and the network
go on.

**A stolen council key.** One member key can sign certificates until the
others remove it; a certificate no claim explains removes its signer by
itself, about eight days after the claim. It cannot change the council
alone, and two versions of a council's history show as a dispute
([UN-RFC 0054](../spec/un-rfc-0054.md)).

**Spam and floods.** Every post costs postage, a small proof of work, and
new keys must ripen before they post cheaply, so throwaway keys cost real
work. What gets through can be reported by issuers you choose, and your
client hides it - visibly.

**The cryptography.** Unseenet invents none of its own. Signatures are
Ed25519, sealed messages use X25519 with libsodium's sealed boxes, closed
groups use XChaCha20-Poly1305 with keys sealed to each member, the vault
is sealed with a key from your passphrase through Argon2id, and postage is
SHA-256. All of it comes from libsodium, through PyNaCl.

## Where it is fragile today

Some weaknesses are temporary - the network is young - and some are part
of the design. Both are listed.

**Few nodes, run by one project.** Today the nodes new users are offered
are the project's own. If they all went at once, the network would be
only the nodes others run. Anyone can run a node, and every node that
does makes this weaker; the network is only as robust as the number of
people who run it.

**The project key still signs the lists and the releases.** The list of
known nodes, the list of hierarchies and who maintains them, the web
entrances, the gateways and the releases are signed by one key. Whoever
holds it - or steals it, or forces its holder - could put a bad node on
the list, give a hierarchy to someone else, or sign a bad release. The
names move to a council with 0.7.0; the lists move to councils in 0.8
([#56](https://github.com/unseenet/unseenet/issues/56)), and releases to
signatures you choose
([#822](https://github.com/unseenet/unseenet/issues/822)) and later
independent rebuilders
([#823](https://github.com/unseenet/unseenet/issues/823)). Until then: a
stolen project key cannot read anything, forge posts or take over
anybody's group, but it is the one key that matters most.

**The first council has one hand on every seat.** The council that keeps
the names starts with three members on different machines, all run by
the project's founder. The machinery runs by itself; its crew does not
yet. It becomes robust when other people run members.

**One maintainer, one implementation.** The code is written and released
by one person today, and there is one implementation of the protocol. A
bug in it is a bug in the whole network, and a maintainer who stops
stops releases. The specifications are written so that others can build
their own ([Build your own](build.md)); the code is open, and the network
keeps running without new releases.

**Where the code comes from.** The source is on GitHub, the packages on
PyPI and the container images on GitHub's registry. Releases are signed
with the project key and servers that update themselves check that
signature and the hash of every package - but the builds are not yet
reproducible, so nobody can yet check independently that a release is
made from the source it claims.

**Tor.** Everything depends on Tor: hiding where people and nodes are,
and reaching nodes at all. Unseenet inherits Tor's strengths and its
limits - someone who can watch traffic everywhere at once may correlate
it - and where Tor is blocked, Unseenet is reached through bridges or not
at all.

**Flooding a node.** Tor has a proof-of-work defence that makes flooding
an onion service with connections expensive. The specification asks
nodes to turn it on; today's node does not do it by itself yet
([#869](https://github.com/unseenet/unseenet/issues/869)).

**Domain names depend on DNS.** A name such as `andlo@lorensen.dk` is
proven by a record in the domain's DNS, checked over the open internet.
Whoever controls that domain's DNS controls the name - as they control
the domain's web site and mail.

**No forward secrecy.** Someone who gets a key can read what was stored
for it: an inbox's old messages, a closed group's old posts. Short
retention for sensitive groups and inboxes limits what there is to read.

**Nodes see what their readers follow.** The node you use learns which
groups some client reads - not who or where. Reading whole hierarchies,
or using several nodes, hides interest.

## What it depends on

The core is Python and a handful of libraries. Each is listed with what it
does here and what happens if it fails or is attacked:

| Dependency | Used for | If it is broken or compromised |
|---|---|---|
| **Tor** | Every connection; nodes as onion services | Locations could leak, or nodes could not be reached. Kept apart: Unseenet runs Tor's own program and talks to it over its control port |
| **libsodium**, through **PyNaCl** | All cryptography: signatures, encryption, the vault, key derivation | The heart of it: a flaw here is a flaw everywhere. Widely used and reviewed |
| **chiavdf** | Ripening keys (a verifiable delay function) | Keys could be ripened faster than intended, making throwaway keys cheaper; nothing could be read or forged |
| **Pillow** | Stripping metadata (location, camera) from pictures before they are posted | A picture could keep its metadata; a crafted picture could attack the client that opens it. Nodes never decode pictures |
| **markdown-it-py** | Turning Markdown in posts into text and pages | Posts could display wrongly. Raw HTML in posts is never passed through, so it makes no scripts |
| **python-socks** | Reaching Tor's SOCKS port | Connections would fail - not go around Tor |
| **spake2** | Copying an identity to another device with a short code | A copy could be intercepted while it happens; nothing else uses it |
| **aiohttp** (optional) | The local API that graphical and web clients use, on 127.0.0.1 with a token made at each start | Another program on the same computer could try to use your client |

Servers that update themselves install only the exact packages, with the
exact hashes, that a release names, so a package swapped on PyPI later is
refused.

## What you can do

- **Run a node.** It is the single biggest thing anyone can do for the
  network's robustness. A Raspberry Pi is enough ([The node](node.md)).
- **Run a replica** as a shadow, so the councils get members who are not
  the project ([Running a replica](../replica.md)).
- **Read the specifications and the code, and report what you find:**
  [Security](https://github.com/unseenet/unseenet/security/policy).
- **Use several nodes** in your client, and read whole hierarchies where
  interest matters.

**Details:**
[UN-RFC 0003](../spec/un-rfc-0003.md) (cryptography),
[0005](../spec/un-rfc-0005.md) (nodes),
[0006](../spec/un-rfc-0006.md) (postage),
[0007](../spec/un-rfc-0007.md) (data at rest),
[0025](../spec/un-rfc-0025.md) (ripening),
[0054](../spec/un-rfc-0054.md) (councils),
[0055](../spec/un-rfc-0055.md) (announcements and finding nodes),
[0062](../spec/un-rfc-0062.md) (updates).
