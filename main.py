import cv2
import PySimpleGUI as sg
import os

def openFile():
    layout = [
    [sg.Input(), sg.FileBrowse('FileBrowse')],
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

    #  choose and read video
    chosenVideoPath = openFile()  # select video to show
    video = cv2.VideoCapture(chosenVideoPath)

    layout = [[sg.Button("Open new video")], 
              [sg.Graph((video.get(cv2.CAP_PROP_FRAME_WIDTH), video.get(cv2.CAP_PROP_FRAME_HEIGHT)), (0, video.get(cv2.CAP_PROP_FRAME_HEIGHT)), (video.get(cv2.CAP_PROP_FRAME_WIDTH), 0), key='-GRAPH-', enable_events=True, drag_submits=True)],
              [sg.Button('Pause'), sg.Button('Play')] ]
    window = sg.Window('SFI Calculator', layout)
    graph_elem = window['-GRAPH-']  # type: sg.Graph
    a_id = None

    # show video
    while True:
        event, values = window.read(timeout=0)
        if event in ('Exit', None):
            break
        
        elif event == 'Pause':
            cv2.waitKey(-1)
            break

        elif event == 'Play':
            video = cv2.VideoCapture(chosenVideoPath)
            break
        

        ret, frame = video.read()

        imgbytes = cv2.imencode('.ppm', frame)[1].tobytes()
        if a_id:
            graph_elem.delete_figure(a_id)  # delete previous image
        a_id = graph_elem.draw_image(data=imgbytes, location=(0, 0))  # draw new image
        graph_elem.send_figure_to_back(a_id)  # move image to the "bottom" of all other drawings

        if event == '-GRAPH-':
            graph_elem.draw_circle(values['-GRAPH-'], 5, fill_color='red', line_color='red')

    window.close()

    video.release()
    cv2.destroyAllWindows()

# main function
if __name__ == '__main__':
    showVideo()
    print("Test SFI run: " + str(calculate_sfi(10,5,15,12,8,7,6,5)))
