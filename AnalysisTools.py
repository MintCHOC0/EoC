from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt

def showAllChoices(player1, player2):
    print(
        f"""
        {player1.__class__.__name__ } : {player1.list_choice}
        {player2.__class__.__name__ } : {player2.list_choice}
        {player1.point} vs {player2.point}"""
    )

def showAllPoints(players):
    for player in players:
        print(f"NAME : {player.__class__.__name__}")
        print(f"POINT : {player.point}\n")

def showNowPlayers(players, gener):
    counter = Counter([player.__class__.__name__ for player in players])
    msg = f"""
    =======================================
    End genration #{gener}
    Now : {counter}
    =======================================
    """
    print(msg)

def showPlayerGraph(file_path):
    df = pd.read_csv(file_path)
    for name in df.columns[1:]:
        plt.plot(df[name])
    plt.title("Trends in the number of strategies\nsurvived by generation")
    plt.legend(df.columns[1:], fontsize=10)
    plt.show()