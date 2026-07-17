# AHI-CHATGPT
## GitHub Standard Specification

**Generation:** G1

**Version:** V1.0.0

**Status:** Approved

**Artifact Type:** GitHub Standard Specification

---

# 1. Purpose

This specification defines the GitHub working standards for AHI-CHATGPT within the AHI ecosystem.

GitHub is the primary Source of Truth for all approved AHI Artifacts.

Every repository, document, specification, workflow, and knowledge artifact shall be managed according to this standard.

---

# 2. Objectives

This specification aims to:

- standardize repository organization;
- preserve Artifact continuity;
- support long-term evolution;
- enable collaboration between humans and AI;
- ensure traceability of every approved Artifact.

---

# 3. Source of Truth

GitHub repositories are the official storage for:

- Constitution
- Specifications
- Artifacts
- Skills
- Knowledge
- Runtime Documents
- Architecture
- Evolution History

Conversation history is temporary.

GitHub Artifacts are authoritative.

---

# 4. Repository Principles

Every repository shall:

- have a clearly defined purpose;
- follow standardized directory structures;
- contain a README;
- maintain version history;
- support continuous evolution;
- comply with the AHI Constitution.

---

# 5. Artifact Principles

Every Artifact shall:

- declare its purpose;
- declare its lifecycle state;
- inherit from previous approved knowledge where applicable;
- remain readable by both humans and AI;
- support future evolution;
- avoid duplicated knowledge.

Artifacts are evolved rather than rewritten.

---

# 6. Directory Standards

Directories should represent logical domains.

Examples:

```text
00_CONSTITUTION/
10_SPECIFICATIONS/
20_PROTOCOLS/
30_SKILLS/
40_RUNTIME/
50_MODELS/
60_LIBRARY/
70_EXAMPLES/
80_VALIDATION/
90_IDENTITIES/
```

Directory names should remain stable over time.

---

# 7. File Naming

File names should:

- use uppercase prefixes for ordering;
- be descriptive;
- remain stable;
- avoid unnecessary renaming.

Examples:

```text
000_IDENTITY.md
001_BOOTSTRAP.md
010_PROTOCOL.md
020_RUNTIME.md
```

---

# 8. Commit Standard

Each commit shall represent one evolutionary step.

Commit Messages become Evolution Signals.

Recommended format:

```text
docs(scope): action artifact
```

Examples:

```text
docs(identity): evolve AHI-CHATGPT Runtime specification

docs(protocol): create AHI-PS Runtime specification

docs(skill): evolve Skill Compiler specification
```

---

# 9. Evolution Rules

No approved Artifact shall be rewritten from scratch.

The standard workflow is:

```text
Read

↓

Inherit

↓

Gap Analysis

↓

Evolution

↓

Validation

↓

Commit

↓

Next Evolution
```

---

# 10. Human–AI Collaboration

AHI-P is responsible for:

- vision;
- approval;
- constitutional direction.

AHI-CHATGPT is responsible for:

- analysis;
- organization;
- drafting;
- evolution;
- validation support.

Human Ownership always has priority.

---

# 11. Repository Context

Before working in a repository, AHI-CHATGPT should receive:

- repository name;
- relative path;
- directory tree;
- existing file list.

Before evolving a file, AHI-CHATGPT should receive:

- current file content;
- Evolution Signal.

---

# 12. Future Evolution

Future versions may define standards for:

- automated repository generation;
- AHI-Factory integration;
- AHI-Or synchronization;
- AHI-V repository validation;
- semantic repository indexing;
- distributed Git repositories;
- AHI-Lang native repository representation.

This specification is governed by the AHI Constitution and evolves through the standard AHI approval process.
