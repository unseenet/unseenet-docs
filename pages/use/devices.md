# Backup and other devices

Everything that is *you* - your keys - is in your vault and nowhere else.
The groups you follow, what you have read, your contacts and the chats you
closed are also kept in the network, encrypted so only your key can read
them. So the one thing to keep safe is the key, and there are two ways.

## Recovery words

Your identity can be written as **24 words**. With them you get it back on
any device, and your groups, contacts and settings come back from the
network.

- **Write them on paper** and keep it away from the stick or computer the
  vault is on. Whoever has the words *is* you.
- **Closed groups do not come back** with the words - that is the price of
  restoring. The client lists the ones you were in and can ask their owners
  to invite you again.
- They are Unseenet words, not a cryptocurrency wallet phrase: never type
  them into a wallet.

=== "Graphical"

    **Show recovery words** in the palette, after your passphrase. Type
    three of them back to note they are written down. *Print* and *Save as
    file* are there behind a warning; paper is safer. To restore: *Restore
    from recovery words* at the first start or in the palette.

=== "Terminal"

    ++ctrl+p++, **Show recovery words**, after your passphrase. To restore:
    *Restore from recovery words* at the first start or in the palette;
    four letters of each word are enough.

## A copy of the vault

The vault is an ordinary encrypted file. A copy of it is the same
identity, closed groups included, and opens with the same passphrase.
Changing the passphrase changes only that one file: copies elsewhere still
open with the old one.

## On another device

**Copy to another device** puts your identity on a phone, another computer
or another stick, straight over Tor - no file to carry. The copy is a copy:
both devices have the identity afterwards.

1. On the device you have: choose which identities to copy and whether the
   keys of your closed groups go too. Leave out an identity that must stay
   hidden - a phone is lost more often than a stick.
2. The client shows a QR code and a code such as `7-guitar-tunnel`. On the
   other device choose **Get identity from another device** (at the first
   start, or in the palette) and scan or type it. The code works once, for
   10 minutes.
3. Both show the same two **check words**. Only when you confirm that they
   match is anything sent.

![Copy to another device: which identities, and the keys of closed groups](../img/guide/copy-to.png)

In the browser, through a [web entrance](../web.md), you can receive a copy
but not send one.

!!! warning "One vault, one program at a time"
    The graphical and the terminal client can share a vault on the same
    stick, but do not open it in both at the same time.

**More:** [Identity](../guide/identity.md) in *How it works*,
[UN-RFC 0044](../spec/un-rfc-0044.md) (your state in the network) and
[0050](../spec/un-rfc-0050.md) (copying an identity, recovery words).
