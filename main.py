import cv2
import PySimpleGUI as sg

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
    playImage = b'iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAByElEQVRoge3ZMWsUQRjG8Z8RFSKCgoJp0qSJjVpoZ2clkk8g5CtYpU+TD5DSUkvbVCFNYiM2dhZqY6GFQooEISGai8Xu4HgmcnM3c+su+4fj2L2dmedhb+Z95x16enp6hljBxaZF5OAE7/GoaSGTchJ9tnCrWTnjE0zs19+HWMPlJkWNQzAyh2c4rq+/YBnnmpOWRjASuIfX0f0d3GlAVzLDRmBG9Ta+1r8d4wVuTFdaGqcZCVzFOn7Uz+ziKc5PR1oa/zISWMRm9OxbPCisK5lRjASW8Clqs4H5MrLSSTECs1jFQd3ue319KbewVFKNBBbwMmr/EY8z6kpmXCOBh3gX9dNYdjCpEbigWs326r6OVKvdlQn7TSKHkcCcKt4MNJAd5DQSuI83Ud87uJ15jL8oYYTf2cE3f2YH1wuMhXJGAtdU8+WnwtlBaSOBu3gVjZc9O5iWEapJ/wSf6zEHeI6bZzWYmY6u/4v+rzUirZ/snVh+hwPitpYFxNanKJ1IGk9L4xcz6Eom18bqg5ZtrDqx1Y2LDwPVG2lV8aH15aDWF+jOKpkWi8o5GKWIXTwq56BzxwqdOejpxNFbJw5DO3M83dPT02J+AbN50HbYDxzCAAAAAElFTkSuQmCC'
    stopImage = b'iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAAaklEQVRoge3ZQQqAMAxFwSre/8p6AZFUiXzKzLqLPNJVOwYAvLcVzpztU9Q8zrr/NUW3Y+JsZXsdSjdimY0ISSMkjZA0QtIISSMkjZA0QtIISSMkjZA0QtIISSMkzcxrfMo/ya1lNgIAX1zq+ANHUjXZuAAAAABJRU5ErkJggg=='

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
              [sg.Text('00:00', key='-TIME_ELAPSED-')], 
               [sg.Slider(range=(0, totalFrames - 1), enable_events=True, resolution=0.0001, disable_number_display=True,
                       background_color='#83D8F5', orientation='h', key='-TIME-')],
              [sg.Button('Rewind'), sg.Button(image_data=playImage, key= '-Play/Pause-'),sg.Button('Fast Forward'),  sg.Button('Restart')] ]
    window = sg.Window('SFI Calculator', layout)
    graph_elem = window['-GRAPH-']  # type: sg.Graph
    a_id = None

    paused = True
    ret, frame = video.read() #get frst frame of video
    currentFrame = 1

    # show video
    while True:
        event, values = window.read(timeout=0)
        if not paused:
            ret, frame = video.read()
            currentFrame += 1
            time_elapsed = "{:02.0f}:{:02.0f}".format(*divmod(video.get(cv2.CAP_PROP_POS_MSEC) // 1000, 60))
            window['-TIME_ELAPSED-'].update(time_elapsed)

        if event in ('Exit', None):
            break
    
        elif event == '-TIME-':
            video.set(cv2.CAP_PROP_POS_FRAMES, int(values['-TIME-'] - 1))
            currentFrame = int(values['-TIME-'] - 1)
            paused = False
                       
        elif event == 'Restart':
            video = cv2.VideoCapture(chosenVideoPath)
        
        elif event == 'Rewind': #TODO
            #paused = True #Prevents video from going backwards and forwards at the same time
            totalFrames -=(fps * fastFowardSpeed)
            video.set(cv2.CAP_PROP_POS_FRAMES, totalFrames)

        #Open new video
        elif event == 'Open video':
            window.close()
            video.release()
            cv2.destroyAllWindows()
            showVideo()
            break  

        #Play/pause button interaction 
        elif event == '-Play/Pause-':
            if paused != True:
                paused = True
                window['-Play/Pause-'].update(image_data=playImage)
            else:
                paused = False
                window['-Play/Pause-'].update(image_data=stopImage)

        #Drawing frame on graph FIXME Crashes when video is done
        if currentFrame is totalFrames - 1:
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
