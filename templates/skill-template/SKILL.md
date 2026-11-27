---
# 必填：与所在目录名 skills/TTT-<Name>-skill/ 完全一致（固定 TTT- 前缀 + -skill 后缀）
name: TTT-<Name>-skill
# 必填：同时写清「做什么」与「何时触发 / 何时不触发」
description: <One-sentence summary of what this skill produces or does>. Use when <specific trigger scenarios and user intents>. Do NOT use when <out-of-scope scenarios>.
---

# <Skill Title> (`TTT-<Name>-skill`)

<!-- 一句话说明本技能的目标、风格定位或核心价值 -->

## Core Principles

<!-- 3–5 条不可妥协的设计原则、风格约束或技术标准 -->
1. **<Principle 1>**: <Concrete, verifiable rule>.
2. **<Principle 2>**: <Concrete, verifiable rule>.

## Workflow

<!-- 按执行顺序写出 Agent 必须遵循的步骤；有参考模板或脚本时用相对路径指明 -->
1. Read `references/<template-or-spec>` before authoring.
2. <Gather required inputs / inspect target files>.
3. <Execute the core task>.
4. <Verify output against the Quality Checklist below>.

## Pitfalls & Constraints

<!-- 列出常见踩坑点与明确禁止的做法 -->
- Do NOT <common mistake>.
- Always <required safeguard>.

## Quality Checklist

<!-- 交付前逐项自查，全部通过后再结束任务 -->
- [ ] <Verifiable check 1>
- [ ] <Verifiable check 2>
- [ ] <No temporary/artifact files left behind>
