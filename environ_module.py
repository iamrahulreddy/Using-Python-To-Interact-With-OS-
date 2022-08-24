import os

print("environ variable: " + os.environ.get("TEMP", "Not Found:("))
print("SHELL: " + os.environ.get("DATAGRIP", "Not Found:("))
print("Fruit: " + os.environ.get("OneDrive", "Not Found:("))
