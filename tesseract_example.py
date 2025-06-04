import easyocr

reader = easyocr.Reader(['en'])

results = reader.readtext("C:\\Users\\kesne\source\\repos\\TD_NewsAggregator\\TD_NewsAggregator\\screenshot.png")
print(results)