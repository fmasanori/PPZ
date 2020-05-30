#!/usr/bin/env python3
"""
Bacon generator. Unfortunately only virtual.

Only tested with bacon slices and avocados but likely works with any food (or
non-food).
"""
import os.path
import platform
import random
import sys
from typing import List, Tuple

from PySide2.QtCore import QTimer, Qt
from PySide2.QtGui import QPainter, QPixmap, QTransform
from PySide2.QtWidgets import QApplication, QWidget


IMAGE_PATH = os.path.join(os.path.dirname(__file__), 'img\abacate.png')
AMOUNT = 47
INTERVAL = 750

SYSTEM = platform.system()


class ImageGeneratorOverlay(QWidget):
    """A fullscreen QWidget that will be filled with copies of an image."""

    def __init__(self, width: int, height: int, image_path: str = IMAGE_PATH,
                 amount: int = AMOUNT, interval: int = INTERVAL):
        super().__init__()

        # Set widget properties
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.NoDropShadowWindowHint |
            Qt.WindowStaysOnTopHint
        )

        if SYSTEM == 'Windows':
            self.setWindowFlags(self.windowFlags() | Qt.Popup)

        if SYSTEM == 'Darwin':
            self.setWindowState(self.windowState() | Qt.WindowMaximized)
        else:
            self.setWindowState(self.windowState() | Qt.WindowFullScreen)

        # Prepare the images
        self.screen_width = width
        self.screen_height = height

        self.image = self._load_image(image_path)
        self.map = self._generate_map(amount)
        self.current = 0

        # Start the timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.repaint)
        self.timer.start(interval)

    def keyPressEvent(self, _) -> None:
        """Stop on any keyboard input."""
        sys.exit()

    def mousePressEvent(self, _) -> None:
        """Stop on any mouse input."""
        sys.exit()

    def repaint(self) -> None:
        """Force a repaint, updating the image counter along the way."""
        if self.current >= len(self.map) - 1:
            self.timer.stop()
            return
        self.current += 1
        super().repaint()

    def paintEvent(self, _) -> None:
        """Paint the current picture and all before it."""
        painter = QPainter(self)
        for i in range(self.current):
            x, y, image = self.map[i]
            painter.drawPixmap(x, y, image)

    def _load_image(self, path: str) -> QPixmap:
        """Load the base image from `path`."""
        if not os.path.isfile(path):
            print('No file found at "{}"'.format(path), file=sys.stderr)
            sys.exit(1)
        try:
            image = QPixmap(path)
        except:
            print('Failed to load "{}"'.format(path), file=sys.stderr)
            sys.exit(1)

        return image

    def _generate_map(self, amount: int) -> List[Tuple[int, int, QPixmap]]:
        """
        Generate the coordinates and sizes of the images to render.

        The result is a list of triples `(x, y, QPixmap)` -- the coordinates
        where to draw and the image to draw.
        """
        generated = []

        for i in range(amount):
            image = self._transform_image()

            x = random.randint(0, self.screen_width - image.width())
            y = random.randint(0, self.screen_height - image.height())

            generated.append((x, y, image))

        return generated

    def _transform_image(self) -> QPixmap:
        """Create a randomly rotated and resized version of self.image."""
        # Rotate
        degrees = random.randint(0, 359)
        transform = QTransform()
        transform.rotate(degrees)
        image = self.image.transformed(transform)

        # Generate random dimensions but make sure the image fits to the screen
        dim = 'width' if image.width() > image.height() else 'height'
        image = self._normalize(image, dim)
        other = {'width': 'height', 'height': 'width'}[dim]
        if getattr(image, other)() >= getattr(self, 'screen_'  + other):
            image = self._normalize(image, other)

        return image

    def _normalize(self, image: QPixmap, dim: str) -> QPixmap:
        """Resize so that the generated width or height is in bounds."""
        dim_cap = dim.capitalize()
        max_size = min(getattr(image, dim)(), getattr(self, 'screen_' + dim))
        size = random.randint(50, max_size - 50)
        image = getattr(image, 'scaledTo' + dim_cap)(size,
                                                     Qt.FastTransformation)
        return image


def main():
    app = QApplication()
    screen = app.desktop().screenGeometry()
    width, height = screen.width(), screen.height()

    widget = ImageGeneratorOverlay(width, height)
    widget.show()
    widget.activateWindow()

    sys.exit(app.exec_())
