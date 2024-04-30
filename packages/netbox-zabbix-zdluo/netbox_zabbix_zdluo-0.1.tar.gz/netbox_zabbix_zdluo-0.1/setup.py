from setuptools import find_packages, setup

setup(
    name='netbox_zabbix_zdluo',  # 与你在__init__.py中定义的插件名称保持一致
    version='0.1',  # 插件版本
    description='A description of your plugin',  # 插件描述
#    url='https://github.com/yourname/netbox_zabbix_plugin',  # 插件的项目主页，如果有的话
    author='zdluo',  # 插件作者的名称
    author_email='zdluo@glprop.com',  # 插件作者的邮箱
    install_requires=[],  # 如果你的插件需要一些额外的Python包，可以在这里列出
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)