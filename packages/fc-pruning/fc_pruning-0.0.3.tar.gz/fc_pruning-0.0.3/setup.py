import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(name="fc_pruning",
                 version="0.0.3",
                 author="Aida Mehammed",
                 author_email="aida.mehammed@studium.uni-hamburg.de",
                 description="FC Pruning",
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url="https://github.com/AidaMehammed/fc_pruning",
                 project_urls={
                     "Bug Tracker": "https://github.com/AidaMehammed/fc_pruning",
                 },
                 packages=setuptools.find_packages(include=['Compress','Compress.*']),

                 classifiers=[
                     "Programming Language :: Python :: 3",
                     "Operating System :: OS Independent",
                 ],
                 python_requires=">=3.8",
                 
                 install_requires=['featurecloud','torch_pruning']

                 )
