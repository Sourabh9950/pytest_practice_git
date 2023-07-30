from selenium import webdriver

class Test_Credence:

    def test_sum_01(self):
        a = 3
        b = 7
        sum = a+b
        print("sum of a and b is :"+ str(sum))
        if sum == 10:
            assert True
        else:
            assert False



    def test_credence_url_02(self):
        driver = webdriver.Chrome()
        driver.get("http://credence.in/")
        if driver.title == "Credence" :
            print("you are at credence.in")
        else:
            print("you are at wrong url")


