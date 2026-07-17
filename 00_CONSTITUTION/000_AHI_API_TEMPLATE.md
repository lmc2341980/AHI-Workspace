# 000. AHI API Template

| Item | Value |
|---|---|
| Template ID | AHI-TPL-API-000 |
| Version | 1.0.0 |
| Status | Artifact |
| Type | API Template |
| Parent | 000_AHI_ARTIFACT_TEMPLATE.md |
| Related | 000_AHI_RUNTIME_TEMPLATE.md |
| Related | 000_AHI_SKILL_TEMPLATE.md |
| Related | 000_AHI_SPECIFICATION_TEMPLATE.md |

---

# 1. Purpose

This template defines the standard structure for every API Artifact in the AHI ecosystem.

An API exposes standardized capabilities that allow Humans, AHI entities, external systems and devices to communicate through the AHI Protocol.

---

# 2. Inheritance

Every API shall inherit:

- AHI Constitution
- Related Specification
- Related Architecture
- Related Runtime
- Related Skill

Inheritance shall always be documented.

---

# 3. Metadata

| Item | Value |
|---|---|
| API ID | |
| Version | |
| Status | Proposal / Discussing / Approved / Artifact / Implemented / Deprecated |
| Type | API |
| Parent | |
| Related | |

---

# 4. Purpose

Describe:

- capability exposed;
- business value;
- intended consumers.

---

# 5. Scope

Define:

Included

Excluded

Dependencies

Boundary

---

# 6. Design Principles

Every API follows:

- Constitution First
- Human Ownership
- AHI-PS Compatible
- Backward Compatible
- Versioned
- Traceable
- Evolvable

---

# 7. Interface

Describe:

API Name

Purpose

Input

Output

Execution Flow

Permissions

Errors

---

# 8. Request Model

Define:

- request schema;
- required fields;
- optional fields;
- validation rules.

---

# 9. Response Model

Define:

- success response;
- warning response;
- error response;
- validation response.

---

# 10. Authentication

Possible methods:

- Human Approval
- AHI Identity
- Token
- Certificate
- Future Identity Mechanisms

Authentication shall never violate the AHI Constitution.

---

# 11. Authorization

Describe:

- permissions;
- ownership;
- access scope;
- constitutional constraints.

---

# 12. Error Handling

Every API shall define:

- validation failure;
- dependency failure;
- permission denied;
- missing resource;
- constitutional violation.

---

# 13. Versioning

API versions evolve through inheritance.

Older versions remain traceable.

Breaking changes shall be explicitly documented.

---

# 14. Validation

AHI-V validates:

- interface consistency;
- dependency correctness;
- constitutional compliance;
- backward compatibility.

---

# 15. Evolution

API evolves by:

- expanding capabilities;
- improving compatibility;
- preserving history;
- reducing breaking changes.

---

# 16. Checklist

Before approval:

- [ ] Purpose defined
- [ ] Scope defined
- [ ] Request documented
- [ ] Response documented
- [ ] Authentication defined
- [ ] Authorization defined
- [ ] Errors documented
- [ ] Validation defined
- [ ] Versioning defined
- [ ] Compatible with Constitution

---

# Current Best Version Principle

Every API should:

- be understandable by humans;
- be executable by AI;
- be reusable across repositories;
- support automatic generation by AHI-Factory;
- support automatic verification by AHI-V.

---

**End of Document**
