# 000. AHI Skill Template

| Item | Value |
|---|---|
| Template ID | AHI-TPL-SKILL-000 |
| Version | 1.0.0 |
| Status | Artifact |
| Type | Skill Template |
| Parent | 000_AHI_ARTIFACT_TEMPLATE.md |
| Related | 000_AHI_WORKFLOW_TEMPLATE.md |
| Related | 000_AHI_ARCHITECTURE_TEMPLATE.md |
| Related | 000_AHI_SPECIFICATION_TEMPLATE.md |

---

# 1. Purpose

This template defines the standard structure for every AHI Skill.

A Skill is the smallest reusable executable knowledge unit within the AHI ecosystem.

A Skill encapsulates a stable capability that can be inherited, executed, validated, evolved and reused.

---

# 2. Inheritance

Every Skill shall inherit:

- AHI Constitution
- Related Workflow
- Related Architecture
- Related Specification
- Existing approved Skill (if any)

Inheritance must always be recorded.

---

# 3. Metadata

| Item | Value |
|---|---|
| Skill ID | |
| Name | |
| Version | |
| Status | Proposal / Discussing / Approved / Artifact / Implemented / Deprecated |
| Type | Skill |
| Parent | |
| Related | |

---

# 4. Purpose

Describe:

- capability;
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

# 6. Trigger

Describe when the Skill should execute.

Possible triggers include:

- Human request
- Workflow step
- Event
- Schedule
- External system
- Validation request
- AI decision

---

# 7. Inputs

Examples:

- User request
- Context
- Memory
- Artifact
- Specification
- Repository
- Parameters

---

# 8. Preconditions

Conditions required before execution.

Examples:

- Constitution loaded
- Dependency satisfied
- Permission granted
- Required Artifact available
- Context synchronized

---

# 9. Execution

Describe execution logic.

Typical flow:

```
Receive Input

↓

Load Context

↓

Validate

↓

Execute

↓

Generate Output

↓

Validate Output

↓

Return Result
```

---

# 10. Outputs

Examples:

- Artifact
- Specification
- Workflow
- Commit Message
- Validation Report
- Knowledge

---

# 11. Dependencies

List:

Direct dependencies

Indirect dependencies

Optional dependencies

Future dependencies

---

# 12. Validation

AHI-V validates:

- constitutional compliance;
- dependency correctness;
- execution consistency;
- output quality;
- evolution compatibility.

---

# 13. Evolution

A Skill evolves by:

- improving capability;
- reducing repetition;
- increasing automation;
- preserving compatibility;
- recording lineage.

A newer Skill should inherit rather than replace an existing Skill whenever possible.

---

# 14. Reusability

Every Skill should be reusable by:

- Human
- AHI-P
- AHI-Or
- AHI-Factory
- AHI-CHATGPT
- Future AHI entities

---

# 15. Automation Readiness

Execution levels:

```
Manual

↓

Human Assisted

↓

Hybrid

↓

Automatic

↓

Self-Evolving
```

---

# 16. Checklist

Before approval:

- [ ] Purpose defined
- [ ] Scope defined
- [ ] Trigger defined
- [ ] Inputs documented
- [ ] Preconditions defined
- [ ] Execution described
- [ ] Outputs documented
- [ ] Dependencies listed
- [ ] Validation defined
- [ ] Automation readiness documented
- [ ] Compatible with Constitution

---

# Current Best Version Principle

A Skill should:

- solve one capability well;
- be executable by AI;
- be understandable by humans;
- be reusable across repositories;
- evolve through inheritance;
- become part of the AHI Skill Library.

---

**End of Document**
