#
# Horizon Generator - Python
#
# Copyright (c) 2020 Nick Banyard
#
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import black

PAGE_SIZE = A4
PAGE_WIDTH, PAGE_HEIGHT = PAGE_SIZE
MARGIN = cm

TITLE_FONT = 'Helvetica'
TITLE_SIZE = 14

DIRECTION_FONT = 'Helvetica'
DIRECTION_SIZE = 10

DIRECTIONS = [
    'N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
    'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW'
]

class Document:
    """
    PDF generator for horizon documents
    """

    def __init__(self, filename, title, panelCount):
        self.canvas = canvas.Canvas(filename, pagesize=PAGE_SIZE)
        self.title = title
        self.panelCount = panelCount

    def save(self):
        self.genPanarama()
        self.genMap()
        self.canvas.save()

    def genPanarama(self):
        self.drawTitle()

        panelHeight = (
            PAGE_HEIGHT - TITLE_SIZE - (self.panelCount + 3) * MARGIN
        )/self.panelCount
        panelWidth = PAGE_WIDTH - 2 * MARGIN
        panelX = MARGIN

        self.canvas.setStrokeColor(black)
        self.canvas.setLineWidth(1)
        for panel in range(self.panelCount):
            panelY = (
                (self.panelCount - panel - 1) * (panelHeight + MARGIN) +
                2 * MARGIN
            )
            self.canvas.rect(panelX, panelY, panelWidth, panelHeight)

        self.canvas.setFont(DIRECTION_FONT, DIRECTION_SIZE)
        dirWidth = (panelWidth * self.panelCount) / len(DIRECTIONS)
        for dirIndex, dirName in enumerate(DIRECTIONS):
            dirPosition = dirIndex * dirWidth
            dirPanel = dirPosition // panelWidth
            dirX = dirPosition % panelWidth + MARGIN
            dirY = (
                (self.panelCount - dirPanel - 1) * (panelHeight + MARGIN) +
                2 * MARGIN - DIRECTION_SIZE
            )
            self.canvas.drawCentredString(dirX, dirY, dirName)
        self.canvas.showPage()

    def genMap(self):
        mapSide = PAGE_WIDTH - 2 * MARGIN
        mapX = MARGIN
        mapY = (PAGE_HEIGHT - mapSide) / 2

        self.drawTitle()
        self.canvas.setStrokeColor(black)
        self.canvas.setLineWidth(1)
        self.canvas.rect(mapX, mapY, mapSide, mapSide)
        self.canvas.showPage()

    def drawTitle(self):
        self.canvas.setFont(TITLE_FONT, TITLE_SIZE)
        self.canvas.drawCentredString(
            PAGE_WIDTH/2,
            PAGE_HEIGHT - MARGIN - TITLE_SIZE,
            self.title
        )
