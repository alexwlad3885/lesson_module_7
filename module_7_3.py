# Домашнее задание по теме "Форматирование строк".

# Использование %:
team1_name = "Мастера кода"
team2_name = "Волшебники данных"
team1_num = 5
team2_num = 6
print('В команде %s участников: %d !' % (team1_name, team1_num))
print('Итого сегодня в командах участников: %d и %d !' %(team1_num, team2_num))

# Использование format():
score2 = 42
team1_time = 1552.512
print('Команда {0} решила задач: {1:2d} !'.format(team2_name, score2))
print('{0} решили задачи за {1:8.3f} c !'.format(team2_name, team1_time))

# Использование f-строк:
score_1 = 40
score_2 = 42
print(f'Команды решили {score_1} и {score_2} задач.')
team2_time = 2153.31451

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = f'Результат битвы: победа команды {team1_name}!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = f'Результат битвы: победа команды {team2_name}!'
else:
    challenge_result = f'Результат битвы: ничья!'
print(challenge_result)

tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total
print(f'Сегодня было решено {tasks_total:2d} задач, в среднем по {time_avg:5.1f} секунды на задачу!.')
