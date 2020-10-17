import platform

print("This is running python version {0}, {1}, {2}".format(platform.python_version(), platform.node(), platform.architecture())) # This is pre python3.6

pythonVersion = platform.python_version()
print(f'This is running python - {pythonVersion}') # This is post python 3.6 where the 'f' indicates a formatter