import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'logging_config.yaml')

print(THIS_FOLDER)
print(my_file)
print(__file__)
print(__name__)