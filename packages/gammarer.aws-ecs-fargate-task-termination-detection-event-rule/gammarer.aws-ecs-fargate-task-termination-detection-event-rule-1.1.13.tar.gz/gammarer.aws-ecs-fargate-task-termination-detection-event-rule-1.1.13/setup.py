import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "gammarer.aws-ecs-fargate-task-termination-detection-event-rule",
    "version": "1.1.13",
    "description": "This an AWS ECS Fargate task termination detection Event Rule.",
    "license": "Apache-2.0",
    "url": "https://github.com/yicr/aws-ecs-fargate-task-termination-detection-event-rule.git",
    "long_description_content_type": "text/markdown",
    "author": "yicr<yicr@users.noreply.github.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/yicr/aws-ecs-fargate-task-termination-detection-event-rule.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "gammarer.aws_ecs_fargate_task_termination_detection_event_rule",
        "gammarer.aws_ecs_fargate_task_termination_detection_event_rule._jsii"
    ],
    "package_data": {
        "gammarer.aws_ecs_fargate_task_termination_detection_event_rule._jsii": [
            "aws-ecs-fargate-task-termination-detection-event-rule@1.1.13.jsii.tgz"
        ],
        "gammarer.aws_ecs_fargate_task_termination_detection_event_rule": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.8",
    "install_requires": [
        "aws-cdk-lib>=2.80.0, <3.0.0",
        "constructs>=10.0.5, <11.0.0",
        "jsii>=1.97.0, <2.0.0",
        "publication>=0.0.3",
        "typeguard~=2.13.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
