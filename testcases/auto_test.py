# -*- coding:utf8 -*-

import pytest
import sys
import allure
sys.path.append('..')
from utils.log import md_logger
logger = md_logger(__name__)


def test_al():
    logger.error('sdfasd')
    assert 1 == 2


@pytest.mark.skip(reason='test skip')
def test_2():
    pass


@pytest.mark.skipif(2 > 1, reason='1不大于2')
def test_3():
    pass


@pytest.mark.xfail(1 < 2, reason='111')
def test_4():
    assert 1 == 2


# 参数化
@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_5(test_input, expected):
    assert eval(test_input) == expected


# 参数化标记，mark标记，id使用例更好识别
@pytest.mark.parametrize(
    "test_input,expected",
    [("3+5", 8), ("2+4", 6),
     pytest.param("6*9", 54, marks=pytest.mark.xfail),
     pytest.param("6*9", 54, id="ttt", marks=pytest.mark.xfail)],
)
def test_6(test_input, expected):
    assert eval(test_input) == expected


# 笛卡尔积
@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_7(x, y):
    pass


def test_8(fixture1):
    print('running')
    assert 1 == 1


# fixture1会应用到类的所有方法中
@pytest.mark.usefixtures('fixture1')
class TestClassScope:
    def test_1(self):
        pass

    def test_2(self):
        pass


# 内置固件
def test_tmpdir(tmpdir):
    print('test tmpdir')
    a_dir = tmpdir.mkdir('mytmpdir')
    print(a_dir)
    a_file = a_dir.join('tmpfile.txt')
    print(a_file)
    a_file.write('hello, pytest!')

    assert a_file.read() == 'hello, pytest!'


@allure.step("第二步")
def test_function():
    n = 1
    while True:
        print("这是我第{}条用例".format(n))
        n += 1
        if n == 5:
            pytest.skip("我跑五次了不跑了")


@pytest.mark.mark
def test_mark_1():
    print('mark 1')
    assert 1 == 1


@pytest.mark.mark
def test_mark_2():
    print('mark 2')
    assert 1 == 1


if __name__ == '__main__':
    """
    1. 直接执行pytest.main() 【自动查找当前目录下，以test_开头的文件或者以_test结尾的py文件】
    2. 设置pytest的执行参数 pytest.main(['--html=./allure_results.html','test_login.py'])【执行test_login.py文件，并生成html格式的报告】
    3. 运行目录及子包下的所有用例  pytest.main(['目录名'])
    4. 运行指定模块所有用例  pytest.main(['test_reg.py'])
    5. 运行指定模块指定类指定用例  pytest.main(['test_reg.py::TestClass::test_method'])  冒号分割
    6.  -m=xxx: 运行打标签的用例
        -reruns=xxx，失败重新运行
    
        -q: 安静模式, 不输出环境信息
        -v: 丰富信息模式, 输出更详细的用例执行信息
        -s: 显示程序中的print/logging输出
        --resultlog=./log.txt 生成log
        --junitxml=./log.xml 生成xml报告
    

    """
    pytest.main(['-s', '-v', '--alluredir', './allure_results/xml'])
    # pytest.main(['-m=mark', '-s', '-v', '--alluredir', './allure_results/xml'])  # 执行带有mark标记的用例
    # pytest.main(['-m=not mark', '-s', '-v', '--alluredir', './allure_results/xml'])  # 执行不带mark标记的用例
    # pytest.main(['-m=mark or mark1', '-s', '-v', '--alluredir', './allure_results/xml'])  # 执行带mark和mark1标记的用例

