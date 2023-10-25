"""
Estimate to complete: 20 minutes
Start time: 10:55
Finish time:
"""

from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

languages = [python, ruby, visual_basic]
print("The dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)
