from typing import Any

from colorama import Fore


class Format:
    @staticmethod
    def squared(value: Any, color: Fore):
        return f"[{color}{value}{Fore.RESET}]"

    @staticmethod
    def curled(value: Any, color: Fore):
        return "{" + f"{color}{value}{Fore.RESET}" + "}"

    @staticmethod
    def parentheses(value: Any, color: Fore):
        return f"({color}{value}{Fore.RESET})"
