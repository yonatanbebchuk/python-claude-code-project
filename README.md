# SuperClaude - Claude Code Cfg Framework

## Legend
| Symbol | Meaning | | Abbrev | Meaning |
|--------|---------|---|--------|---------|
| → | leads to | | cfg | configuration |
| & | and/with | | fn | function |
| w/ | with | | impl | implementation |
| @ | at/located | | env | environment |
| + | add/include | | dev | development |
| - | remove/exclude | | auth | authentication |
| ∀ | for all/every | | API | application interface |

> Advanced cfg framework for Claude Code | v4.0.0

## What is SuperClaude

**Comprehensive cfg system** enhancing Claude Code w/:
- **CLAUDE.md** → Main cfg + ops  
- **RULES.md** → Governance + practices
- **PERSONAS.md** → 9 cognitive archetypes
- **MCP.md** → Model Context Protocol patterns
- **18 Slash Commands** → Specialized workflows
- **19 Shared Resources** → Advanced cfgs

## Installation

SuperClaude installs globally → `~/.claude/` ∀ projects.

### Directory Structure
```
~/.claude/
├── CLAUDE.md          # Main cfg (loads others)
├── RULES.md           # Ops rules & standards  
├── PERSONAS.md        # 9 cognitive archetypes
├── MCP.md             # Model Context Protocol ops
└── commands/          # 17 specialized slash commands + index
    ├── analyze.md     ├── build.md       ├── cleanup.md
    ├── deploy.md      ├── design.md      ├── dev-setup.md
    ├── document.md    ├── estimate.md    ├── explain.md
    ├── git.md         ├── improve.md     ├── index.md
    ├── load.md        ├── migrate.md     ├── scan.md
    ├── spawn.md       ├── test.md        ├── troubleshoot.md
    └── shared/        # 19 cfg resources
        ├── ambiguity-check.yml    ├── audit.yml
        ├── checkpoint.yml         ├── cleanup-patterns.yml
        ├── command-memory.yml     ├── documentation-dirs.yml
        ├── evidence.yml           ├── git-operations.yml
        ├── git-workflow.yml       ├── impl.yml
        ├── loading-cfg.yml        ├── mcp-flags.yml
        ├── patterns.yml           ├── performance-monitoring.yml
        ├── planning-mode.yml      ├── research-first.yml
        ├── thinking-modes.yml     ├── ultracompressed.yml
        └── validation.yml
```

### Quick Install (Recommended)
```bash
git clone https://github.com/your-username/SuperClaude.git
cd SuperClaude
./install.sh
```

### Manual Install
```bash
# 1. Create structure
mkdir -p ~/.claude/commands/shared

# 2. Copy cfg files
cp CLAUDE.md RULES.md PERSONAS.md MCP.md ~/.claude/

# 3. Copy commands
cp .claude/commands/*.md ~/.claude/commands/

# 4. Copy shared resources  
cp .claude/commands/shared/*.yml ~/.claude/commands/shared/
```

### Verify Installation
```bash
# Check installation
ls -la ~/.claude/          # Should show 4 main files
ls -la ~/.claude/commands/ # Should show 17 files (16 commands + index)

# Test usage
# Open any project in Claude Code & try:
/user:analyze --code
/persona:architect
```

## How to Use SuperClaude

### Core Usage Patterns

#### 1. Personas - Cognitive Archetypes
Activate specialized thinking w/ `/persona:<name>`:

| Persona | Focus | Use When | Example |
|---------|-------|----------|---------|
| **architect** | Systems design, long-term maintainability | Planning large systems | `/persona:architect` → `/user:design --api --ddd` |
| **frontend** | UX, visual interfaces | UI/UX work | `/persona:frontend` → `/user:build --react` |
| **backend** | Performance, reliability, APIs | Server-side dev | `/persona:backend` → `/user:build --api` |
| **analyzer** | Root cause analysis, evidence-based | Debugging complex issues | `/persona:analyzer` → `/user:troubleshoot --investigate` |
| **security** | Threat modeling, secure by default | Security reviews | `/persona:security` → `/user:scan --security` |
| **mentor** | Teaching, guided discovery | Learning/explaining | `/persona:mentor` → `/user:explain --depth` |
| **refactorer** | Code quality, simplification | Code improvement | `/persona:refactorer` → `/user:improve --quality` |
| **performance** | Speed optimization, bottlenecks | Performance tuning | `/persona:performance` → `/user:improve --performance` |
| **qa** | Quality assurance, testing | Testing workflows | `/persona:qa` → `/user:test --coverage` |

#### 2. Slash Commands - Specialized Workflows

**Universal Flags (∀ commands):**

*Planning & Thinking:*
- `--plan` - Show execution plan before running
- `--think` - Standard analysis mode (multi-file context)
- `--think-hard` - Deep analysis mode (architecture level)
- `--ultrathink` - Critical analysis mode (system-wide)

*Documentation Control:*
- `--ultracompressed` / `--uc` - ~70% token reduction mode

*MCP Server Control:*
- `--c7` / `--no-c7` - Enable/disable Context7 documentation
- `--seq` / `--no-seq` - Enable/disable Sequential thinking
- `--magic` / `--no-magic` - Enable/disable Magic UI builder
- `--pup` / `--no-pup` - Enable/disable Puppeteer browser
- `--all-mcp` - Enable all MCP servers
- `--no-mcp` - Disable all MCP servers (native tools only)

**Dev Commands (3):**
- `/user:build` - Universal project builder
  - `--init` (new project), `--feature` (add feature), `--react` (React app), `--api` (backend), `--tdd` (test-driven)
- `/user:dev-setup` - Dev env setup  
  - `--install` (tools), `--ci` (CI/CD), `--monitor` (monitoring)
- `/user:test` - Testing framework
  - `--coverage` (coverage), `--watch` (watch mode), `--e2e` (end-to-end)

**Analysis & Improvement Commands (4):**
- `/user:analyze` - Multi-dimensional analysis
  - `--code` (code review), `--architecture` (design), `--profile` (performance), `--security` (vulnerabilities)
- `/user:troubleshoot` - Debug & fix issues
  - `--investigate` (explore), `--fix` (repair), `--five-whys` (root cause), `--prod` (production)
- `/user:improve` - Enhance code/performance  
  - `--quality` (refactor), `--performance` (optimize), `--iterate` (continuous), `--threshold` (target %)
- `/user:explain` - Deep explanations
  - `--depth` (complexity level), `--visual` (diagrams), `--examples` (code samples)

**Ops Commands (6):**
- `/user:deploy` - App deployment
  - `--env` (environment), `--rollback` (revert)
- `/user:migrate` - DB/code migration
  - `--dry-run` (preview), `--rollback` (revert)
- `/user:scan` - Security & validation
  - `--validate` (verify), `--security` (vulnerabilities), `--owasp` (security scan), `--deps` (dependencies)
- `/user:estimate` - Time/complexity predictions  
  - `--detailed` (breakdown), `--worst-case` (pessimistic)
- `/user:cleanup` - Project maintenance
  - `--code` (clean code), `--files` (artifacts), `--deps` (dependencies), `--git` (git cleanup), `--all` (everything), `--dry-run` (preview)
- `/user:git` - Git workflow mgmt
  - `--status` (comprehensive status), `--commit` (create commits), `--branch` (manage branches), `--sync` (fetch/pull/push), `--merge` (merge branches), `--stash` (stash changes), `--history` (view history), `--checkpoint` (create checkpoint), `--rollback` (revert changes)

**Design & Architecture Commands (1):**
- `/user:design` - System design
  - `--api` (REST), `--ddd` (domain-driven), `--prd` (requirements), `--openapi` (specs), `--graphql` (GraphQL), `--bounded-context` (DDD contexts)

**Workflow Commands (2):**
- `/user:spawn` - Create specialized sub-agent
  - `--task` (specific assignment)
- `/user:document` - Documentation creation
  - `--api` (API docs), `--user` (user guides)

**System Commands (1):**
- `/user:load` - Load project context
  - `--depth` (analysis level)

#### 3. MCP Integration - Intelligent Tool Usage

SuperClaude: auto & manual control over Model Context Protocol tools:

**Manual Control w/ Flags:**
```bash
# Explicit MCP control
/user:build --react --magic          # Force Magic UI builder
/user:analyze --code --no-c7         # Disable Context7
/user:troubleshoot --seq --think     # Sequential + thinking mode
/user:test --e2e --pup              # Force Puppeteer for testing
/user:explain --no-mcp              # Use only native tools

# Combine multiple MCPs
/user:design --api --seq --c7       # Sequential planning + docs
/user:build --react --magic --pup   # UI generation + testing
```

**Auto Activation:**

**Context7 (C7) - Docs & Libraries:**
```bash
# Auto activation:
"How to use React hooks?" → C7 resolve-library-id → get-docs
"Express.js auth" → C7 get-docs → impl

# Manual w/ personas:
/persona:mentor → asks about lib → C7 provides learning resources
```

**Sequential - Complex Analysis:**
```bash  
# Auto activation:
"Why is my app slow?" → Sequential analysis → optimization plan
"Design microservices architecture" → Sequential system design

# Manual w/ personas:
/persona:architect → /user:design → Sequential long-term thinking
/persona:analyzer → /user:troubleshoot → Sequential root cause analysis
```

**Magic UI Builder - Component Generation:**
```bash
# Auto activation:
"I need a dashboard" → Magic builder → component integration
"Create a form component" → Magic builder → refiner if needed

# Manual w/ personas:
/persona:frontend → UI request → Magic + Puppeteer testing
```

**Puppeteer - Browser Testing:**
```bash
# Auto activation:
UI components → Puppeteer validation
Performance testing → Puppeteer metrics

# Manual w/ personas:
/persona:qa → testing workflows → Puppeteer comprehensive testing
/persona:performance → /user:improve → Puppeteer performance monitoring
```

#### 4. Planning Mode

**Default:** Execute immediately
**Control:** Add `--plan` → preview before execution

Ex: `/user:deploy --plan` → show plan first

#### 5. Thinking Modes

Control analysis depth via flags:

```bash
/user:analyze --code                    # Basic
/user:analyze --code --think           # Standard (~4K)
/user:design --api --think-hard        # Deep (~10K)
/user:troubleshoot --prod --ultrathink # Critical (~32K)
```

Natural language: "think about X" / "think hard about Y" / "ultrathink Z"

#### 6. Research-First Standards

**Auto Research:**
- External libs → C7 docs lookup
- UI components → Magic search
- API integration → official docs
- Performance → benchmarks

**Workflow:** Detect → Research → Cite → Implement

Ex:
```bash
# ❌ Blocked w/o docs
import { fn } from 'unknown-lib'

# ✓ Proceeds w/ citation  
// Source: React docs
import { useState } from 'react'
```

### Workflow Examples

#### Full-Stack Dev
```bash
/persona:architect → /user:load --depth deep → /user:analyze --architecture
/user:design --api --ddd → /user:estimate --detailed
/persona:backend → /user:build --api
/persona:frontend → /user:build --react → /user:test --coverage
/persona:security → /user:scan --security → /user:improve --quality
/user:cleanup --all → /user:deploy --env staging
```

#### Debug & Performance
```bash
/persona:analyzer → /user:troubleshoot --investigate --prod → /user:analyze --profile
"think hard about performance bottlenecks" → /user:troubleshoot --five-whys
/persona:performance → /user:improve --performance --iterate --threshold 90%
/persona:qa → /user:test --e2e → /user:scan --validate
```

#### Learning & Mentoring
```bash
/persona:mentor → /user:explain --depth beginner --visual --examples
/user:document --user → /user:build --tdd → /user:analyze --code
```

#### Git Workflow
```bash
/user:git --status → /user:git --branch feature/new-component
/user:build --react --magic → /user:test --coverage → /user:git --commit "feat: Add dashboard"
/user:git --sync → /user:git --merge develop --think → /user:git --push
/user:git --history → /user:git --checkpoint before-refactor → /user:cleanup --git
```

### UltraCompressed Mode - 70% Token Reduction

**Auto:** Context >70% | Token budget | "minimal tokens"
**Manual:** `/user:document --uc` | `/user:explain --uc "OAuth"`

**Features:**
- Telegram-style: Remove articles/conjunctions/prepositions
- Symbols: →(to), &(and), @(at), w/(with), +(add), -(remove)
- Abbrevs: cfg(config), fn(function), impl(implementation)
- Auto-legend: @ doc start w/ used symbols/abbrevs
- Format: YAML>JSON>tables>lists>prose

**Transform Ex:**
```yaml
# Normal (45): "This comprehensive guide provides detailed instructions for configuring the authentication system including all environment variables and dependencies"
# UltraCompressed (14): "Auth cfg guide: env vars & deps"
```

### Docs Directory Standards

**Separation:** ops reports vs project docs

```
.claudedocs/              # Claude ops docs
├── audit/ reports/ summaries/ metrics/ incidents/

/docs                     # Project docs  
├── api/ guides/ architecture/ development/
```

**Auto Reports:** analyze→reports/ | scan→reports/ | test→metrics/ | troubleshoot→incidents/

**Manual Docs:** `/user:document` → API→/docs/api/ | guides→/docs/guides/

### Model Selection

- Simple → sonnet (cost-effective)
- Complex → sonnet-4 (balanced)  
- Critical → opus-4 (max capability)

### Context Mgmt

```bash
/compact  # Smart reduction
/clear    # Fresh start
/model    # Switch models
```

## Troubleshooting

**Commands not working:** `ls ~/.claude/commands/` (should show 17 files)

**Planning:** Add `--plan` flag → `/user:deploy --plan`

**Personas:** `/persona:architect` → `/persona:security → /user:scan --security`

**MCP:** "React docs" → C7 | "slow app" → Sequential

### Help

- Install issues: `./install.sh` again
- Cmd ref: `/user:load` in project
- Advanced: Read `~/.claude/commands/`
- Config: Modify `~/.claude/`

## Update & Maintenance

**Update:**
```bash
cd SuperClaude && git pull && ./install.sh
```

**Backup:**
```bash
cp -r ~/.claude/ ~/.claude.backup.$(date +%Y%m%d)
```

**Uninstall:**
```bash
rm -rf ~/.claude/
```

---
*SuperClaude v4.0.0 - Cfg framework, not executable code*