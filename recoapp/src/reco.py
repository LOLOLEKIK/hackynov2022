import easyocr
from .analyse import analyze

class reco:
    @classmethod
    def reco(self, img):
        tab_result = []
        reader = easyocr.Reader(['en'], gpu = False) # need to run only once to load model into memory
        result = reader.readtext(img)
        for lign in result:
            result_good_bad = analyze.analyze(str(lign[1]))
            tab_result.append(result_good_bad) 
        return tab_result


