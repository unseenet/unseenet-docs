# Show your name elsewhere

On a website, in a mail signature or on a business card, a name like
`andreas@lorensen` looks like an e-mail address. So outside Unseenet, a
name always carries the word **Unseenet** in front, the way "Mail:" or
"Tel:" do (UN-RFC 0019 section 8.5):

```text
Unseenet: andreas@lorensen
```

Where there is room for a link, the name links to your **key** - not to
the name. A name can change hands; a key cannot be swapped. A reader who
follows the link sees the key the name belongs to, and can check that the
two match.

## Your address

Your address is `unseenet:` and your key's **fingerprint** - 16 letters
and digits. Your client shows the fingerprint with your key (**K** in the
graphical client, ++k++ in the terminal client), and the command line
prints your whole address with `unseenet address`.

`unseenet:` links only work for people who have a client. For everyone
else, use the address's **web form** on a web entrance: the same address
without `unseenet:`, after `https://entrance.unseenet.net/a/`. Clients
read the web form on any host as the address it stands for, so the link
keeps working even if that entrance goes away.

| | Address |
|---|---|
| In Unseenet | `unseenet:<fingerprint>` |
| On the web | `https://entrance.unseenet.net/a/<fingerprint>` |

Never write a name as an address: `unseenet:andreas@lorensen` is not
valid, and clients will not open it.

## The icon

A small Unseenet mark to put in front of the name, like an envelope before
an e-mail address.

| | On a light background | On a dark background |
|---|---|---|
| 16 px | ![](../img/name/unseenet-mark-light-16.png) | ![](../img/name/unseenet-mark-dark-16.png){ style="background:#111816" } |
| 24 px | ![](../img/name/unseenet-mark-light-24.png) | ![](../img/name/unseenet-mark-dark-24.png){ style="background:#111816" } |
| 32 px | ![](../img/name/unseenet-mark-light-32.png) | ![](../img/name/unseenet-mark-dark-32.png){ style="background:#111816" } |
| SVG | [unseenet-mark-light.svg](../img/name/unseenet-mark-light.svg) | [unseenet-mark-dark.svg](../img/name/unseenet-mark-dark.svg) |

Copy the files to your own site rather than linking to unseenet.org, so
your page loads nothing from anyone else.

## Copy and paste

Put in your own name and fingerprint.

=== "Website (HTML)"

    ```html
    <a href="https://entrance.unseenet.net/a/<fingerprint>"
       title="unseenet:<fingerprint>">
      <img src="unseenet-mark-light-16.png" width="16" height="16" alt=""
           style="vertical-align:-3px"> Unseenet: andreas@lorensen</a>
    ```

    On a dark page, use `unseenet-mark-dark-16.png`.

=== "Mail signature"

    ```text
    Unseenet: andreas@lorensen
    unseenet:<fingerprint>
    ```

    The second line is optional; it lets a reader with a client check the
    name.

=== "Markdown"

    ```markdown
    Unseenet: [andreas@lorensen](https://entrance.unseenet.net/a/<fingerprint>)
    ```

=== "Plain text"

    ```text
    Unseenet: andreas@lorensen
    ```

## When someone pastes it

A client takes a name wherever you can paste an address - `@lorensen`,
`sonia@lorensen`, with or without `Unseenet:` in front - looks it up, and
**shows the key it found** before you follow, add or write to anyone. If a
pasted name and a pasted address name different keys, it says so and asks.

**More:** [Names](names.md) and
[UN-RFC 0019](../spec/un-rfc-0019.md) section 8.5.
