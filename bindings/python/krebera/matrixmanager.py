from samplebase import SampleBase
import asyncio

class MatrixManager(SampleBase):

    # Inherits correct settings and matrix object to write to
    def __init__(self):
        super(MatrixManager, self).__init__()

    async def update(self):
        print("Frame")