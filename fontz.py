import fontforge
import sys
import psMat
import math
import random

fontName = sys.argv[1]
ext = fontName.split('.')[-1]
font = fontforge.open(fontName)

minRads = -20
maxRads = 20
maxNrOfRandomPoints = 30
maxLength = 1000
maxWidth = 100
maxArea = 2000
minArea = -100
minScale = 10

for glyph in font.glyphs():
    if random.randint(1, 10) % 3 == 0 and maxRads > minRads:
        matrix = psMat.rotate(math.radians(random.randint(minRads, maxRads)))
        glyph.transform(matrix)
#         glyph.nltransform('sin(x) * 500', 'y')

    pen = glyph.glyphPen(False)
    points = random.randint(1, maxNrOfRandomPoints)
    
    for p in range(points):
        x1 = random.randint(minArea, maxArea)
        y1 = random.randint(minArea, maxArea)
        pen.moveTo((x1, y1))
         
        length = random.randint(int(maxLength / minScale), maxLength)
        width = random.randint(int(maxWidth / minScale), maxWidth)
        
        if random.randint(1, 10) % 2 == 0:
            pen.lineTo((x1, y1 + length))
            pen.lineTo((x1 + width, y1 + length))
            pen.lineTo((x1 + width, y1))
            pen.lineTo((x1, y1))
        else:
            pen.lineTo((x1 + length, y1))
            pen.lineTo((x1 + length, y1 + width))
            pen.lineTo((x1, y1 + width))
            pen.lineTo((x1, y1))
         
        pen.curveTo((x1 / 2, y1), (x1 / 2, y1 + width * 2))
        pen.closePath()
    
    if random.randint(1, 10) % 2 == 0 and maxRads > minRads:
        matrix = psMat.rotate(math.radians(random.randint(minRads, maxRads)))
        glyph.transform(matrix)

font.generate(fontName + '_out.' + ext)