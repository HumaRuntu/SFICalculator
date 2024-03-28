import cv2
import PySimpleGUI as sg
from os import listdir

def openFile():
    layout = [
    [sg.Input(), sg.FileBrowse('Browse')],
    [sg.Submit(), sg.Cancel()],
    ]

    window = sg.Window('File Select', layout)

    while True:
        event, value = window.read()     
        if event is None or event == 'Cancel':
            exit()
        
        if event == 'Submit': 
            filename = value[0] #save the one selected file
            break
    
    window.close()
    return filename


def calculate_sfi(etof, ntof, npl, epl, ets, nts, eit, nit):
    #TODO
    """
    Calculates the Sciatic Function Index (SFI) based on input parameters.
    :param etof: Experimental TOF (orthogonal distance)
    :param ntof: Normal TOF (orthogonal distance)
    :param npl: Normal print length
    :param epl: Experimental print length
    :param ets: Experimental total spread
    :param nts: Normal total spread
    :param eit: Experimental intermediate toes
    :param nit: Normal intermediate toes
    """
    sfi = ((etof - ntof) / ntof) + ((npl - epl) / epl) + ((ets - nts) / nts) + ((eit - nit) / nit) * 220
    return sfi

def showVideo():
    playImage = b'iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAEAklEQVRYCe1YX2hTVxj/ThJtVWp1Yy/qcE5RoWtiTLral033og/CUOge1QdbUSnrbYftm5GBdmwmVdiDfx6UvinbHoYKgymibrNpar2p2uqGY2OMgdusjlkz7/32O7k9JUrVmp57L8gN33dOvt9Jzv39vpPzL0TBK8hAkIEgA0EGggz4kIFotjVTa3bO9eHREz4yNCE6GVCILaLw8KfanNFMTGIyX3HzM+ULcVjNFUyHojnjq3j/rnkO5E85VSGK9fuW/d+t2r62jsYTjWEFelnrEiI5zxTEXcOLF3wbu9y2VAJeui4hD8ZJM73LYb4a6zM6V59LRcZxl99oEcIhex14HoTbcGmVTLTv76qRGyuyravJg5cWIeFH4p6ZzHwYYn4HnG/AiwYxS2whzsayxqFlF3dVFUGXCi1CFLeBuu5L9+5XryQWe4AV4NIEC2quqCwMxXLGBgm44VqFSII/r0mNmnXpFEYjibgXPmZiHjN9iblzIt7f8toYqK3SLkQxyyczeTNR3YDR2AbsH3jRILDRsiPDxY20iOgpXBNSpCdSdj6ROUxWOAoB3xQxp3A20qxxJt7fvtCBpla6K2SMm1n/2W2M0FqcZD4AdAfumKB1lm1f17GReiLEYU2UT6ZP2o/st3Ay61EYamcjXbTgQqzXqEFclnkqRDIcXHXgDzOR2RQiXo/4V7hjgho4RFewGHQtudVS4YCTLz0XoqgNJLtPFaxCHPFxuLJpTNQxcyTyfSzbJtsU/tzaNyGS2VD9539iI90iiNYivg1XFmfBvbFc2ycN3xkzFPis2lchzyKGtjDZPOfBDK7A++eaZ4e6iZgsv7zz1enh6fuZaPMT7TfZpmbz7cz5J/Cnhv6MCNZhuSFCxI9gVipiFE2dr9yvrsm/gAj0QZ6PiLyrcB8dIVE8YEoOys9agrZdS6SlOIVNuvZMiLw5Dr35+kdMvBvsSifwXzhkGmYy3UO4maGtLPNESG2uPTHM9lHwXPEYS0FfTGNuydVlfn8MLyNwVcgb51KV1VUjKWa7HdxKn/Ubsr8dG+PXwLVYaedaOlSdRHOt7xHfPYzJu1hhqLE90BER4Y6BePddxNpMu5D6H1pmj4Yjn+Lu0QSWAq5sGKPQdDWZuaAAnbXW5TeWa934byQyhDtIM0gqEQVM5j2zChTHT8kVEXiWpuU3RPOjfcbHGIX1ir3snIXIMllbB5MHTBm76Vp+WjaJkyBZuqQ+hKC9VuXsrms1qQLaXDctQsCyVMQlW3DTYKJ7/N8UtLtuuoRIonewQu2QlycZeO16JrugHnnz80uETNpUR+QXZrEdAk7Lzvz08keE+ZiFJTVfl/ZdhJ8JDJ4dZCDIQJCBIAMvRwb+B4AoOR330njlAAAAAElFTkSuQmCC'
    pauseImage = b'iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAABAUlEQVRYCe2ZMQrCQBBF/0gOIdYWHiJga5Mz2HgIj5BD2HiGNJYKe4gUFlbiLcbZwj7+MCDylxl2A/kf9v1UGUBLBERABERABEQANofBs2tbgx2qh8HH5VD6ep7ar649OmxT33f4aTWUUs9MN4zoo4lLrOG+r88O3GLvoyeXO3aAb6vAzK4ASjRVC0r1gyJd5NdCUSJKJImAPq0ksLStEqHRJQmVSBJY2laJ0OiShEokCSxtq0RodElCJZIElrZVIjS6JKESSQJL2yoRGl2SUIkkgaVt/yaRhkYQwhgF3OMv+jmOMZ/wse7ftBkuMVZ4IFb1ik0lAiIgAiIgAiIwh8Absw8i5F6csaMAAAAASUVORK5CYII='
    forwardImage = b'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'
    rewindImage = b'iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAASbSURBVGhD7VprSCNXFDaJWd82+CrEVFYk6lbrCwSF+qigC0VhbRUtVmXFP4VqFPa3rva3tBHBP1JClIpg1UJXhC6GpqJEUKvVqhHW+sqKVVQaHzVqdg7MhbPDTTLRSUgkH3wkc+ac4Xz3nrn3zCQiq9Xq9xAgZj+9Hj4hngafEE+DT4izsFgsUvbrneAo3i1Curu7VW1tbd+xh07h6Ogosry8/JeVlZUU1kQHbIiu4vHxsayiouJnsVhsbW1t/Z7mY496vT4/Li5uB+IXFhYyaD6ELpuR1dXVJ/n5+VMjIyNfsCbeYBITdXV1vSguLn69u7urYM32wVUmBNVqtSo4OPgCRpKQ74zs7e3Ji4qKdDgW6GhGqMa78uzsLLihoeFHbhJAPkJ0Ot1nCoVijxbvttKCUsrNzTVoNJrnrIk3bm5uJO3t7Z0lJSW/mUwmOWt2DjR1zlKr1daFhYWZ8QhCfdfU1PxEjm3NyM7OjqKgoECPY6Ese3t7v4mIiDgmNpeWFl6VCAMDA/+He+T29lYEyRM7Tcjg4OBXMpnsFMdnZWUtrK2tJcF5twiBCycnJ6/jJBISEt7Mzs5mEx9bQsxmc0h9fb0Wx0okkluVSqW+uLgIJH4uF0JblcrKyn49PDyMxH40IYuLi2kpKSl/49ioqKijsbGxZzgW6DIhJycnH9grJa4/FtLS0vIDbQCYveaP7e3tj7ixQJcIYVal5LS0tL9wEnK5/C0smTR/IBYSHR19iGOhlEDc5eVlAC0WKLgQvqXEJRaCGRsba5qcnCyixWAKJuT8/DyosbGxDychlUqvOzo62pm1X0yLwaQJKSws/B2WXJo/l4IIgVJKT09fwklAKfEZSUIsBAaA6YA7r6+vJTRfGu8tZGBg4Ovw8PD/yEWAsMHt7+9/SPO3RSIE2g5795It3lnIfUuJSxBSWlr66uDgIJp23hGdEfJer3V1dfXo9PRUxh56F2jqenp6vg0KCrrEM+NVpYU5NzeXlZiYuEEuBPS6m52QKbPw6urqIXIxkpBXLb+YtDY9JyfHsLm5+ZjmT0gTAoSOFzpfWgym4EKA8/PzmUlJSUackNe1KITQYkOrzU0IbMyKJ+X6YyHwHTpc6HRxPHTCS0tLn3BjgS4TQtjf31/L3TBppcYVAratra24vLy8KRwLfRz0czgW6HIhQHiKy8jIWMQJxcTE/Ds+Pv458aEJAVosFv+XDPz9/W9wfGVl5TA8dRI/twgBOio1W0IIYSmHThjHx8fH/zMzM5ML590mhLCvr68xJCTkHCfkVS8fMNfX1xMzMzP/xAlh2hIChKdLuEcCAgKuaLFAR0IEe6/FdAFGvV7/aW1tbT9r4g2RSGRtbm5WT0xMPGWWdBNrdgqCvvsNDQ01azSauuHh4S+ZTe+ENfMGs+vrlpeXP66qqhpiTfxBmyYhaDQalfCOipSGvdKiEboJZmDO3F5aXCiVyo3p6emcpqambtbkFJgS1RoMhuzU1NRl1mQfNHVCc3R0tBwaTdo5R4SHPVjOHc2I2/75AD+dMbCwh07DUbzvLxyeBp8QT4NPiKfhgQjx83sHmbpg4pwo80UAAAAASUVORK5CYII='

    # choose and read video
    chosenVideoPath = openFile()  # select video to show
    video = cv2.VideoCapture(chosenVideoPath)
    if not video.isOpened():
        window.close()
        video.release()
        cv2.destroyAllWindows()
        showVideo()
        raise ValueError(f"Failed to open media: {chosenVideoPath}")
    totalFrames = video.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = video.get(cv2.CAP_PROP_FPS)
    fastFowardSpeed = 1000 #Speed for fastforward or rewind

    #Create window
    sg.theme('DarkTeal6')
    layout = [[sg.Button('Open video')],
              [sg.Graph((video.get(cv2.CAP_PROP_FRAME_WIDTH), video.get(cv2.CAP_PROP_FRAME_HEIGHT)), (0, video.get(cv2.CAP_PROP_FRAME_HEIGHT)), (video.get(cv2.CAP_PROP_FRAME_WIDTH), 0), key='-GRAPH-', enable_events=True, drag_submits=True)],
              [sg.Text('00:00', key='-TIME_ELAPSED-'), sg.Slider(range=(0, totalFrames - 1), enable_events=True, resolution=0.0001, disable_number_display=True,
                       background_color='#83D8F5', orientation='h', key='-TIME-', size=(video.get(cv2.CAP_PROP_FRAME_WIDTH) * 0.073, 20))],
              [sg.Button(key='-REWIND-', image_data=rewindImage), sg.Button(image_data=playImage, key= '-PLAY-'), sg.Button(image_data=pauseImage, key='-PAUSE-'),sg.Button(key='-FASTFORWARD-', image_data=forwardImage),  sg.Button('Restart')] ]
    window = sg.Window('SFI Calculator', layout)
    graph_elem = window['-GRAPH-']  # type: sg.Graph
    a_id = None

    paused = True
    rewind = False
    fastForward = False
    ret, frame = video.read() #get frst frame of video
    currentFrame = 1

    # show video
    while True:
        event, values = window.read(timeout=0)
        if not paused and not rewind and not fastForward:
            ret, frame = video.read()
            currentFrame += 1
            time_elapsed = "{:02.0f}:{:02.0f}".format(*divmod(video.get(cv2.CAP_PROP_POS_MSEC) // 1000, 60))
            window['-TIME_ELAPSED-'].update(time_elapsed)
        elif rewind:
            ret, frame = video.read()
            currentFrame -=(fps)
            if currentFrame < 0:
                currentFrame = 0
            video.set(cv2.CAP_PROP_POS_FRAMES, int(currentFrame))
            time_elapsed = "{:02.0f}:{:02.0f}".format(*divmod(video.get(cv2.CAP_PROP_POS_MSEC) // 1000, 60))
            window['-TIME_ELAPSED-'].update(time_elapsed)
            window['-TIME-'].update(currentFrame)
        elif fastForward:
            ret, frame = video.read()
            currentFrame +=(fps)
            if currentFrame > totalFrames:
                currentFrame = totalFrames
            video.set(cv2.CAP_PROP_POS_FRAMES, int(currentFrame))
            time_elapsed = "{:02.0f}:{:02.0f}".format(*divmod(video.get(cv2.CAP_PROP_POS_MSEC) // 1000, 60))
            window['-TIME_ELAPSED-'].update(time_elapsed)
            window['-TIME-'].update(currentFrame)

        if event in ('Exit', None):
            break
    
        elif event == '-TIME-':
            video.set(cv2.CAP_PROP_POS_FRAMES, int(values['-TIME-'] - 1))
            currentFrame = int(values['-TIME-'] - 1)
            paused = False
                       
        elif event == 'Restart':
            paused = True
            rewind = False
            fastForward = False
            values['-TIME-'] = 0
            currentFrame = 0
            video.set(cv2.CAP_PROP_POS_FRAMES, 0)
            window['-TIME-'].update(0)
        
        elif event == '-REWIND-':
            rewind = True
            paused = False 
            fastForward = False

        elif event == '-FASTFORWARD-':
            fastForward = True
            paused = False 
            rewind = False

        #Open new video
        elif event == 'Open video':
            window.close()
            video.release()
            cv2.destroyAllWindows()
            showVideo()
            break  

        #Play/pause button interaction 
        elif event == '-PLAY-':
            paused = False
            rewind = False 
            fastForward = False

        elif event == '-PAUSE-':
            paused = True
            rewind = False
            fastForward = False

        #Drawing frame on graph
        if currentFrame >= totalFrames:
            #Video end was reached so stay on last frame
            video.set(cv2.CAP_PROP_POS_FRAMES, totalFrames - 1) 
        imgbytes = cv2.imencode('.ppm', frame)[1].tobytes()
        if a_id:
            graph_elem.delete_figure(a_id)  # delete previous image
        a_id = graph_elem.draw_image(data=imgbytes, location=(0, 0))  # draw new image
        graph_elem.send_figure_to_back(a_id)  # move image to the "bottom" of all other drawings

        #draw on graph TODO
        if event == '-GRAPH-':
            graph_elem.draw_circle(values['-GRAPH-'], 5, fill_color='red', line_color='red')

    window.close()

    video.release()
    cv2.destroyAllWindows()

# main function
if __name__ == '__main__':
    showVideo()
    print("Test SFI run: " + str(calculate_sfi(10,5,15,12,8,7,6,5)))
