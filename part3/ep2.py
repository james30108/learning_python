# โปรแกรมบัญชีธนาคาร


account = {"นายA" : 5000, "นายB" : 0}

def getBalance () :
    print ("ยอดเงินคงเหลือ = ", account)

def deposit (money) :
    if money <= 0 :
        raise Exception ("ยอดเงินที่ฝากต้องมากกว่า 0")
    print ("ฝากเงินเข้าบัญี A", money)
    account["นายA"] += money

def franfer (monney) :
    print ("โอนเงินไป B", money)
    account["นายB"] += monney
    account["นายA"] -= monney


try :
    getBalance ()
    deposit (1000)
    getBalance ()
except Exception as e :
    print (e)