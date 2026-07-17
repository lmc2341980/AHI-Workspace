# 000. AHI Workflow Template

| Item | Value |
|---|---|
| Template ID | AHI-TPL-WF-000 |
| Version | 1.0.0 |
| Status | Artifact |
| Type | Workflow Template |
| Parent | 000_AHI_ARTIFACT_TEMPLATE.md |
| Related | 000_AHI_ARCHITECTURE_TEMPLATE.md |
| Related | 000_AHI_SPECIFICATION_TEMPLATE.md |

---

# 1. Purpose

This template defines the standard structure for every Workflow Artifact in the AHI ecosystem.

A Workflow describes how work is performed from input to output while preserving constitutional compliance, traceability and evolution.

---

# 2. Inheritance

Every Workflow shall inherit:

- AHI Constitution
- Related Architecture
- Related Specification
- Existing approved Workflow

Inheritance must be explicitly documented.

---

# 3. Document Metadata

| Item | Value |
|---|---|
| Document ID | |
| Version | |
| Status | Proposal / Discussing / Approved / Artifact / Implemented / Deprecated |
| Type | Workflow |
| Parent | |
| Related | |

---

# 4. Purpose

Describe:

- objective;
- business value;
- expected outcome.

---

# 5. Scope

Define:

Included

Excluded

Actors

Boundary

Dependencies

---

# 6. Workflow Principles

Every Workflow shall follow:

- Constitution First
- Human Ownership
- Inheritance First
- Artifact First
- Evolution First
- Validation Before Approval

---

# 7. Actors

Describe every participant.

Possible actors include:

- Human
- AHI-P
- AHI-Or
- AHI-V
- AHI-Factory
- AHI-Old
- External AI
- Device
- Robot

---

# 8. Inputs

List all required inputs.

Examples:

- User Request
- Artifact
- Context
- Skill
- Memory
- External Resource

---

# 9. Workflow Steps

Describe the workflow as sequential stages.

Example:

```
Input

↓

Validation

↓

Context Loading

↓

Knowledge Retrieval

↓

Reasoning

↓

Artifact Generation

↓

Validation

↓

Approval

↓

Output
```

Each step should define:

- Purpose
- Input
- Processing
- Output
- Responsible Actor

---

# 10. Outputs

Describe produced outputs.

Examples:

- Artifact
- Specification
- Skill
- Decision
- Validation Report

---

# 11. Exception Handling

Describe:

- missing dependency;
- validation failure;
- constitutional conflict;
- permission denial;
- incomplete context.

Every exception shall have a documented resolution path.

---

# 12. Evolution

Workflow evolves by:

- improving efficiency;
- reducing manual steps;
- increasing automation;
- preserving compatibility;
- maintaining traceability.

---

# 13. Validation

AHI-V validates:

- workflow completeness;
- dependency correctness;
- constitutional compliance;
- execution consistency.

---

# 14. Automation Readiness

Workflow should clearly identify:

- manual steps;
- semi-automatic steps;
- fully automatic steps.

Target:

```
Human Assisted

↓

Hybrid Execution

↓

Automated Execution

↓

Self-Evolving Workflow
```

---

# 15. Checklist

Before approval:

- [ ] Purpose defined
- [ ] Scope defined
- [ ] Actors identified
- [ ] Inputs documented
- [ ] Workflow steps completed
- [ ] Outputs defined
- [ ] Exceptions handled
- [ ] Validation defined
- [ ] Automation readiness documented
- [ ] Compatible with Constitution

---

# Current Best Version Principle

Every Workflow should:

- be understandable by humans;
- be executable by AI;
- be verifiable by AHI-V;
- be reusable by AHI-Factory;
- evolve without breaking inheritance.

---

**End of Document**
