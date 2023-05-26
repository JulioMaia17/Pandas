import csv

data = [
    ["PONTOS", "PTS"],
    ["Kawhi Leonard", "LAC", 34.5],
    ["Devin Booker", "PHX", 33.7],
    ["Anthony Edwards", "MIN", 31.6],
    ["Stephen Curry", "GS", 30.5],
    ["Nikola Jokic", "DEN", 29.9],
    ["ASSISTÊNCIAS", "AST"],
    ["Nikola Jokic", "DEN", 10.3],
    ["Trae Young", "ATL", 10.2],
    ["James Harden", "PHI", 8.3],
    ["Jrue Holiday", "MIL", 8.0],
    ["De'Aaron Fox", "SAC", 7.7],
    ["ARREMESSOS DE 3 PONTOS", "3PM"],
    ["Stephen Curry", "GS", 4.4],
    ["Klay Thompson", "GS", 3.8],
    ["Jamal Murray", "DEN", 3.1],
    ["Tyrese Maxey", "PHI", 3.1],
    ["Kawhi Leonard", "LAC", 3.0],
    ["REBOTES", "REB"],
    ["Anthony Davis", "LAL", 14.1],
    ["Nikola Jokic", "DEN", 13.3],
    ["Kevon Looney", "GS", 13.1],
    ["Rudy Gobert", "MIN", 12.2],
    ["Giannis Antetokounmpo", "MIL", 11.0],
    ["TOCOS", "BLK"],
    ["Anthony Davis", "LAL", 3.1],
    ["Joel Embiid", "PHI", 2.8],
    ["Jaren Jackson Jr.", "MEM", 2.0],
    ["Anthony Edwards", "MIN", 2.0],
    ["Al Horford", "BOS", 1.8],
    ["ROUBOS", "STL"],
    ["De'Aaron Fox", "SAC", 2.1],
    ["Jimmy Butler", "MIA", 2.1],
    ["Kawhi Leonard", "LAC", 2.0],
    ["Dejounte Murray", "ATL", 2.0],
    ["Donovan Mitchell", "CLE", 2.0]
]

filename = "nba_stats.csv"

with open(filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

print("Arquivo CSV criado com sucesso: ", filename)