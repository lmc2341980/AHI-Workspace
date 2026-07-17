id: AHI-METADATA-SPEC-0001
name: AHI Artifact Metadata Specification
type: Specification
status: Proposal
version: 0.1.0
owner: AHI-LeMinhCong
created: 2026-07-17
updated: 2026-07-17

parent:

dependencies:

tags:
  - AHI
  - Metadata
  - Artifact
---

# AHI Artifact Metadata Specification

## Purpose

Define the metadata standard for AHI Artifacts.

Metadata provides a common structure so humans and AI systems can understand, manage, inherit, and evolve AHI Artifacts.

---

# Metadata Concept

Each AHI Artifact should contain metadata at the beginning of the Markdown file.

Metadata acts as the identity information of an Artifact.

Example:

```yaml
---
id: AHI-ARTIFACT-0001
name: Example Artifact
type: Artifact
status: Proposal
version: 0.1.0
owner: AHI-LeMinhComg
---
````

---

# Required Fields

## id

Unique identifier of the Artifact.

Purpose:

* Identify the Artifact.
* Allow AI systems to reference the exact Artifact.
* Preserve identity during evolution.

Rules:

* Must be unique.
* Must not be reused.
* Should remain unchanged during updates.

Example:

```yaml
id: AHI-CHATGPT-IDENTITY-0001
```

---

## name

Human-readable Artifact name.

Purpose:

* Allow humans to understand the Artifact.

Example:

```yaml
name: AHI-CHATGPT Identity
```

---

## type

Defines the Artifact category.

Purpose:

* Allow AI systems to understand the role of the Artifact.

Initial supported types:

```text
Constitution
Specification
Skill
Workflow
Artifact
Knowledge
Identity
```

Example:

```yaml
type: Specification
```

---

## status

Defines the lifecycle state of the Artifact.

Purpose:

* Prevent AI from treating unfinished ideas as official knowledge.

Lifecycle:

```text
Proposal
    ↓
Discussing
    ↓
Approved
    ↓
Artifact
    ↓
Implemented
    ↓
Deprecated
```

Example:

```yaml
status: Proposal
```

---

## version

Defines Artifact version.

Format:

```text
Major.Minor.Patch
```

Example:

```yaml
version: 0.1.0
```

Meaning:

* Major: major architectural change.
* Minor: new capability or extension.
* Patch: correction or small improvement.

---

## owner

Defines the responsible owner of the Artifact.

Purpose:

* Preserve human ownership.
* Identify who has final decision authority.

Example:

```yaml
owner: AHI-LeMinhCong
```

---

# Optional Fields

## parent

Defines inheritance relationship.

Example:

```yaml
parent:
  - AHI-FOUNDATION-0001
```

---

## dependencies

Defines required related Artifacts.

Example:

```yaml
dependencies:
  - AHI-SPEC-0001
```

---

## tags

Defines search keywords.

Example:

```yaml
tags:
  - AI
  - Memory
  - Knowledge
```

---

# AI Processing Rules

AI systems working with AHI Artifacts should:

1. Read metadata before content.
2. Respect Artifact status.
3. Never treat Proposal as final knowledge.
4. Preserve Artifact identity.
5. Follow inheritance and dependency relationships.
6. Support continuous evolution.

---

# Repository Integration

AHI Repository Indexer will extract metadata fields:

* id
* name
* type
* status
* version
* owner
* parent
* dependencies
* tags

and generate machine-readable indexes:

```text
artifact.json

metadata.json

dependency.json
```

---

# Design Principle

## One Meaning - Many Representations

Human representation:

```text
Markdown Artifact
```

Machine representation:

```text
JSON Metadata
```

AI representation:

```text
Knowledge Graph
```

All representations must preserve the same Artifact identity.
