# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
# coding: utf-8

from setuptools import setup, find_packages

NAME = "azure-ai-language-conversations"
VERSION = "1.0.0b1"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["msrest>=0.6.21", "azure-core<2.0.0,>=1.16.0"]

setup(
    name=NAME,
    version=VERSION,
    description="azure-ai-language-conversations",
    author_email="",
    url="",
    keywords=["Swagger", "ConversationAnalysisClient"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    This API accepts a request and mediates among multiple language projects, such as LUIS Generally Available, Question Answering, LUIS Deepstack, and then calls the best candidate service to handle the request. At last, it returns a response with the candidate service's response as a payload.

 In some cases, this API needs to forward requests and responses between the caller and an upstream service.
    """
)
