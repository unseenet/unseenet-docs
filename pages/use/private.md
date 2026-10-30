# Private posts, chats and contacts

You can write to anyone whose key or name you know. What you write is
**sealed to their key**: only they can read it. The node cannot, and does
not even learn who sent it. Inside the sealed message you prove who you
are, so they see your name as checked.

Like in groups, there are two kinds:

- a **private post** has a subject and is answered with a quote - a letter;
- a **private chat** is a running conversation, one per person, both
  sides together.

## Writing to someone

=== "Graphical"

    **Write a private post** (++m++) or **Chat with someone** in the
    palette. Both open the person picker: recent people, then your
    contacts - type to find someone, or paste a key. **Chat** / **Post** at
    the top switches between the two.

    ![The person picker: recent people, a contact or a pasted key; Chat or Post](../img/guide/write-chat.png)

    Your private posts and chats are at the top of your list:
    **Private posts**, **Private chats** and **Your contacts**.

=== "Terminal"

    ++m++ writes a private post; ++ctrl+p++, **Chat with someone**, starts
    a chat. Both open the person picker; ++tab++ switches between a chat
    and a post. ++r++ on a private message answers it privately.

    ![The person picker: recent people, then contacts; Tab for a chat or a post](../img/client-picker.svg)

    *@ Private posts* and *» Private chats* are at the top of your groups.

## Contacts

A **contact** is a name *you* give someone's key. It is yours alone - it
never leaves your client - and it is tied to the key, so only the real
Sonia shows as **Sonia √**, everywhere, also in public groups. Someone else
can call themselves Sonia; they get no √.

=== "Graphical"

    **Add a contact** in the palette, or from the person's profile.
    **Your contacts** (++c++) chats with one, writes a post, renames or
    removes them.

=== "Terminal"

    ++a++ on a post adds its author as a contact. ++c++ lists your contacts:
    chat, write a post, rename, remove.

## Sharing your key

Give your key to people who should be able to write to you (**K** in the
graphical client, ++k++ in the terminal), or get a [name](names.md) they
can type instead.

**More:** [Identity](../guide/identity.md) in *How it works* and
[UN-RFC 0028](../spec/un-rfc-0028.md) (chats and posts).
