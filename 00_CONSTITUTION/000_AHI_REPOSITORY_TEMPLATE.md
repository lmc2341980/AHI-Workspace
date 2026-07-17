# 000. AHI Root Repository Template

| Item | Value |
|---|---|
| Repository Type | Root Template |
| Version | 1.0.0 |
| Status | Artifact |
| Owner | AHI-LeMinhCong |
| Parent | 000_AHI_ARTIFACT_TEMPLATE.md |

---

# 1. Purpose

This template defines the standard structure of every repository in the AHI ecosystem.

Every repository shall inherit this template before defining its own structure.

GitHub Repository is the Source of Truth.

---

# 2. Mission

Provide a unified repository architecture that is:

- understandable by humans;
- executable by AI;
- evolvable over time;
- automatically verifiable;
- reusable across the AHI ecosystem.

---

# 3. Repository Principles

Every repository follows:

- Constitution First
- Inheritance First
- Artifact First
- Copy First
- Think Twice, Write Once
- Evolution First
- Human Ownership
- One Meaning, Many Representations

---

# 4. Standard Repository Structure

```
Repository

├── README.md
├── LICENSE
├── .github/
├── docs/
├── artifacts/
├── skills/
├── specifications/
├── architecture/
├── runtime/
├── workflows/
├── templates/
└── tools/
```

A repository may simplify this structure, but shall preserve its intent.

---

# 5. Repository Responsibilities

Every repository shall clearly define:

- Purpose
- Scope
- Dependencies
- Owner
- Artifact hierarchy
- Evolution policy

---

# 6. Required Documents

Minimum required documents:

- README.md
- LICENSE
- Artifact Index
- Changelog
- Dependency description

---

# 7. Artifact Organization

Artifacts should be organized by responsibility rather than chronology.

Example:

```
00_CONSTITUTION/
10_ARCHITECTURE/
20_SPECIFICATIONS/
30_SKILLS/
40_WORKFLOWS/
90_IDENTITIES/
```

---

# 8. Repository Lifecycle

```
Proposal

↓

Repository Creation

↓

Initial Artifact

↓

Evolution

↓

Validation

↓

Stable Release

↓

Continuous Evolution
```

---

# 9. Validation

AHI-V validates:

- structure;
- dependencies;
- inheritance;
- naming;
- document completeness;
- constitutional compliance.

---

# 10. Evolution

Repositories evolve by:

- adding Artifacts;
- evolving existing Artifacts;
- preserving history;
- maintaining compatibility.

Repositories shall not rewrite history without explicit approval.

---

# 11. Relationship with AHI-Factory

Repositories are inputs to AHI-Factory.

AHI-Factory may automatically generate:

- documents;
- skills;
- implementations;
- APIs;
- tests;
- validation reports.

---

# 12. Current Best Version Principle

Every repository should be designed as if:

- it will live for decades;
- it will be read by humans;
- it will be read by AI;
- it will generate future repositories;
- it will generate future implementations.

---

# Repository Checklist

Before approval:

- [ ] README exists.
- [ ] Purpose defined.
- [ ] Scope defined.
- [ ] Dependency documented.
- [ ] Artifact hierarchy documented.
- [ ] Naming follows standards.
- [ ] Compatible with Constitution.
- [ ] Evolvable.
- [ ] Reusable.
- [ ] Verifiable.

---

**End of Document**
