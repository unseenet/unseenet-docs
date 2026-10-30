# Your key and ripening

## You are a key

On Unseenet you have no account. You have a **key**, made by your client
and kept in your vault. Everything you write is signed with it, so readers
can check that it came from you and nobody can post in your name.

A key is long, so people see you by:

- the name **they** gave you, if they made you a contact (`Sonia √`),
- else a **name** you hold, such as `@lorensen` (see [Names](names.md)),
- else your display name with the start of your key's fingerprint:
  `Andreas~2byg`. Anyone can call themselves Andreas; the four letters
  tell two of them apart.

Your key is the same on every node, so you are the same person
everywhere you read.

=== "Graphical"

    Your name and key are at the bottom of the group list; **K** shows the
    whole key, to give to someone who wants to write to you or invite you.

=== "Terminal"

    ++k++ shows your key, to give to someone who wants to write to you or
    invite you.

## Why a new key waits: ripening

Making a key is free, so a spammer could make thousands. Instead of asking
for a phone number, Unseenet asks a new key to **ripen**: your device
works for a while to show the key has been around. It costs a throwaway
key the same time, and that keeps spam out with nobody in charge.

- **Level 0** - a brand-new key gets there in **about a quarter of an
  hour**. From then on you can post.
- **Levels 1-3** - each takes about eight times as long as the one before,
  and makes postage (the small proof-of-work on every post) cheaper. The
  client ripens on up to level 3 by itself while it is open, and carries
  on next time from where it stopped. Some groups ask for a riper key.
- **Level 4** - only if you choose it: a couple of weeks of one core, while
  the client is open, and then every post costs about a quarter of the
  work. Worth it for a machine that is on a lot; not needed to post.

Ripening never signs anything, uses no more memory than your device has
free, and only one device needs to do it for a key.

=== "Graphical"

    The box at the bottom of the group list says how far your key is
    (*New key getting ready …*). Click it, or choose **Key ripening** in
    the command palette (++ctrl+p++), for your level, **Pause** (on a warm
    phone or on battery - it stays paused until you resume it) and *Keep
    ripening to level 4*.

    ![Key ripening: the level, what it means, Pause](../img/guide/ripening.png)

=== "Terminal"

    The status line says how far your key is. In the command palette
    (++ctrl+p++), **Key ripening** pauses or resumes it and explains it,
    and **Ripen to level 4** goes on to level 4 (*Ripen to level 3* stops
    at 3 again; what was done towards 4 is kept).

## Several identities

Everything one key writes can be linked together. If you want to keep a
part of your life apart - work and family, a hobby, something you would
rather not have tied to your name - use **another identity** for it, with
its own key and no shared names, contacts or profile.

=== "Graphical"

    The graphical client uses one identity per vault for now. Keep another
    vault for the other identity, or use the terminal client.

=== "Terminal"

    Keep a vault per identity and choose it when you start:
    `unseenet-tui --vault ~/other.vault`.

**More:** [Identity](../guide/identity.md) and
[UN-RFC 0025](../spec/un-rfc-0025.md) (key ripening).
