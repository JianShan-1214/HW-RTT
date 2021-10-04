import tkinter as tk
import tkinter.messagebox as messagebox
import hw

def window():
    root = tk.Tk()
    RTT = hw.RTT()
    labelWidth = tk.Label(text="RTTm")
    labelWidth.grid(column=0, row=1, ipadx=5, pady=5, sticky=tk.W+tk.N)
    labelHeight = tk.Label(text="INIT RTO")
    labelHeight.grid(column=0, row=0, ipadx=5, pady=5, sticky=tk.W+tk.S)
    
    inputRTTm = tk.Text( width=20, height=1 ,highlightbackground="black",bd=0.5)
    inputRTO = tk.Text( width=20, height=1 ,highlightbackground="black",bd=0.5)

    inputRTTm.grid(column=1, row=1, padx=10, pady=5, sticky=tk.N)
    inputRTO.grid(column=1, row=0, padx=10, pady=5, sticky=tk.S)
    def resetButton():
        check = messagebox.askokcancel("Reset ALL","你確定要刪除歷史記錄嗎")
        if check:
            output = RTT.reset()
            labelAns.configure(text=output)
            

    def resultButton():

        if RTT.check:
            RTT.RTTm = int(inputRTTm.get(1.0,"end"))
            RTT.RTO = int(inputRTO.get(1.0,"end"))
            output = RTT.firstRTT()
            RTT.check = False
        else:
            RTT.RTTm = int(inputRTTm.get(1.0,"end"))
            output = RTT.otherRTT()
        labelAns.configure(text=output)
        
    resultButton = tk.Button( text='Result',command = resultButton)
    resetButton = tk.Button( text='Reset' , command = resetButton)
    resultButton.grid(column=0, row=2, pady=10, sticky=tk.E)
    resetButton.grid(column=1, row=2, pady=10, sticky=tk.W)
    labelAns = tk.Label(text="")
    labelAns.grid(row=3,column=0)

    root.mainloop()

window()