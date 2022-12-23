python3 -m pytest Tests/UnitTests/GuideServiceUnitTest.py --alluredir=allure-results
python3 -m pytest Tests/UnitTests/GuideUnitTest.py --alluredir=allure-results
allure generate allure-results
allure serve allure-results