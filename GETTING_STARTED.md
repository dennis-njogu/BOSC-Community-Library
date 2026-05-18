# 🎓 Getting Started with BOSC Community Library

Welcome! This guide will help you get up and running as a contributor.

---

## 📋 Table of Contents

1. [Before You Start](#before-you-start)
2. [Setting Up Your Environment](#setting-up-your-environment)
3. [Understanding Our Structure](#understanding-our-structure)
4. [Making Your First Contribution](#making-your-first-contribution)
5. [Common Tasks](#common-tasks)
6. [Getting Help](#getting-help)

---

## ✅ Before You Start

Please ensure you've read and understood:

- **[Code of Conduct](community/Code_of_Conduct.md)** — Our community values
- **[Contributing Guidelines](community/Contributing.md)** — Contribution process
- **[Governance](community/GOVERNANCE.md)** — Team structure

These set expectations for all community members.

---

## 🛠️ Setting Up Your Environment

### Prerequisites
- Git installed and configured
- Python 3.8+ (for scripts and tools)
- Text editor or IDE (VS Code recommended)

### Step 1: Clone the Repository
```bash
git clone https://github.com/BOSC/Community-Library.git
cd BOSC-Community-Library
```

### Step 2: Create a Feature Branch
Follow our branch naming convention:

```bash
# For new features
git checkout -b feature/descriptive-name

# For bug fixes
git checkout -b bugfix/issue-description

# For refactoring
git checkout -b refactor/area-to-refactor
```

### Step 3: Install Dependencies (if needed)
```bash
python scripts/setup.py
```

### Step 4: Understand the Project Structure
See [Directory Map](README.md#-directory-structure) in main README for a complete overview.

---

## 🏗️ Understanding Our Structure

The project is organized into clear sections:

| Section | Purpose | What's Inside |
|---------|---------|---------------|
| **community/** | Governance & guidelines | Code of conduct, contribution rules, governance |
| **docs/** | Technical documentation | Architecture, proposals, deployment guides |
| **resources/** | Educational content | Learning materials, categories, multilingual content |
| **scripts/** | Automation tools | Python utilities for search, setup, etc. |
| **legal/** | Legal framework | License, legal analysis |
| **reports/** | Project documentation | Sustainability, reflection, submissions |

🔗 **Quick Links:**
- [Full Directory Structure](README.md#-directory-structure)
- [Community Governance](community/GOVERNANCE.md)
- [Contribution Guidelines](community/Contributing.md)

---

## 🚀 Making Your First Contribution

### Contribution Workflow

#### 1. **Find or Create an Issue**
- Browse existing GitHub issues
- Or create a new issue describing what you want to contribute
- Ask in [Discussions](community/MEETINGS.md) if unsure

#### 2. **Create a Feature Branch**
```bash
git checkout -b feature/my-awesome-feature
```

#### 3. **Make Your Changes**

**For Content Contributors:**
- Add resources to appropriate categories in [resources/](resources/)
- Follow the structure in [categories.md](resources/categories.md)
- Use the correct language folder in [localization/](resources/localization/)

**For Documentation:**
- Update relevant README in the section
- Follow existing formatting patterns
- Link to related files

**For Code/Scripts:**
- Write clear, documented Python
- Include docstrings
- Add comments for complex logic
- Update [scripts/README.md](scripts/README.md) if needed

**For Translations:**
- Add content to [localization/](resources/localization/)
- Follow existing format in language files
- Ensure accuracy and cultural appropriateness

#### 4. **Commit Your Changes**

Follow our commit message format:

```bash
# Format: <type>: <description>

git commit -m "feat: Add new mathematics resources"
git commit -m "fix: Update broken resource links"
git commit -m "docs: Improve architecture documentation"
git commit -m "refactor: Organize scripts directory"
```

**Commit Types:**
- `feat:` — New feature or resource
- `fix:` — Bug fix or correction
- `docs:` — Documentation changes
- `refactor:` — Code reorganization

#### 5. **Push & Create Pull Request**
```bash
git push origin feature/my-awesome-feature
```

Then open a Pull Request on GitHub with:
- Clear title describing the change
- Description of what was changed and why
- Reference to any related issues

#### 6. **Address Feedback**
- Review comments from maintainers
- Make requested changes
- Push updates to same branch
- PR will update automatically

#### 7. **Merge!**
Once approved, a maintainer will merge your changes.

---

## 💡 Common Tasks

### Adding a New Educational Resource

1. Navigate to [resources/](resources/)
2. Check [categories.md](resources/categories.md) for subject area
3. Create/update resource file in correct category
4. Add to appropriate language in [localization/](resources/localization/)
5. Commit and create PR

Example:
```bash
# Add mathematics resource
git checkout -b feature/add-geometry-materials
# Create or update resources/mathematics/geometry.md
git add resources/mathematics/geometry.md
git commit -m "feat: Add geometry learning materials"
git push origin feature/add-geometry-materials
```

### Searching for Resources

```bash
# Use the search utility
python scripts/search_resources.py "mathematics"
python scripts/search_resources.py "kiswahili"
```

### Translating Content

1. Review existing translations in [resources/localization/](resources/localization/)
2. Create/update translation file
3. Ensure accuracy and cultural appropriateness
4. Submit as PR for review

### Improving Documentation

1. Find the relevant README in the section
2. Improve clarity, add examples, fix errors
3. Test any code examples
4. Submit as PR

### Reporting Issues

1. Check if issue already exists
2. Create new GitHub issue with:
   - Clear title
   - Description of the problem
   - Steps to reproduce (if applicable)
   - Expected vs actual behavior
   - Environment info (OS, Python version, etc.)

---

## 🎯 What We're Looking For

### High-Quality Contributions Include:

✅ **Clear, readable content** — Easy for others to understand  
✅ **Proper documentation** — Explain what and why  
✅ **Following patterns** — Consistent with existing code/content  
✅ **Testing** — Verify your changes work  
✅ **Respectful communication** — Collaborative tone in PRs/issues  

### We Value:

- 📚 Educational resources that fill gaps
- 🌍 Multilingual translations
- 🐛 Bug reports with clear reproduction steps
- 📖 Documentation improvements
- 💡 Feature suggestions with clear use cases
- ♿ Accessibility improvements

---

## 📞 Getting Help

### Where to Find Answers:

| Question | Resource |
|----------|----------|
| How do I...? | Check [FAQ](#) (coming soon) |
| What's the project about? | See [main README](README.md) |
| Who approves my changes? | See [GOVERNANCE](community/GOVERNANCE.md) |
| Code/script help? | Check [Architecture](docs/architecture.md) |
| Translation questions? | See [Localization README](resources/localization/README.md) |
| General discussion? | See [Meeting Notes](community/MEETINGS.md) |

### Contact:

- **GitHub Issues** — Bug reports & feature requests
- **Discussions** — General questions & ideas
- **Email** — (add contact if available)

---

## 🎉 Next Steps

1. ✅ Read this guide completely
2. ✅ Read the [Code of Conduct](community/Code_of_Conduct.md)
3. ✅ Review [Contributing Guidelines](community/Contributing.md)
4. ✅ Set up your local environment
5. ✅ Find your first issue or create one
6. ✅ Make your first contribution!
7. ✅ Help others by reviewing their PRs

---

## 📚 Additional Resources

- [Main README](README.md) — Project overview
- [Community Guidelines](community/) — Governance & rules
- [Architecture Docs](docs/architecture.md) — Technical details
- [Deployment Guide](docs/deployment/installation.md) — Setup & deployment
- [Educational Resources](resources/) — Browse learning materials

---

## 🙏 Thank You!

Thank you for being part of the BOSC Community Library! Your contributions make education more accessible. 

**Welcome aboard!** 🚀

---

*Questions? Open an issue or check [Meeting Notes](community/MEETINGS.md) for team discussions.*
