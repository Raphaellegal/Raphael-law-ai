from app.config.settings import settings


print("Current language:")
print(settings.language)

print("\nAvailable languages:")

for name, code in settings.available_languages.items():
    print(name, "=", code)