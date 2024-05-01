import json
import platform
import logging
logging.basicConfig(format='%(levelname)s:%(asctime)s %(funcName)s:%(lineno)d - %(message)s', level=logging.INFO)


def get_library_name(prefix:str = 'libkoverse_labeler-') -> str:
    os_info = platform.platform().casefold()
    architecture = platform.architecture()


    logging.debug(f"Operating System: {os_info}")
    logging.debug(f"CPU Architecture: {architecture}")

    if "macos" in os_info and "arm64" in os_info:
        return prefix + "arm64-apple-darwin.dylib"

    if "macos" in os_info and "x86_64" in os_info:
        return prefix + "x86_64-apple-darwin.dylib"

    if "linux" in os_info and "x86_64" in os_info:
        return prefix + "x86_64-linux-gnu.so"

    if "linux" in os_info and "aarch64" in os_info:
        return prefix + "aarch64-linux-gnu.so"



def read_file(filePath: str):
    with open(filePath) as file:
        content = json.load(file)
        file.close()

    return content
