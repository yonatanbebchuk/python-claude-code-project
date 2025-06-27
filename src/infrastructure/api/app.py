import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


class App(FastAPI):
    def __init__(self):
        super().__init__(
            title="...",
            description="..."
        )

        self.add_middleware(
            CORSMiddleware,
            allow_origins=os.getenv("ALLOWED_ORIGINS", "*").split(","),
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
