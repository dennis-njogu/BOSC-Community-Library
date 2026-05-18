# 🌍 Localization & Multilingual Resources

This section contains educational resources translated into multiple languages.

---

## 📋 Available Languages

### 🇬🇧 [English](english.md)
Primary language for the BOSC Community Library.

**Coverage:** Complete resource library  
**Latest Update:** May 2026  
**Contributors:** [See GitHub]

---

### 🇰🇪 [Kiswahili](kiswahili.md)
Resources for East African learners.

**Coverage:** Core materials  
**Latest Update:** May 2026  
**Contributors:** [See GitHub]

---

### 🇺🇬 [Luganda](luganda.md)
Resources for Central African learners.

**Coverage:** Essential topics  
**Latest Update:** May 2026  
**Contributors:** [See GitHub]

---

## 🔄 Adding a New Language

### Step 1: Prepare Translation

- Translate core resources accurately
- Ensure cultural appropriateness
- Include at least 5-10 foundational topics
- Get reviewed by native speakers

### Step 2: Create Language File

1. Copy existing language file as template
2. Rename to language code: `[language_code].md`
3. Replace content with translations
4. Maintain format structure

### Step 3: Update Documentation

1. Add language to [localization/README.md](README.md) (this file)
2. Update [resources/README.md](../README.md)
3. Update main [README.md](../../README.md)

### Step 4: Submit & Review

1. Create PR with translation
2. Note language code and native speakers
3. Request review from native speakers
4. Address feedback
5. Merge when approved

---

## 📝 Translation Standards

### Quality Requirements

✅ **Accuracy**
- Factually correct translation
- Technical terms properly rendered
- No meaning lost in translation

✅ **Clarity**
- Easy to understand for learners
- Appropriate vocabulary level
- Clear structure and formatting

✅ **Consistency**
- Consistent terminology throughout
- Same terms always translated the same way
- Consistent formatting across all resources

✅ **Cultural Appropriateness**
- Culturally sensitive language
- Relevant examples for target audience
- Respectful of local customs

### Format Guidelines

```markdown
# [Language Name]

## Topic Title

**Level:** Beginner / Intermediate / Advanced

**Learning Objectives:**
- [Objectives in target language]

**Content**
[Educational content in target language]

**Practice**
[Exercises in target language]

**References**
- [References in target language]
```

---

## 🤝 Contributing Translations

### Steps to Contribute

1. **Choose a language**
   - Check if language already exists
   - Ensure there's community need
   - Verify you can commit to quality

2. **Prepare translations**
   - Translate accurately
   - Get reviewed by native speakers
   - Check format consistency

3. **Create PR**
   - Follow [Contributing Guide](../../community/Contributing.md)
   - Reference language you're adding
   - Include translator credits
   - Note review completion

4. **Respond to feedback**
   - Make requested adjustments
   - Ask for clarification if needed
   - Verify translations with reviewers

### Translation Reviewers

We need native speakers to review translations for:
- Accuracy
- Clarity
- Cultural appropriateness
- Consistency

**Interested in reviewing?** Open an issue or contact maintainers!

---

## 🌐 Language Roadmap

### Completed
✅ English (May 2026)
✅ Kiswahili (May 2026)
✅ Luganda (May 2026)

### In Progress
🔄 [Language] — [Status]

### Planned
📋 French — Needed for West Africa
📋 Portuguese — Needed for Southern Africa
📋 Amharic — Needed for East Africa
📋 Arabic — Needed for Northern Africa

---

## 💡 Using Multilingual Resources

### For Learners
- Browse resources in your language
- Use translations to learn effectively
- Share with others in your language
- Suggest improvements if needed

### For Educators
- Use translated materials in your classroom
- Adapt for local context
- Share with colleague educators
- Report errors or suggest additions

### For Translators
- Help expand to more languages
- Review existing translations
- Suggest translation improvements
- Help onboard new translators

---

## 🔍 Translation Search

```bash
# Search by language
python scripts/search_resources.py "kiswahili"
python scripts/search_resources.py "luganda"
python scripts/search_resources.py "english"

# Search specific topic in language
python scripts/search_resources.py "mathematics kiswahili"
```

---

## 📞 Localization Support

### Questions About Languages?
- Check [language-specific file](english.md) you're using
- See [main resources README](../README.md)
- Check [community guidelines](../../community/GOVERNANCE.md)
- Open GitHub Discussion

### Need a Translation?
- Check if language exists in [Available Languages](#available-languages)
- Open a GitHub Issue requesting language
- Community may be able to help!

### Want to Translate?
- See [Steps to Contribute](#steps-to-contribute)
- Follow quality standards
- Get reviewed by native speakers
- Submit as PR

---

## 🙏 Translation Credits

We thank the following for their translations:

**Kiswahili Translators:**
- [Translator names here]

**Luganda Translators:**
- [Translator names here]

**Add Your Name:** Contribute a translation and be credited!

---

## 📚 Technical Details

### File Organization
```
localization/
├── README.md           (This file)
├── english.md          (English content)
├── kiswahili.md        (Kiswahili content)
└── luganda.md          (Luganda content)
```

### Adding to Build Process

If resources are generated/built, update build script:
```python
# In scripts/build_resources.py
SUPPORTED_LANGUAGES = [
    'english',
    'kiswahili',
    'luganda',
    # 'new_language'  # Add here when ready
]
```

---

## 📖 More Information

- [Resource Categories](../categories.md) — What topics are available
- [Contributing Guide](../../GETTING_STARTED.md) — How to contribute
- [Community Standards](../../community/Code_of_Conduct.md) — Our values
- [Main Resources](../README.md) — Resources overview
- [Main README](../../README.md) — Project overview

---

**[← Back to Resources](../README.md) | [← Back to Main README](../../README.md)**

---

*Help us reach learners worldwide! Translate resources into your language.*
