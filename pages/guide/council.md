# Who runs Unseenet?

A network nobody owns still has a few things everybody shares: which
names belong to whom, which nodes there are, which hierarchies exist and
who looks after them. Somebody has to keep those, and whoever keeps
them could, in principle, steer the network. This chapter is about who
keeps them, what they can and cannot do, and how that is changing.

## What was never in anybody's hands

Some things no key, council or project can do, because the network is
built so that there is nothing to take hold of:

- **read closed groups or private messages** - they are sealed to the
  members' keys before they leave the writer's device;
- **change a post** - every post is signed by its writer, and a changed
  post no longer matches its signature;
- **delete posts or groups across the network** - each node keeps what
  its operator chooses, and a group belongs to its owner's key;
- **decide what a node carries** - each operator chooses the
  hierarchies their node carries and says so openly
  ([The node](node.md));
- **decide what you see** - your client shows posts in the order they
  were written, by your own rules ([Your own rules](rules.md)).

What is left is the short list of things the network shares. Until
version 0.7.0 one key - the project's - kept all of them.

## Councils

A **council** is a group of keys that keeps something together. It
changes only when a majority of its members sign exactly the same
change, so no single key can change it - the project's included.

Each member of a council is a **council member**: a key held by a small
program, the **replica**, that runs on its own machine. A replica does
not judge. It reads public posts, applies rules written down in the
specifications ([UN-RFC 0054](../spec/un-rfc-0054.md)) and signs what
those rules give. Every member computes the same answer from the same
public data, and anybody can repeat the work and check it.

The rules are mechanical on purpose:

- **Names go to the first claim.** A claim is made in the open in two
  steps: first a sealed promise of what you will claim, then, an hour
  later, the claim itself. Nobody can see a claim and get in ahead of
  it. A domain name such as `lorensen.dk` goes to whoever proves the
  domain in DNS.
- **A member that breaks the rules is removed by the others.** A
  certificate no claim explains, losing alone on DNS again and again,
  or 90 days of silence - each replica notices it by itself, and the
  others remove that member.
- **A council's history cannot be rewritten quietly.** If somebody signs
  two different versions, both show, and the council stops at that
  point until people choose which one to follow.

## Anybody can become a member

Anybody can run a replica and become a member - also a big company or a
government. That is on purpose, and it is safe because of what a member
can and cannot do, and because getting in is slow and public:

1. A newcomer first runs as a **shadow**: a replica that does all the
   work but signs nothing, and reports every day what it would have
   decided.
2. When it has agreed with the council for 60 days, it is admitted
   **on probation**. The council admits at most one member a month.
3. After half a year on probation it becomes a **full member**, and
   only then does it count when the council changes.

So the first member from outside is a full member after about eight
months, and taking over a council would take most of a year for every
seat - in full view, while honest newcomers queue for the same seats.
Members who see something wrong can hold an admission, and anybody can
post an objection that clients show next to the candidate.

If a council is captured all the same, people can leave it: two or more
keys can found a new council that carries on from the last state they
trust, and each client and node chooses which one to follow. A council
has power only because nodes and clients choose to follow it.

## Honest about today

From version 0.7.0 the **names** are kept by a council. The other shared
lists - the known nodes, the hierarchies, the web entrances, the
gateways - and the signatures on releases are still kept by the
project's key, and move to councils next, one at a time. Nodes already
announce themselves and find each other without any list, so the node
list is no longer the only way in.

At the start, the names council has three members, all run by the
project's founder on different machines with different providers. That
is the right shape with one hand on it, and we say so plainly: the
machinery runs by itself, but its crew does not yet. A council is only
alive when several people, on different infrastructure, sit in it.

To get there sooner, the council has a **founding period**: for up to
three years, or until it has nine full members, the founder may ask the
council to admit a member after only a week as a shadow and a month on
probation. The founder can only admit - never remove anybody, change
the rules or lengthen the period - and every admission is public.

Anybody can look at the council: `unseenet council show` lists its
members, which of them the founder admitted, and how long the founding
period lasts, and `unseenet council hearings` shows the proposals and
objections.

## Becoming a member yourself

A member is a replica's key, not a person's. To become one, you run a
replica - a Raspberry Pi or a small virtual machine is enough - and let
it run as a shadow until it is admitted. It holds no secret but its own
key, needs no agreement with anybody, and learns nothing about the
people who claim names: claims arrive over Tor. How to set one up is in
[Running a replica](https://github.com/unseenet/unseenet/blob/main/docs/replica.md).
