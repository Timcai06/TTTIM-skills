# TTTIM-skills

Timcai06 的个人 AI Agent Skills 合集仓库，遵循 [agentskills.io](https://agentskills.io) 开放规范，兼容 Claude Code、Antigravity / Gemini、Codex、Cursor 等主流 Agent。

## 技能目录

| Skill | 简介 | 目录 |
|---|---|---|
| `TTT-MonoPDF-skill` | 极简黑白瑞士编辑风中英文汇报 PDF 生成技能（XeLaTeX + PingFang SC / Helvetica Neue + TikZ，含逐页视觉自查） | [`skills/TTT-MonoPDF-skill`](./skills/TTT-MonoPDF-skill) |

## 安装方式

### 方式 1：通用 CLI（推荐，跨所有 Agent）
```bash
# 安装全部技能
npx skills add Timcai06/TTTIM-skills -g

# 或只安装指定技能
npx skills add Timcai06/TTTIM-skills --skill TTT-MonoPDF-skill -g
```

### 方式 2：Claude Code 插件市场
```text
/plugin marketplace add Timcai06/TTTIM-skills
```

### 方式 3：本地克隆 + 一键软链（适合本地持续开发同步）
```bash
git clone https://github.com/Timcai06/TTTIM-skills.git ~/DEV/Skill
cd ~/DEV/Skill && chmod +x install.sh && ./install.sh
```

## 目录规范
```text
TTTIM-skills/
├── AGENTS.md                         # Agent 开发规范（CLAUDE.md 软链至此）
├── .claude-plugin/marketplace.json   # Claude Code 市场清单
├── install.sh                        # 本机多 Agent 一键软链脚本
├── templates/skill-template/         # 新建 Skill 空白样板
└── skills/
    └── TTT-<Name>-skill/             # 统一 TTT-xxx-skill 命名，与 SKILL.md 的 name 一致
        ├── SKILL.md                  # 必填：YAML frontmatter + 执行规范
        └── references/               # 可选：模板、脚本、示例
```
