
class RTT():
    def __init__(self):
        self.RTTs=0
        self.RTTd=0
        self.RTO = 0
        self.RTTm=0
        self.output = ""
        self.check = True
    def firstRTT(self):
        if self.RTTs==0 :
            self.RTTs=self.RTTm
            self.RTTd=self.RTTm/2
        self.output+='RTTm: '+str(round(self.RTTm,1))+' RTTs: '+str(round(self.RTTs,1))+'\nRTTd: '+str(round(self.RTTd,1))+' RTO: '+str(round(self.RTO,1))+"\n"
        return self.output

    def otherRTT(self):
        if self.RTTm>self.RTO:
                self.RTO*=2
        else :
            self.RTTs=0.875*self.RTTs+0.125*self.RTTm
            self.RTTd=0.75*self.RTTd+0.25*abs(self.RTTs-self.RTTm)
            self.RTO=self.RTTs+self.RTTd*4
        self.output+='RTTm: '+str(round(self.RTTm,1))+' RTTs: '+str(round(self.RTTs,1))+'\nRTTd: '+str(round(self.RTTd,1))+' RTO: '+str(round(self.RTO,1))+"\n"
        return self.output
        
    def reset(self):
        self.RTTs=0
        self.RTTd=0
        self.RTO = 0
        self.RTTm=0
        self.output = ""
        self.check=True
        return self.output