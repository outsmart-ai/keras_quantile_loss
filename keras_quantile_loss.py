import keras.backend as K


class QR:
    def __init__(self, a):
        self.alpha = a
    

    def func(self, true, pred):
        try:
            true = np.array(true)
            pred = np.array(pred)
        except:
            raise ValueError
            
        flag = (true-pred > 0).astype(int)
    
        prefactor = self.alpha*flag + (1.-self.alpha)*(1-flag)
        return prefactor * abs(true-pred)

        return x + self.alpha * y


    def qloss(self):
        return self.func


if __name__ == "__main__":
    ex_true = [1,0,0]
    ex_pred = [0,1,0]
    q = QR(0.9)
    ff = q.get_func()
    ff(ex_true, ex_pred)