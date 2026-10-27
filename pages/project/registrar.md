# Running a registrar replica

The registrar gives out names for identities, such as `@lorensen`
([UN-RFC 0019](../spec/un-rfc-0019.md)). It runs as several **replicas**,
each on its own machine, so that names keep being given out and renewed
when one machine is gone. A replica is a client, not a node: it reads and
posts through whichever nodes are up, over Tor, and it needs no connection
to the other replicas.

Every replica reads the same claims from one shared claim inbox, handles
them in the same order, and signs its own certificate for each decision.
Because all of that comes from the network, a replica keeps nothing that
cannot be rebuilt: start it on a new machine and it catches up by itself.

## What a replica needs

- Python 3.11 or newer, Tor, and `dig` (for checking the DNS records of
  domain names). On Debian: `apt install tor dnsutils python3-venv`.
- Its own **registrar key**, made on its machine by `init`.
- The shared **inbox key**, from the owner of the registrar's group.

## Setting one up

1. Install Unseenet without a node, as the user `unseenet`:
   ```bash
   curl -fsSL https://raw.githubusercontent.com/unseenet/unseenet/main/deploy/install-registrar.sh | sudo bash
   ```
2. Make the replica's vault. Press Enter at the first question to make a
   new registrar key here; at the second, type the inbox key's seed, which
   the group's owner gets with `tools/project/setup_registrar.py
   --show-inbox-seed`:
   ```bash
   sudo -u unseenet /home/unseenet/unseenet/.venv/bin/unseenet-registrar init /home/unseenet/registrar.vault
   ```
   It prints the replica's registrar key. That key is public.
3. The group's owner adds it:
   ```bash
   python tools/project/setup_registrar.py --add ed25519:...
   ```
4. Put the vault's passphrase in `/etc/unseenet-registrar.passphrase`
   (owner root, mode `600`), install
   [`deploy/unseenet-registrar.service`](https://github.com/unseenet/unseenet/blob/main/deploy/unseenet-registrar.service)
   and start it:
   ```bash
   sudo cp deploy/unseenet-registrar.service /etc/systemd/system/
   sudo systemctl enable --now unseenet-registrar
   journalctl -u unseenet-registrar -f
   ```

Every five minutes the replica reads the group and the claim inbox,
handles the claims that are more than an hour old, follows decisions of
other replicas that win over its own, and renews domain names whose DNS
record is still there at the start of each month.

## Where to run replicas

Not on the project's nodes, and not all in one place: the point is that
taking one machine down does not stop the registrar. A small virtual
machine, a Raspberry Pi at home or a machine run by someone the project
trusts will do; each runs with its own key, and the group's owner can
remove any one of them without affecting the names the others signed.

## Offering a replica

You don't have to be part of the project to run a replica: more replicas,
run by more people in more places, are what keep names working when a
machine is taken down. What you take on:

- **Your key gives out names.** For now every trusted registrar key can
  sign a certificate on its own, so a replica is trusted with all names.
  Keep the machine for the replica alone, keep it updated, and keep the
  vault's passphrase where only root can read it.
- **It should keep running.** A replica that is off now and then does no
  harm - the others carry on, and it catches up when it starts - but one
  that is gone for good should be taken out of the list.
- **You learn little.** A replica sees which key claimed which name and
  when, but not where from: claims arrive over Tor. Nothing about your
  machine is published either - the group's manifest lists only the
  replica's key.

How it goes today:

1. Write to the project in the group `unseenet.admin` (or open an issue on
   GitHub) that you would like to run a replica, and roughly where it
   would run - a VM provider, a Raspberry Pi at home - so that the replicas
   do not end up in one place. You don't have to say who you are.
2. Install the machine (step 1 of *Setting one up*).
3. The owner of the group sends you the inbox key's seed in a **private
   post** to the identity you wrote from. Type it in at `init` (step 2),
   and don't keep it anywhere else.
4. Send back the registrar key that `init` printed. It is public; the
   owner lists it with `setup_registrar.py --add` (step 3).
5. Start the service (step 4) and follow the journal. Once the owner has
   listed your key, certificates signed with it appear in
   `unseenet.names` with every new decision.

If you stop, or the machine is lost or seized, tell the project, so your
key is taken out of the list: certificates only your key signed stop
counting, while the same decisions signed by the others stay valid.

## Keeping it up to date

All replicas must reach the same decisions, so update when a release asks
for it (see `unseenet.announce`):

```bash
sudo -u unseenet bash -c 'cd ~/unseenet && git pull && .venv/bin/pip install -q -e .'
sudo systemctl restart unseenet-registrar
```

A replica that decides differently for a while does no lasting harm: when
it sees that another replica's certificate wins, it signs that decision
too (UN-RFC 0019 section 6.8, rule 4).

## A spare replica

Because a replica keeps nothing of its own, a spare costs nothing but a
vault in a safe place:

1. Make a vault with a new registrar key of its own and the inbox key's
   seed, with `init`, on any machine.
2. Keep the vault and its passphrase with the project's backups - not on
   a running replica - and note its registrar key. Don't list the key yet.
3. When the replicas are gone - machines seized, a provider closed -
   install a new machine, copy the vault there, have the owner list its
   key, and start it. It rebuilds what it knows from the group and the
   claim inbox and carries on.

A spare must have a key of its own: never start a copy of a vault that is
already running elsewhere. When the inbox key is changed, make the spare
again with the new seed.

## Moving a replica

A replica's vault holds its registrar key, so moving the vault moves the
replica: its key stays the same, and the group's owner changes nothing.

1. Install the new machine (step 1 above), but do not start the service.
2. **Stop the old replica first**, so the same key never runs in two
   places: `sudo systemctl disable --now unseenet-registrar`.
3. Copy `/home/unseenet/registrar.vault*` (owner `unseenet`, mode `600`)
   and `/etc/unseenet-registrar.passphrase` (owner root, mode `600`) to
   the new machine, for example as a tar stream over ssh, and check that
   the vault's `sha256sum` matches.
4. Start it: `sudo systemctl enable --now unseenet-registrar`. The journal
   prints the same `registrar ed25519:...` key as before.

The Tor data does not need to move; the replica starts a new one.

## The project's replicas

| Replica | Where |
|---------|-------|
| registrar1 | the maintainer's Proxmox, Denmark |
| registrar2 | Oracle Cloud Always Free (VM.Standard.E2.1.Micro) |

They run on different infrastructure, so one machine, power cut or
network going down leaves the other giving out names.

## If a key is stolen

- **A registrar key:** the owner removes it with `setup_registrar.py
  --remove`. Its certificates stop counting; the same decisions, signed by
  the other replicas, stay valid.
- **The inbox key:** it opens claims, which say little that the
  certificates do not. The owner makes a new one; for now that means
  removing `registrar_inbox` from the owner vault and running
  `setup_registrar.py` again, then giving every replica the new seed.

## Where this is going

Today the owner of the registrar's group - the project key - decides which
replicas are trusted, so that one key is the registrar's weak point. The
aim is a registrar that runs by itself: a group owned by a **council** of
the replicas' keys, which admits a new replica once it has run as a
shadow for a while and made the same decisions, and removes one that
decides on its own - with no single key, the project's included, able to
change who the replicas are. See
[unseenet#683](https://github.com/unseenet/unseenet/issues/683).
