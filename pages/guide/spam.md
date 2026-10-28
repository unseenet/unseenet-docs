# Spam and reports

There is no company behind Unseenet that reads everything and deletes what
it does not like, and there never will be. That is the point. But a network
anyone can post to is also a network spammers can post to, and some posts
are worse than spam: threats, scams, illegal material.

This chapter is about how Unseenet deals with that without handing anyone
power over anyone else: who can do what, how a post you report reaches the
people who can act on it, and what they can do when it arrives.

## The layers, from the bottom up

Nothing on this list can be switched off for you by someone else, and none
of it needs a central authority.

1. **Every post costs a little.** Each article carries postage - a small
   proof-of-work - and a new key must [ripen](identity.md#why-a-new-key-has-to-ripen)
   before it posts cheaply. A spammer who throws keys away pays the full
   price every time.
2. **A group's owner looks after the group.** Owners and moderators can
   withdraw posts, ban keys from the group, and approve posts in a moderated
   group ([Groups](groups.md#moderation)).
3. **Spam reports, from issuers you choose.** Anyone can publish signed
   reports saying "these posts, or this key, are spam". Your client hides
   what the issuers *you follow* report - and only those. This chapter is
   mostly about this layer.
4. **A hierarchy's maintainer** can block a key in its whole hierarchy, for
   example someone who posts threats in group after group in `dk.*`
   ([Groups](groups.md#names-and-hierarchies)).
5. **A node's operator** decides what their own node carries: they can drop
   a group, honour maintainers' blocks, or act on the reports of issuers
   they follow ([The node](node.md)).

And at every level: **you** decide what you read. You can ignore a person,
leave a group, show what a report or a block hid, and stop following any
issuer.

## Issuers

An **issuer** is a key that publishes spam reports. Any key can be one - a
person, a group of volunteers, a program that spots floods of the same text,
the project itself. An issuer has a group of its own, `reports@` followed by
its fingerprint, where only it posts. Its manifest says what it reports and
how (its *policy*), where to object to a report, and whether a program makes
the reports.

A report names **posts** (by their Message-ID) or **keys**, each with a
reason: spam, flooding, phishing, malware, illegal, or other. A key is
reported for at most a year, so that a mistake, or a stolen key given back,
does not follow its owner forever. A report about a post ends when the post
does. An issuer can withdraw a report at any time.

The issuer is pseudonymous like everyone else. A report never names the
person who told the issuer about a post.

## Who follows which issuer

A report does nothing by itself. It hides posts only for those who follow
its issuer:

| Who | Follows | For |
|-----|---------|-----|
| **You** | the issuers you choose | every group you read |
| **A hierarchy's maintainer** | names issuers in its hierarchy's list | the groups of that hierarchy, for everyone who reads them, by default |
| **A group's owner** | names issuers in the group's manifest | that group, for everyone who reads it, by default |
| **A node's operator** | names issuers in the node's configuration | what the node carries and passes on |

So a new user who reads `unseenet.*` follows the project's issuer from the
start, and spam there is hidden for them without them doing anything. But
it stays their choice: under **Spam reports** in the client they see every
issuer that hides posts for them and why ("named for unseenet.*", "named for
alt.space.nasa"), and can turn any of them off. The project names its issuer
for its own groups only, never for the whole network. Hierarchies and groups
the project does not run - `dk.*`, say - are for whoever runs them to decide.

## What a hidden post looks like

A post hidden by a report is **never hidden silently**. It keeps its place,
and where its text would be it says who hid it and why:

> ⊘ Hidden by reports@unseenet: spam

with **Show anyway** and **Stop following reports@unseenet** right there. The
group's title says how many posts reports hide in it. Your own posts and
your contacts' are never hidden by reports, whoever reports them.

Hidden is not deleted. The post is still on the nodes, unless their
operators chose otherwise, and anyone who does not follow the issuer sees it
as before.

## Reporting a post

When a post goes against a group's charter or the law, choose **Report** in its ⋯
menu - in a discussion, a feed, a comment or a chat (in the terminal client:
**Report post** in the command palette). The report window shows the post,
and you choose:

- **what is wrong**: spam, illegal, threats or harassment, or something else;
- **who gets it**: the group's owner and moderators, the maintainer of its
  hierarchy, the operator of the node you read it from, and the spam report
  issuers that apply to the group - each of them who can be reached;
- **what you want to tell them**, in Markdown, as long as you like;
- **screenshots or documents** - pictures and PDFs, which are sent encrypted;
- whether to report **anonymously**: then nobody can see who you are, and
  nobody can answer you.

Each person you send it to gets their own sealed copy, which only they can
read. A sealed copy is signed by a one-time key, which cannot ripen, so it
pays the full postage: sending to three people can take a few minutes. The
window closes at once, and the client tells you when every copy has gone.

**In an emergency, contact the police.** Nobody on Unseenet - not the node
operators, not the project - can see who anyone is or where they are.

## When a report reaches you

A report arrives as a private post: the post it is about, its group and
author, the reason, the note and any files. Where it arrives depends on why
you got it - your own inbox, or a **team inbox** you read with others (see
below). Your client shows **Open the reported post**, and if you are an
issuer, **Publish a spam report…**.

Then:

1. **Look at the post in its place** before you act. Read the group's charter.
2. **Decide whether the report is right.** If not, do nothing. Nobody is told.
3. **Act as far as your role reaches:**
    - *As an issuer*: publish a report of the post - and, if the author does
      nothing else, of their key for up to a year. It hides for everyone who
      follows you. The reason the reporter gave is filled in; you can change it.
    - *As the group's owner or a moderator*: withdraw the post, or ban the
      author from the group.
    - *As a hierarchy's maintainer*: block the author in your hierarchy, with a
      public reason.
    - *As a node's operator*: drop the group from your node if it should not
      be there at all, or act on an issuer's reports on your node.
4. **Illegal material**: do not keep copies, and report it to the police.
5. **Answer the reporter** if they were not anonymous - from a team inbox,
   your answer goes out as the team.

## Team inboxes

A project, an organisation running a hierarchy, or a group of volunteers
should not have to share one key, or each check a separate mailbox. A
**team inbox** is an inbox up to 16 people read, each with a team key of
their own made for that inbox only. Messages to it are sealed for all of its
readers at once. Readers answer **on the inbox's behalf** - "Unseenet
(operator)" - so nobody learns which person wrote. The owner key is needed
only to change who reads, and can stay offline.

The team inbox is the natural place for reports: an issuer or a hierarchy
names it as its contact, and every report sent to that issuer or maintainer
lands there, where the team reads them in their everyday clients. An issuer
can even live beside your own identity in your vault, so you publish its
reports from the report itself, without opening anything else.

## Becoming an issuer

Anyone can. In the graphical client choose **Become a spam report issuer** in
the command palette; in the terminal client the same; on the command line
`unseenet reports start`. You say what you report and how, and where reports
sent to you should land - your own inbox, or a team inbox you read.

Nobody follows you because you exist. People, groups, hierarchies and nodes
follow an issuer because they trust it, and stop when they no longer do. An
issuer that reports things that are not spam soon has nobody following.

## Why it is built this way

- **No central list.** A shared report group would be one place to flood,
  and whoever owned it would decide who may report. With an issuer per key,
  nobody stands between issuers and readers.
- **Defaults without control.** A new user should not have to find issuers
  before spam goes away. So whoever runs a hierarchy or a group may name some
  for its readers - and every reader may turn them off.
- **Never cheaper.** Nothing a report does can make posting cheaper or a key
  more trusted for anyone; if reports could, whoever issued them would hold
  the key to the network.
- **Never silent.** Something hidden says by whom and why, one click from
  being shown. Silencing by report only works where people cannot see it.

The details are in [UN-RFC 0045](https://unseenet.org/spec/un-rfc-0045/) (spam
reports), [UN-RFC 0047](https://unseenet.org/spec/un-rfc-0047/) (team inboxes)
and [UN-RFC 0018](https://unseenet.org/spec/un-rfc-0018/) (hierarchies and their
blocks).
