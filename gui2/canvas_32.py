from tkinter import *
import canvas_30 as canvasDraw_tags
import _thread, time
class CanvasEventsDemo(canvasDraw_tags.CanvasEventsDemo):
    def moveEm(self, tag):
        for i in range(5):
            for (diffx, diffy) in [(+20, 0), (0, +20), (-20, 0), (0, -20)]:
                self.canvas.move(tag, diffx, diffy)
                time.sleep(0.25) # pause this thread only
    def moveInSquares(self, tag):
        _thread.start_new_thread(self.moveEm, (tag,))
if __name__ == '__main__':
    CanvasEventsDemo()
    mainloop()