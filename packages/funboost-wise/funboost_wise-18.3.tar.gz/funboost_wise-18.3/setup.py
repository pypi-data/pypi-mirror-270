# coding=utf-8
from setuptools import setup, find_packages
# from funboost import __version__

extra_brokers = ['confluent_kafka==1.7.0',
                 "pulsar-client==3.1.0; python_version>='3.7'",
                 'celery',
                 'flower',
                 'nameko==2.14.1',
                 'sqlalchemy==1.4.13',
                 'sqlalchemy_utils==0.36.1',
                 'dramatiq==1.14.2',
                 'huey==2.4.5',
                 'rq==1.15.0',
                 'kombu'
                 ]
setup(
    name='funboost-wise',  #
    version=18.3,
    description=(
        'pip install funboost，python全功能分布式函数调度框架,。支持python所有类型的并发模式和一切知名消息队列中间件，支持如 celery dramatiq等框架整体作为funboost中间件，python函数加速器，框架包罗万象，用户能想到的控制功能全都有。一统编程思维，兼容50% python业务场景，适用范围广。只需要一行代码即可分布式执行python一切函数，99%用过funboost的pythoner 感受是　简易 方便 强劲 强大，相见恨晚 '
    ),
    # long_description=open('README.md', 'r',encoding='utf8').read(),
    keywords=["funboost-wise", "distributed-framework", "function-scheduling", "rabbitmq", "kafka", "nsq", "redis", "disk",
              "sqlachemy", "consume-confirm", "timing", "task-scheduling", "apscheduler", "pulsar", "mqtt", "kombu", "的", "celery", "框架", '分布式调度'],
    long_description_content_type="text/markdown",
    long_description=open('README.md', 'r', encoding='utf8').read(),
    author='bfzs',
    author_email='ydf0509@sohu.com',
    maintainer='ydf',
    maintainer_email='ydf0509@sohu.com',
    license='BSD License',
    # packages=['douban'], #
    packages=find_packages(),  # 也可以写在 MANiFEST.in
    # packages=['function_scheduling_distributed_framework'], # 这样内层级文件夹的没有打包进去。
    include_package_data=True,
    platforms=["all"],
    url='https://github.com/ydf0509/funboost',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        # 'Programming Language :: Python :: 3.13',
        # 'Programming Language :: Python :: 3.14',
        # 'Programming Language :: Python :: 3.15',
        # 'Programming Language :: Python :: 3.16',
        # 'Programming Language :: Python :: 3.17',
        # 'Programming Language :: Python :: 3.18',
        # 'Programming Language :: Python :: 3.19',
        # 'Programming Language :: Python :: 3.20',
        # 'Programming Language :: Python :: 3.21',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=[
        'nb_log>=12.6',
        'nb_libs>=0.9',
        # 'eventlet==0.33.3',
        # 'gevent==22.10.2',
        'pymongo==4.3.3',  # 3.5.1  -> 4.0.2
        'AMQPStorm==2.10.6',
        'rabbitpy==2.0.1',
        'decorator==5.1.1',
        # 'pysnooper==0.0.11',
        'Flask',
        'flask_bootstrap',
        'flask_wtf',
        'wtforms',
        'flask_login',
        'tomorrow3==1.1.0',
        'persist-queue>=0.4.2',
        'elasticsearch',
        'kafka-python==2.0.2',
        'requests',
        'gnsq==1.0.1',
        'psutil',
        # 'sqlalchemy==1.3.10',
        # 'sqlalchemy_utils==0.36.1',    # 用户使用数据库作为消息队列时候，自行安装，不自动安装这个包。也可以使用kombu中间件的sqlalchemy模式来操作数据库或者peewee操作。
        # 'peewee==3.17.3',    # 'peewee==3.15.1',  # 惰性安装
        'apscheduler==3.10.1',
        'pikav0',
        'pikav1',
        'redis2',
        'redis3',
        'redis5',
        'redis',
        'zmq',
        'pyzmq',
        'paho-mqtt',
        'setuptools_rust',
        'fabric2==2.6.0',  # 有的机器包rust错误， 这样做 curl https://sh.rustup.rs -sSf | sh
        'nats-python',
        # 'pulsar-client==3.1.0',   # python3.6 无法安装 pulsar-client
        # 'kombu',
        'nb_filelock',
        'aiohttp==3.8.3',
        'pysnooper',
        'deprecated',
        'cryptography',
        'auto_run_on_remote',
        'frozenlist',
        'fire',
        'pydantic',

    ],
    extras_require={'all': extra_brokers,
                    'extra_brokers': extra_brokers,
                    },

    entry_points={
        'console_scripts': [
            'funboost = funboost.__main__:main',
            'funboost_cli_super = funboost.__main__:main',
        ]}
)