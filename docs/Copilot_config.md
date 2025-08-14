# Enhanced Prompt-Driven Development (PDD) + GitHub Copilot Playbook

## Chapter 1 – Enhanced VS Code Settings

### Main Settings (settings.json)
```jsonc
{
  // Core Copilot Settings
  "github.copilot.inlineSuggest.enable": true,
  "github.copilot.editor.enable": true,
  "github.copilot.editor.iterativeEditing": true,
  "github.copilot.suggestion.showEditorCompletions": false,
  "github.copilot.chat.welcomeMessage": "never",
  "github.copilot.conversation.codeGeneration": "focused",
  "github.copilot.advanced": {
    "debug": false,
    "length": 500,
    "temperature": 0.1
  },
  
  // Editor Optimizations
  "editor.inlineSuggest.enabled": true,
  "editor.inlineSuggest.suppressSuggestions": false,
  "editor.quickSuggestions": {
    "other": false,
    "comments": false,
    "strings": false
  },
  "editor.suggest.showWords": false,
  "editor.suggest.preview": true,
  "editor.suggest.filterGraceful": false,
  "editor.tabCompletion": "on",
  "editor.acceptSuggestionOnCommitCharacter": false,
  "editor.acceptSuggestionOnEnter": "smart",
  
  // Formatting & Linting
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.organizeImports": true,
    "source.fixAll.eslint": true
  },
  
  // Language-specific Settings
  "[typescript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "editor.codeActionsOnSave": {
      "source.organizeImports": true,
      "source.fixAll.eslint": true
    }
  },
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter",
    "editor.codeActionsOnSave": {
      "source.organizeImports": true,
      "source.fixAll.ruff": true
    }
  },
  "[javascript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[markdown]": {
    "editor.wordWrap": "on",
    "editor.quickSuggestions": true,
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  
  // Python Development
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": true,
  "python.linting.mypyEnabled": true,
  "python.testing.pytestEnabled": true,
  "python.testing.unittestEnabled": false,
  "python.analysis.autoImportCompletions": true,
  
  // Git Integration
  "gitlens.hovers.enabled": true,
  "gitlens.defaultDateFormat": "YYYY-MM-DD",
  "gitlens.defaultDateShortFormat": "YYYY-MM-DD",
  "gitlens.defaultTimeFormat": "HH:mm",
  "gitlens.advanced.messages": {
    "suppressShowKeyBindingsNotice": true
  },
  "git.confirmSync": false,
  "git.autofetch": true,
  "git.enableSmartCommit": true,
  
  // Terminal & Performance
  "terminal.integrated.scrollback": 10000,
  "terminal.integrated.enableMultiLinePasteWarning": false,
  "workbench.commandPalette.experimental.suggestCommands": true,
  
  // File Management
  "files.exclude": {
    "**/.git": true,
    "**/.DS_Store": true,
    "**/node_modules": true,
    "**/__pycache__": true,
    "**/.pytest_cache": true
  },
  "search.exclude": {
    "**/node_modules": true,
    "**/dist": true,
    "**/build": true,
    "**/.venv": true,
    "**/venv": true
  },
  
  // AI-specific Enhancements
  "editor.suggest.localityBonus": true,
  "editor.suggest.shareSuggestSelections": true,
  "editor.wordBasedSuggestions": false,
  "editor.parameterHints.enabled": true
}
```

### Workspace Tasks (tasks.json)
```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Prepare AI Context",
      "type": "shell",
      "command": "python",
      "args": [".github/scripts/context-builder.py"],
      "group": "build",
      "presentation": {
        "echo": true,
        "reveal": "always",
        "panel": "new"
      }
    },
    {
      "label": "AI Code Quality Check",
      "type": "shell",
      "command": "python",
      "args": [".github/scripts/ai-quality-check.py"],
      "group": "test"
    },
    {
      "label": "Generate Prompt Template",
      "type": "shell",
      "command": "python",
      "args": [".github/scripts/prompt-generator.py"],
      "group": "build"
    }
  ]
}
```

## Chapter 2 – Enhanced Repository Structure

### File Structure
```
project/
├── .copilotcontext/
│   ├── project-context.md
│   ├── architecture.md
│   ├── coding-standards.md
│   └── current-sprint.md
├── .github/
│   ├── CODEOWNERS
│   ├── copilot-instructions.md
│   ├── ISSUE_TEMPLATE/
│   │   ├── ai-task.md
│   │   └── ai-bug-report.md
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── workflows/
│   │   ├── ci.yml
│   │   └── ai-metrics.yml
│   └── scripts/
│       ├── context-builder.py
│       ├── ai-quality-check.py
│       └── ai-metrics.py
├── prompts/
│   ├── templates/
│   ├── v1.0/
│   └── active/
├── ai-learnings/
│   ├── successful-patterns.md
│   ├── failure-cases.md
│   └── team-tips.md
└── .ai-tools.yml
```

### .copilotcontext/project-context.md
```md
# Project Context for AI Assistance

## Project Overview
- **Name**: [Your Project Name]
- **Type**: [Web App/API/CLI Tool/etc.]
- **Tech Stack**: [Languages, Frameworks, Databases]
- **Architecture**: [Microservices/Monolith/Serverless]

## Current Focus
- **Sprint Goal**: [Current sprint objective]
- **Priority Features**: [List of current priorities]
- **Known Issues**: [Critical bugs or technical debt]

## Development Standards
- **Code Style**: [Link to style guide]
- **Testing Requirements**: [Coverage targets, test types]
- **Security Requirements**: [Security standards to follow]
- **Performance Targets**: [Response times, throughput goals]

## Context for AI
When generating code, always consider:
1. Existing architectural patterns in this codebase
2. Team coding standards and conventions
3. Current sprint priorities and constraints
4. Security and performance requirements
```

### .github/copilot-instructions.md
```md
# Enhanced Copilot Usage Guidelines (PDD v2.0)

## Core Principles
1. **Context First**: Always review `.copilotcontext/` before generating code
2. **Prompt-Driven**: Use structured prompts from `/prompts/templates/`
3. **Iterative Refinement**: Generate → Review → Refine → Test
4. **Documentation**: Store all prompts with semantic versioning
5. **Quality Gates**: All AI-generated code must pass quality checks

## Workflow
1. **Preparation**: Run "Prepare AI Context" task
2. **Prompting**: Use templates from `/prompts/templates/`
3. **Generation**: Use Copilot Chat with prepared context
4. **Validation**: Run local tests and quality checks
5. **Documentation**: Save prompt and results
6. **Commit**: Use semantic commit with `[ai-assisted]` tag

## Commit Convention
```
<type>(ai): <description> [ai-assisted]

Examples:
feat(ai): implement user authentication system [ai-assisted]
fix(ai): resolve memory leak in data processor [ai-assisted]
refactor(ai): optimize database query performance [ai-assisted]
test(ai): add comprehensive edge case coverage [ai-assisted]
docs(ai): generate API documentation [ai-assisted]
```

## Quality Requirements
- [ ] Code follows project standards
- [ ] Security review completed
- [ ] Performance impact assessed
- [ ] Tests written and passing
- [ ] Documentation updated
- [ ] Prompt saved in `/prompts/active/`
```

### .github/ISSUE_TEMPLATE/ai-task.md
```md
---
name: AI Development Task
about: Define a structured task for AI-assisted development
title: "[AI TASK]: "
labels: ["ai-assisted", "enhancement"]
---

## Task Context
**Priority**: [High/Medium/Low]
**Estimated Complexity**: [Simple/Moderate/Complex]
**Related Epic**: [Link to epic/parent issue]

## Problem Statement
[Clear description of what needs to be solved]

## Acceptance Criteria
- [ ] [Specific, testable requirement 1]
- [ ] [Specific, testable requirement 2]
- [ ] [Performance/security requirements]

## Technical Context
**Affected Components**: [List of files/modules]
**Dependencies**: [External libs, internal modules]
**Constraints**: [Performance, security, compatibility]

## AI Assistance Plan
**Prompt Strategy**: [Which prompt templates to use]
**Expected AI Tools**: [Copilot Chat, inline suggestions, etc.]
**Human Review Points**: [Critical review checkpoints]

## Definition of Done
- [ ] Code generated and reviewed
- [ ] Tests written and passing (>90% coverage)
- [ ] Security review completed
- [ ] Performance benchmarked
- [ ] Documentation updated
- [ ] Prompt archived in `/prompts/active/`
```

### .github/PULL_REQUEST_TEMPLATE.md
```md
## Summary
[Brief description of changes]

## AI Assistance Details
- [ ] No AI assistance used
- [ ] AI-assisted development
  - **Tools Used**: [Copilot Chat, Inline Suggestions, etc.]
  - **Prompt Files**: [Links to prompts in `/prompts/active/`]
  - **AI Contribution %**: [Estimate: 10%, 50%, 90%]
  - **Human Review Level**: [Code review, logic review, full rewrite]

## Changes Made
- [Specific change 1]
- [Specific change 2]

## Testing Performed
- [ ] Unit tests added/updated
- [ ] Integration tests verified
- [ ] Manual testing completed
- [ ] Performance impact assessed

## Quality Checklist
- [ ] Code follows project standards
- [ ] Security review completed
- [ ] Linting passed
- [ ] Type checking passed
- [ ] Documentation updated

## Deployment Notes
[Any special deployment considerations]

## AI Learning Notes
[What worked well/poorly with AI assistance - for team knowledge sharing]
```

### .github/workflows/enhanced-ci.yml
```yaml
name: Enhanced CI with AI Tracking

on:
  pull_request:
  push:
    branches: [ "main", "develop" ]

jobs:
  ai-analysis:
    runs-on: ubuntu-latest
    name: AI Code Analysis
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
          
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install flake8 black mypy pytest coverage
          
      - name: Detect AI-assisted commits
        run: |
          echo "=== AI-Assisted Commits in this PR ==="
          git log origin/main..HEAD --grep="\[ai-assisted\]" --oneline || echo "No AI commits found"
          
      - name: AI Code Quality Check
        run: python .github/scripts/ai-quality-check.py
        
      - name: Verify Prompt Documentation
        run: python .github/scripts/verify-prompts.py
        
      - name: Run Linting
        run: |
          flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
          black --check .
          
      - name: Type Checking
        run: mypy . --ignore-missing-imports
        
      - name: Run Tests with Coverage
        run: |
          coverage run -m pytest
          coverage report --fail-under=80
          coverage xml
          
      - name: Upload Coverage
        uses: codecov/codecov-action@v3
        with:
          file: ./coverage.xml
          
      - name: AI Metrics Collection
        if: github.event_name == 'push' && github.ref == 'refs/heads/main'
        run: python .github/scripts/ai-metrics.py
```

## Chapter 3 – Enhanced Prompt Templates

### Template Structure (/prompts/templates/)

#### general-function.md
```md
# Function Generation Template v2.0

## Role & Context
**Role**: Senior [Backend/Frontend/Full-stack] Engineer
**Project Context**: [Brief project description]
**Architecture**: [Current system architecture]
**Tech Stack**: [Languages, frameworks, libraries in use]

## Task Definition
**Function Purpose**: [What this function should accomplish]
**Integration Point**: [Where this fits in the larger system]
**Performance Requirements**: [Response time, throughput, memory constraints]
**Security Requirements**: [Authentication, authorization, data validation]

## Input Specifications
```
[Function signature or API contract]
```

## Output Requirements
- **Code Style**: [PEP8/ESLint/etc.] compliant
- **Documentation**: Comprehensive docstrings/comments
- **Error Handling**: Proper exception handling and logging
- **Testing**: Unit tests with >90% coverage
- **Type Safety**: Full type annotations (if applicable)

## Constraints
- **Dependencies**: [Allowed/forbidden libraries]
- **Compatibility**: [Browser/Python version requirements]
- **Resource Limits**: [Memory, CPU, network constraints]
- **Security**: [Specific security considerations]

## Success Criteria
- [ ] Function works correctly for all specified inputs
- [ ] Handles edge cases gracefully
- [ ] Performance meets requirements
- [ ] Security requirements satisfied
- [ ] Code is maintainable and well-documented
```

#### architecture-decision.md
```md
# Architecture Decision Template v2.0

## Context & Problem
**Current State**: [Description of current architecture]
**Problem**: [What needs to be solved or improved]
**Impact Scope**: [Which parts of system are affected]
**Timeline**: [When this needs to be implemented]

## Requirements
**Functional**: [What the solution must do]
**Non-functional**: [Performance, scalability, security needs]
**Constraints**: [Budget, timeline, technology limitations]

## Solution Analysis
Please provide 3 alternative solutions with:
1. **Approach**: [High-level solution description]
2. **Pros**: [Benefits and advantages]
3. **Cons**: [Drawbacks and risks]
4. **Complexity**: [Implementation difficulty: Low/Medium/High]
5. **Cost**: [Development and operational costs]
6. **Timeline**: [Implementation time estimate]

## Recommendation Criteria
Prioritize solutions based on:
1. Long-term maintainability
2. Scalability potential
3. Development team expertise
4. Total cost of ownership
5. Risk mitigation
```

#### debugging-investigation.md
```md
# Bug Investigation Template v2.0

## Bug Report
**Error Description**: [What's going wrong]
**Error Messages/Logs**: 
```
[Paste full error messages and relevant logs]
```

**Environment**: [OS, language version, dependencies]
**Reproduction Steps**: [Step-by-step reproduction]

## Context
**Recent Changes**: [What changed recently in the codebase]
**Affected Components**: [Which parts of the system are impacted]
**User Impact**: [How this affects end users]
**Frequency**: [How often this occurs]

## Investigation Request
Please provide:
1. **Root Cause Analysis**: [Why this is happening]
2. **Fix Options**: [Multiple potential solutions]
3. **Risk Assessment**: [Risks of each fix option]
4. **Prevention Strategy**: [How to prevent similar issues]
5. **Testing Plan**: [How to verify the fix works]

## Priority Assessment
**Severity**: [Critical/High/Medium/Low]
**User Impact**: [Number of users affected]
**Business Impact**: [Revenue/reputation impact]
```

#### optimization.md
```md
# Performance Optimization Template v2.0

## Current Code Analysis
```
[Paste the code that needs optimization]
```

## Performance Context
**Current Metrics**: [Response time, throughput, resource usage]
**Target Metrics**: [Desired performance improvements]
**Bottleneck Analysis**: [Known or suspected bottlenecks]
**Load Patterns**: [How the code is typically used]

## Optimization Requirements
**Maintain**: [What must remain unchanged]
**Improve**: [Specific metrics to optimize]
**Constraints**: [Memory, CPU, compatibility limits]
**Acceptable Trade-offs**: [What can be sacrificed for performance]

## Deliverables
Please provide:
1. **Optimized Code**: [Improved implementation]
2. **Performance Analysis**: [Expected improvements]
3. **Trade-off Analysis**: [What changed and why]
4. **Testing Strategy**: [How to verify improvements]
5. **Monitoring Plan**: [How to track performance in production]

## Benchmarking Plan
Include benchmarking code to:
- [ ] Measure current performance
- [ ] Validate improvements
- [ ] Compare different optimization approaches
```

## Chapter 4 – Support Scripts

### .github/scripts/context-builder.py
```python
#!/usr/bin/env python3
"""
Context Builder for AI-Assisted Development
Prepares context files for better AI assistance
"""

import os
import json
from datetime import datetime
from pathlib import Path

def build_context():
    """Build AI context from project files"""
    
    context = {
        "timestamp": datetime.now().isoformat(),
        "project_structure": get_project_structure(),
        "recent_changes": get_recent_changes(),
        "active_branches": get_active_branches(),
        "dependencies": get_dependencies(),
        "current_sprint": get_current_sprint()
    }
    
    # Save context for AI tools
    with open('.copilotcontext/generated-context.json', 'w') as f:
        json.dump(context, f, indent=2)
    
    print("✅ AI context prepared successfully")
    print(f"📁 Project files analyzed: {len(context['project_structure'])}")
    print(f"🔄 Recent commits: {len(context['recent_changes'])}")

def get_project_structure():
    """Get relevant project file structure"""
    structure = []
    ignore_dirs = {'.git', 'node_modules', '__pycache__', '.pytest_cache', 'venv', '.venv'}
    
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        for file in files:
            if file.endswith(('.py', '.js', '.ts', '.md', '.yml', '.yaml')):
                structure.append(os.path.join(root, file))
    
    return structure

def get_recent_changes():
    """Get recent git changes"""
    import subprocess
    try:
        result = subprocess.run(
            ['git', 'log', '--oneline', '-10'],
            capture_output=True, text=True
        )
        return result.stdout.strip().split('\n')
    except:
        return []

def get_active_branches():
    """Get active git branches"""
    import subprocess
    try:
        result = subprocess.run(
            ['git', 'branch', '-a'],
            capture_output=True, text=True
        )
        return [line.strip() for line in result.stdout.split('\n') if line.strip()]
    except:
        return []

def get_dependencies():
    """Get project dependencies"""
    deps = {}
    
    # Python dependencies
    if os.path.exists('requirements.txt'):
        with open('requirements.txt') as f:
            deps['python'] = [line.strip() for line in f if line.strip()]
    
    # Node.js dependencies
    if os.path.exists('package.json'):
        with open('package.json') as f:
            package_data = json.load(f)
            deps['node'] = package_data.get('dependencies', {})
    
    return deps

def get_current_sprint():
    """Get current sprint information"""
    sprint_file = '.copilotcontext/current-sprint.md'
    if os.path.exists(sprint_file):
        with open(sprint_file) as f:
            return f.read()
    return "No current sprint information"

if __name__ == "__main__":
    build_context()
```

### .github/scripts/ai-quality-check.py
```python
#!/usr/bin/env python3
"""
AI Code Quality Checker
Validates AI-generated code meets quality standards
"""

import os
import re
import subprocess
import sys
from pathlib import Path

class AIQualityChecker:
    def __init__(self):
        self.issues = []
        self.warnings = []
    
    def check_ai_commits(self):
        """Check AI-assisted commits for quality indicators"""
        try:
            result = subprocess.run(
                ['git', 'log', '--grep=\\[ai-assisted\\]', '-10', '--oneline'],
                capture_output=True, text=True
            )
            
            ai_commits = result.stdout.strip().split('\n')
            ai_commits = [commit for commit in ai_commits if commit.strip()]
            
            print(f"🤖 Found {len(ai_commits)} AI-assisted commits")
            
            for commit in ai_commits:
                self.check_commit_quality(commit)
                
        except Exception as e:
            self.warnings.append(f"Could not analyze git commits: {e}")
    
    def check_commit_quality(self, commit_line):
        """Check individual commit quality"""
        commit_hash = commit_line.split()[0]
        
        # Check if prompt documentation exists
        prompt_files = list(Path('prompts/active').glob('*.md'))
        if not prompt_files:
            self.issues.append(f"No prompt documentat