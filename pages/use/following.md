# Following and feeds

A **feed** is a group shown newest first, with comments under each entry -
like Facebook, Mastodon or X. A person can have their own feed, and their
own **site** of pages.

Your **Timeline** shows the entries of every feed you follow, newest
first. Nothing is reordered, weighed or left out by anybody but you: no
algorithm decides what you see. (If you want one, you write it yourself -
see [Your own rules](../guide/rules.md).)

## Following someone

Following a person means following their feeds, now and as they change.
**Nobody is told** - not the person, not the node - and the list stays in
your vault.

=== "Graphical"

    Click an author's name to open their profile and choose **Follow**; or
    **Follow someone** in the palette (++ctrl+p++) and give their key,
    their name (such as `andreas@lorensen`) or an `unseenet:` address.
    They come under **People you follow** in your list, their feed and
    site together.

    ![Follow someone: a key, a name or an address](../img/guide/follow.png)

=== "Terminal"

    ++ctrl+p++, **Follow**: the selected post's author, or anyone by key
    or name. **Following** lists whom you follow and stops following one.

    ![A person's feed: an entry cut at "… more", the comments folded](../img/client-feed.svg)

## Your timeline

=== "Graphical"

    **Timeline** at the top of your list. **Add to timeline** in a group's
    head puts a discussion group in too (each new thread, with its
    answers); the same button takes a feed out. Chat groups are never in it.

=== "Terminal"

    **Timeline** at the top of your groups. ++ctrl+p++, *Add to timeline /
    take out of timeline*, puts a discussion group in or takes a feed out;
    `•` marks the groups in it.

    ![The timeline: feeds and a discussion group, newest first](../img/client-timeline.svg)

## Your own feed, site and profile

Your feed and site are **public and tied to your key**, so the client asks
before it starts them. Anyone can comment on your feed unless you say
otherwise.

=== "Graphical"

    **Start your feed** and **Start your site** at the top of your list
    (later *Your feed* and *Your site*). **Your profile** in the palette
    writes a few lines about you, your languages, links elsewhere and a
    picture.

    ![Your profile](../img/guide/my-profile.png)

=== "Terminal"

    ++ctrl+p++, **Start your feed**; on the command line also
    `unseenet site-start`. ++ctrl+p++, **Your profile**, writes your
    profile.

A profile links this identity to whatever you put in it. If you want to
stay unknown, leave it out - or use [another identity](your-key.md#several-identities).

**More:** [Groups](../guide/groups.md) in *How it works* and
[UN-RFC 0034](../spec/un-rfc-0034.md) (feeds and following).
