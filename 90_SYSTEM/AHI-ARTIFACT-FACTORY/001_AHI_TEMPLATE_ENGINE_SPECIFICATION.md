# 001. AHI Template Engine Specification

| Item        | Value                                                                     |
| ----------- | ------------------------------------------------------------------------- |
| Document ID | AHI-AF-001                                                                |
| Version     | 1.0.0                                                                     |
| Status      | Artifact                                                                  |
| Type        | System Specification                                                      |
| Parent      | 000_AHI_ARTIFACT_FACTORY_SPECIFICATION.md                                 |
| Repository  | AHI-Workspace                                                             |
| Path        | `90_SYSTEM/AHI-ARTIFACT-FACTORY/001_AHI_TEMPLATE_ENGINE_SPECIFICATION.md` |
| Related     | 000_AHI_ARTIFACT_FACTORY_SPECIFICATION.md                                 |
| Related     | 000_AHI_SPECIFICATION_TEMPLATE.md                                         |
| Related     | 000_AHI_ARCHITECTURE_TEMPLATE.md                                          |
| Related     | 000_AHI_WORKFLOW_TEMPLATE.md                                              |
| Related     | 000_AHI_SKILL_TEMPLATE.md                                                 |
| Related     | 000_AHI_RUNTIME_TEMPLATE.md                                               |
| Related     | 000_AHI_API_TEMPLATE.md                                                   |

---

# 1. Purpose

AHI Template Engine defines the template generation system of AHI Artifact Factory.

The purpose is to transform AHI development from:

```
Manual Document Creation
```

into:

```
Specification Driven Artifact Generation
```

AHI Template Engine provides standardized templates for:

* Specification;
* Architecture;
* Workflow;
* Skill;
* Runtime;
* API;
* Protocol;
* Service;
* Component;
* Artifact.

---

# 2. Inheritance

AHI Template Engine inherits from:

* AHI Constitution.
* AHI Protocol Specification.
* AHI Artifact Factory Specification.

Principles inherited:

* Constitution First.
* Inheritance First.
* Artifact First.
* Think Twice, Write Once.
* Evolution First.
* One Meaning, Many Representations.

---

# 3. Mission

AHI Template Engine ensures every Artifact in AHI ecosystem has:

* consistent structure;
* inheritance information;
* version control;
* lifecycle status;
* validation capability;
* evolution capability.

The goal:

```
Knowledge

↓

Template

↓

Artifact

↓

Implementation

↓

Evolution
```

---

# 4. Core Principle

AHI Template Engine follows:

```
One Template

↓

Many Artifacts

↓

Continuous Evolution
```

A template is not only a document format.

A template is a reusable knowledge pattern.

---

# 5. Template Architecture

AHI Template Engine consists of:

```
AHI Template Engine

├── Metadata Template
├── Specification Template
├── Architecture Template
├── Workflow Template
├── Skill Template
├── Runtime Template
├── API Template
├── Protocol Template
├── Service Template
├── Component Template
└── Evolution Template
```

---

# 6. Template Metadata Standard

Every template must define:

```yaml
Document ID:
Version:
Status:
Type:
Parent:
Related:
Repository:
Path:
Author:
Created:
Updated:
Evolution History:
```

Purpose:

* preserve lineage;
* support automation;
* support AHI-V validation.

---

# 7. Template Lifecycle

Every template follows:

```
Idea

↓

Proposal

↓

Discussion

↓

Approved

↓

Template Artifact

↓

Factory Usage

↓

Evolution
```

A template cannot become official without approval.

---

# 8. Artifact Generation Flow

AHI Template Engine operates:

```
Specification

↓

Select Template

↓

Fill Metadata

↓

Generate Artifact

↓

Validate Structure

↓

Commit GitHub

↓

Evolution Tracking
```

---

# 9. Template Inheritance Model

Templates inherit from higher-level templates.

Example:

```
AHI Specification Template

        ↓

AHI Architecture Template

        ↓

AHI Runtime Template

        ↓

AHI Implementation Artifact
```

Every generated artifact must preserve:

* parent relationship;
* dependency relationship;
* evolution history.

---

# 10. AHI-V Integration

AHI-V validates generated artifacts:

* metadata correctness;
* inheritance correctness;
* dependency consistency;
* Constitution compliance;
* duplicate detection;
* evolution compatibility.

Validation flow:

```
Template

↓

Generated Artifact

↓

AHI-V

↓

Approved Artifact
```

---

# 11. AHI-Factory Integration

AHI Template Engine is a core module of AHI-Factory.

Relationship:

```
AHI-Factory

├── Template Engine
├── Artifact Generator
├── Validator Interface
├── Version Manager
└── Evolution Manager
```

---

# 12. Multi-Representation Support

Following:

```
One Meaning

↓

Many Representations
```

A template may generate:

* Markdown;
* JSON;
* YAML;
* Database schema;
* API specification;
* Code skeleton;
* Runtime configuration.

---

# 13. AI Readability Requirement

Every template must be designed for:

* Human reading;
* AI understanding;
* Machine processing;
* Automatic validation;
* Future evolution.

Templates should minimize ambiguity.

---

# 14. Current Best Version Principle

Templates are evolved using:

```
Existing Template

↓

Review

↓

Extension

↓

Validation

↓

Current Best Version
```

Do not replace templates without preserving previous lineage.

---

# 15. Future Extensions

Future modules:

* AHI Template Compiler.
* AHI Template Validator.
* AHI Template Marketplace.
* AHI Auto Documentation Generator.
* AHI Multi-language Template Generator.
* AHI Template Evolution Engine.

---

# Status

```
ARTIFACT
```

Version:

```
1.0.0
```

Evolution Principle:

```
Template Once

↓

Generate Many

↓

Validate Always

↓

Evolve Continuously
```
