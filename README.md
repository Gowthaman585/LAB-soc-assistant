# LOG-HERALD

> **Not everything that happened. Only what changed.**


A lightweight tool that reads a Linux machine's logs and tells you, in plain language, what is **new or unusual** each day.

> ❗ **Project status: early development and testing.**
> This repository is being rebuilt around a new idea. The sections below describe what is being built, why, and what is being tested. Nothing here is a finished release yet, and details may change.

> Looking for the earlier SOC Assistant Lab scripts? See below ⬇️

## Overview

Every Linux machine keeps logs: a record of each login, failed password, crash and restart. A small server can write thousands of lines a day, and almost nobody reads them. When something unusual happens, it gets buried in the noise.

This project aims to read those logs for you and surface only what matters.

## How it is designed to work

1. **Learn what is normal.** Observe a machine's logs for a few days and remember its usual activity: regular logins, routine restarts, common warnings.
2. **Spot what is new.** Compare each new day against that baseline and pick out anything unfamiliar.
3. **Report in plain language.** Produce a short summary a non-expert can read in under a minute, with routine activity collapsed into simple counts.

## How is this different?

Several good tools already help with Linux logs. This project is an experiment in a simpler approach to the same problem.

| Existing approach | How it works | What this project does differently |
|---|---|---|
| **Logwatch** | Summarizes a period's logs into a daily report using per-service parsing scripts, usually sent by email. | Reports only what is new compared with the machine's own normal, instead of summarizing everything. |
| **Logcheck** | Scans logs on a schedule (hourly by default) and emails any lines not matched by its ignore rules. What counts as "unusual" is defined by pattern rules that usually need customizing for each machine. | Learns what is normal automatically from the machine itself, so there are no ignore rules to write and maintain. |
| **Full log platforms** (for example Logatory, Wazuh) | Broad feature sets: many log sources, dashboards, rule libraries, and agents or central servers. | Deliberately small: one machine, one short summary, minimal setup. |

> **A fair note:** some of these tools include their own anomaly-detection features. This project does not claim to do something nobody else can. It is testing whether a narrower, simpler experience is easier to live with.

## What is being tested

Because the project is in its testing phase, these are the questions it is trying to answer:

1. **Is "what's new" more useful than "what happened"?** Does a digest limited to new or unusual activity actually get read, compared with a full summary?
2. **Can "normal" be learned automatically?** Can a few days of observation replace hand-written rules, and how many digest items turn out to be genuinely useful rather than noise?
3. **Is it simple enough to keep running?** How long does setup take, and is it still running a week later?

## Goals

- **Built for a single machine.** Suited to a personal server, home lab or student lab, with no cloud account or large log platform required.
- **Easy to read.** Short, plain-language output instead of raw log lines.
- **Easy to set up.** Quick to install and quick to try.
- **Private by design.** Analysis runs locally on your own machine.
- **Starting with common sources.** SSH and authentication logs first, followed by system service logs.

## Roadmap

- [ ] Read authentication and system service logs
- [ ] Build a baseline of normal activity
- [ ] Detect what is new compared with the baseline
- [ ] Generate a short plain-language daily summary
- [ ] Deliver the summary by email or chat message
- [ ] Simple installation

## Legacy version (v1.0.0)

This repository previously contained **SOC Assistant Lab**, a set of small Python command-line tools for analysing specific kinds of log lines (sudo activity, SSH login abuse and file access by user).

That version is **deprecated and no longer maintained**.

- Documentation: [`docs/v1_0_0_documentation.md`](docs/v1_0_0_documentation.md)
- Source at that release: [`v1.0.0` tag](https://github.com/Gowthaman585/LAB-soc-assistant/releases/tag/v1.0.0)

## Feedback

This project is shaped by real-world use, so feedback is the most helpful contribution right now. Please open an issue and share:

- how you currently deal with your server logs,
- what you find most frustrating about it,
- which Linux distribution and log sources you use (please remove usernames, IP addresses and other private data first).
