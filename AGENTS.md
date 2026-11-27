# AGENTS.md — TTTIM-skills 开发规范

本仓库（`Timcai06/TTTIM-skills`）是个人 AI Agent Skills 合集，遵循 [agentskills.io](https://agentskills.io) 开放规范，一次维护、多端兼容（Claude Code、Antigravity / Gemini、Codex、Cursor 等）。

## 目录约定

```text
TTTIM-skills/
├── AGENTS.md                         # 本文件（CLAUDE.md 软链至此）
├── README.md                         # 仓库说明与技能索引表
├── install.sh                        # 本机多 Agent 软链同步脚本
├── .claude-plugin/marketplace.json   # Claude Code 插件市场清单
├── templates/
│   └── skill-template/SKILL.md       # 新建 Skill 标准样板
└── skills/
    └── TTT-<Name>-skill/             # 命名规范：TTT-<Name>-skill，必须与 SKILL.md 的 name 完全一致
        ├── SKILL.md                  # 必填：YAML frontmatter + 执行规范
        ├── references/               # 可选：模板、范例、静态参考资料
        └── scripts/                  # 可选：辅助脚本
```

### 命名与边界规则
- Skill 目录统一放在 `skills/TTT-<Name>-skill/` 下，固定 `TTT-` 前缀 + 大驼峰模块名 + `-skill` 后缀（例如 `TTT-MonoPDF-skill`、`TTT-Readme-skill`）。
- 目录名必须与 `SKILL.md` YAML frontmatter 中的 `name` 字段**完全一致**。
- `SKILL.md` 保持精炼、可执行；大段模板、范例或长参考文档放到 `references/`，在 `SKILL.md` 中按相对路径引用。
- 涉及真实项目的范例放入 `references/` 前应完成脱敏，避免泄露密钥、内网地址或私有敏感信息。

## 新增 / 修改 Skill 标准 5 步检查清单

1. **创建 Skill 目录与文件**
   基于 `templates/skill-template/SKILL.md` 创建 `skills/TTT-<Name>-skill/SKILL.md`，按需补充 `references/` 或 `scripts/`。
2. **写好触发描述（`description`）**
   YAML frontmatter 中的 `description` 必须同时写清：
   - **做什么**（核心能力与产物）；
   - **何时触发 / 何时不触发**（明确适用场景与排除边界，避免误触发）。
3. **同步更新仓库清单**
   - 在 `.claude-plugin/marketplace.json` 的 `plugins[0].skills` 数组中登记 `<name>`；
   - 在根目录 `README.md` 的「技能目录」表格中补充一行说明。
4. **刷新本机多 Agent 软链**
   在仓库根目录执行 `./install.sh`，确保 `~/.agents/skills`、`~/.gemini/config/skills`、`~/.claude/skills`、`~/.codex/skills` 均已同步。
5. **校验并提交推送**
   检查目录名与 `name` 一致、无临时编译/垃圾文件后，执行 `git commit` 并推送到 `origin main`。
