import setuptools

PACKAGE_NAME = "messages-local"

package_dir = PACKAGE_NAME.replace("-", "_")

setuptools.setup(
    name=PACKAGE_NAME,
    version='0.0.49', # https://pypi.org/project/messages-local
    author="Circles",
    author_email="info@circles.life",
    url=f"https://github.com/circles-zone/messages-local-python-package",
    packages=[package_dir],
    package_dir={package_dir: f'{package_dir}/src'},
    package_data={package_dir: ['*.py']},
    long_description="messages-local",
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    install_requires=["item-local",
                      "message-local>=0.0.118",
                      "queue-worker-local>=0.0.37",
                      "label-message-local>=0.0.2",
                      "whatsapp-message-vonage-local",
                      "whataspp-inforu-local",
                      "email-message-aws-ses-local",
                      "sms-message-aws-sns-local>=0.0.8",
                      ]
)
