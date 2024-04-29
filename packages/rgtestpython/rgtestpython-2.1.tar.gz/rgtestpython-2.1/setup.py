import setuptools

with open("README.md","r") as fs:
    long_description=fs.read()

setuptools.setup(name="rgtestpython",version="2.1",author="rongge",\
                 author_email="78380834@qq.com",description="测试python包",\
                 long_description=long_description,\
                 long_description_content_type="text/markdown",\
                 packages=setuptools.find_packages(),\
                 classifiers=["Programming Language :: Python :: 3"],\
                              # "License::OSI Approved::MIT License",\
                              # "Operating System::OS Independent"],\
                 install_requires=['pillow',],\
                 python_requires='>=3',)