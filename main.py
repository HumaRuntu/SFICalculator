from mediaplayer import mediaPlayer

def measureLine(aspectBeingMeasured):
    """
    Calculates distance between user drawn points
    """
    

def calculate_sfi(npl, epl, ets, nts, eit, nit):
    #TODO?

    """
    SFI = -38.3((EPL-NPL)/NPL) + 109.5((ETS-NTS)/NTS) + 13.3((EIT-NIT)/NIT) - 8.8

    SFI Formula from:

    Bain, J. R. M.D.; Mackinnon, S. E. M.D., F.R.C.S.(C), 
    F.A.C.S.; Hunter, D. A. R.T.. Functional Evaluation of Complete 
    Sciatic, Peroneal, and Posterior Tibial Nerve Lesions in the Rat.
    Plastic and Reconstructive Surgery 83(1):p 129-136, January 1989.""" 
    """
    Calculates the Sciatic Function Index (SFI) based on input parameters.
    :param npl: Normal print length
    :param epl: Experimental print length
    :param ets: Experimental total spread
    :param nts: Normal total spread
    :param eit: Experimental intermediate toes
    :param nit: Normal intermediate toes
    """
    sfi = (float(-38.3) * ((epl-npl)/npl)) + (float(109.5) * ((ets-nts)/nts)) + (float(13.3) * ((eit-nit)/nit)) - float(8.8) 
    return float(sfi)

# main function
if __name__ == '__main__':
    player = mediaPlayer()
    player.showVideo()
    print("Test SFI run: " + str(calculate_sfi(15,12,8,7,6,5)))
