"""
Muda a cor no terminal
"""

class Cor:
    # Códigos ANSI para as cores no terminal
    _RESET = "\033[0m"
    _VERMELHO = "\033[31m"
    _VERDE = "\033[32m"
    _AMARELO = "\033[33m"
    _AZUL = "\033[34m"
    _ROXO = "\033[35m"
    _CIANO = "\033[36m"
    _BRANCO = "\033[37m"

    @staticmethod
    def vermelho(texto: str) -> str:
        return f"{Cor._VERMELHO}{texto}{Cor._RESET}"

    @staticmethod
    def verde(texto: str) -> str:
        return f"{Cor._VERDE}{texto}{Cor._RESET}"

    @staticmethod
    def amarelo(texto: str) -> str:
        return f"{Cor._AMARELO}{texto}{Cor._RESET}"

    @staticmethod
    def azul(texto: str) -> str:
        return f"{Cor._AZUL}{texto}{Cor._RESET}"

    @staticmethod
    def roxo(texto: str) -> str:
        return f"{Cor._ROXO}{texto}{Cor._RESET}"

    @staticmethod
    def ciano(texto: str) -> str:
        return f"{Cor._CIANO}{texto}{Cor._RESET}"
