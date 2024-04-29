import setuptools

with open("./cfxs_merge/README.md", "r") as fh:
  long_description = fh.read()

requires_list = open(f'./cfxs_merge/requirements.txt', 'r', encoding='utf8').readlines()
requires_list = [i.strip() for i in requires_list]

setuptools.setup(
  name="cfxs_merge",
  version="0.0.1",
  author="bitfugui",
  author_email="bitfugui@gmail.com",
  description="cfxs merge",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/bitfugui/cfxs_merge",
  packages=setuptools.find_packages(),
  install_requires=requires_list,
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License", 
  "Operating System :: OS Independent",
  ],
)