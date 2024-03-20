import tkinter as tk
self._customGUI = Tk(baseName="userGUIs")
arrowX = self._customGUI.winfo_pointerx()
self._customGUI.protocol('WM_DELETE_WINDOW', self._abnormAbort)
self._customGUI.title("Blend Models")

### Center the user GUI on the screen ###
totWidth = self._customGUI.winfo_screenwidth(S
middlePoint = totWidth / 2
if arrowX >= middlePoint:
    useWidth = middlePoint
else:
    useWidth = 0
self._guiXPos = useWidth

### Size of initial user GUI
self._setupGUIheight = 425
self._setupGUIwidth = 325
self._customGUI.geometry("%dx%d+%d+%d" % (self._setupGUIwidth, self._setupGUIheight, self._guiXPos, 0))

### Create a canvas within the main GUI defined early for widget organization ###
self._buttonCanvas = Canvas(self._customGUI, borderwidth=0)
### Create a frame to put in the Canvas
self._buttonFrame = Frame(self._buttonCanvas)
### Create a vertical scrollbar
self._vertScroll = Scrollbar(self._customGUI, orient="vertical", width=18, command=self._buttonCanvas.yview)
self._buttonCanvas.configure(yscrollcommand=self._vertScroll.set)
self._vertScroll.pack(side="right", fill="y")
self._buttonCanvas.pack(side="left", fill="both", expand=True)
self._buttonCanvas.create_window((0, 0), window=self._buttonFrame, anchor="nw")
self._buttonFrame.bind("<Configure>", lambda event, canvas=self._buttonCanvas: self._buttonCanvas.configure(
    scrollregion=self._buttonCanvas.bbox("all")))
self._buttonFrame.bind("<Button-4>",
                       lambda event, canvas=self._buttonCanvas: self._buttonCanvas.yview('scroll', -1, 'units'))
self._buttonFrame.bind("<Button-5>",
                       lambda event, canvas=self._buttonCanvas: self._buttonCanvas.yview('scroll', 1, 'units'))