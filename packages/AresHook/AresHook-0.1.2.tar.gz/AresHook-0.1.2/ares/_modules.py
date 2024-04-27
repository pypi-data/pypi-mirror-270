from pydantic import BaseModel


class AresMessage(BaseModel):
    device_serial: str
    package_name: str
    pid: int
    script_name: str
    message: str
