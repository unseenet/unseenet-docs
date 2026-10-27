# Your own rules

There is no algorithm on Unseenet deciding what you see. Your feed is newest
first, a group is its threads in order, and nothing is pushed up or down because
someone else wanted it. But you may want it otherwise: friends first, bots
quieter, a subject you are tired of out of sight. That is what your own rules are
for - the old Usenet idea of a *scorefile*.

**You decide, and only you.** Your rules run in your own client. Nobody else sees
them, no node knows them, and they never change what anyone else sees. Without
rules everything is as it always is.

Open them with **Ctrl+P → Your rules** in the graphical and the terminal client,
or `unseenet rules` on the command line. The editor checks every line as you type
and says what is wrong, with a suggestion where it can.

## A rule is a line

Each line gives points, or does something, when a condition holds:

```
+30 if author in contacts            # my contacts first
-20 if from a bot                    # bots quieter
hide if subject matches "valg"       # not that again
+5 per reaction max 20               # popular, a little
```

- **Points** (`+30`, `-20`) add up to a post's score. With `per … max` a rule counts
  something - reactions, replies, days old - up to a limit.
- **Actions** do something: `show` (only posts that match are shown), `hide`,
  `blur` (text and pictures behind *Show anyway*), and in threaded groups `fold`,
  `dim`, `highlight` and `mark read`.
- **`sort by`** orders the feed or a group's threads: `sort by score`, `sort by
  date`, `sort by reactions then date`.
- `#` starts a comment, and case does not matter.

Some conditions: `author in contacts`, `author in following`, `from a bot`,
`subject matches "…"`, `text matches "…"`, `group is dk.*`, `has pictures`,
`older than 2 days`, `I reacted`, `I posted in thread`, `seen`, `reactions >= 3`, `tagged linux politics`
(the author's or the group's [tags](spam.md)), `labelled spoiler` (from
[labellers](spam.md) you follow). Combine them with `and`, `or`, `not` and
parentheses. **Ctrl+P → Your rules → Help** has them all, in short.

## Where a rule acts: scopes

A line like `[feed]` starts a scope; the rules under it act only there:

| Scope       | Acts on                                              |
|-------------|------------------------------------------------------|
| (none)      | the feed and your groups                             |
| `[feed]`    | your timeline - the feeds you follow                 |
| `[groups]`  | threaded groups                                      |
| `[dk.*]`    | groups whose name matches, here everything in `dk.*` |
| `[foryou]`  | For you - and nothing else (below)                   |

## For you

*For you* lists replies to your posts and posts that name you, from all your
groups. It is not a feed: nothing disappears from it because you have seen it -
the count drops, the entry stays until you open it or it expires.

Rules for the feed or your groups **never** act on For you, so a post you hide in
its group still reaches you when it answers you. Only rules under `[foryou]` do,
and there is one action only for it:

```
[foryou]
quiet if for you is mention and from a bot   # listed, not counted, no notification
hide if author is "ed25519:…"                     # not at all
highlight if for you is reply and author in contacts
```

## Show all

Wherever your rules act - the feed, a threaded group, For you - **Show all** shows
that view as it is without them, plainly marked while it is on: *your rules are
paused here*. It is a look, not a setting: nothing is saved, and it ends when you
leave the view.

## Why is this here?

Every post's ⋯ menu has **Why?**: which of your rules gave it its score, hid it,
folded or blurred it. From the same menu you can **watch** or **ignore** a thread;
your rules see that as `thread in watched` and `thread in ignored`, so you decide
what it means - for example `+50 if thread in watched` or `hide if thread in ignored`.

## Ready to copy

```
# Friends first, bots quieter
+30 if author in contacts
+20 if author in following
-15 if from a bot

# I have seen it: further down
-10 if older than 2 days and not I reacted

# Not that subject, in Danish groups
[dk.*]
hide if subject matches "valg" or tagged valg

# Long side discussions, folded
[groups]
fold if replies > 30 and not I posted in thread

# Spoilers and gore: never by surprise
blur if tagged spoiler or labelled spoiler
hide if labelled gore

# For you: bots that name me are quiet
[foryou]
quiet if from a bot
```

On the command line: `unseenet rules show`, `set`, `check`, `on`, `off`,
`clear`; `unseenet thread watch|ignore|clear`; `unseenet timeline --why`;
`unseenet foryou --all --why`.

The full language is [UN-RFC 0051](https://unseenet.org/spec/un-rfc-0051/); this
page is the friendly version.
