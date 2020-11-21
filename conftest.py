# -*- coding:utf8 -*-
"""
专门存放fixture的配置文件
1. pytest 会在执行测试函数之前（或之后）加载运行它们
2. 如何在执行前或后运行他们么？Pytest 使用 yield 关键词将固件分为两部分，yield 之前的代码属于预处理，会在测试前执行；yield 之后的代码属于后处理，将在测试完成后执行。
比如每个用例都要ssh到PCU环境上，就可以把fixture放到这里
3. pytest会默认读取conftest.py中的所有fixture
4. conftest.py只有一个package下的所有测试用例生效
5. 不同目录可以有自己的conftest.py
6. 测试用例不需要手动导入conftest.py，pytest会自己找
7. 在定义固件时，通过 scope 参数声明作用域，可选项有：

    function: 函数级，每个测试函数都会执行一次固件；默认的作用域
    class: 类级别，每个测试类执行一次，所有方法都可以使用；
    module: 模块级，每个模块执行一次，模块内函数和方法都可使用；
    session: 会话级，一次测试只执行一次，所有被找到的函数和方法都可用。
8. 如何固件自动执行？定义时指定 autouse 参数，例子timer_session_scope1，timer_session_scope
9. 固件重命名，通过 name 选项指定名称，例子：calculate_average_age
10. 固件也可以参数化，固件参数化需要使用 pytest 内置的固件 request，并通过 request.param 获取参数
11. 内置固件,
    tmpdir(只有函数作用域) & tmpdir_factory（作用域function, class, module, session）
    pytestconfig 可以很方便的读取命令行参数和配置文件
"""

import pytest
import time


@pytest.fixture
def fixture1(scope='function'):
    print('I am fixture1')
    yield
    print('fixture1 end')


@pytest.fixture
def fixture2():
    print('I am fixture2')


DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
#
#
# @pytest.fixture(scope='class', autouse=True)
# def timer_session_scope1():
#     start = time.time()
#     print('\nstart: {}'.format(time.strftime(DATE_FORMAT, time.localtime(start))))
#
#     yield
#
#     finished = time.time()
#     print('finished: {}'.format(time.strftime(DATE_FORMAT, time.localtime(finished))))
#     print('Total time cost: {:.3f}s'.format(finished - start))
#
#


@pytest.fixture(autouse=True)
def timer_function_scope():
    start = time.time()
    yield
    print(' Time cost: {:.3f}s'.format(time.time() - start))


@pytest.fixture(name='age')
def calculate_average_age():
    return 28


@pytest.fixture(params=[
    ('redis', '6379'),
    ('elasticsearch', '9200')
])
def param(request):
    return request.param


# @pytest.fixture(autouse=True)
# def db(param):
#     print('\nSucceed to connect %s:%s' % param)
#
#     yield
#
#     print('\nSucceed to close %s:%s' % param)


@pytest.fixture(scope='module')
def my_tmpdir_factory(tmpdir_factory):
    a_dir = tmpdir_factory.mktemp('mytmpdir')
    a_file = a_dir.join('tmpfile.txt')

    a_file.write('hello, pytest!')

    return a_file
