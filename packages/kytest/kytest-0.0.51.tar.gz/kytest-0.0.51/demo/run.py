import kytest


if __name__ == '__main__':
    # 主程序入口

    # android
    kytest.main(
        proj='平台',
        path="tests/test_adr.py",
        did=["UJK0220521066836", 'e6b6fc7d'],
        pkg="com.qizhidao.clientapp",
        rule="split_parallel"
    )

    # api
    kytest.main(
        proj='平台',
        path="tests/test_api.py",
        host='https://app-test.qizhidao.com'
    )

    # web
    kytest.main(
        proj='平台',
        path="tests/test_web.py",
        host="https://www-test.qizhidao.com/",
    )
