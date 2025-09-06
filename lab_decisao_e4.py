import random

team1 = input("Insira o time A: ")
team2 = input("Insira o time B: ")
team3 = input("Insira o time C: ")
team4 = input("Insira o time D: ")

avg1 = float(input(f"\nInsira a média de gols do {team1}: "))
avg2 = float(input(f"Insira a média de gols do {team2}: "))
avg3 = float(input(f"Insira a média de gols do {team3}: "))
avg4 = float(input(f"Insira a média de gols do {team4}: "))

def play_match(home_team, away_team, home_avg, away_avg):
    goals_home = random.randint(0, round(home_avg))
    goals_away = random.randint(0, round(away_avg))

    print(f"\n{home_team} {goals_home} x {goals_away} {away_team}")

    if goals_home == goals_away:
        print(f"Empate! Vantagem do time da casa: {home_team}")
        return home_team, home_avg
    else:
        if goals_home > goals_away:
            print(f"Vencedor: {home_team}")
            return home_team, home_avg
        else:
            print(f"Vencedor: {away_team}")
            return away_team, away_avg


# Semifinais
winner1, avgWinner1 = play_match(team1, team2, avg1, avg2)
winner2, avgWinner2 = play_match(team3, team4, avg3, avg4)

# Final
goals_winner1 = random.randint(0, round(avgWinner1))
goals_winner2 = random.randint(0, round(avgWinner2))

print(f"\nFinal: {winner1} {goals_winner1} x {goals_winner2} {winner2}")

if goals_winner1 == goals_winner2:
    print("Disputa por pênaltis...")

    goals_winner1 = random.randint(0, 5)
    goals_winner2 = random.randint(0, 5)

    print(f"Pênaltis: {winner1} {goals_winner1} x {goals_winner2} {winner2}")

    if goals_winner1 == goals_winner2:
        print("Novo empate! Decisão na moeda...")

        coin = random.randint(0, 1)

        if coin == 0:
            champion = winner1
        else:
            champion = winner2
    else:
        if goals_winner1 > goals_winner2:
            champion = winner1
        else:
            champion = winner2
else:
    if goals_winner1 > goals_winner2:
        champion = winner1
    else:
        champion = winner2

print(f"\nO campeão é: {champion}")
