"""
Author: Bilal Vandenberge
Date: July 2024
-> Show a nice little title screen when the game is 'loading' (there is no loading, only sleeping)
"""


import time
import os


SCREEN = (
"                                                                                                                                                                              \n"
"                                                                                                                                                                              \n"
"RRRRRRRRRRRRRRRRR   UUUUUUUU     UUUUUUUU   SSSSSSSSSSSSSSS    SSSSSSSSSSSSSSS IIIIIIIIII               AAA               NNNNNNNN        NNNNNNNN                            \n"
"R::::::::::::::::R  U::::::U     U::::::U SS:::::::::::::::S SS:::::::::::::::SI::::::::I              A:::A              N:::::::N       N::::::N                            \n"
"R::::::RRRRRR:::::R U::::::U     U::::::US:::::SSSSSS::::::SS:::::SSSSSS::::::SI::::::::I             A:::::A             N::::::::N      N::::::N                            \n"
"RR:::::R     R:::::RUU:::::U     U:::::UUS:::::S     SSSSSSSS:::::S     SSSSSSSII::::::II            A:::::::A            N:::::::::N     N::::::N                            \n"
"  R::::R     R:::::R U:::::U     U:::::U S:::::S            S:::::S              I::::I             A:::::::::A           N::::::::::N    N::::::N                            \n"
"  R::::R     R:::::R U:::::D     D:::::U S:::::S            S:::::S              I::::I            A:::::A:::::A          N:::::::::::N   N::::::N                            \n"
"  R::::RRRRRR:::::R  U:::::D     D:::::U  S::::SSSS          S::::SSSS           I::::I           A:::::A A:::::A         N:::::::N::::N  N::::::N                            \n"
"  R:::::::::::::RR   U:::::D     D:::::U   SS::::::SSSSS      SS::::::SSSSS      I::::I          A:::::A   A:::::A        N::::::N N::::N N::::::N                            \n"
"  R::::RRRRRR:::::R  U:::::D     D:::::U     SSS::::::::SS      SSS::::::::SS    I::::I         A:::::A     A:::::A       N::::::N  N::::N:::::::N                            \n"
"  R::::R     R:::::R U:::::D     D:::::U        SSSSSS::::S        SSSSSS::::S   I::::I        A:::::AAAAAAAAA:::::A      N::::::N   N:::::::::::N                            \n"
"  R::::R     R:::::R U:::::D     D:::::U             S:::::S            S:::::S  I::::I       A:::::::::::::::::::::A     N::::::N    N::::::::::N                            \n"
"  R::::R     R:::::R U::::::U   U::::::U             S:::::S            S:::::S  I::::I      A:::::AAAAAAAAAAAAA:::::A    N::::::N     N:::::::::N                            \n"
"RR:::::R     R:::::R U:::::::UUU:::::::U SSSSSSS     S:::::SSSSSSSS     S:::::SII::::::II   A:::::A             A:::::A   N::::::N      N::::::::N                            \n"
"R::::::R     R:::::R  UU:::::::::::::UU  S::::::SSSSSS:::::SS::::::SSSSSS:::::SI::::::::I  A:::::A               A:::::A  N::::::N       N:::::::N                            \n"
"R::::::R     R:::::R    UU:::::::::UU    S:::::::::::::::SS S:::::::::::::::SS I::::::::I A:::::A                 A:::::A N::::::N        N::::::N                            \n"
"RRRRRRRR     RRRRRRR      UUUUUUUUU       SSSSSSSSSSSSSSS    SSSSSSSSSSSSSSS   IIIIIIIIIIAAAAAAA                   AAAAAAANNNNNNNN         NNNNNNN                            \n"
"                                                                                                                                                                              \n"
"                                                                                                                                                                              \n"
"RRRRRRRRRRRRRRRRR        OOOOOOOOO     UUUUUUUU     UUUUUUUULLLLLLLLLLL             EEEEEEEEEEEEEEEEEEEEEETTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTEEEEEEEEEEEEEEEEEEEEEE\n"
"R::::::::::::::::R     OO:::::::::OO   U::::::U     U::::::UL:::::::::L             E::::::::::::::::::::ET:::::::::::::::::::::TT:::::::::::::::::::::TE::::::::::::::::::::E\n"
"R::::::RRRRRR:::::R  OO:::::::::::::OO U::::::U     U::::::UL:::::::::L             E::::::::::::::::::::ET:::::::::::::::::::::TT:::::::::::::::::::::TE::::::::::::::::::::E\n"
"RR:::::R     R:::::RO:::::::OOO:::::::OUU:::::U     U:::::UULL:::::::LL             EE::::::EEEEEEEEE::::ET:::::TT:::::::TT:::::TT:::::TT:::::::TT:::::TEE::::::EEEEEEEEE::::E\n"
"  R::::R     R:::::RO::::::O   O::::::O U:::::U     U:::::U   L:::::L                 E:::::E       EEEEEETTTTTT  T:::::T  TTTTTTTTTTTT  T:::::T  TTTTTT  E:::::E       EEEEEE\n"
"  R::::R     R:::::RO:::::O     O:::::O U:::::D     D:::::U   L:::::L                 E:::::E                     T:::::T                T:::::T          E:::::E             \n"
"  R::::RRRRRR:::::R O:::::O     O:::::O U:::::D     D:::::U   L:::::L                 E::::::EEEEEEEEEE           T:::::T                T:::::T          E::::::EEEEEEEEEE   \n"
"  R:::::::::::::RR  O:::::O     O:::::O U:::::D     D:::::U   L:::::L                 E:::::::::::::::E           T:::::T                T:::::T          E:::::::::::::::E   \n"
"  R::::RRRRRR:::::R O:::::O     O:::::O U:::::D     D:::::U   L:::::L                 E:::::::::::::::E           T:::::T                T:::::T          E:::::::::::::::E   \n"
"  R::::R     R:::::RO:::::O     O:::::O U:::::D     D:::::U   L:::::L                 E::::::EEEEEEEEEE           T:::::T                T:::::T          E::::::EEEEEEEEEE   \n"
"  R::::R     R:::::RO:::::O     O:::::O U:::::D     D:::::U   L:::::L                 E:::::E                     T:::::T                T:::::T          E:::::E             \n"
"  R::::R     R:::::RO::::::O   O::::::O U::::::U   U::::::U   L:::::L         LLLLLL  E:::::E       EEEEEE        T:::::T                T:::::T          E:::::E       EEEEEE\n"
"RR:::::R     R:::::RO:::::::OOO:::::::O U:::::::UUU:::::::U LL:::::::LLLLLLLLL:::::LEE::::::EEEEEEEE:::::E      TT:::::::TT            TT:::::::TT      EE::::::EEEEEEEE:::::E\n"
"R::::::R     R:::::R OO:::::::::::::OO   UU:::::::::::::UU  L::::::::::::::::::::::LE::::::::::::::::::::E      T:::::::::T            T:::::::::T      E::::::::::::::::::::E\n"
"R::::::R     R:::::R   OO:::::::::OO       UU:::::::::UU    L::::::::::::::::::::::LE::::::::::::::::::::E      T:::::::::T            T:::::::::T      E::::::::::::::::::::E\n"
"RRRRRRRR     RRRRRRR     OOOOOOOOO           UUUUUUUUU      LLLLLLLLLLLLLLLLLLLLLLLLEEEEEEEEEEEEEEEEEEEEEE      TTTTTTTTTTT            TTTTTTTTTTT      EEEEEEEEEEEEEEEEEEEEEE\n"
"                                                                                                                                                                              \n"
)


DEBUG_SCREEN = (
"______________________________  __________   ______  ___________________________\n"
"___/ __ \__/ ____/__/ __ )_/ / / /_/ ____/   ___/  |/  /_/ __ \__/ __ \__/ ____/\n"
"__/ / / /_/ __/  __/ __ | / / / /_/ / __     __/ /|_/ /_/ / / /_/ / / /_/ __/   \n"
"_/ /_/ /_/ /___  _/ /_/ // /_/ / / /_/ /     _/ /  / / / /_/ /_/ /_/ /_/ /___   \n"
"/_____/ /_____/  /_____/ \____/  \____/      /_/  /_/  \____/ /_____/ /_____/   \n"
"                                                                                \n"
)


def clear_terminal() -> None:
    """
    clear the terminal
    """
    if os.name == "posix": # Unix
        os.system("clear")
    else: # Windows
        os.system("cls")


def show_title(debug_mode: bool = False):
    clear_terminal()
    print(SCREEN, DEBUG_SCREEN if debug_mode else "")
    time.sleep(2 if debug_mode else 5)
    clear_terminal()

if __name__ == "__main__":
    show_title(True)