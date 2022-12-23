python3 -m pytest Tests/UnitTests/GuideServiceUnitTest.py --alluredir=allure-results
python3 -m pytest Tests/UnitTests/GuideUnitTest.py --alluredir=allure-results

python3 -m pytest Tests/IntTests/integration_tests.py --alluredir=allure-results
python3 -m pytest Tests/IntTests/integration_tests_mock.py --alluredir=allure-results

python3 -m pytest Tests/E2E/testAll.py --alluredir=allure-results

allure serve allure-results