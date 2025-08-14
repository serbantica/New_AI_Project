# Lightweight AI Development Setup
*Speed & Flexibility First - Minimal Overhead*

## VS Code Settings - Optimized for Speed

### Essential Settings (settings.json)
```jsonc
{
  // Copilot - Maximum Responsiveness
  "github.copilot.inlineSuggest.enable": true,
  "github.copilot.editor.enable": true,
  "github.copilot.editor.iterativeEditing": true,
  "github.copilot.chat.welcomeMessage": "never",
  "github.copilot.advanced": {
    "temperature": 0.3,
    "length": 1000
  },
  
  // Editor - Fast Suggestions
  "editor.inlineSuggest.enabled": true,
  "editor.quickSuggestions": {
    "other": "on",
    "comments": "on",
    "strings": "on"
  },
  "editor.suggestOnTriggerCharacters": true,
  "editor.acceptSuggestionOnEnter": "on",
  "editor.tabCompletion": "on",
  "editor.wordBasedSuggestions": "off",
  "editor.suggest.localityBonus": true,
  
  // Auto-save & Format - Zero Friction
  "files.autoSave": "afterDelay",
  "files.autoSaveDelay": 1000,
  "editor.formatOnSave": true,
  "editor.formatOnPaste": true,
  "editor.formatOnType": true,
  
  // Performance - Faster Everything
  "editor.suggest.showWords": false,
  "editor.suggest.showSnippets": false,
  "search.followSymlinks": false,
  "git.autofetch": false,
  "extensions.autoUpdate": false,
  
  // Language Specific - Minimal Setup
  "[javascript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "editor.codeActionsOnSave": {
      "source.fixAll.eslint": true
    }
  },
  "[typescript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "editor.codeActionsOnSave": {
      "source.fixAll.eslint": true
    }
  },
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter",
    "editor.formatOnSave": true
  },
  "[json]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  
  // Hide Distractions
  "workbench.startupEditor": "none",
  "explorer.confirmDelete": false,
  "explorer.confirmDragAndDrop": false,
  "git.confirmSync": false,
  "git.enableSmartCommit": true,
  
  // Terminal Shortcuts
  "terminal.integrated.fontSize": 14,
  "terminal.integrated.scrollback": 5000
}
```

### Keyboard Shortcuts (keybindings.json)
```json
[
  {
    "key": "ctrl+shift+i",
    "command": "github.copilot.generate",
    "when": "editorTextFocus"
  },
  {
    "key": "ctrl+;",
    "command": "github.copilot.acceptInlineSuggestion",
    "when": "inlineSuggestionVisible"
  },
  {
    "key": "alt+;",
    "command": "editor.action.inlineSuggest.showNext",
    "when": "inlineSuggestionVisible"
  },
  {
    "key": "ctrl+shift+;",
    "command": "workbench.action.chat.open"
  }
]
```

## Minimal Project Structure

```
project/
├── .vscode/
│   ├── settings.json
│   └── snippets.code-snippets
├── scripts/
│   └── quick-context.py
├── .gitignore
├── README.md
└── [your source files]
```

## Speed-First Snippets

### .vscode/snippets.code-snippets
```json
{
  "AI Function": {
    "prefix": "aif",
    "body": [
      "# AI: Create a ${1:function_name} function that ${2:description}",
      "# Requirements: ${3:requirements}",
      "# Return: ${4:return_type}",
      "",
      "$0"
    ],
    "description": "Quick AI function prompt"
  },
  
  "AI Fix": {
    "prefix": "aifix",
    "body": [
      "# AI: Fix this code - ${1:issue_description}",
      "# Current behavior: ${2:current}",
      "# Expected: ${3:expected}",
      "",
      "$0"
    ],
    "description": "Quick AI debugging prompt"
  },
  
  "AI Optimize": {
    "prefix": "aiopt",
    "body": [
      "# AI: Optimize this for ${1:performance/readability/memory}",
      "# Keep: ${2:what_to_maintain}",
      "# Improve: ${3:what_to_improve}",
      "",
      "$0"
    ],
    "description": "Quick optimization prompt"
  },
  
  "AI Test": {
    "prefix": "aitest",
    "body": [
      "# AI: Generate tests for the above function",
      "# Test cases: normal, edge cases, errors",
      "# Framework: ${1:pytest/jest/etc}",
      "",
      "$0"
    ],
    "description": "Quick test generation"
  }
}
```

## Lightning-Fast Context Builder

### scripts/quick-context.py
```python
#!/usr/bin/env python3
"""
Ultra-fast context builder for AI assistance
Run with: python scripts/quick-context.py
"""

import os
import sys
from pathlib import Path

def quick_context():
    """Build minimal context in seconds"""
    
    print("🚀 Quick AI Context Builder")
    
    # Get recent files
    recent_files = []
    for ext in ['.py', '.js', '.ts', '.jsx', '.tsx', '.vue', '.go', '.rs']:
        files = list(Path('.').rglob(f'*{ext}'))
        files = [f for f in files if not any(skip in str(f) for skip in ['node_modules', '.git', 'dist', 'build'])]
        recent_files.extend(files[:5])  # Top 5 per extension
    
    # Quick file summary
    total_lines = 0
    for file in recent_files[:20]:  # Max 20 files
        try:
            with open(file, 'r', encoding='utf-8', errors='ignore') as f:
                lines = len(f.readlines())
                total_lines += lines
        except:
            pass
    
    # Quick README scan
    readme_content = ""
    for readme in ['README.md', 'README.txt', 'readme.md']:
        if os.path.exists(readme):
            with open(readme, 'r', encoding='utf-8', errors='ignore') as f:
                readme_content = f.read()[:500] + "..."
            break
    
    # Output context
    context = f"""
# Quick Project Context

## Project Structure
- Files analyzed: {len(recent_files)}
- Total lines: {total_lines}
- Main languages: {', '.join(set(f.suffix[1:] for f in recent_files))}

## About
{readme_content}

## Recent Files
{chr(10).join(f"- {f}" for f in recent_files[:10])}

Ready for AI assistance! 🤖
"""
    
    print(context)
    
    # Save for reference
    with open('.ai-context.md', 'w') as f:
        f.write(context)
    
    print(f"\n✅ Context saved to .ai-context.md")

if __name__ == "__main__":
    quick_context()
```

## Flexible Git Integration

### .gitignore (AI-friendly)
```gitignore
# AI Context (optional to commit)
.ai-context.md
ai-scratch/

# Standard ignores
node_modules/
dist/
build/
*.log
.env
.DS_Store
__pycache__/
*.pyc
.venv/
venv/
```

### Simple Git Aliases (run once)
```bash
# Add these to your git config for speed
git config alias.aip "!git add . && git commit -m"
git config alias.quick "!git add . && git commit -m 'quick update' && git push"
git config alias.ai "!git add . && git commit -m 'ai-assisted:'"
```

## Speed-Optimized Workflow

### 1. **Instant AI Prompting**
Just type `aif` + Tab in VS Code and get an instant AI function prompt template.

### 2. **One-Command Context**
```bash
python scripts/quick-context.py
```

### 3. **Rapid Commits**
```bash
git ai "added user login feature"  # Commits with ai-assisted: prefix
git quick                          # Instant commit + push
```

### 4. **Fast AI Iteration**
1. Write comment with `aif` snippet
2. Use Copilot Chat (Ctrl+Shift+;)
3. Accept/modify suggestion
4. Test quickly
5. Commit with `git ai "description"`

## Essential Extensions (Minimal Set)

Install only these for maximum speed:
```json
{
  "recommendations": [
    "github.copilot",
    "github.copilot-chat",
    "esbenp.prettier-vscode",
    "ms-python.python",
    "bradlc.vscode-tailwindcss"
  ]
}
```

## Quick Start Templates

### Python Quick Starter
```python
# AI: Create a [DESCRIPTION] that [FUNCTIONALITY]
# Input: [INPUT_TYPE]
# Output: [OUTPUT_TYPE] 
# Requirements: [REQUIREMENTS]

def quick_function():
    pass

# AI: Generate tests for the above function
# Test: normal cases, edge cases, errors

def test_quick_function():
    pass
```

### JavaScript Quick Starter
```javascript
// AI: Create a [DESCRIPTION] that [FUNCTIONALITY]
// Input: [INPUT_TYPE]
// Output: [OUTPUT_TYPE]
// Requirements: [REQUIREMENTS]

function quickFunction() {
  // Implementation here
}

// AI: Generate tests for the above function
// Framework: Jest/Vitest
// Test: normal cases, edge cases, errors

describe('quickFunction', () => {
  // Tests here
});
```

## Pro Tips for Speed & Flexibility

### 1. **Use AI Comments as Specs**
```python
# AI: Parse CSV file with error handling and return clean DataFrame
# Handle: missing files, malformed data, encoding issues
# Return: pandas DataFrame or None if failed

def parse_csv(file_path):
    # AI will generate this based on the comment
    pass
```

### 2. **Chain AI Tasks**
```python
# AI: Create user class with email validation

# AI: Add password hashing to above class

# AI: Add JSON serialization methods

# AI: Generate unit tests for all methods above
```

### 3. **Quick Debug Pattern**
```python
# Current issue: [DESCRIBE BUG]
# Expected: [WHAT SHOULD HAPPEN]
# AI: Fix this code and explain the issue

buggy_code_here()
```

### 4. **Instant Optimization**
```python
# AI: Optimize this for speed while keeping same interface
slow_function()

# AI: Now optimize for memory usage
memory_heavy_function()
```

## One-Minute Setup Script

### setup.sh (Linux/Mac)
```bash
#!/bin/bash
echo "🚀 Setting up lightweight AI development..."

# Create structure
mkdir -p scripts .vscode ai-scratch

# Create quick context script
cat > scripts/quick-context.py << 'EOF'
#!/usr/bin/env python3
import os
from pathlib import Path

print("🤖 Quick context ready!")
files = list(Path('.').rglob('*.py'))[:10]
print(f"Found {len(files)} Python files")
for f in files: print(f"- {f}")
EOF

# Git aliases
git config alias.ai "!git add . && git commit -m 'ai-assisted:'"
git config alias.quick "!git add . && git commit -m 'quick update'"

# Make executable
chmod +x scripts/quick-context.py

echo "✅ Setup complete! Start coding with AI assistance."
echo "💡 Type 'aif + Tab' in VS Code for instant AI prompts"
```

### setup.bat (Windows)
```batch
@echo off
echo 🚀 Setting up lightweight AI development...

mkdir scripts .vscode ai-scratch 2>nul

echo print("🤖 Quick context ready!") > scripts\quick-context.py

git config alias.ai "!git add . && git commit -m 'ai-assisted:'"
git config alias.quick "!git add . && git commit -m 'quick update'"

echo ✅ Setup complete! Start coding with AI assistance.
echo 💡 Type 'aif + Tab' in VS Code for instant AI prompts
```

## Daily Workflow Example

```bash
# Start new feature
python scripts/quick-context.py  # 2 seconds

# In VS Code:
# 1. Type "aif" + Tab
# 2. Fill in function description
# 3. Use Copilot Chat to generate
# 4. Test/refine quickly
# 5. git ai "added login validation"

# Repeat for each small feature/fix
```

This setup prioritizes:
- ⚡ **Speed**: Minimal configuration, instant prompting
- 🔄 **Flexibility**: Easy to modify, no complex rules  
- 🎯 **Focus**: Just the essentials for AI-assisted coding
- 🚀 **Flow**: Optimized for rapid iteration and testing

Perfect for personal projects, prototypes, and rapid development where you want AI assistance without enterprise overhead!