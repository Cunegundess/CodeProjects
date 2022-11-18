def add_time(start, duration, day = None):
    
    # variaveis iniciais
    format_later = 0
    days_later = 0
    days_of_week = ['Sunday', 
          'Monday', 
          'Tuesday', 
          'Wednesday', 
          'Thursday', 
          'Friday', 
          'Saturday']

    format = start.split(" ")[1]
    initial_format = format

    start = start.split(" ")
    start.pop(1)
    start = ''.join(start)

    hour = int(start.split(":")[0]) + int(duration.split(":")[0])
    minutes = int(start.split(":")[1]) + int(duration.split(":")[1])

    # formatando o tempo
    if minutes > 59:
        hour += 1
        minutes -= 60

    hour_format = hour

    while hour > 12:
        hour -= 12

    while hour_format > 11:
        hour_format -= 12
        format = 'PM' if format == 'AM' else 'AM'
        format_later += 1

    if format_later % 2 != 0:
        if initial_format == 'PM':
          format_later += 1
        else:
          format_later -= 1
    
    days_later = format_later / 2
    
    # adicionando o 'novo tempo'
    new_time = f'{hour}:{str(minutes).zfill(2)} {format}'

    # trabalhando na contagem de dias 
    if day:
        weekday = days_of_week.index(day.title())
        weekday_new = int((weekday + days_later) % 7)
        new_time += f', {days_of_week[weekday_new]}'

    if days_later == 1:
        new_time += ' (next day)'

    if days_later > 1: 
        new_time += f' ({int(days_later)} days later)'


    return new_time
