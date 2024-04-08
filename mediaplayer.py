import cv2
import PySimpleGUI as sg

class mediaPlayer():

    playImage = b'iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAEAklEQVRYCe1YX2hTVxj/ThJtVWp1Yy/qcE5RoWtiTLral033og/CUOge1QdbUSnrbYftm5GBdmwmVdiDfx6UvinbHoYKgymibrNpar2p2uqGY2OMgdusjlkz7/32O7k9JUrVmp57L8gN33dOvt9Jzv39vpPzL0TBK8hAkIEgA0EGggz4kIFotjVTa3bO9eHREz4yNCE6GVCILaLw8KfanNFMTGIyX3HzM+ULcVjNFUyHojnjq3j/rnkO5E85VSGK9fuW/d+t2r62jsYTjWEFelnrEiI5zxTEXcOLF3wbu9y2VAJeui4hD8ZJM73LYb4a6zM6V59LRcZxl99oEcIhex14HoTbcGmVTLTv76qRGyuyravJg5cWIeFH4p6ZzHwYYn4HnG/AiwYxS2whzsayxqFlF3dVFUGXCi1CFLeBuu5L9+5XryQWe4AV4NIEC2quqCwMxXLGBgm44VqFSII/r0mNmnXpFEYjibgXPmZiHjN9iblzIt7f8toYqK3SLkQxyyczeTNR3YDR2AbsH3jRILDRsiPDxY20iOgpXBNSpCdSdj6ROUxWOAoB3xQxp3A20qxxJt7fvtCBpla6K2SMm1n/2W2M0FqcZD4AdAfumKB1lm1f17GReiLEYU2UT6ZP2o/st3Ay61EYamcjXbTgQqzXqEFclnkqRDIcXHXgDzOR2RQiXo/4V7hjgho4RFewGHQtudVS4YCTLz0XoqgNJLtPFaxCHPFxuLJpTNQxcyTyfSzbJtsU/tzaNyGS2VD9539iI90iiNYivg1XFmfBvbFc2ycN3xkzFPis2lchzyKGtjDZPOfBDK7A++eaZ4e6iZgsv7zz1enh6fuZaPMT7TfZpmbz7cz5J/Cnhv6MCNZhuSFCxI9gVipiFE2dr9yvrsm/gAj0QZ6PiLyrcB8dIVE8YEoOys9agrZdS6SlOIVNuvZMiLw5Dr35+kdMvBvsSifwXzhkGmYy3UO4maGtLPNESG2uPTHM9lHwXPEYS0FfTGNuydVlfn8MLyNwVcgb51KV1VUjKWa7HdxKn/Ubsr8dG+PXwLVYaedaOlSdRHOt7xHfPYzJu1hhqLE90BER4Y6BePddxNpMu5D6H1pmj4Yjn+Lu0QSWAq5sGKPQdDWZuaAAnbXW5TeWa934byQyhDtIM0gqEQVM5j2zChTHT8kVEXiWpuU3RPOjfcbHGIX1ir3snIXIMllbB5MHTBm76Vp+WjaJkyBZuqQ+hKC9VuXsrms1qQLaXDctQsCyVMQlW3DTYKJ7/N8UtLtuuoRIonewQu2QlycZeO16JrugHnnz80uETNpUR+QXZrEdAk7Lzvz08keE+ZiFJTVfl/ZdhJ8JDJ4dZCDIQJCBIAMvRwb+B4AoOR330njlAAAAAElFTkSuQmCC'
    pauseImage = b'iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAABAUlEQVRYCe2ZMQrCQBBF/0gOIdYWHiJga5Mz2HgIj5BD2HiGNJYKe4gUFlbiLcbZwj7+MCDylxl2A/kf9v1UGUBLBERABERABEQANofBs2tbgx2qh8HH5VD6ep7ar649OmxT33f4aTWUUs9MN4zoo4lLrOG+r88O3GLvoyeXO3aAb6vAzK4ASjRVC0r1gyJd5NdCUSJKJImAPq0ksLStEqHRJQmVSBJY2laJ0OiShEokCSxtq0RodElCJZIElrZVIjS6JKESSQJL2yoRGl2SUIkkgaVt/yaRhkYQwhgF3OMv+jmOMZ/wse7ftBkuMVZ4IFb1ik0lAiIgAiIgAiIwh8Absw8i5F6csaMAAAAASUVORK5CYII='
    forwardImage = b'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'
    rewindImage = b'iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAASbSURBVGhD7VprSCNXFDaJWd82+CrEVFYk6lbrCwSF+qigC0VhbRUtVmXFP4VqFPa3rva3tBHBP1JClIpg1UJXhC6GpqJEUKvVqhHW+sqKVVQaHzVqdg7MhbPDTTLRSUgkH3wkc+ac4Xz3nrn3zCQiq9Xq9xAgZj+9Hj4hngafEE+DT4izsFgsUvbrneAo3i1Curu7VW1tbd+xh07h6Ogosry8/JeVlZUU1kQHbIiu4vHxsayiouJnsVhsbW1t/Z7mY496vT4/Li5uB+IXFhYyaD6ELpuR1dXVJ/n5+VMjIyNfsCbeYBITdXV1vSguLn69u7urYM32wVUmBNVqtSo4OPgCRpKQ74zs7e3Ji4qKdDgW6GhGqMa78uzsLLihoeFHbhJAPkJ0Ot1nCoVijxbvttKCUsrNzTVoNJrnrIk3bm5uJO3t7Z0lJSW/mUwmOWt2DjR1zlKr1daFhYWZ8QhCfdfU1PxEjm3NyM7OjqKgoECPY6Ese3t7v4mIiDgmNpeWFl6VCAMDA/+He+T29lYEyRM7Tcjg4OBXMpnsFMdnZWUtrK2tJcF5twiBCycnJ6/jJBISEt7Mzs5mEx9bQsxmc0h9fb0Wx0okkluVSqW+uLgIJH4uF0JblcrKyn49PDyMxH40IYuLi2kpKSl/49ioqKijsbGxZzgW6DIhJycnH9grJa4/FtLS0vIDbQCYveaP7e3tj7ixQJcIYVal5LS0tL9wEnK5/C0smTR/IBYSHR19iGOhlEDc5eVlAC0WKLgQvqXEJRaCGRsba5qcnCyixWAKJuT8/DyosbGxDychlUqvOzo62pm1X0yLwaQJKSws/B2WXJo/l4IIgVJKT09fwklAKfEZSUIsBAaA6YA7r6+vJTRfGu8tZGBg4Ovw8PD/yEWAsMHt7+9/SPO3RSIE2g5795It3lnIfUuJSxBSWlr66uDgIJp23hGdEfJer3V1dfXo9PRUxh56F2jqenp6vg0KCrrEM+NVpYU5NzeXlZiYuEEuBPS6m52QKbPw6urqIXIxkpBXLb+YtDY9JyfHsLm5+ZjmT0gTAoSOFzpfWgym4EKA8/PzmUlJSUackNe1KITQYkOrzU0IbMyKJ+X6YyHwHTpc6HRxPHTCS0tLn3BjgS4TQtjf31/L3TBppcYVAratra24vLy8KRwLfRz0czgW6HIhQHiKy8jIWMQJxcTE/Ds+Pv458aEJAVosFv+XDPz9/W9wfGVl5TA8dRI/twgBOio1W0IIYSmHThjHx8fH/zMzM5ML590mhLCvr68xJCTkHCfkVS8fMNfX1xMzMzP/xAlh2hIChKdLuEcCAgKuaLFAR0IEe6/FdAFGvV7/aW1tbT9r4g2RSGRtbm5WT0xMPGWWdBNrdgqCvvsNDQ01azSauuHh4S+ZTe+ENfMGs+vrlpeXP66qqhpiTfxBmyYhaDQalfCOipSGvdKiEboJZmDO3F5aXCiVyo3p6emcpqambtbkFJgS1RoMhuzU1NRl1mQfNHVCc3R0tBwaTdo5R4SHPVjOHc2I2/75AD+dMbCwh07DUbzvLxyeBp8QT4NPiKfhgQjx83sHmbpg4pwo80UAAAAASUVORK5CYII='


    def __init__(self):
        self.paused = True
        self.rewind = False
        self.fastForward = False
        self.savedFrames = []
        self.subtractedImages = False
        self.noBackgroundFrames = []

    def pause(self):
        self.paused = True
        self.rewind = False
        self.fastForward = False

    def unpause(self):
        self.paused = False

    def rewindVideo(self):
        self.rewind = True
        self.paused = False 
        self.fastForward = False

    def fastForwardVideo(self):
        self.fastForward = True
        self.paused = False 
        self.rewind = False

    def play(self):
        self.paused = False
        self.rewind = False 
        self.fastForward = False

    def updateTime(self):
        time_elapsed = "{:02.0f}:{:02.0f}".format(*divmod(self.video.get(cv2.CAP_PROP_POS_MSEC) // 1000, 60))
        self.window['-TIME_ELAPSED-'].update(time_elapsed)

    def updateCurrentFrameNumber(self, change):
        self.currentFrameNumber = change
    
    def updateSlider(self):
        self.window['-TIME-'].update(self.currentFrameNumber)

    def restartVideo(self):
        self.pause()
        self.updateCurrentFrameNumber(0)
        self.video.set(cv2.CAP_PROP_POS_FRAMES, 0)
        self.updateSlider()
        self.updateTime()

    def saveFrame(self, frame):
        #[0] position should always be the first frame of the video for later subtraction
        self.savedFrames.append(frame)

    def clearSavedFrames(self):
        self.savedFrames = []
        self.subtractedImages = False
        self.noBackgroundFrames = []

    def subtractBackground(self):
        self.subtractedImages = True
        tempList = []
        backgroundFrame = None
        i = 0
        for frame in self.savedFrames:
            if i == 0:
                backgroundFrame = frame
            else:
               tempList.append(cv2.subtract(backgroundFrame, frame)) 
            i += 1

        self.noBackgroundFrames = tempList

    def showSingleFrame(self, subtracted):
        # TO show the output 
        cv2.imshow('image', subtracted) 
  
        # To close the window 
        cv2.waitKey(0) 
        cv2.destroyAllWindows() 

    def openFile(self):
        layout = [
        [sg.Input(), sg.FileBrowse('Browse')],
        [sg.Submit(), sg.Cancel()],
        ]

        self.window = sg.Window('File Select', layout)

        while True:
            event, value = self.window.read()     
            if event is None or event == 'Cancel':
                exit()
            
            if event == 'Submit': 
                filename = value[0] #save the one selected file
                break
        
        self.window.close()
        return filename
    
    def drawVideoToGraph(self, frame):
        #Drawing frame on graphs
        if self.currentFrameNumber >= self.totalFrames:
            #Video end was reached so stay on last frame
            self.video.set(cv2.CAP_PROP_POS_FRAMES, self.totalFrames - 1) 
        imgbytes = cv2.imencode('.ppm', frame)[1].tobytes()
        if self.a_id:
            self.graph_elem.delete_figure(self.a_id)  # delete previous image
        self.a_id = self.graph_elem.draw_image(data=imgbytes, location=(0, 0))  # draw new image
        self.graph_elem.send_figure_to_back(self.a_id)  # move image to the "bottom" of all other drawings

    def drawFrameToMeasure(self, frame, setting=None):
        #convert frame to gray scale
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #apply changes to frame
        if setting == '-THRESH-':
            frame = cv2.threshold(frame, self.threshSlider, 255, cv2.THRESH_BINARY)[1]
        elif setting == '-CANNY-':
            frame = cv2.Canny(frame, self.cannySliderA, self.cannySliderB)

        imgbytes = cv2.imencode('.png', frame)[1].tobytes()
        if self.measure_a_id:
            self.measure_graph_elem.delete_figure(self.measure_a_id)  # delete previous image
        self.measure_a_id = self.measure_graph_elem.draw_image(data=imgbytes, location=(0, 0))  # draw new image
        self.measure_graph_elem.send_figure_to_back(self.measure_a_id)
        

    def openMeasureWindow(self, frameList):
        framesToMeasure = frameList
        sg.theme('DarkTeal6')
        self.layout = [[sg.Button('Exit Measure Mode', key='-CLOSE-')],
                [sg.Graph((self.video.get(cv2.CAP_PROP_FRAME_WIDTH), self.video.get(cv2.CAP_PROP_FRAME_HEIGHT)), (0, self.video.get(cv2.CAP_PROP_FRAME_HEIGHT)), (self.video.get(cv2.CAP_PROP_FRAME_WIDTH), 0), key='-GRAPH-', enable_events=True, drag_submits=True)],
                [sg.Button(key='-BACK-', image_data=self.rewindImage), sg.Button(key='-FORWARD-', image_data=self.forwardImage)],
                [sg.Radio('None', 'Radio', True, size=(10, 1))],
                [sg.Radio('threshold', 'Radio', size=(10, 1), key='-THRESH-'),
                sg.Slider((0, 255), 128, 1, orientation='h', size=(40, 15), key='-THRESH SLIDER-')],
                [sg.Radio('canny', 'Radio', size=(10, 1), key='-CANNY-'),
                sg.Slider((0, 255), 128, 1, orientation='h', size=(20, 15), key='-CANNY SLIDER A-'),
                sg.Slider((0, 255), 128, 1, orientation='h', size=(20, 15), key='-CANNY SLIDER B-')]]

        self.measureWindow = sg.Window('SFI Measure Mode', self.layout, resizable=True, element_justification='c', return_keyboard_events=True)
        self.measure_graph_elem = self.measureWindow['-GRAPH-']
        self.measure_a_id = None

        self.measureFramesTotal = len(framesToMeasure)
        self.currentMeasureFrame = 0
        event, values = self.measureWindow.read(timeout=0)
        self.drawFrameToMeasure(frame=framesToMeasure[self.currentMeasureFrame])

        while True:
            try:
                event, values = self.measureWindow.read(timeout=0) 

                if event in ('Exit', None) or event == '-CLOSE-':
                    break

                elif event == '-BACK-' or event == 'Left:37':
                    if self.currentMeasureFrame > 0:
                        self.currentMeasureFrame -= 1
                    print(self.currentMeasureFrame)
                    self.drawFrameToMeasure(frame=framesToMeasure[self.currentMeasureFrame])

                elif event == '-FORWARD-' or event == 'Right:39':
                    if self.currentMeasureFrame < self.measureFramesTotal - 1:
                        self.currentMeasureFrame += 1
                    print(self.currentMeasureFrame)
                    self.drawFrameToMeasure(frame=framesToMeasure[self.currentMeasureFrame])

                elif event == '-DELETEFRAME-':
                    if len(framesToMeasure) != 0:
                        del framesToMeasure[self.currentMeasureFrame]
                        self.measureFramesTotal -= 1
                        if self.currentMeasureFrame != 0:
                            self.currentMeasureFrame -= 1
                    if len(framesToMeasure) == 0:
                         break
                    else:
                        self.drawFrameToMeasure(frame=framesToMeasure[self.currentMeasureFrame])

                elif values['-THRESH-']:
                    self.threshSlider = values['-THRESH SLIDER-']
                    self.drawFrameToMeasure(frame=framesToMeasure[self.currentMeasureFrame], setting='-THRESH-')
                elif values['-CANNY-']:
                    self.cannySliderA = values['-CANNY SLIDER A-']
                    self.cannySliderB = values['-CANNY SLIDER B-']
                    self.drawFrameToMeasure(frame=framesToMeasure[self.currentMeasureFrame], setting='-CANNY-')                

                #draw on graph TODO
                if event == '-GRAPH-':
                    self.measure_graph_elem.draw_circle(values['-GRAPH-'], 5, fill_color='red', line_color='red')
            except Exception as err:
                print(sg.popup_error(f"Unexpected {err=}, {type(err)=}"))
        self.measureWindow.close()


    def showVideo(self):
        # select video to show
        chosenVideoPath = self.openFile()  

        #open video and get video prop
        self.video = cv2.VideoCapture(chosenVideoPath)
        if not self.video.isOpened():
            self.window.close()
            self.video.release()
            cv2.destroyAllWindows()
            self.showVideo()
            raise ValueError(f"Failed to open media: {chosenVideoPath}")
        self.totalFrames = self.video.get(cv2.CAP_PROP_FRAME_COUNT)
        fps = self.video.get(cv2.CAP_PROP_FPS)

        #Create window
        sg.theme('DarkTeal6')
        self.layout = [[sg.Button('Open video')],
                [sg.Graph((self.video.get(cv2.CAP_PROP_FRAME_WIDTH), self.video.get(cv2.CAP_PROP_FRAME_HEIGHT)), (0, self.video.get(cv2.CAP_PROP_FRAME_HEIGHT)), (self.video.get(cv2.CAP_PROP_FRAME_WIDTH), 0), key='-GRAPH-', enable_events=True, drag_submits=True)],
                [sg.Text('00:00', key='-TIME_ELAPSED-'), sg.Slider(range=(0, self.totalFrames - 1), enable_events=True, resolution=0.0001, disable_number_display=True,
                        background_color='#83D8F5', orientation='h', key='-TIME-', size=(self.video.get(cv2.CAP_PROP_FRAME_WIDTH) * 0.073, 20))],
                [sg.Button(key='-REWIND-', image_data=self.rewindImage), sg.Button(image_data=self.playImage, key= '-PLAY-'), sg.Button(image_data=self.pauseImage, key='-PAUSE-'),sg.Button(key='-FASTFORWARD-', image_data=self.forwardImage),  sg.Button('Restart')],
                [sg.Button('Measure Mode', key='-MEASURE-'),  sg.Button('Save Frame', key='-SAVEFRAME-'), sg.Button('Clear Saved Frames', key='-CLEARSAVEDFRAMES-'), sg.Button('Display Single Frame', key='-DISPLAYFRAME-'), sg.Button('Subtract', key='-SUBTRACT-')]]
        self.window = sg.Window('SFI Calculator', self.layout, resizable=True, element_justification='c', return_keyboard_events=True)
        self.graph_elem = self.window['-GRAPH-']
        self.a_id = None

        self.pause()
        ret, frame = self.video.read() #get first frame of video
        self.updateCurrentFrameNumber(1)

        # show video
        while True:
            try:
                event, values = self.window.read(timeout=0)

                if not self.paused and not self.rewind and not self.fastForward:
                    ret, frame = self.video.read()
                    self.updateCurrentFrameNumber(self.currentFrameNumber + 1)
                    self.updateTime()
                    
                elif self.rewind:
                    ret, frame = self.video.read()
                    self.updateCurrentFrameNumber(self.currentFrameNumber - fps)
                    if self.currentFrameNumber < 0:
                        self.currentFrameNumber = 0
                    self.video.set(cv2.CAP_PROP_POS_FRAMES, int(self.currentFrameNumber))
                    self.updateTime()
                    self.updateSlider()

                elif self.fastForward:
                    ret, frame = self.video.read()
                    self.updateCurrentFrameNumber(self.currentFrameNumber + fps)
                    if self.currentFrameNumber > self.totalFrames:
                        self.currentFrameNumber = self.totalFrames
                    self.video.set(cv2.CAP_PROP_POS_FRAMES, int(self.currentFrameNumber))
                    self.updateTime()
                    self.updateSlider()

                if event in ('Exit', None):
                    break
            
                elif event == '-TIME-':
                    self.video.set(cv2.CAP_PROP_POS_FRAMES, int(values['-TIME-'] - 1))
                    self.updateCurrentFrameNumber(int(values['-TIME-'] - 1))
                    self.updateSlider()
                    self.updateTime()
                    self.unpause()
                            
                elif event == 'Restart':
                    self.restartVideo()
                
                elif event == '-REWIND-':
                    self.rewindVideo()

                elif event == '-FASTFORWARD-':
                    self.fastForwardVideo()

                #Open new video
                elif event == 'Open video':
                    self.window.close()
                    self.video.release()
                    cv2.destroyAllWindows()
                    self.showVideo()
                    break  

                #Play/pause button interaction 
                elif event == '-PLAY-' or (event == ' ' and self.paused):#space key
                    self.play()

                elif event == '-PAUSE-' or (event == ' ' and not self.paused): 
                    self.pause()

                elif event == '-MEASURE-':
                    self.pause()
                    if len(self.noBackgroundFrames) > 0:
                        self.openMeasureWindow(self.noBackgroundFrames)     
                    elif len(self.savedFrames) > 0:
                        self.openMeasureWindow(self.savedFrames)
                    else:
                        print(sg.popup_auto_close('Frames must be saved before measuring can be done.'))

                #move 1 frame either forwards or backwards using the arrow keys
                if (event == 'Left:37'):
                    self.paused = True
                    ret, frame = self.video.read()
                    self.updateCurrentFrameNumber(self.currentFrameNumber - 1)
                    if self.currentFrameNumber < 0:
                        self.currentFrameNumber = 0
                    self.video.set(cv2.CAP_PROP_POS_FRAMES, int(self.currentFrameNumber))
                    self.updateSlider()
                    self.updateTime()
                                                                                        
                elif (event == 'Right:39'):
                    self.paused = True
                    ret, frame = self.video.read()
                    self.updateCurrentFrameNumber(self.currentFrameNumber + 1)
                    if self.currentFrameNumber > self.totalFrames:
                        self.currentFrameNumber = self.totalFrames
                    self.video.set(cv2.CAP_PROP_POS_FRAMES, int(self.currentFrameNumber))
                    self.updateSlider()
                    self.updateTime()

                elif (event == '-DISPLAYFRAME-'):
                    if self.subtractedImages:
                        for frame in self.noBackgroundFrames:
                            self.showSingleFrame(frame)
                    else:
                        for frame in self.savedFrames:
                            self.showSingleFrame(frame)

                elif (event == '-SAVEFRAME-'):
                    self.saveFrame(frame)
                
                elif (event == '-CLEARSAVEDFRAMES-'):
                    self.clearSavedFrames()

                elif (event == '-SUBTRACT-'):
                    self.subtractBackground()

                self.drawVideoToGraph(frame)
            except Exception as err:
                print(sg.popup_error(f"Unexpected {err=}, {type(err)=}"))
                break

        self.window.close()

        self.video.release()
        cv2.destroyAllWindows()