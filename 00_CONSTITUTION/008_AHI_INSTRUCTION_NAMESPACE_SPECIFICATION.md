# 008. AHI Instruction Namespace Specification

| Item | Value |
|------|-------|
| Document ID | AHI-INS-008 |
| Version | 1.0.0 |
| Status | Draft |
| Type | Root Specification |
| Parent | 007_AHI_INSTRUCTION_SET_ARCHITECTURE.md |

---

# 1. Purpose

AHI Instruction Namespace (AHI-INS) định nghĩa không gian tên (Namespace) của toàn bộ Instruction trong hệ sinh thái Artificial Hybrid Intelligence.

Namespace giúp:

- tránh trùng lặp;
- mở rộng không giới hạn;
- chuẩn hóa Runtime;
- chuẩn hóa Robot;
- chuẩn hóa AI;
- chuẩn hóa Compiler;
- chuẩn hóa Brain Interface.

---

# 2. Design Principle

Instruction

↓

Namespace

↓

Opcode

↓

Runtime

↓

Execution

Opcode không được định nghĩa trực tiếp từ Instruction.

Opcode luôn được ánh xạ từ Namespace.

---

# 3. Namespace Hierarchy

ROOT

├── CORE

├── GITHUB

├── WORKSPACE

├── CONSTITUTION

├── SPECIFICATION

├── ARCHITECTURE

├── SKILL

├── ARTIFACT

├── KNOWLEDGE

├── MEMORY

├── LANGUAGE

├── ORCHESTRATOR

├── FACTORY

├── SUCCESSOR

├── OM

├── DEVICE

├── ROBOT

├── COMPUTER_VISION

├── BRAIN_INTERFACE

└── FUTURE

Namespace có thể mở rộng vô hạn.

---

# 4. CORE Namespace

Ví dụ:

CORE.CR

CORE.EV

CORE.RV

CORE.CMP

CORE.N

CORE.C

CORE.D

CORE.CUR

---

# 5. GitHub Namespace

GITHUB.PUSH

GITHUB.PULL

GITHUB.READ

GITHUB.WRITE

GITHUB.COMMIT

GITHUB.TAG

GITHUB.RELEASE

---

# 6. Skill Namespace

SKILL.CREATE

SKILL.READ

SKILL.UPDATE

SKILL.DELETE

SKILL.EXPORT

SKILL.IMPORT

SKILL.VALIDATE

---

# 7. Specification Namespace

SPEC.CREATE

SPEC.UPDATE

SPEC.REVIEW

SPEC.COMPARE

SPEC.EVOLVE

---

# 8. Artifact Namespace

ART.CREATE

ART.UPDATE

ART.READ

ART.EVOLVE

ART.VERSION

---

# 9. Workspace Namespace

WS.OPEN

WS.SCAN

WS.READ

WS.WRITE

WS.SYNC

---

# 10. Future Namespace

Các Namespace mới sẽ được bổ sung khi AHI tiến hóa.

Ví dụ:

ENERGY

BIOLOGY

QUANTUM

SWARM

SPACE

DIGITAL_TWIN

METAVERSE

Không giới hạn.

---

# 11. Naming Rules

Tên Namespace:

- UPPER_CASE
- tiếng Anh
- ngắn
- rõ nghĩa
- ổn định

Instruction:

VERB

hoặc

VERB.NOUN

Ví dụ:

CREATE

READ

WRITE

EXPORT

IMPORT

SYNC

VALIDATE

---

# 12. Evolution Principle

Namespace phải:

- tương thích ngược;
- không đổi tên tùy tiện;
- ưu tiên mở rộng;
- ưu tiên kế thừa;
- tránh trùng ngữ nghĩa.

---

# 13. Human Interaction

Con người không cần nhớ Namespace đầy đủ.

Ví dụ:

AHI+ CR

↓

CORE.CREATE

↓

Opcode

↓

Runtime

↓

Execution

AHI tự động ánh xạ.

---

# 14. Long-term Vision

Trong tương lai:

Natural Language

↓

Voice

↓

Computer Vision

↓

Brain Interface

↓

Intent

↓

Namespace

↓

Opcode

↓

Runtime

↓

Execution

Namespace trở thành lớp ngữ nghĩa ổn định giữa con người và máy.

---

End of Document
