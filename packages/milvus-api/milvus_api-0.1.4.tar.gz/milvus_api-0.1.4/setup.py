from setuptools import setup, find_packages

setup(
    name='milvus_api',
    version='0.1.4',
    packages=find_packages(),
    install_requires=[
        "pymilvus==2.4.0",
        "milvus-model==0.2.0",
        "pydantic==2.7.0",
        "tqdm==4.66.2",
        "FlagEmbedding==1.2.9",
        "torch==2.2.2",
        "numpy==1.24.4"
    ],
    author='ShengWen',
    author_email='shengwen8785@example.com',
    description='A Milvus API used for quickly setting up a Milvus vector database',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)