# 007. AHI Service Protocol Specification (AHI-SP)

| Item | Value |
|---|---|
| Document ID | AHI-SP-007 |
| Version | 1.0.0 |
| Status | Artifact |
| Type | Root Specification |
| Parent | 001_AHI_CONSTITUTION_EVOLUTION_SPECIFICATION.md |
| Related | 002_AHI_PROTOCOL_SPECIFICATION.md |
| Related | 005_AHI_ORCHESTRATOR_SPECIFICATION.md |
| Related | 006_AHI_LANG_SPECIFICATION.md |

---

# 1. Purpose

AHI Service Protocol (AHI-SP) defines the standard service model of the AHI ecosystem.

AHI-SP standardizes how capabilities are exposed, discovered, executed, validated and evolved.

AHI-SP is independent of implementation technology.

---

# 2. Mission

AHI-SP provides one unified service model for:

- Human
- AHI-P
- AHI-G
- AHI-O
- AHI-Or
- AHI-V
- AHI-Factory
- AHI-Successor
- Devices
- Robots
- External AI
- Future AHI entities

---

# 3. Position in AHI

```
Human

↓

AHI Constitution

↓

AHI-PS

↓

AHI-SP

↓

AHI API

↓

Runtime

↓

Execution
```

AHI-PS defines communication.

AHI-SP defines services.

AHI API exposes services.

Runtime executes services.

---

# 4. Relationship with AHI-PS

AHI-PS defines:

- protocol;
- governance;
- permissions;
- routing;
- lifecycle.

AHI-SP defines:

- service;
- capability;
- interface;
- dependency;
- execution contract.

---

# 5. Relationship with AHI-Lang

AHI-Lang provides semantic representation.

AHI-SP provides executable capability.

```
Meaning

↓

AHI-Lang

↓

AHI-SP

↓

Executable Service
```

---

# 6. Relationship with MCP

AHI-SP does not replace MCP.

MCP is treated as an interoperability protocol.

Architecture:

```
External AI

↓

MCP

↓

AHI Adapter

↓

AHI-PS

↓

AHI-SP

↓

AHI API

↓

Runtime
```

AHI-SP remains implementation independent.

---

# 7. Service Definition

Every service shall define:

- Service Identity
- Purpose
- Inputs
- Outputs
- Preconditions
- Postconditions
- Dependencies
- Permissions
- Validation
- Evolution

---

# 8. Service Lifecycle

```
Design

↓

Validation

↓

Approval

↓

Artifact

↓

Implementation

↓

Execution

↓

Evolution

↓

Deprecation
```

---

# 9. Service Categories

Examples:

- Knowledge Service
- Memory Service
- Identity Service
- Permission Service
- Device Service
- AI Provider Service
- Semantic Search Service
- Workflow Service
- Skill Service
- Runtime Service

---

# 10. Service Execution

```
Request

↓

Validation

↓

Authorization

↓

Runtime

↓

Execution

↓

Validation

↓

Response

↓

Evolution Record
```

---

# 11. Validation

AHI-V validates:

- constitutional compliance;
- protocol compatibility;
- service compatibility;
- dependency integrity;
- execution correctness.

---

# 12. Evolution

AHI-SP evolves through:

- capability expansion;
- service refinement;
- compatibility preservation;
- inheritance.

Breaking changes shall be explicitly documented.

---

# 13. Future Extensions

Future specifications may include:

```
010_AHI_SERVICE_ARCHITECTURE.md

020_AHI_SERVICE_INTERACTION.md

030_AHI_SERVICE_DISCOVERY.md

040_AHI_SERVICE_RUNTIME.md

050_AHI_SERVICE_REGISTRY.md

060_AHI_SERVICE_VERSIONING.md

070_AHI_SERVICE_VALIDATION.md

080_AHI_SERVICE_EXAMPLES.md

090_AHI_SERVICE_APPENDIX.md
```

---

# Status

```
ARTIFACT
```

Version

```
1.0.0
```

Core Principle

```
One Capability

↓

One Service

↓

Many Implementations
```

---

**End of Document**
