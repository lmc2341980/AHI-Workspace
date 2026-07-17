# AHI Artifact Metadata Specification

## Status

Proposal

## Purpose

Define a common metadata standard for all AHI Artifacts.

The metadata allows humans and AI systems to understand:

* Artifact identity
* Artifact type
* Lifecycle status
* Version
* Ownership
* Dependencies
* Evolution history

## Metadata Location

Metadata is defined at the beginning of each Artifact file using YAML Front Matter.

Example:

```yaml
---
id: AHI-ARTIFACT-0001

name: AHI Artifact Name

type: Artifact

status: Proposal

version: 0.1.0

created: 2026-07-17

updated: 2026-07-17

owner: AHI

parent:

dependencies:

tags:

---
```

---

# Required Fields

## id

Unique identifier of the Artifact.

Example:

```yaml
id: AHI-CHATGPT-IDENTITY-0001
```

Rules:

* Must be unique.
* Never reused.
* Used by AI systems for reference.

---

## name

Human-readable Artifact name.

Example:

```yaml
name: AHI-CHATGPT Identity
```

---

## type

Defines Artifact category.

Allowed initial values:

```yaml
type:
- Constitution
- Specification
- Skill
- Workflow
- Artifact
- Knowledge
- Identity
```

---

## status

Defines lifecycle state.

Allowed values:

```yaml
status:
- Proposal
- Discussing
- Approved
- Artifact
- Implemented
- Deprecated
```

---

## version

Semantic version.

Format:

```
Major.Minor.Patch
```

Example:

```yaml
version: 1.0.0
```

---

## owner

Human or organization responsible for ownership.

Example:

```yaml
owner: AHI-LeMinhCong
```

---

# Optional Fields

## parent

Defines inheritance source.

Example:

```yaml
parent:

- AHI-FOUNDATION-0001
```

---

## dependencies

Defines required Artifacts.

Example:

```yaml
dependencies:

- AHI-SPEC-0001
- AHI-SKILL-0001
```

---

## tags

Used for search and AI retrieval.

Example:

```yaml
tags:

- AHI
- Memory
- AI
```

---

## Evolution History

Optional evolution tracking.

Example:

```yaml
history:

- version: 0.1.0
  date: 2026-07-17
  change: Initial proposal
```

---

# AI Processing Rules

AI systems should:

1. Read metadata before content.
2. Respect status lifecycle.
3. Never treat Proposal as final knowledge.
4. Follow dependencies before modification.
5. Preserve artifact identity during evolution.

---

# Repository Index Integration

AHI Repository Indexer will later extract:

* id
* type
* status
* version
* dependencies
* tags

and generate:

```
90_SYSTEM/AHI-INDEX/

artifact.json

metadata.json

dependency.json
```

---

# Design Principle

One Meaning - Many Representations

Human representation:

Markdown Artifact

Machine representation:

JSON Metadata Index

AI representation:

Knowledge Graph

All representations must refer to the same Artifact identity.
