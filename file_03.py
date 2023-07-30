class Test_Credence:

    def test_sub_01(self):
        a = 3
        b = 7
        sub = a-b
        print("sum of a and b is :"+ str(sub))
        if sub == 10:
            assert True
        else:
            assert False